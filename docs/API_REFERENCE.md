# API Reference

## Main Entry Point

### `run.py` - Unified Command Interface

**Usage:**
```bash
python run.py <command>
```

**Commands:**
- `oauth`: Run OAuth2 analysis (safe, limited data)
- `user`: Run user token analysis (full access)
- `mech-interp`: Run Mech Interp server analysis
- `dashboard`: Launch main Streamlit dashboard
- `dashboard-oauth`: Launch OAuth-compatible dashboard

## Analysis Scripts Overview

### OAuth2 Analyzer (`scripts/discord_reader_oauth.py`)
- **Purpose**: Safe analysis using Discord OAuth2 flow
- **Data Access**: Limited server metadata (5 channels/server, 50 messages/channel)
- **Authentication**: OAuth2 with automatic browser flow
- **Output**: `data/discord_analysis_oauth.json`
- **Rate Limiting**: Built-in delays between API calls
- **Permissions**: Respects Discord OAuth2 scopes (`identify guilds guilds.members.read`)

### User Token Analyzer (`scripts/discord_reader_user.py`)
- **Purpose**: Comprehensive analysis using user authentication token
- **Data Access**: Full message history and activity (10 channels/server, 100 messages/channel)
- **Authentication**: User token from browser session
- **Output**: `data/discord_analysis.json`
- **Features**: Complete interaction patterns, detailed timestamps

### Legacy Bot Analyzer (`scripts/discord_reader.py`)
- **Purpose**: Original Discord.py bot-based implementation
- **Data Access**: Bot permissions only (100 messages/channel)
- **Authentication**: Discord bot token
- **Output**: `discord_analysis.json` (project root)
- **Status**: Legacy implementation, use other methods preferred

### Specialized Mech Interp Analyzer (`scripts/mech_interp_analyzer.py`)
- **Purpose**: Deep analysis of Mechanistic Interpretability Discord server
- **Data Access**: Comprehensive server analysis (500 messages/channel with pagination)
- **Target Server**: Hardcoded server ID `"1080558777608183829"`
- **Output**: `data/mech_interp_analysis.json`
- **Features**: User profiling, daily/hourly statistics, channel topic analysis

## Data Structure Specifications

### Standard Analysis Format (`discord_analysis.json`)
```json
{
  "servers": {
    "server_id": {
      "name": "Server Name",
      "channels": [
        {
          "id": "channel_id",
          "name": "channel-name", 
          "message_count": 123,
          "last_message_time": "2025-01-01T00:00:00Z"
        }
      ]
    }
  },
  "channels": {
    "channel_id": {
      "name": "channel-name",
      "server_id": "server_id",
      "message_count": 123
    }
  },
  "messages": [
    {
      "id": "message_id",
      "content": "Message content",
      "author": "username",
      "timestamp": "2025-01-01T00:00:00Z",
      "channel_id": "channel_id",
      "server_id": "server_id"
    }
  ],
  "interactions": {
    "username": reply_count
  },
  "activity_times": {
    "hour_0_to_23": message_count
  }
}
```

### OAuth Analysis Format (`discord_analysis_oauth.json`)
```json
{
  "servers": {
    "server_id": {
      "name": "Server Name",
      "channels": ["limited_channel_list"]
    }
  },
  "channels": {
    "channel_id": {
      "name": "channel-name",
      "message_count": 50
    }
  },
  "messages": ["limited_message_data"],
  "interactions": {"basic_interaction_data"},
  "activity_times": {"hourly_activity"},
  "channel_activity": {
    "channel_id": {
      "hour_0_to_23": message_count
    }
  }
}
```

### Specialized Mech Interp Format (`mech_interp_analysis.json`)
```json
{
  "server_info": {
    "id": "1080558777608183829",
    "name": "Server Name",
    "description": "Server description",
    "member_count": 1000,
    "features": ["COMMUNITY", "THREADS_ENABLED"],
    "created_at": "2025-01-01T00:00:00Z"
  },
  "channels": {
    "channel_id": {
      "name": "channel-name",
      "topic": "Channel topic description",
      "messages": [
        {
          "id": "message_id",
          "content": "Message content",
          "author_id": "user_id",
          "author_name": "username", 
          "timestamp": "2025-01-01T00:00:00Z",
          "channel_id": "channel_id"
        }
      ]
    }
  },
  "users": {
    "user_id": {
      "username": "username",
      "message_count": 123,
      "channels_active": ["channel_list"]
    }
  },
  "message_stats": {
    "hour_0_to_23": total_message_count
  },
  "daily_activity": {
    "2025-01-01": message_count_for_day
  },
  "channel_activity": {
    "channel_id": {
      "hour_0_to_23": message_count
    }
  }
}
```

## OAuth2 Configuration

### OAuth Server (`scripts/oauth_server.py`)
- **Port**: `8888` (hardcoded)
- **Redirect URI**: `http://localhost:8888/callback`
- **Scopes**: `identify guilds guilds.members.read`
- **Token Storage**: `data/discord_token.json`
- **Features**: Automatic browser opening, token caching, success/error pages

### Environment Variables Required
```bash
DISCORD_CLIENT_ID=your_application_client_id
DISCORD_CLIENT_SECRET=your_application_client_secret
DISCORD_TOKEN=your_user_token_here  # For user token method
```

## Visualization Components

### Main Dashboard (`visualizers/visualizer.py`)
- **Data Source**: `data/discord_analysis.json`
- **Features**:
  - Interactive server filtering sidebar
  - 24-hour activity polar charts (Plotly)
  - Server activity bar charts and pie charts
  - Top user interactions ranking
  - Channel-specific activity breakdowns
  - Message count statistics

### OAuth Dashboard (`visualizers/visualizer_oauth.py`)
- **Data Source**: `data/discord_analysis_oauth.json` (with fallback)
- **Features**:
  - Adaptive UI based on available data
  - Server ownership status visualization
  - Discord server feature analysis
  - OAuth limitations awareness
  - Fallback to standard data if OAuth data unavailable

### Dashboard Commands
```bash
# Via run.py (recommended)
python run.py dashboard        # Main dashboard
python run.py dashboard-oauth  # OAuth dashboard

# Direct Streamlit
streamlit run visualizers/visualizer.py
streamlit run visualizers/visualizer_oauth.py
```

## Rate Limiting & API Behavior

### Built-in Rate Limiting
- **Standard**: 1 second delay between API requests
- **OAuth**: Respects Discord API limits automatically
- **Error Handling**: Graceful handling of 429 rate limit responses
- **Timeouts**: Built-in request timeouts and retries

### Message Limits
- **OAuth**: 50 messages per channel, 5 channels per server
- **User Token**: 100 messages per channel, 10 channels per server  
- **Mech Interp**: 500 messages per channel with pagination
- **Legacy Bot**: 100 messages per channel

## Error Handling & Logging

### Current Implementation
- **Logging**: Console output via `print()` statements (not proper logging framework)
- **Permission Errors**: Silent continuation for inaccessible channels
- **API Failures**: Basic exception handling with error messages
- **Token Issues**: Clear error messages for authentication failures

### Debug Features
- Console progress reporting during analysis
- Detailed error messages for troubleshooting
- Token validation and status checking
- Channel permission verification

## Security & Privacy

### Token Management
- Environment variable storage for sensitive data
- OAuth token caching in local JSON file
- No external server communication (all local)
- Automatic token refresh handling (OAuth)

### Data Privacy
- All analysis data stored locally in `data/` directory
- No telemetry or external data transmission
- Respects Discord user permissions and privacy settings
- Rate limiting prevents excessive API usage