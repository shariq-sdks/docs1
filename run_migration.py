#!/usr/bin/env python3
"""
Simple runner script for the Authlete documentation migration
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

from enhanced_migrate import EnhancedAuthleteMigrator

def main():
    """Run the migration with proper error handling"""
    source_dir = "/Users/muhammadshariqnazr/website/public/developers"
    target_dir = "/Users/muhammadshariqnazr/Downloads/new-api-doc"
    
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory {source_dir} does not exist")
        return 1
    
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    print(f"Starting migration from {source_dir} to {target_dir}")
    
    try:
        migrator = EnhancedAuthleteMigrator(source_dir, target_dir)
        migrator.migrate_all_docs()
        print("Migration completed successfully!")
        return 0
    except Exception as e:
        print(f"Migration failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
