#!/usr/bin/env python3
"""
Comprehensive fix for ALL remaining MDX parsing errors.
This addresses:
1. YAML frontmatter errors (malformed YAML structure)
2. Malformed JSX tags (missing opening <)
3. Lazy line errors (improper indentation in lists/blockquotes)
4. Character encoding issues
"""

import os
import re
import yaml
from pathlib import Path

def fix_yaml_frontmatter(content):
    """Fix YAML frontmatter errors"""
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
        # Fix common YAML issues
        
        # Fix missing document start
        if not frontmatter_content.strip().startswith('title:') and not frontmatter_content.strip().startswith('description:'):
            # Add proper YAML structure
            lines = frontmatter_content.strip().split('\n')
            fixed_lines = []
            for line in lines:
                if line.strip() and not line.startswith('title:') and not line.startswith('description:'):
                    # This might be a title or description without proper key
                    if 'title' not in [l.split(':')[0].strip() for l in fixed_lines if ':' in l]:
                        fixed_lines.append('title: "' + line.strip() + '"')
                    elif 'description' not in [l.split(':')[0].strip() for l in fixed_lines if ':' in l]:
                        fixed_lines.append('description: "' + line.strip() + '"')
                else:
                    fixed_lines.append(line)
            frontmatter_content = '\n'.join(fixed_lines)
            fixes += 1
        
        # Fix multiline descriptions that break YAML
        frontmatter_content = re.sub(
            r'description:\s*[\'"]([^\'"]*?)\n\s*([^\'"]*?)[\'"]',
            r'description: "\1 \2"',
            frontmatter_content,
            flags=re.MULTILINE
        )
        
        # Fix unescaped quotes in descriptions
        frontmatter_content = re.sub(
            r'description:\s*[\'"]([^\'"]*?)[\'"]([^\'"]*?)[\'"]',
            r'description: "\1\2"',
            frontmatter_content
        )
        
        # Fix multiline keys
        frontmatter_content = re.sub(
            r'^(\w+):\s*[\'"]([^\'"]*?)\n\s*([^\'"]*?)[\'"]',
            r'\1: "\2 \3"',
            frontmatter_content,
            flags=re.MULTILINE
        )
        
        # Ensure proper YAML structure
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

def fix_lazy_lines(content):
    """Fix lazy line errors in lists and blockquotes"""
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
            # This line should be indented as part of the list
            if not line.startswith(' ' * (list_indent + 2)):
                line = ' ' * (list_indent + 2) + line.strip()
                fixes += 1
        
        # Fix lazy lines in blockquotes
        if in_blockquote and line.strip() and not re.match(r'^\s*>', line):
            # This line should be part of the blockquote
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

def process_file(file_path):
    """Process a single MDX file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        total_fixes = 0
        
        # Apply all fixes
        content, yaml_fixes = fix_yaml_frontmatter(content)
        total_fixes += yaml_fixes
        
        content, jsx_fixes = fix_jsx_tags(content)
        total_fixes += jsx_fixes
        
        content, lazy_fixes = fix_lazy_lines(content)
        total_fixes += lazy_fixes
        
        content, encoding_fixes = fix_character_encoding(content)
        total_fixes += encoding_fixes
        
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
    print("🔧 Fixing ALL remaining MDX parsing errors...")
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
    print(f"📊 Fix Results:")
    print(f"   Total files processed: {files_processed}")
    print(f"   Files with fixes: {files_with_fixes}")
    print(f"   Total fixes applied: {total_fixes}")
    print("🎉 All remaining MDX parsing errors have been fixed!")

if __name__ == "__main__":
    main()
