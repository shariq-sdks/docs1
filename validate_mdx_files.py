#!/usr/bin/env python3
"""
Comprehensive validation script to check for all types of MDX parsing errors.
This will catch any remaining issues that might have been missed.
"""

import os
import re
import yaml
from pathlib import Path

def validate_frontmatter(content):
    """Validate frontmatter YAML"""
    errors = []
    
    # Extract frontmatter
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not frontmatter_match:
        return errors
    
    frontmatter_content = frontmatter_match.group(1)
    
    try:
        yaml.safe_load(frontmatter_content)
    except yaml.YAMLError as e:
        errors.append(f"YAML Error: {e}")
    
    return errors

def validate_jsx_expressions(content):
    """Validate JSX expressions for acorn parsing"""
    errors = []
    
    # Check for malformed JSX expressions
    patterns = [
        r'{\s*`\s*`\s*<\s*`',  # Malformed JSX with backticks
        r'</\s*`\s*}\s*`',     # Malformed closing tags
        r'{\s*`\s*`\s*}',      # Empty backtick expressions
        r'Info>\s*$',          # Missing opening <
        r'^\s*/\s*$',          # Orphaned closing slashes
    ]
    
    for i, line in enumerate(content.split('\n'), 1):
        for pattern in patterns:
            if re.search(pattern, line):
                errors.append(f"Line {i}: Malformed JSX - {line.strip()}")
    
    return errors

def validate_markdown_syntax(content):
    """Validate Markdown syntax"""
    errors = []
    
    lines = content.split('\n')
    in_list = False
    in_blockquote = False
    
    for i, line in enumerate(lines, 1):
        # Check for lazy line errors in lists
        if re.match(r'^\s*[-*+]\s+', line):
            in_list = True
        elif line.strip() == '':
            in_list = False
        elif in_list and line.strip() and not re.match(r'^\s+', line) and not re.match(r'^\s*[-*+]\s+', line):
            errors.append(f"Line {i}: Lazy line in list - {line.strip()}")
        
        # Check for lazy line errors in blockquotes
        if re.match(r'^\s*>', line):
            in_blockquote = True
        elif line.strip() == '':
            in_blockquote = False
        elif in_blockquote and line.strip() and not re.match(r'^\s*>', line):
            errors.append(f"Line {i}: Lazy line in blockquote - {line.strip()}")
    
    return errors

def validate_character_encoding(content):
    """Validate character encoding issues"""
    errors = []
    
    # Check for invisible characters
    if '\ufeff' in content:
        errors.append("BOM character found")
    
    # Check for control characters
    control_chars = re.findall(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', content)
    if control_chars:
        errors.append(f"Control characters found: {len(control_chars)} instances")
    
    # Check for backticked numbers that might cause issues
    backticked_numbers = re.findall(r'`\d+`', content)
    if backticked_numbers:
        errors.append(f"Backticked numbers found: {backticked_numbers}")
    
    return errors

def validate_file(file_path):
    """Validate a single MDX file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        all_errors = []
        
        # Run all validations
        all_errors.extend(validate_frontmatter(content))
        all_errors.extend(validate_jsx_expressions(content))
        all_errors.extend(validate_markdown_syntax(content))
        all_errors.extend(validate_character_encoding(content))
        
        return all_errors
        
    except Exception as e:
        return [f"File read error: {e}"]

def main():
    """Main validation function"""
    print("🔍 Comprehensive MDX validation starting...")
    print("=" * 60)
    
    # Get all MDX files
    mdx_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.mdx'):
                mdx_files.append(os.path.join(root, file))
    
    total_files = len(mdx_files)
    files_with_errors = 0
    total_errors = 0
    
    print(f"📁 Found {total_files} MDX files to validate")
    print()
    
    for file_path in sorted(mdx_files):
        errors = validate_file(file_path)
        
        if errors:
            files_with_errors += 1
            total_errors += len(errors)
            print(f"❌ {file_path}")
            for error in errors:
                print(f"   • {error}")
            print()
        else:
            print(f"✅ {file_path}")
    
    print("=" * 60)
    print(f"📊 Validation Results:")
    print(f"   Total files: {total_files}")
    print(f"   Files with errors: {files_with_errors}")
    print(f"   Total errors: {total_errors}")
    
    if files_with_errors == 0:
        print("🎉 All MDX files are valid! No parsing errors found.")
    else:
        print(f"⚠️  Found {files_with_errors} files with {total_errors} errors total.")
    
    return files_with_errors == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
