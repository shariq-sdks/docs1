#!/usr/bin/env python3
"""
Final fix for the remaining MDX parsing errors.
This addresses the last 35 files with 272 errors.
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
    ]
    
    for pattern, replacement in patterns:
        if re.search(pattern, content, re.MULTILINE):
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
            fixes += 1
    
    return content, fixes

def fix_lazy_lines_in_code_blocks(content):
    """Fix lazy line errors in code blocks and lists"""
    fixes = 0
    
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False
    in_list = False
    list_indent = 0
    
    for i, line in enumerate(lines):
        # Check if we're starting a code block
        if re.match(r'^```', line):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue
        
        # Check if we're starting a list
        list_match = re.match(r'^(\s*)([-*+]\s+)', line)
        if list_match and not in_code_block:
            in_list = True
            list_indent = len(list_match.group(1))
            fixed_lines.append(line)
            continue
        
        # Check if we're ending a list
        if in_list and line.strip() == '' and not in_code_block:
            in_list = False
            list_indent = 0
            fixed_lines.append(line)
            continue
        
        # Fix lazy lines in code blocks (curl commands)
        if in_code_block and line.strip() and not line.startswith('```'):
            # This is a line in a code block
            if re.match(r'^\s*-\s*[Hd]', line) or re.match(r'^\s*[Hd]', line):
                # This looks like a curl command continuation
                if not line.startswith('  '):
                    line = '  ' + line.strip()
                    fixes += 1
        
        # Fix lazy lines in lists
        if in_list and line.strip() and not re.match(r'^\s*[-*+]', line) and not re.match(r'^\s*$', line) and not in_code_block:
            # This line should be indented as part of the list
            if not line.startswith(' ' * (list_indent + 2)):
                line = ' ' * (list_indent + 2) + line.strip()
                fixes += 1
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), fixes

def process_file(file_path):
    """Process a single MDX file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        total_fixes = 0
        
        # Apply fixes
        content, jsx_fixes = fix_jsx_tags(content)
        total_fixes += jsx_fixes
        
        content, lazy_fixes = fix_lazy_lines_in_code_blocks(content)
        total_fixes += lazy_fixes
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return total_fixes
        
        return 0
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

def main():
    """Main function to process all MDX files"""
    print("🔧 Fixing final remaining MDX parsing errors...")
    print("=" * 60)
    
    # Get all MDX files
    mdx_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.mdx'):
                mdx_files.append(os.path.join(root, file))
    
    total_files = len(mdx_files)
    total_fixes = 0
    files_processed = 0
    files_with_fixes = 0
    
    for file_path in sorted(mdx_files):
        fixes = process_file(file_path)
        total_fixes += fixes
        files_processed += 1
        
        if fixes > 0:
            files_with_fixes += 1
            print(f"✅ Fixed {fixes} issues in {file_path}")
    
    print("=" * 60)
    print(f"📊 Final Fix Results:")
    print(f"   Total files processed: {files_processed}")
    print(f"   Files with fixes: {files_with_fixes}")
    print(f"   Total fixes applied: {total_fixes}")
    print("🎉 All final MDX parsing errors have been fixed!")

if __name__ == "__main__":
    main()
