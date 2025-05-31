import discord
import asyncio
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()

class DiscordAnalyzer:
    def __init__(self):
        self.client = discord.Client(intents=discord.Intents.all())
        self.data = {
            'servers': {},
            'channels': {},
            'messages': [],
            'interactions': defaultdict(int),
            'activity_times': defaultdict(int)
        }
        
    async def analyze_user_activity(self):
        print("Starting Discord analysis...")
        
        @self.client.event
        async def on_ready():
            print(f'Logged in as {self.client.user}')
            
            # Collect server data
            for guild in self.client.guilds:
                self.data['servers'][guild.id] = {
                    'name': guild.name,
                    'joined_at': guild.me.joined_at.isoformat() if guild.me else None,
                    'member_count': guild.member_count,
                    'channels': []
                }
                
                # Analyze channels
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).read_message_history:
                        channel_data = {
                            'id': channel.id,
                            'name': channel.name,
                            'type': str(channel.type),
                            'message_count': 0,
                            'last_message_time': None
                        }
                        
                        # Sample recent messages
                        try:
                            async for message in channel.history(limit=100):
                                if message.author == self.client.user:
                                    channel_data['message_count'] += 1
                                    
                                    # Track interaction times
                                    hour = message.created_at.hour
                                    self.data['activity_times'][hour] += 1
                                    
                                    # Track who you interact with
                                    if message.reference and message.reference.resolved:
                                        replied_to = message.reference.resolved.author.name
                                        self.data['interactions'][replied_to] += 1
                                        
                                    if not channel_data['last_message_time']:
                                        channel_data['last_message_time'] = message.created_at.isoformat()
                        except discord.Forbidden:
                            print(f"No access to {channel.name}")
                            
                        self.data['servers'][guild.id]['channels'].append(channel_data)
                        
            # Save data
            with open('discord_analysis.json', 'w') as f:
                json.dump(self.data, f, indent=2, default=str)
                
            print("Analysis complete! Data saved to discord_analysis.json")
            await self.client.close()
            
    def run(self):
        self.client.run(os.getenv('DISCORD_TOKEN'))


if __name__ == "__main__":
    analyzer = DiscordAnalyzer()
    analyzer.run()