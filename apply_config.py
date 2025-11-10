#!/usr/bin/env python3
"""
apply_config.py
────────────────
Synchronizes the project based on config_options.py
"""

import argparse
from config_options import PROJECT_NAME

def main():
    parser = argparse.ArgumentParser(description="Apply project configuration.")
    parser.add_argument("--skip-osm", action="store_true")
    parser.add_argument("--skip-timetables", action="store_true")
    args = parser.parse_args()

    print(f"Applying configuration for {PROJECT_NAME}")

    if not args.skip_osm:
        print("Importing OSM data... (simulate)")
    if not args.skip_timetables:
        print("Importing timetables... (simulate)")

    print("Configuration applied successfully.")

if __name__ == "__main__":
    main()
