#!/usr/bin/env python3
import os
import re
import glob

def restore_breadcrumbs(file_path):
    """Restore navigation breadcrumbs to MDX files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has breadcrumbs
        if re.search(r'^\d+\.\s*\[.*\]\(.*\)', content, re.MULTILINE):
            return False
        
        # Find the main H1 heading
        h1_match = re.search(r'^# ([^\n]+)', content, re.MULTILINE)
        if not h1_match:
            return False
        
        h1_title = h1_match.group(1).strip()
        
        # Create breadcrumbs
        breadcrumbs = f"1. [Home](https://www.authlete.com/)\n3. {h1_title}"
        
        # Insert breadcrumbs after the H1
        new_content = re.sub(
            r'^(# [^\n]+)\n',
            f'\\1\n{breadcrumbs}\n',
            content,
            flags=re.MULTILINE
        )
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Restored breadcrumbs: {file_path}")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    # Only restore breadcrumbs for concept files and main pages
    target_files = [
        'concepts/*.mdx',
        'overview.mdx',
        'api-reference.mdx',
        'quickstart.mdx',
        'getting-started.mdx',
        'getting_started.mdx',
        'index.mdx'
    ]
    
    fixed_count = 0
    for pattern in target_files:
        files = glob.glob(pattern)
        for file_path in files:
            if restore_breadcrumbs(file_path):
                fixed_count += 1
    
    print(f"Restored breadcrumbs in {fixed_count} files")

if __name__ == "__main__":
    main()
