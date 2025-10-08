#!/usr/bin/env python3
"""
Quick Fix Frontmatter Script
Fixes broken frontmatter that's causing sidebar to show descriptions instead of titles
"""

import re
from pathlib import Path

def fix_frontmatter(file_path):
    """Fix frontmatter in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix broken frontmatter patterns
        # Fix title with extra quotes and line breaks
        content = re.sub(
            r"title: '\s*'([^']+)'\s*'\s*\n\s*description: '([^']+)'\s*'",
            r"title: '\1'\ndescription: '\2'",
            content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        # Fix title with extra quotes
        content = re.sub(
            r"title: '\s*'([^']+)'\s*'",
            r"title: '\1'",
            content
        )
        
        # Fix description with extra quotes
        content = re.sub(
            r"description: '\s*'([^']+)'\s*'",
            r"description: '\1'",
            content
        )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Fix all MDX files with broken frontmatter"""
    base_dir = Path("/Users/muhammadshariqnazr/Downloads/new-api-doc")
    
    print("🔧 Fixing broken frontmatter...")
    
    # Find all MDX files
    mdx_files = list(base_dir.rglob("*.mdx"))
    
    fixed_count = 0
    
    for file_path in mdx_files:
        if fix_frontmatter(file_path):
            print(f"✅ Fixed: {file_path.name}")
            fixed_count += 1
    
    print(f"\n🎉 Fixed {fixed_count} files")

if __name__ == "__main__":
    main()
