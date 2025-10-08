#!/usr/bin/env python3
"""
Fix Quotes Final Script
Fixes the exact pattern: title: "'text'" -> title: 'text'
"""

import re
from pathlib import Path

def fix_file(file_path):
    """Fix quotes in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix the exact pattern: title: "'text'" -> title: 'text'
        content = re.sub(r'title: "\'([^\']+)\'"', r"title: '\1'", content)
        
        # Fix the exact pattern: description: "'text'" -> description: 'text'
        content = re.sub(r'description: "\'([^\']+)\'"', r"description: '\1'", content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Fix all MDX files with extra quotes"""
    base_dir = Path("/Users/muhammadshariqnazr/Downloads/new-api-doc")
    
    print("🔧 Fixing extra quotes in titles and descriptions...")
    
    # Find all MDX files
    mdx_files = list(base_dir.rglob("*.mdx"))
    
    print(f"📁 Found {len(mdx_files)} MDX files")
    
    fixed_count = 0
    
    for file_path in mdx_files:
        if fix_file(file_path):
            print(f"✅ Fixed: {file_path.name}")
            fixed_count += 1
    
    print(f"\n🎉 Fixed {fixed_count} files")
    
    # Final check
    print("\n🔍 Final check...")
    remaining_issues = 0
    
    for file_path in mdx_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for any remaining extra quotes
            if (re.search(r'title: "\'[^\']+\'"', content) or 
                re.search(r'description: "\'[^\']+\'"', content)):
                print(f"⚠️  Still has extra quotes: {file_path.name}")
                remaining_issues += 1
        except:
            pass
    
    if remaining_issues == 0:
        print("✅ ALL extra quotes fixed!")
    else:
        print(f"⚠️  Found {remaining_issues} files still with extra quotes")

if __name__ == "__main__":
    main()
