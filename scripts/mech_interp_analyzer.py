import aiohttp
import asyncio
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()

class MechInterpAnalyzer:
    def __init__(self):
        self.token = os.getenv('DISCORD_TOKEN')
        self.api_base = 'https://discord.com/api/v10'
        self.headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }
        self.mech_interp_id = "1080558777608183829"  # From the previous analysis
        self.data = {
            'server_info': {},
            'channels': {},
            'messages': [],
            'users': {},
            'message_stats': defaultdict(int),
            'daily_activity': defaultdict(int),
            'channel_activity': defaultdict(int)
        }
        self.user_id = None
        
    async def fetch_user_info(self, session):
        async with session.get(f'{self.api_base}/users/@me', headers=self.headers) as resp:
            if resp.status == 200:
                user_data = await resp.json()
                self.user_id = user_data['id']
                print(f"Logged in as {user_data['username']}#{user_data['discriminator']}")
                return True
            else:
                print(f"Failed to authenticate: {resp.status}")
                return False
                
    async def fetch_server_info(self, session):
        # Get basic server info
        async with session.get(f'{self.api_base}/guilds/{self.mech_interp_id}', headers=self.headers) as resp:
            if resp.status == 200:
                guild_data = await resp.json()
                self.data['server_info'] = {
                    'name': guild_data['name'],
                    'id': guild_data['id'],
                    'description': guild_data.get('description'),
                    'member_count': guild_data.get('approximate_member_count'),
                    'created_at': guild_data.get('id'),  # Can derive from snowflake
                    'features': guild_data.get('features', []),
                    'verification_level': guild_data.get('verification_level'),
                    'rules_channel_id': guild_data.get('rules_channel_id'),
                    'system_channel_id': guild_data.get('system_channel_id')
                }
                print(f"Server: {guild_data['name']}")
                return True
            else:
                print(f"Failed to get server info: {resp.status}")
                return False
                
    async def fetch_channels(self, session):
        async with session.get(f'{self.api_base}/guilds/{self.mech_interp_id}/channels', headers=self.headers) as resp:
            if resp.status == 200:
                channels = await resp.json()
                text_channels = [c for c in channels if c['type'] == 0]  # Text channels only
                
                print(f"Found {len(text_channels)} text channels")
                
                for channel in text_channels:
                    channel_data = {
                        'id': channel['id'],
                        'name': channel['name'],
                        'type': channel['type'],
                        'topic': channel.get('topic'),
                        'position': channel.get('position'),
                        'parent_id': channel.get('parent_id'),
                        'nsfw': channel.get('nsfw', False),
                        'rate_limit_per_user': channel.get('rate_limit_per_user', 0),
                        'messages': [],
                        'message_count': 0,
                        'user_count': 0,
                        'first_message_time': None,
                        'last_message_time': None
                    }
                    
                    self.data['channels'][channel['id']] = channel_data
                    topic = channel.get('topic', 'None')
                    topic_display = topic[:50] + "..." if topic and len(topic) > 50 else topic or "None"
                    print(f"  - {channel['name']} (Topic: {topic_display})")
                    
                return True
            else:
                print(f"Failed to get channels: {resp.status}")
                return False
                
    async def fetch_channel_messages(self, session, channel_id, channel_name, limit=500):
        print(f"Fetching messages from #{channel_name}...")
        
        messages_fetched = 0
        last_message_id = None
        users_in_channel = set()
        
        while messages_fetched < limit:
            # Build URL for pagination
            url = f'{self.api_base}/channels/{channel_id}/messages?limit=100'
            if last_message_id:
                url += f'&before={last_message_id}'
                
            try:
                async with session.get(url, headers=self.headers) as resp:
                    if resp.status == 200:
                        messages = await resp.json()
                        
                        if not messages:  # No more messages
                            break
                            
                        for message in messages:
                            # Store user info
                            author = message['author']
                            if author['id'] not in self.data['users']:
                                self.data['users'][author['id']] = {
                                    'username': author['username'],
                                    'discriminator': author.get('discriminator', '0'),
                                    'global_name': author.get('global_name'),
                                    'bot': author.get('bot', False),
                                    'avatar': author.get('avatar'),
                                    'message_count': 0
                                }
                            
                            users_in_channel.add(author['id'])
                            self.data['users'][author['id']]['message_count'] += 1
                            
                            # Process message
                            message_data = {
                                'id': message['id'],
                                'content': message['content'],
                                'author_id': author['id'],
                                'author_name': author['username'],
                                'timestamp': message['timestamp'],
                                'edited_timestamp': message.get('edited_timestamp'),
                                'attachments': len(message.get('attachments', [])),
                                'embeds': len(message.get('embeds', [])),
                                'reactions': len(message.get('reactions', [])),
                                'reply_to': message.get('referenced_message', {}).get('id') if message.get('referenced_message') else None,
                                'thread_id': message.get('thread', {}).get('id') if message.get('thread') else None
                            }
                            
                            self.data['channels'][channel_id]['messages'].append(message_data)
                            self.data['messages'].append({**message_data, 'channel_id': channel_id, 'channel_name': channel_name})
                            
                            # Update stats
                            created_at = datetime.fromisoformat(message['timestamp'].replace('Z', '+00:00'))
                            date_key = created_at.strftime('%Y-%m-%d')
                            hour_key = created_at.hour
                            
                            self.data['daily_activity'][date_key] += 1
                            self.data['message_stats'][hour_key] += 1
                            self.data['channel_activity'][channel_name] += 1
                            
                            # Update channel timestamps
                            if not self.data['channels'][channel_id]['first_message_time']:
                                self.data['channels'][channel_id]['first_message_time'] = message['timestamp']
                            self.data['channels'][channel_id]['last_message_time'] = message['timestamp']
                            
                            messages_fetched += 1
                            last_message_id = message['id']
                            
                        print(f"  Fetched {len(messages)} messages (total: {messages_fetched})")
                        
                    elif resp.status == 403:
                        print(f"  No permission to read #{channel_name}")
                        break
                    else:
                        print(f"  Error fetching messages from #{channel_name}: {resp.status}")
                        break
                        
            except Exception as e:
                print(f"  Error processing #{channel_name}: {e}")
                break
                
        # Update channel stats
        self.data['channels'][channel_id]['message_count'] = messages_fetched
        self.data['channels'][channel_id]['user_count'] = len(users_in_channel)
        
        print(f"  Completed #{channel_name}: {messages_fetched} messages, {len(users_in_channel)} users")
        
    async def analyze(self):
        print("Starting Mech Interp Discord analysis...")
        
        async with aiohttp.ClientSession() as session:
            # Authenticate
            if not await self.fetch_user_info(session):
                return False
                
            # Get server info
            if not await self.fetch_server_info(session):
                return False
                
            # Get channels
            if not await self.fetch_channels(session):
                return False
                
            # Fetch messages from each channel
            for channel_id, channel_data in self.data['channels'].items():
                await self.fetch_channel_messages(session, channel_id, channel_data['name'])
                await asyncio.sleep(1)  # Rate limiting
                
            # Save comprehensive data
            with open('data/mech_interp_analysis.json', 'w') as f:
                json.dump(self.data, f, indent=2, default=str)
                
            print("\nAnalysis complete! Data saved to data/mech_interp_analysis.json")
            
            # Print summary
            total_messages = len(self.data['messages'])
            total_users = len(self.data['users'])
            active_channels = len([c for c in self.data['channels'].values() if c['message_count'] > 0])
            
            print(f"\nSummary:")
            print(f"- Server: {self.data['server_info']['name']}")
            print(f"- Total channels: {len(self.data['channels'])}")
            print(f"- Active channels: {active_channels}")
            print(f"- Total messages analyzed: {total_messages}")
            print(f"- Unique users: {total_users}")
            print(f"- Most active channel: {max(self.data['channel_activity'], key=self.data['channel_activity'].get) if self.data['channel_activity'] else 'None'}")
            
            # Top channels by activity
            if self.data['channel_activity']:
                print("\nTop 5 most active channels:")
                sorted_channels = sorted(self.data['channel_activity'].items(), key=lambda x: x[1], reverse=True)
                for channel, count in sorted_channels[:5]:
                    print(f"  #{channel}: {count} messages")
                    
            # Top users by message count
            if self.data['users']:
                print("\nTop 10 most active users:")
                sorted_users = sorted(self.data['users'].items(), key=lambda x: x[1]['message_count'], reverse=True)
                for user_id, user_data in sorted_users[:10]:
                    name = user_data.get('global_name') or user_data['username']
                    print(f"  {name}: {user_data['message_count']} messages")
            
            return True

async def main():
    analyzer = MechInterpAnalyzer()
    await analyzer.analyze()

if __name__ == "__main__":
    asyncio.run(main())