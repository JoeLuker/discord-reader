#!/usr/bin/env python3
"""
Discord Reader - Main Entry Point

Usage:
  python run.py oauth          # Run OAuth analysis (limited data)
  python run.py user           # Run user token analysis (full data)
  python run.py mech-interp    # Run Mech Interp analysis
  python run.py dashboard      # Launch dashboard
  python run.py dashboard-oauth # Launch OAuth dashboard
"""

import sys
import subprocess
import os


def run_oauth():
    """Run OAuth analysis"""
    subprocess.run([sys.executable, "scripts/discord_reader_oauth.py"])


def run_user():
    """Run user token analysis"""
    subprocess.run([sys.executable, "scripts/discord_reader_user.py"])


def run_mech_interp():
    """Run Mech Interp analysis"""
    subprocess.run([sys.executable, "scripts/mech_interp_analyzer.py"])


def run_dashboard():
    """Launch main dashboard"""
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", "visualizers/visualizer.py"]
    )


def run_dashboard_oauth():
    """Launch OAuth dashboard"""
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", "visualizers/visualizer_oauth.py"]
    )


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    command = sys.argv[1].lower()

    commands = {
        "oauth": run_oauth,
        "user": run_user,
        "mech-interp": run_mech_interp,
        "dashboard": run_dashboard,
        "dashboard-oauth": run_dashboard_oauth,
    }

    if command in commands:
        commands[command]()
    else:
        print(f"Unknown command: {command}")
        print(__doc__)


if __name__ == "__main__":
    main()
