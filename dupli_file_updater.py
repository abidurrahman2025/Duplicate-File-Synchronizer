#!/usr/bin/env python3
"""
One-time file synchronizer
"""

import sys
from pathlib import Path


def sync_file_once():
    target = input("Enter target file path: ").strip()
    search_dir = input("Enter directory to search: ").strip()

    target_path = Path(target)
    search_path = Path(search_dir)

    if not target_path.exists():
        print("Target file not found!")
        return

    target_name = target_path.name
    target_content = target_path.read_bytes()

    updated = 0
    for file_path in search_path.rglob('*'):
        if file_path.is_file() and file_path.name == target_name and file_path != target_path:
            try:
                file_path.write_bytes(target_content)
                print(f"Updated: {file_path}")
                updated += 1
            except Exception as e:
                print(f"Failed: {file_path} - {e}")

    print(f"\nDone! Updated {updated} files.")


if __name__ == "__main__":
    sync_file_once()