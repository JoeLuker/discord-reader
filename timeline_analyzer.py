#!/usr/bin/env python3
"""
Timeline analyzer for Mechanistic Interpretability Discord server data.
Extracts key events and discussions to create a chronological timeline.
"""

import json
import logging
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple, Any
import re

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_discord_data(file_path: str) -> Dict[str, Any]:
    """Load the Discord analysis JSON data."""
    logger.info(f"Loading Discord data from {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    logger.info("Successfully loaded Discord data")
    return data

def parse_timestamp(timestamp_str: str) -> datetime:
    """Parse ISO timestamp string to datetime object."""
    return datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))

def is_significant_message(message: Dict[str, Any]) -> bool:
    """Determine if a message is significant based on engagement metrics."""
    reactions = message.get('reactions', 0)
    embeds = message.get('embeds', 0)
    content_length = len(message.get('content', ''))
    
    # Consider significant if:
    # - High reactions (3+)
    # - Contains embeds (likely links/media)
    # - Long content (400+ chars)
    # - Contains URLs to papers/resources
    content = message.get('content', '').lower()
    has_important_keywords = any(keyword in content for keyword in [
        'paper', 'research', 'announcement', 'release', 'important', 
        'arxiv', 'github', 'transformer', 'interpretability', 'mechanistic',
        'circuit', 'feature', 'activation', 'attention', 'embedding'
    ])
    
    return (reactions >= 3 or 
            embeds > 0 or 
            content_length > 400 or 
            has_important_keywords)

def extract_key_channels(data: Dict[str, Any]) -> List[str]:
    """Extract channel IDs that are likely to contain important discussions."""
    important_channel_names = [
        'general', 'announcements', 'mod-announcements', 'paper-discussion',
        'research', 'interesting-findings', 'project-proposals', 'welcome',
        'general-resources', 'about', 'layerscope'
    ]
    
    key_channels = []
    channels = data.get('channels', {})
    
    for channel_id, channel_info in channels.items():
        channel_name = channel_info.get('name', '').lower()
        if any(important_name in channel_name for important_name in important_channel_names):
            message_count = channel_info.get('message_count', 0)
            if message_count > 0:  # Only include channels with messages
                key_channels.append(channel_id)
                logger.info(f"Added key channel: {channel_name} (ID: {channel_id}, {message_count} messages)")
    
    return key_channels

def analyze_timeline(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Analyze the Discord data and extract timeline events."""
    logger.info("Starting timeline analysis")
    
    key_channels = extract_key_channels(data)
    timeline_events = []
    
    channels = data.get('channels', {})
    
    for channel_id in key_channels:
        if channel_id not in channels:
            continue
            
        channel_info = channels[channel_id]
        channel_name = channel_info.get('name', 'unknown')
        messages = channel_info.get('messages', [])
        
        logger.info(f"Analyzing {len(messages)} messages in #{channel_name}")
        
        for message in messages:
            if is_significant_message(message):
                try:
                    timestamp = parse_timestamp(message['timestamp'])
                    
                    event = {
                        'date': timestamp.strftime('%Y-%m-%d'),
                        'time': timestamp.strftime('%H:%M:%S UTC'),
                        'timestamp': timestamp,
                        'channel': channel_name,
                        'author': message.get('author_name', 'unknown'),
                        'content': message.get('content', '')[:500] + ('...' if len(message.get('content', '')) > 500 else ''),
                        'reactions': message.get('reactions', 0),
                        'embeds': message.get('embeds', 0),
                        'message_id': message.get('id', ''),
                        'reply_to': message.get('reply_to'),
                        'thread_id': message.get('thread_id')
                    }
                    
                    timeline_events.append(event)
                    
                except Exception as e:
                    logger.warning(f"Error processing message {message.get('id', 'unknown')}: {e}")
                    continue
    
    # Sort events by timestamp
    timeline_events.sort(key=lambda x: x['timestamp'])
    
    logger.info(f"Found {len(timeline_events)} significant timeline events")
    return timeline_events

def categorize_events(events: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Categorize events by type/topic."""
    categories = defaultdict(list)
    
    for event in events:
        content = event['content'].lower()
        channel = event['channel'].lower()
        
        # Categorize based on content and channel
        if 'paper' in content or 'arxiv' in content or channel == 'paper-discussion':
            categories['Papers & Research'].append(event)
        elif 'announcement' in content or channel in ['announcements', 'mod-announcements']:
            categories['Announcements'].append(event)
        elif 'project' in content or channel == 'project-proposals':
            categories['Projects'].append(event)
        elif any(term in content for term in ['circuit', 'feature', 'attention', 'embedding', 'activation']):
            categories['Technical Discussions'].append(event)
        elif channel == 'interesting-findings':
            categories['Research Findings'].append(event)
        elif channel == 'general':
            categories['General Discussions'].append(event)
        else:
            categories['Other'].append(event)
    
    return dict(categories)

def generate_timeline_report(events: List[Dict[str, Any]]) -> str:
    """Generate a formatted timeline report."""
    if not events:
        return "No significant events found in the timeline."
    
    categorized = categorize_events(events)
    
    report = "# Mechanistic Interpretability Discord Server Timeline\n\n"
    report += f"**Analysis Period:** {events[0]['date']} to {events[-1]['date']}\n"
    report += f"**Total Significant Events:** {len(events)}\n\n"
    
    # Summary by category
    report += "## Event Categories Summary\n\n"
    for category, cat_events in categorized.items():
        report += f"- **{category}**: {len(cat_events)} events\n"
    report += "\n"
    
    # Chronological timeline
    report += "## Chronological Timeline\n\n"
    
    current_date = None
    for event in events:
        if event['date'] != current_date:
            current_date = event['date']
            report += f"### {current_date}\n\n"
        
        report += f"**{event['time']}** - #{event['channel']} - **{event['author']}**"
        if event['reactions'] > 0:
            report += f" ({event['reactions']} reactions)"
        report += "\n"
        report += f"{event['content']}\n\n"
    
    # Category-specific sections
    for category, cat_events in categorized.items():
        if category != 'Other' and cat_events:
            report += f"## {category} Highlights\n\n"
            for event in cat_events[-10:]:  # Show last 10 events in each category
                report += f"**{event['date']}** - #{event['channel']} - {event['author']}\n"
                report += f"{event['content'][:200]}{'...' if len(event['content']) > 200 else ''}\n\n"
    
    return report

def main():
    """Main function to run the timeline analysis."""
    file_path = '/Users/jluker/discord-reader/data/mech_interp_analysis.json'
    
    try:
        # Load and analyze data
        data = load_discord_data(file_path)
        events = analyze_timeline(data)
        
        # Generate timeline report
        report = generate_timeline_report(events)
        
        # Save report
        output_path = '/Users/jluker/discord-reader/timeline_report.md'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        logger.info(f"Timeline report saved to {output_path}")
        
        # Print summary
        print(f"\nTimeline Analysis Complete!")
        print(f"Found {len(events)} significant events")
        print(f"Report saved to: {output_path}")
        
        # Show first few events as preview
        print(f"\nFirst 5 significant events:")
        for i, event in enumerate(events[:5]):
            print(f"{i+1}. {event['date']} - #{event['channel']} - {event['author']}")
            print(f"   {event['content'][:100]}{'...' if len(event['content']) > 100 else ''}")
            print()
            
    except Exception as e:
        logger.error(f"Error during analysis: {e}")
        raise

if __name__ == "__main__":
    main()