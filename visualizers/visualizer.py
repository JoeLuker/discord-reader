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
        with open("data/discord_analysis.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def main():
    st.title("🎮 Discord Analytics Dashboard")

    data = load_data()
    if not data:
        st.error("No analysis data found. Run discord_reader.py first!")
        return

    # Sidebar
    st.sidebar.header("Filters")
    selected_server = st.sidebar.selectbox(
        "Select Server", ["All"] + [s["name"] for s in data["servers"].values()]
    )

    # Main metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Servers", len(data["servers"]))
    with col2:
        total_channels = sum(len(s["channels"]) for s in data["servers"].values())
        st.metric("Active Channels", total_channels)
    with col3:
        total_messages = sum(
            sum(c["message_count"] for c in s["channels"])
            for s in data["servers"].values()
        )
        st.metric("Messages Analyzed", total_messages)
    with col4:
        st.metric("Unique Interactions", len(data["interactions"]))

    # Activity Heatmap
    st.header("📊 Activity Patterns")

    if data["activity_times"]:
        hours = list(range(24))
        activity = [data["activity_times"].get(h, 0) for h in hours]

        fig = go.Figure(
            data=go.Scatterpolar(
                r=activity,
                theta=[f"{h}:00" for h in hours],
                fill="toself",
                name="Activity",
            )
        )
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True),
            ),
            title="24-Hour Activity Pattern",
        )
        st.plotly_chart(fig, use_container_width=True)

    # Server breakdown
    st.header("🏠 Server Activity")

    server_data = []
    for server_id, server in data["servers"].items():
        message_count = sum(c["message_count"] for c in server["channels"])
        active_channels = len([c for c in server["channels"] if c["message_count"] > 0])
        server_data.append(
            {
                "Server": server["name"],
                "Messages": message_count,
                "Active Channels": active_channels,
                "Total Channels": len(server["channels"]),
            }
        )

    df_servers = pd.DataFrame(server_data).sort_values("Messages", ascending=False)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(
            df_servers.head(10),
            x="Server",
            y="Messages",
            title="Top 10 Most Active Servers",
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.pie(
            df_servers.head(10),
            values="Messages",
            names="Server",
            title="Message Distribution",
        )
        st.plotly_chart(fig, use_container_width=True)

    # Interaction analysis
    st.header("👥 Top Interactions")

    if data["interactions"]:
        interactions_df = (
            pd.DataFrame(
                [(user, count) for user, count in data["interactions"].items()],
                columns=["User", "Replies"],
            )
            .sort_values("Replies", ascending=False)
            .head(20)
        )

        fig = px.bar(
            interactions_df, x="User", y="Replies", title="People You Reply To Most"
        )
        st.plotly_chart(fig, use_container_width=True)

    # Detailed server view
    if selected_server != "All":
        st.header(f"📋 {selected_server} Details")

        server_info = next(
            s for s in data["servers"].values() if s["name"] == selected_server
        )
        channels_df = pd.DataFrame(server_info["channels"])

        if not channels_df.empty:
            channels_df = channels_df[channels_df["message_count"] > 0].sort_values(
                "message_count", ascending=False
            )

            st.dataframe(channels_df[["name", "message_count", "last_message_time"]])


if __name__ == "__main__":
    main()
