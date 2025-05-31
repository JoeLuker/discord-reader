# Discord Reader

Analyze your Discord usage patterns to understand how you interact with different servers and identify what's important to you.

## 📁 Project Structure

```
discord-reader/
├── scripts/                     # Analysis scripts
│   ├── discord_reader.py       # Legacy Discord.py bot-based analyzer
│   ├── discord_reader_oauth.py # OAuth2-based analyzer (recommended)
│   ├── discord_reader_user.py  # User token analyzer (full access)
│   ├── mech_interp_analyzer.py # Specialized Mech Interp server analyzer
│   └── oauth_server.py         # OAuth callback server
├── visualizers/                 # Data visualization dashboards
│   ├── visualizer.py           # Main Streamlit dashboard
│   └── visualizer_oauth.py     # OAuth-compatible dashboard
├── data/                        # Analysis results and logs
│   ├── discord_analysis.json   # Full analysis data
│   ├── discord_analysis_oauth.json # OAuth analysis data
│   ├── mech_interp_analysis.json   # Mech Interp server data
│   └── discord_token.json      # OAuth token cache
├── docs/                        # Documentation
│   └── API_REFERENCE.md        # Detailed API documentation
├── requirements.txt             # Python dependencies
├── run.py                      # Main entry point (recommended)
├── .env                        # Environment configuration
└── README.md                   # This file
```

## 🚀 Quick Start

### Unified Entry Point (Recommended)

Use `run.py` for all operations:

```bash
# Install dependencies
pip install -r requirements.txt

# Create environment file
echo "DISCORD_CLIENT_ID=your_client_id" > .env
echo "DISCORD_CLIENT_SECRET=your_client_secret" >> .env

# Run analysis (choose one method)
python run.py oauth          # OAuth2 analysis (safe, limited data)
python run.py user           # User token analysis (full access)
python run.py mech-interp    # Mech Interp server analysis

# Launch dashboard
python run.py dashboard      # Full data dashboard
python run.py dashboard-oauth # OAuth data dashboard
```

### Method 1: OAuth2 (Recommended - Limited Data)

1. **Create a Discord Application:**
   - Go to https://discord.com/developers/applications
   - Click "New Application"
   - Name it "Discord Reader" or similar
   - Go to OAuth2 section
   - Add redirect URL: `http://localhost:8888/callback`
   - Copy your Client ID and Client Secret

2. **Configure and run:**
   ```bash
   echo "DISCORD_CLIENT_ID=your_client_id" > .env
   echo "DISCORD_CLIENT_SECRET=your_client_secret" >> .env
   python run.py oauth
   ```

### Method 2: User Token (Full Access)

1. **Get your Discord token:**
   - Open Discord in your browser
   - Open Developer Tools (F12)
   - Go to Network tab → Refresh page
   - Look for requests to `discord.com/api`
   - Find the `Authorization` header
   - Copy the token value

2. **Configure and run:**
   ```bash
   echo "DISCORD_TOKEN=your_token_here" >> .env
   python run.py user
   ```

## 📊 Visualization

Launch interactive analytics dashboards:

```bash
# Using run.py (recommended)
python run.py dashboard        # Full data analysis
python run.py dashboard-oauth  # OAuth data (limited)

# Direct Streamlit commands
streamlit run visualizers/visualizer.py       # Full data
streamlit run visualizers/visualizer_oauth.py # OAuth data
```

## 🔍 Specialized Analysis

### Mech Interp Discord Server

Deep analysis of the Mechanistic Interpretability Discord server:

```bash
# Using run.py (recommended)
python run.py mech-interp

# Direct script execution
python scripts/mech_interp_analyzer.py
```

**Features:**
- Comprehensive message history analysis (500+ messages per channel)
- User activity profiles and statistics 
- Channel-by-channel breakdown with topics
- Daily and hourly activity patterns
- Built-in rate limiting and error handling

## ✨ Features

### 📈 Analytics
- **Server Overview**: All servers you're part of
- **Activity Heatmap**: When you're most active (24-hour patterns)
- **Channel Analysis**: Most active channels and message counts
- **Interaction Patterns**: Who you interact with most
- **Time-based Analysis**: Daily/hourly usage patterns

### 🛠️ Multiple Analysis Methods
- **OAuth2**: Safe, limited server metadata (5 channels/server, 50 messages/channel)
- **User Token**: Full access to messages and activity (10 channels/server, 100 messages/channel)
- **Legacy Bot**: Original Discord.py bot implementation (100 messages/channel)
- **Specialized**: Deep-dive analysis of specific servers (500 messages/channel)

### 🎨 Visualizations
- Interactive 24-hour activity polar charts
- Server activity bar charts and breakdowns
- Message distribution pie charts
- User interaction analysis and rankings
- Channel-specific activity views
- Daily/hourly timeline visualizations

## 🔒 Privacy & Security

- ✅ **Local Storage**: All data stored locally, never sent to external servers
- ✅ **Token Security**: Environment variables for sensitive data
- ✅ **Token Caching**: OAuth tokens cached in `data/discord_token.json`
- ✅ **Rate Limiting**: Built-in delays (1 second between requests)
- ✅ **Permission Aware**: Only accesses channels you have permission to read
- ✅ **Error Handling**: Graceful handling of permission denials and API limits

## 📋 Data Formats

### Analysis Output (`data/discord_analysis.json`)
```json
{
  "servers": {...},           // Server metadata and channels
  "channels": {...},          // Channel details and message counts
  "messages": [...],          // Individual message data
  "interactions": {...},      // User interaction patterns
  "activity_times": {...}     // Hourly activity distribution
}
```

### Specialized Analysis (`data/mech_interp_analysis.json`)
```json
{
  "server_info": {...},       // Detailed server information
  "channels": {...},          // Channel topics and metadata
  "messages": [...],          // Full message history (up to 500/channel)
  "users": {...},            // User profiles and activity statistics
  "message_stats": {...},     // Hourly message statistics
  "daily_activity": {...},    // Daily activity patterns
  "channel_activity": {...}   // Per-channel activity breakdown
}
```

### OAuth Analysis (`data/discord_analysis_oauth.json`)
```json
{
  "servers": {...},           // Limited server metadata
  "channels": {...},          // Basic channel information
  "messages": [...],          // Limited message data (50/channel max)
  "interactions": {...},      // Basic interaction patterns
  "activity_times": {...},    // Hourly activity distribution
  "channel_activity": {...}   // Per-channel activity data
}
```

## 🐛 Troubleshooting

### Common Issues

1. **"Improper token" error**: Get a fresh Discord token from browser
2. **"Permission denied"**: Some channels require special permissions
3. **Port conflicts**: Kill existing Streamlit processes: `pkill -f streamlit`
4. **OAuth flow fails**: Verify redirect URI is exactly `http://localhost:8888/callback`
5. **Empty data files**: Check console output for API errors and permission issues

### Configuration

**Environment Variables (.env):**
```bash
# For OAuth2 method
DISCORD_CLIENT_ID=your_application_client_id
DISCORD_CLIENT_SECRET=your_application_client_secret

# For user token method  
DISCORD_TOKEN=your_user_token_here
```

### Getting Help

- Check console output for detailed error messages
- Verify Discord application OAuth2 settings match documentation
- Ensure tokens have appropriate permissions for your intended analysis method
- Review `data/discord_token.json` for OAuth token status

## 📄 License

This project is for educational and personal use. Respect Discord's Terms of Service.

---

*Built for analyzing Discord community patterns and understanding digital social interactions.*