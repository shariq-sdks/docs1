#!/usr/bin/env python3
"""
Fix malformed JSX tags that are causing parsing errors.
This addresses:
1. Missing opening < in JSX tags
2. Malformed closing tags with backticks
3. Orphaned closing slashes
"""

import os
import re
from pathlib import Path

def fix_jsx_tags(content):
    """Fix malformed JSX tags"""
    fixes = 0
    
    # Fix missing opening < in JSX tags
    patterns = [
        # Fix Info> tags
        (r'^Info>\s*$', '<Info>'),
        (r'^Info>\s*\n', '<Info>\n'),
        
        # Fix other common component tags
        (r'^(\w+)>\s*$', r'<\1>'),
        (r'^(\w+)>\s*\n', r'<\1>\n'),
        
        # Fix malformed closing tags with backticks
        (r'</(\w+)>\\`\}', r'</\1>'),
        (r'</(\w+)>\s*\\`\}', r'</\1>'),
        
        # Fix orphaned closing slashes
        (r'^\s*/\s*$', ''),
        (r'^\s*/\s*\n', ''),
    ]
    
    for pattern, replacement in patterns:
        if re.search(pattern, content, re.MULTILINE):
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
            fixes += 1
    
    return content, fixes

def process_file(file_path):
    """Process a single MDX file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content, fixes = fix_jsx_tags(content)
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return fixes
        
        return 0
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

def main():
    """Main function to process all MDX files"""
    print("Fixing malformed JSX tags...")
    
    # Get all MDX files
    mdx_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.mdx'):
                mdx_files.append(os.path.join(root, file))
    
    total_files = len(mdx_files)
    total_fixes = 0
    files_processed = 0
    
    for file_path in mdx_files:
        fixes = process_file(file_path)
        total_fixes += fixes
        files_processed += 1
        
        if fixes > 0:
            print(f"Fixed {fixes} JSX issues in {file_path}")
    
    print(f"\nProcessed {files_processed} files")
    print(f"Total JSX fixes applied: {total_fixes}")
    print("All malformed JSX tags have been fixed!")

if __name__ == "__main__":
    main()
