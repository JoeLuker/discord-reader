import discord
import asyncio
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
import aiohttp
from dotenv import load_dotenv
from oauth_server import get_discord_token

load_dotenv()


class DiscordAnalyzerOAuth:
    def __init__(self):
        self.token = None
        self.user_data = None
        self.api_base = "https://discord.com/api/v10"
        self.data = {
            "servers": {},
            "channels": {},
            "messages": [],
            "interactions": defaultdict(int),
            "activity_times": defaultdict(int),
            "channel_activity": defaultdict(lambda: defaultdict(int)),
        }

    async def get_headers(self):
        if not self.token:
            self.token = await get_discord_token()
        return {"Authorization": f"Bearer {self.token['access_token']}"}

    async def fetch_user_data(self):
        headers = await self.get_headers()

        async with aiohttp.ClientSession() as session:
            # Get user info
            async with session.get(
                f"{self.api_base}/users/@me", headers=headers
            ) as resp:
                if resp.status == 200:
                    self.user_data = await resp.json()
                    print(f"Logged in as {self.user_data['username']}")
                else:
                    print(f"Failed to get user data: {resp.status}")
                    return False

            # Get guilds
            async with session.get(
                f"{self.api_base}/users/@me/guilds", headers=headers
            ) as resp:
                if resp.status == 200:
                    guilds = await resp.json()
                    print(f"Found {len(guilds)} servers")

                    for guild in guilds:
                        self.data["servers"][guild["id"]] = {
                            "id": guild["id"],
                            "name": guild["name"],
                            "icon": guild["icon"],
                            "owner": guild["owner"],
                            "permissions": guild["permissions"],
                            "features": guild.get("features", []),
                        }

                        # For each guild, try to get more detailed info
                        await self.analyze_guild(session, guild["id"], headers)
                else:
                    print(f"Failed to get guilds: {resp.status}")

        return True

    async def analyze_guild(self, session, guild_id, headers):
        # Try to get guild channels (requires specific permissions)
        try:
            async with session.get(
                f"{self.api_base}/guilds/{guild_id}/channels", headers=headers
            ) as resp:
                if resp.status == 200:
                    channels = await resp.json()
                    text_channels = [c for c in channels if c["type"] == 0]

                    self.data["servers"][guild_id]["channels"] = []

                    for channel in text_channels[
                        :5
                    ]:  # Limit to 5 channels per guild for demo
                        channel_data = {
                            "id": channel["id"],
                            "name": channel["name"],
                            "type": channel["type"],
                        }

                        # Try to get recent messages
                        await self.analyze_channel_messages(
                            session, channel["id"], headers
                        )

                        self.data["servers"][guild_id]["channels"].append(channel_data)

        except Exception as e:
            print(f"Could not analyze guild {guild_id}: {e}")

    async def analyze_channel_messages(self, session, channel_id, headers):
        try:
            async with session.get(
                f"{self.api_base}/channels/{channel_id}/messages?limit=50",
                headers=headers,
            ) as resp:
                if resp.status == 200:
                    messages = await resp.json()

                    for msg in messages:
                        if msg["author"]["id"] == self.user_data["id"]:
                            # Track activity time
                            created_at = datetime.fromisoformat(
                                msg["timestamp"].replace("Z", "+00:00")
                            )
                            hour = created_at.hour
                            self.data["activity_times"][hour] += 1

                            # Track channel activity
                            self.data["channel_activity"][channel_id]["messages"] += 1

                            # Track interactions (replies)
                            if msg.get("referenced_message"):
                                replied_to = msg["referenced_message"]["author"][
                                    "username"
                                ]
                                self.data["interactions"][replied_to] += 1

        except Exception as e:
            pass  # Silently fail if no permissions

    async def analyze(self):
        print("Starting Discord OAuth analysis...")

        success = await self.fetch_user_data()
        if success:
            # Save data
            with open("data/discord_analysis_oauth.json", "w") as f:
                json.dump(self.data, f, indent=2, default=str)

            print("Analysis complete! Data saved to data/discord_analysis_oauth.json")

            # Print summary
            print(f"\nSummary:")
            print(f"- Servers: {len(self.data['servers'])}")
            print(
                f"- Most active hours: {sorted(self.data['activity_times'].items(), key=lambda x: x[1], reverse=True)[:3]}"
            )
            print(
                f"- Top interactions: {sorted(self.data['interactions'].items(), key=lambda x: x[1], reverse=True)[:5]}"
            )


async def main():
    analyzer = DiscordAnalyzerOAuth()
    await analyzer.analyze()


if __name__ == "__main__":
    asyncio.run(main())
