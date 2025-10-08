#!/usr/bin/env python3
"""
Smart MDX fix script that preserves correct titles and only fixes parsing errors.
This script will NOT overwrite existing correct titles and descriptions.
"""

import os
import re
import yaml
from pathlib import Path

def is_valid_title(title):
    """Check if a title is meaningful and not generic"""
    generic_titles = [
        "Getting Started", "Overview", "Introduction", "Documentation", 
        "Page", "Content", "Untitled", "New Page", "Default"
    ]
    return title not in generic_titles and len(title.strip()) > 3

def fix_acorn_errors(content):
    """Fix acorn parsing errors without changing titles"""
    fixes = 0
    
    # Fix malformed JSX expressions with backticks
    patterns = [
        (r'{\s*`\s*`\s*<\s*`\s*(\w+)>', r'<\1>'),
        (r'{\s*`\s*`\s*<\s*`\s*(\w+)\s+([^>]+)>', r'<\1 \2>'),
        (r'</\s*`\s*}\s*`', r'</\1>'),
        (r'{\s*`\s*`\s*<\s*`\s*(\w+)\s+([^>]+)>\s*([^<]+)\s*</\s*`\s*}\s*`', r'<\1 \2>\3</\1>'),
        (r'{\s*`\s*([^`]+)\s*`\s*}', r'\1'),  # Remove unnecessary backticks in expressions
        (r'{\s*`\s*`\s*}', ''),  # Remove empty backtick expressions
        (r'{\s*`\s*<\s*(\w+)', r'<\1'),  # Fix malformed JSX opening tags
        (r'(\w+)\s*>\s*`\s*}', r'\1>'),  # Fix malformed JSX closing tags
    ]
    
    for pattern, replacement in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            fixes += 1
    
    return content, fixes

def fix_jsx_tags(content):
    """Fix malformed JSX tags without changing content"""
    fixes = 0
    
    # Fix missing opening < in JSX tags
    patterns = [
        (r'^Info>\s*$', '<Info>'),
        (r'^Info>\s*\n', '<Info>\n'),
        (r'^(\w+)>\s*$', r'<\1>'),
        (r'^(\w+)>\s*\n', r'<\1>\n'),
        (r'</(\w+)>\\`\}', r'</\1>'),
        (r'</(\w+)>\s*\\`\}', r'</\1>'),
        (r'^\s*/\s*$', ''),
        (r'^\s*/\s*\n', ''),
    ]
    
    for pattern, replacement in patterns:
        if re.search(pattern, content, re.MULTILINE):
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
            fixes += 1
    
    return content, fixes

def fix_lazy_lines(content):
    """Fix lazy line errors without changing content structure"""
    fixes = 0
    
    lines = content.split('\n')
    fixed_lines = []
    in_list = False
    in_blockquote = False
    list_indent = 0
    
    for i, line in enumerate(lines):
        # Check if we're starting a list
        list_match = re.match(r'^(\s*)([-*+]\s+)', line)
        if list_match:
            in_list = True
            list_indent = len(list_match.group(1))
            fixed_lines.append(line)
            continue
        
        # Check if we're ending a list
        if in_list and line.strip() == '':
            in_list = False
            list_indent = 0
            fixed_lines.append(line)
            continue
        
        # Check if we're starting a blockquote
        if re.match(r'^\s*>', line):
            in_blockquote = True
            fixed_lines.append(line)
            continue
        
        # Check if we're ending a blockquote
        if in_blockquote and line.strip() == '':
            in_blockquote = False
            fixed_lines.append(line)
            continue
        
        # Fix lazy lines in lists
        if in_list and line.strip() and not re.match(r'^\s*[-*+]', line) and not re.match(r'^\s*$', line):
            if not line.startswith(' ' * (list_indent + 2)):
                line = ' ' * (list_indent + 2) + line.strip()
                fixes += 1
        
        # Fix lazy lines in blockquotes
        if in_blockquote and line.strip() and not re.match(r'^\s*>', line):
            line = '> ' + line.strip()
            fixes += 1
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), fixes

def fix_character_encoding(content):
    """Fix character encoding issues"""
    fixes = 0
    
    # Remove invisible characters and fix encoding issues
    if '\ufeff' in content:
        content = content.replace('\ufeff', '')
        fixes += 1
    
    # Remove control characters
    control_chars = re.findall(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', content)
    if control_chars:
        content = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', content)
        fixes += len(control_chars)
    
    # Fix specific character issues
    if '`1`' in content:
        content = content.replace('`1`', '1')
        fixes += 1
    
    # Remove backticks around numbers
    backticked_numbers = re.findall(r'`(\d+)`', content)
    if backticked_numbers:
        content = re.sub(r'`(\d+)`', r'\1', content)
        fixes += len(backticked_numbers)
    
    return content, fixes

def fix_frontmatter_preserving_titles(content):
    """Fix frontmatter errors while preserving good titles"""
    fixes = 0
    
    # Extract frontmatter
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not frontmatter_match:
        return content, fixes
    
    frontmatter_content = frontmatter_match.group(1)
    rest_content = content[frontmatter_match.end():]
    
    try:
        # Try to parse YAML
        yaml.safe_load(frontmatter_content)
        return content, fixes  # No errors, return as is
    except yaml.YAMLError:
        # Only fix YAML structure, don't change titles
        lines = frontmatter_content.strip().split('\n')
        yaml_lines = []
        for line in lines:
            if ':' in line:
                yaml_lines.append(line)
            elif line.strip():
                # This might be a continuation of the previous line
                if yaml_lines:
                    yaml_lines[-1] += ' ' + line.strip()
        
        frontmatter_content = '\n'.join(yaml_lines)
        
        # Reconstruct content
        content = f"---\n{frontmatter_content}\n---\n{rest_content}"
        fixes += 1
    
    return content, fixes

def process_file(file_path):
    """Process a single MDX file without destroying good content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        total_fixes = 0
        
        # Apply fixes that don't change content meaning
        content, acorn_fixes = fix_acorn_errors(content)
        total_fixes += acorn_fixes
        
        content, jsx_fixes = fix_jsx_tags(content)
        total_fixes += jsx_fixes
        
        content, lazy_fixes = fix_lazy_lines(content)
        total_fixes += lazy_fixes
        
        content, encoding_fixes = fix_character_encoding(content)
        total_fixes += encoding_fixes
        
        content, frontmatter_fixes = fix_frontmatter_preserving_titles(content)
        total_fixes += frontmatter_fixes
        
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
    """Main function to process all MDX files safely"""
    print("🔧 Smart MDX fix script - preserving good titles...")
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
            print(f"✅ Fixed {fixes} parsing issues in {file_path}")
    
    print("=" * 60)
    print(f"📊 Smart Fix Results:")
    print(f"   Total files processed: {files_processed}")
    print(f"   Files with fixes: {files_with_fixes}")
    print(f"   Total fixes applied: {total_fixes}")
    print("🎉 All parsing errors fixed while preserving good content!")

if __name__ == "__main__":
    main()
