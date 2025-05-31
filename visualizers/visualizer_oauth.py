import streamlit as st
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from collections import Counter

st.set_page_config(page_title="Discord Analytics", layout="wide")

@st.cache_data
def load_data():
    try:
        # Try OAuth data first
        with open('data/discord_analysis_oauth.json', 'r') as f:
            return json.load(f), 'oauth'
    except FileNotFoundError:
        try:
            # Fall back to regular data
            with open('data/discord_analysis.json', 'r') as f:
                return json.load(f), 'regular'
        except FileNotFoundError:
            return None, None

def main():
    st.title("🎮 Discord Analytics Dashboard")
    
    data, data_type = load_data()
    if not data:
        st.error("No analysis data found. Run discord_reader.py or discord_reader_oauth.py first!")
        return
    
    if data_type == 'oauth':
        st.info("Using OAuth data (limited information available)")
    
    # Sidebar
    st.sidebar.header("Filters")
    selected_server = st.sidebar.selectbox(
        "Select Server",
        ["All"] + [s['name'] for s in data['servers'].values()]
    )
    
    # Main metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Servers", len(data['servers']))
    
    if data_type == 'regular' and any('channels' in s for s in data['servers'].values()):
        with col2:
            total_channels = sum(len(s.get('channels', [])) for s in data['servers'].values())
            st.metric("Active Channels", total_channels)
        with col3:
            total_messages = sum(
                sum(c.get('message_count', 0) for c in s.get('channels', [])) 
                for s in data['servers'].values()
            )
            st.metric("Messages Analyzed", total_messages)
    else:
        with col2:
            st.metric("Active Channels", "N/A (OAuth)")
        with col3:
            st.metric("Messages Analyzed", "N/A (OAuth)")
    
    with col4:
        st.metric("Unique Interactions", len(data.get('interactions', {})))
    
    # Activity Heatmap
    if data.get('activity_times'):
        st.header("📊 Activity Patterns")
        hours = list(range(24))
        activity = [data['activity_times'].get(str(h), 0) for h in hours]
        
        if any(activity):  # Only show if there's actual activity
            fig = go.Figure(data=go.Scatterpolar(
                r=activity,
                theta=[f"{h}:00" for h in hours],
                fill='toself',
                name='Activity'
            ))
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True),
                ),
                title="24-Hour Activity Pattern"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No activity data available (OAuth limitations)")
    
    # Server breakdown
    st.header("🏠 Server Overview")
    
    server_data = []
    for server_id, server in data['servers'].items():
        if data_type == 'regular' and 'channels' in server:
            message_count = sum(c.get('message_count', 0) for c in server['channels'])
            active_channels = len([c for c in server['channels'] if c.get('message_count', 0) > 0])
            total_channels = len(server['channels'])
        else:
            message_count = 0
            active_channels = 0
            total_channels = 0
            
        server_data.append({
            'Server': server['name'],
            'Messages': message_count,
            'Active Channels': active_channels,
            'Total Channels': total_channels,
            'Owner': server.get('owner', False),
            'Features': len(server.get('features', []))
        })
    
    df_servers = pd.DataFrame(server_data).sort_values('Server')
    
    # For OAuth, show server list with features
    if data_type == 'oauth':
        st.subheader("Your Discord Servers")
        # Create a more informative display for OAuth data
        for _, row in df_servers.iterrows():
            with st.expander(f"**{row['Server']}**" + (" 👑" if row['Owner'] else "")):
                st.write(f"Features: {row['Features']}")
                server_info = next(s for s in data['servers'].values() if s['name'] == row['Server'])
                if server_info.get('features'):
                    st.write("Server features:", ", ".join(server_info['features'][:5]))
                    if len(server_info['features']) > 5:
                        st.write(f"... and {len(server_info['features']) - 5} more")
    else:
        # Regular visualizations for full data
        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(df_servers.sort_values('Messages', ascending=False).head(10), 
                         x='Server', y='Messages', 
                         title="Top 10 Most Active Servers")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.pie(df_servers[df_servers['Messages'] > 0].head(10), 
                         values='Messages', names='Server',
                         title="Message Distribution")
            st.plotly_chart(fig, use_container_width=True)
    
    # Interaction analysis
    if data.get('interactions') and len(data['interactions']) > 0:
        st.header("👥 Top Interactions")
        
        interactions_df = pd.DataFrame(
            [(user, count) for user, count in data['interactions'].items()],
            columns=['User', 'Replies']
        ).sort_values('Replies', ascending=False).head(20)
        
        fig = px.bar(interactions_df, x='User', y='Replies',
                     title="People You Reply To Most")
        st.plotly_chart(fig, use_container_width=True)
    
    # Server count by features
    if data_type == 'oauth':
        st.header("📊 Server Statistics")
        
        # Count servers by owner status
        owner_count = sum(1 for s in data['servers'].values() if s.get('owner'))
        member_count = len(data['servers']) - owner_count
        
        col1, col2 = st.columns(2)
        with col1:
            fig = px.pie(
                values=[owner_count, member_count],
                names=['Owned by you', 'Member'],
                title="Server Ownership"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Most common features
            all_features = []
            for server in data['servers'].values():
                all_features.extend(server.get('features', []))
            
            if all_features:
                feature_counts = Counter(all_features)
                top_features = dict(feature_counts.most_common(10))
                
                fig = px.bar(
                    x=list(top_features.values()),
                    y=list(top_features.keys()),
                    orientation='h',
                    title="Most Common Server Features"
                )
                st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()