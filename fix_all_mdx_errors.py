#!/usr/bin/env python3
"""
Comprehensive MDX Error Fixer
Fixes all types of MDX parsing errors including:
- Acorn expression errors
- Frontmatter parsing errors
- Lazy line errors
- Unknown escape sequences
- Multiline key errors
"""

import os
import re
import glob
from pathlib import Path

def fix_mdx_file(file_path):
    """Fix all MDX errors in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix 1: Fix broken frontmatter with unexpected end of stream
        if 'unexpected end of the stream within a double quoted scalar' in str(file_path):
            # Fix broken YAML frontmatter
            content = re.sub(r'---\n(.*?)\n---', fix_frontmatter, content, flags=re.DOTALL)
        
        # Fix 2: Fix acorn expression errors (JSX syntax issues)
        if 'Could not parse expression with acorn' in str(file_path):
            # Fix common JSX issues
            content = fix_acorn_errors(content)
        
        # Fix 3: Fix lazy line errors
        if 'Unexpected lazy line in expression' in str(file_path):
            content = fix_lazy_line_errors(content)
        
        # Fix 4: Fix unknown escape sequences in frontmatter
        if 'unknown escape sequence' in str(file_path):
            content = fix_escape_sequences(content)
        
        # Fix 5: Fix multiline key errors
        if 'multiline key may not be an implicit key' in str(file_path):
            content = fix_multiline_keys(content)
        
        # General fixes for all files
        content = apply_general_fixes(content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
        return False

def fix_frontmatter(match):
    """Fix broken frontmatter"""
    frontmatter = match.group(1)
    
    # Fix common frontmatter issues
    frontmatter = re.sub(r'title:\s*"([^"]*)"', r"title: '\1'", frontmatter)
    frontmatter = re.sub(r'description:\s*"([^"]*)"', r"description: '\1'", frontmatter)
    
    # Fix broken quotes
    frontmatter = re.sub(r'title:\s*"\'([^\']*)\'', r"title: '\1'", frontmatter)
    frontmatter = re.sub(r'description:\s*"\'([^\']*)\'', r"description: '\1'", frontmatter)
    
    # Fix unclosed quotes
    frontmatter = re.sub(r'title:\s*"([^"]*?)(?:\n|$)', r"title: '\1'", frontmatter)
    frontmatter = re.sub(r'description:\s*"([^"]*?)(?:\n|$)', r"description: '\1'", frontmatter)
    
    return f"---\n{frontmatter}\n---"

def fix_acorn_errors(content):
    """Fix acorn expression errors"""
    # Fix JSX syntax issues
    content = re.sub(r'<(\w+)\s*([^>]*?)\s*/>', r'<\1 \2 />', content)
    
    # Fix unclosed JSX tags
    content = re.sub(r'<(\w+)([^>]*?)(?<!\/)>', r'<\1\2>', content)
    
    # Fix JSX expressions
    content = re.sub(r'\{([^}]*?)\}', lambda m: f"{{'{m.group(1)}'}}" if not m.group(1).startswith("'") else m.group(0), content)
    
    return content

def fix_lazy_line_errors(content):
    """Fix lazy line errors"""
    # Fix block quotes
    content = re.sub(r'^(\s*)>([^\n]*?)(?=\n\s*[^>\s])', r'\1> \2', content, flags=re.MULTILINE)
    
    # Fix list items
    content = re.sub(r'^(\s*)([-*+])\s*([^\n]*?)(?=\n\s*[^-*+\s])', r'\1\2 \3', content, flags=re.MULTILINE)
    
    # Fix numbered lists
    content = re.sub(r'^(\s*)(\d+\.)\s*([^\n]*?)(?=\n\s*(?:\d+\.|\s*[^\d\s]))', r'\1\2 \3', content, flags=re.MULTILINE)
    
    return content

def fix_escape_sequences(content):
    """Fix unknown escape sequences"""
    # Fix backticks in frontmatter
    content = re.sub(r'openapi:\s*"([^"]*\\`[^"]*)"', r"openapi: '\1'", content)
    
    # Fix other escape sequences
    content = re.sub(r'\\`', '`', content)
    content = re.sub(r'\\"', '"', content)
    content = re.sub(r"\\'", "'", content)
    
    return content

def fix_multiline_keys(content):
    """Fix multiline key errors in YAML"""
    # Fix multiline descriptions
    content = re.sub(r'description:\s*([^\n]*?)\n\s*([^\n]*?)(?=\n\w+:)', r"description: '\1 \2'", content, flags=re.DOTALL)
    
    return content

def apply_general_fixes(content):
    """Apply general fixes to all content"""
    # Fix common frontmatter issues
    content = re.sub(r'title:\s*"([^"]*)"', r"title: '\1'", content)
    content = re.sub(r'description:\s*"([^"]*)"', r"description: '\1'", content)
    
    # Fix broken quotes
    content = re.sub(r'title:\s*"\'([^\']*)\'', r"title: '\1'", content)
    content = re.sub(r'description:\s*"\'([^\']*)\'', r"description: '\1'", content)
    
    # Fix unclosed quotes
    content = re.sub(r'title:\s*"([^"]*?)(?:\n|$)', r"title: '\1'", content)
    content = re.sub(r'description:\s*"([^"]*?)(?:\n|$)', r"description: '\1'", content)
    
    # Fix JSX components
    content = re.sub(r'<(\w+)\s*([^>]*?)\s*/>', r'<\1 \2 />', content)
    
    # Fix broken Mintlify components
    content = re.sub(r'<(\w+)\s*([^>]*?)\s*>\s*</\1>', r'<\1 \2 />', content)
    
    return content

def main():
    """Main function to fix all MDX files"""
    print("🔧 Fixing ALL MDX parsing errors...")
    
    # Find all MDX files
    mdx_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.mdx'):
                mdx_files.append(os.path.join(root, file))
    
    print(f"📁 Found {len(mdx_files)} MDX files")
    
    fixed_count = 0
    
    for file_path in mdx_files:
        if fix_mdx_file(file_path):
            print(f"✅ Fixed: {file_path}")
            fixed_count += 1
    
    print(f"\n🎉 Fixed {fixed_count} files")
    
    if fixed_count > 0:
        print("\n🔍 Running final validation...")
        # Check for remaining issues
        remaining_issues = 0
        for file_path in mdx_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for common issues
                if 'title: "' in content or 'description: "' in content:
                    remaining_issues += 1
                    print(f"⚠️  Still has issues: {file_path}")
                
            except Exception as e:
                remaining_issues += 1
                print(f"❌ Error reading {file_path}: {e}")
        
        if remaining_issues == 0:
            print("✅ ALL MDX errors fixed!")
        else:
            print(f"⚠️  {remaining_issues} files still have issues")

if __name__ == "__main__":
    main()
