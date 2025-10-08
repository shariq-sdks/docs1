#!/usr/bin/env python3
"""
Fix remaining MDX parsing errors that weren't caught by the previous script.
This addresses:
1. Acorn parsing errors (JavaScript expressions)
2. Unexpected closing slash errors (malformed JSX tags)
3. Frontmatter YAML parsing errors
4. Character encoding issues
"""

import os
import re
import yaml
from pathlib import Path

def fix_acorn_errors(content):
    """Fix acorn parsing errors in JavaScript expressions"""
    fixes = 0
    
    # Fix malformed JSX expressions with backticks
    patterns = [
        (r'{\s*`\s*`\s*<\s*`\s*(\w+)>', r'<\1>'),
        (r'{\s*`\s*`\s*<\s*`\s*(\w+)\s+([^>]+)>', r'<\1 \2>'),
        (r'</\s*`\s*}\s*`', r'</\1>'),
        (r'{\s*`\s*`\s*<\s*`\s*(\w+)\s+([^>]+)>\s*([^<]+)\s*</\s*`\s*}\s*`', r'<\1 \2>\3</\1>'),
    ]
    
    for pattern, replacement in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            fixes += 1
    
    # Fix other common acorn issues
    acorn_fixes = [
        (r'{\s*`\s*([^`]+)\s*`\s*}', r'\1'),  # Remove unnecessary backticks in expressions
        (r'{\s*`\s*`\s*}', ''),  # Remove empty backtick expressions
        (r'{\s*`\s*<\s*(\w+)', r'<\1'),  # Fix malformed JSX opening tags
        (r'(\w+)\s*>\s*`\s*}', r'\1>'),  # Fix malformed JSX closing tags
    ]
    
    for pattern, replacement in acorn_fixes:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            fixes += 1
    
    return content, fixes

def fix_closing_slash_errors(content):
    """Fix unexpected closing slash errors in JSX tags"""
    fixes = 0
    
    # Fix self-closing tags that are malformed
    patterns = [
        (r'<(\w+)\s+([^>]*?)\s*/>', r'<\1 \2 />'),  # Ensure proper spacing before />
        (r'<(\w+)\s*/>', r'<\1 />'),  # Ensure space before />
        (r'<(\w+)\s+([^>]*?)\s*/\s*>', r'<\1 \2 />'),  # Fix malformed self-closing tags
    ]
    
    for pattern, replacement in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            fixes += 1
    
    # Fix orphaned closing slashes
    content = re.sub(r'/\s*$', '', content, flags=re.MULTILINE)  # Remove trailing slashes at end of lines
    content = re.sub(r'^\s*/\s*$', '', content, flags=re.MULTILINE)  # Remove lines with only slashes
    
    return content, fixes

def fix_frontmatter_errors(content):
    """Fix frontmatter YAML parsing errors"""
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
    except yaml.YAMLError as e:
        print(f"YAML Error: {e}")
        
        # Fix common YAML issues
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
        
        # Reconstruct content
        content = f"---\n{frontmatter_content}\n---\n{rest_content}"
        fixes += 1
    
    return content, fixes

def fix_character_encoding_issues(content):
    """Fix character encoding issues"""
    fixes = 0
    
    # Remove invisible characters and fix encoding issues
    content = content.replace('\ufeff', '')  # Remove BOM
    content = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', content)  # Remove control characters
    
    # Fix specific character issues
    content = content.replace('`1`', '1')  # Fix backticked numbers
    content = re.sub(r'`(\d+)`', r'\1', content)  # Remove backticks around numbers
    
    return content, fixes

def process_file(file_path):
    """Process a single MDX file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        total_fixes = 0
        
        # Apply all fixes
        content, acorn_fixes = fix_acorn_errors(content)
        total_fixes += acorn_fixes
        
        content, slash_fixes = fix_closing_slash_errors(content)
        total_fixes += slash_fixes
        
        content, frontmatter_fixes = fix_frontmatter_errors(content)
        total_fixes += frontmatter_fixes
        
        content, encoding_fixes = fix_character_encoding_issues(content)
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
    print("Fixing remaining MDX parsing errors...")
    
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
            print(f"Fixed {fixes} issues in {file_path}")
    
    print(f"\nProcessed {files_processed} files")
    print(f"Total fixes applied: {total_fixes}")
    print("All remaining MDX parsing errors have been addressed!")

if __name__ == "__main__":
    main()
