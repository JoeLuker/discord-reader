import aiohttp
import asyncio
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()


class DiscordUserAnalyzer:
    def __init__(self):
        self.token = os.getenv("DISCORD_TOKEN")
        self.api_base = "https://discord.com/api/v10"
        self.headers = {"Authorization": self.token, "Content-Type": "application/json"}
        self.data = {
            "servers": {},
            "channels": {},
            "messages": [],
            "interactions": defaultdict(int),
            "activity_times": defaultdict(int),
        }
        self.user_id = None

    async def fetch_user_info(self, session):
        async with session.get(
            f"{self.api_base}/users/@me", headers=self.headers
        ) as resp:
            if resp.status == 200:
                user_data = await resp.json()
                self.user_id = user_data["id"]
                print(
                    f"Logged in as {user_data['username']}#{user_data['discriminator']}"
                )
                return True
            else:
                print(f"Failed to authenticate: {resp.status}")
                return False

    async def fetch_guilds(self, session):
        async with session.get(
            f"{self.api_base}/users/@me/guilds", headers=self.headers
        ) as resp:
            if resp.status == 200:
                guilds = await resp.json()
                print(f"Found {len(guilds)} servers")

                for guild in guilds:
                    self.data["servers"][guild["id"]] = {
                        "name": guild["name"],
                        "id": guild["id"],
                        "icon": guild.get("icon"),
                        "owner": guild.get("owner", False),
                        "permissions": guild.get("permissions"),
                        "features": guild.get("features", []),
                        "channels": [],
                    }

                    # Get detailed guild info and channels
                    await self.analyze_guild(session, guild["id"])

                return True
            else:
                print(f"Failed to get guilds: {resp.status}")
                return False

    async def analyze_guild(self, session, guild_id):
        try:
            # Get guild channels
            async with session.get(
                f"{self.api_base}/guilds/{guild_id}/channels", headers=self.headers
            ) as resp:
                if resp.status == 200:
                    channels = await resp.json()
                    text_channels = [
                        c for c in channels if c["type"] == 0
                    ]  # Text channels only

                    print(
                        f"Analyzing {len(text_channels)} channels in {self.data['servers'][guild_id]['name']}"
                    )

                    for channel in text_channels[
                        :10
                    ]:  # Limit to 10 channels per server
                        channel_data = {
                            "id": channel["id"],
                            "name": channel["name"],
                            "type": channel["type"],
                            "message_count": 0,
                            "last_message_time": None,
                        }

                        # Analyze messages in this channel
                        await self.analyze_channel_messages(
                            session, channel["id"], channel_data
                        )

                        self.data["servers"][guild_id]["channels"].append(channel_data)

                elif resp.status == 403:
                    print(
                        f"No permission to access channels in {self.data['servers'][guild_id]['name']}"
                    )
                else:
                    print(f"Failed to get channels for guild {guild_id}: {resp.status}")

        except Exception as e:
            print(f"Error analyzing guild {guild_id}: {e}")

    async def analyze_channel_messages(self, session, channel_id, channel_data):
        try:
            # Get recent messages from this channel
            async with session.get(
                f"{self.api_base}/channels/{channel_id}/messages?limit=100",
                headers=self.headers,
            ) as resp:
                if resp.status == 200:
                    messages = await resp.json()

                    for message in messages:
                        if message["author"]["id"] == self.user_id:
                            channel_data["message_count"] += 1

                            # Track activity times
                            created_at = datetime.fromisoformat(
                                message["timestamp"].replace("Z", "+00:00")
                            )
                            hour = created_at.hour
                            self.data["activity_times"][hour] += 1

                            # Track interactions (replies)
                            if message.get("referenced_message"):
                                replied_to = message["referenced_message"]["author"][
                                    "username"
                                ]
                                self.data["interactions"][replied_to] += 1

                            # Update last message time
                            if not channel_data["last_message_time"]:
                                channel_data["last_message_time"] = message["timestamp"]

                elif resp.status == 403:
                    print(f"No permission to read messages in channel {channel_id}")
                else:
                    print(
                        f"Failed to get messages for channel {channel_id}: {resp.status}"
                    )

        except Exception as e:
            print(f"Error analyzing messages in channel {channel_id}: {e}")

    async def analyze(self):
        print("Starting Discord user token analysis...")

        async with aiohttp.ClientSession() as session:
            # Authenticate
            if not await self.fetch_user_info(session):
                return False

            # Get guilds and analyze them
            if not await self.fetch_guilds(session):
                return False

            # Save data
            with open("data/discord_analysis.json", "w") as f:
                json.dump(self.data, f, indent=2, default=str)

            print("Analysis complete! Data saved to data/discord_analysis.json")

            # Print summary
            total_messages = sum(
                sum(c["message_count"] for c in server["channels"])
                for server in self.data["servers"].values()
            )

            print(f"\nSummary:")
            print(f"- Servers: {len(self.data['servers'])}")
            print(f"- Total messages analyzed: {total_messages}")
            print(
                f"- Most active hours: {sorted(self.data['activity_times'].items(), key=lambda x: x[1], reverse=True)[:3]}"
            )
            print(
                f"- Top interactions: {sorted(self.data['interactions'].items(), key=lambda x: x[1], reverse=True)[:5]}"
            )

            return True


async def main():
    analyzer = DiscordUserAnalyzer()
    await analyzer.analyze()


if __name__ == "__main__":
    asyncio.run(main())
