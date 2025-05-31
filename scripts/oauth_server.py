import asyncio
import aiohttp
from aiohttp import web
import webbrowser
import json
import os
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

class DiscordOAuth:
    def __init__(self):
        self.client_id = os.getenv('DISCORD_CLIENT_ID')
        self.client_secret = os.getenv('DISCORD_CLIENT_SECRET')
        self.redirect_uri = 'http://localhost:8888/callback'
        self.scope = 'identify guilds guilds.members.read'
        self.token = None
        
    async def start_auth_flow(self):
        # Build authorization URL
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'response_type': 'code',
            'scope': self.scope,
            'prompt': 'consent'
        }
        auth_url = f"https://discord.com/oauth2/authorize?{urlencode(params)}"
        
        # Open browser
        print(f"Opening browser for authorization...")
        webbrowser.open(auth_url)
        
        # Start local server
        app = web.Application()
        app.router.add_get('/callback', self.oauth_callback)
        
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', 8888)
        await site.start()
        
        print("Waiting for authorization...")
        
        # Wait for callback
        while self.token is None:
            await asyncio.sleep(0.1)
            
        await runner.cleanup()
        return self.token
        
    async def oauth_callback(self, request):
        code = request.query.get('code')
        if not code:
            return web.Response(text="Authorization failed!", status=400)
            
        # Exchange code for token
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri
        }
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        auth = aiohttp.BasicAuth(self.client_id, self.client_secret)
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                'https://discord.com/api/v10/oauth2/token',
                data=data,
                headers=headers,
                auth=auth
            ) as resp:
                if resp.status == 200:
                    self.token = await resp.json()
                    
                    # Save token
                    with open('discord_token.json', 'w') as f:
                        json.dump(self.token, f)
                        
                    return web.Response(text="""
                    <html>
                    <body style="font-family: Arial; text-align: center; padding: 50px;">
                        <h1>✅ Authorization Successful!</h1>
                        <p>You can close this window and return to the terminal.</p>
                    </body>
                    </html>
                    """, content_type='text/html')
                else:
                    error = await resp.text()
                    print(f"Token exchange failed: {error}")
                    return web.Response(text="Token exchange failed!", status=400)

async def get_discord_token():
    # Check if token exists and is valid
    if os.path.exists('discord_token.json'):
        with open('discord_token.json', 'r') as f:
            token = json.load(f)
            # TODO: Check if token is expired
            return token
    
    # Otherwise, start OAuth flow
    oauth = DiscordOAuth()
    return await oauth.start_auth_flow()

if __name__ == "__main__":
    token = asyncio.run(get_discord_token())
    print(f"Got token! Access token: {token['access_token'][:10]}...")