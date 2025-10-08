#!/usr/bin/env python3
"""
Fix Broken Frontmatter Script
Fixes all broken frontmatter patterns that cause sidebar to show descriptions
"""

import re
from pathlib import Path

def fix_file_frontmatter(file_path):
    """Fix frontmatter in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern 1: title with extra quotes and line breaks
        content = re.sub(
            r"title: '\s*'([^']+)'\s*'\s*\n\s*description: '([^']+)'\s*'",
            r"title: '\1'\ndescription: '\2'",
            content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        # Pattern 2: title with extra quotes only
        content = re.sub(
            r"title: '\s*'([^']+)'\s*'",
            r"title: '\1'",
            content
        )
        
        # Pattern 3: description with extra quotes only
        content = re.sub(
            r"description: '\s*'([^']+)'\s*'",
            r"description: '\1'",
            content
        )
        
        # Pattern 4: Fix any remaining broken patterns
        content = re.sub(
            r"title: '\s*([^']*)\s*'\s*\n\s*description: '\s*([^']*)\s*'\s*'",
            r"title: '\1'\ndescription: '\2'",
            content,
            flags=re.MULTILINE | re.DOTALL
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
    
    print("🔧 Fixing broken frontmatter patterns...")
    
    # Find all MDX files
    mdx_files = list(base_dir.rglob("*.mdx"))
    
    fixed_count = 0
    
    for file_path in mdx_files:
        if fix_file_frontmatter(file_path):
            print(f"✅ Fixed: {file_path.name}")
            fixed_count += 1
    
    print(f"\n🎉 Fixed {fixed_count} files")
    
    # Check for remaining issues
    print("\n🔍 Checking for remaining broken patterns...")
    remaining_issues = 0
    
    for file_path in mdx_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for broken patterns
            if re.search(r"title: '\s*'[^']+'\s*'", content) or re.search(r"description: '\s*'[^']+'\s*'", content):
                print(f"⚠️  Still broken: {file_path.name}")
                remaining_issues += 1
        except:
            pass
    
    if remaining_issues == 0:
        print("✅ No more broken frontmatter patterns found!")
    else:
        print(f"⚠️  Found {remaining_issues} files still with issues")

if __name__ == "__main__":
    main()
