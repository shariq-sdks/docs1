#!/usr/bin/env python3
import os
import re
import yaml
import glob

def fix_acorn_errors(file_path):
    """Fix JavaScript expression parsing errors (acorn)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix common acorn errors
        # 1. Fix malformed JSX expressions with backticks
        content = re.sub(r'\{`[^`]*`\}', '', content)
        content = re.sub(r'\{\`[^`]*\`\}', '', content)
        content = re.sub(r'\{`[^`]*<\`\}', '', content)
        content = re.sub(r'\{\`[^`]*<\`\}', '', content)
        
        # 2. Fix malformed JSX with backticks and angle brackets
        content = re.sub(r'\{`[^`]*<\`[^`]*\`\}', '', content)
        content = re.sub(r'\{\`[^`]*<\`[^`]*\`\}', '', content)
        
        # 3. Fix any remaining malformed expressions
        content = re.sub(r'\{[^}]*`[^}]*\}', '', content)
        content = re.sub(r'\{[^}]*\`[^}]*\}', '', content)
        
        # 4. Remove any remaining problematic characters in expressions
        content = re.sub(r'\{[^}]*[`\\][^}]*\}', '', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed acorn errors in {file_path}")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing acorn errors in {file_path}: {e}")
        return False

def fix_lazy_line_errors(file_path):
    """Fix lazy line markdown parsing errors"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        lines = content.split('\n')
        fixed_lines = []
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check for lazy line issues
            if line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                # Check if this line should be part of a list or blockquote
                if i > 0:
                    prev_line = lines[i-1].strip()
                    if prev_line.endswith(':') or prev_line.endswith('*') or prev_line.endswith('-'):
                        # This might be a lazy line in a list
                        if not line.startswith('  ') and not line.startswith('\t'):
                            # Add proper indentation
                            line = '  ' + line
                    elif prev_line.startswith('>'):
                        # This might be a lazy line in a blockquote
                        if not line.startswith('>') and not line.startswith('  '):
                            line = '> ' + line
            
            fixed_lines.append(line)
            i += 1
        
        fixed_content = '\n'.join(fixed_lines)
        
        if fixed_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"Fixed lazy line errors in {file_path}")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing lazy line errors in {file_path}: {e}")
        return False

def fix_frontmatter_errors(file_path):
    """Fix YAML frontmatter parsing errors"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not frontmatter_match:
            return False
        
        frontmatter_content = frontmatter_match.group(1)
        body_content = content[frontmatter_match.end():]
        
        # Fix common YAML issues
        fixed_frontmatter = frontmatter_content
        
        # 1. Fix multiline keys
        fixed_frontmatter = re.sub(r'^(\w+):\s*\n\s*([^\n]+)$', r'\1: "\2"', fixed_frontmatter, flags=re.MULTILINE)
        
        # 2. Fix unquoted values with special characters
        fixed_frontmatter = re.sub(r'^(\w+):\s*([^"\n][^"\n]*[^"\n\s])\s*$', r'\1: "\2"', fixed_frontmatter, flags=re.MULTILINE)
        
        # 3. Fix values that start with numbers or special characters
        fixed_frontmatter = re.sub(r'^(\w+):\s*([0-9][^\n]*)\s*$', r'\1: "\2"', fixed_frontmatter, flags=re.MULTILINE)
        
        # 4. Fix values with colons
        fixed_frontmatter = re.sub(r'^(\w+):\s*([^"\n]*:[^"\n]*)\s*$', r'\1: "\2"', fixed_frontmatter, flags=re.MULTILINE)
        
        # 5. Fix values with quotes
        fixed_frontmatter = re.sub(r'^(\w+):\s*([^"\n]*"[^"\n]*)\s*$', r'\1: "\2"', fixed_frontmatter, flags=re.MULTILINE)
        
        # 6. Ensure all values are properly quoted
        lines = fixed_frontmatter.split('\n')
        fixed_lines = []
        for line in lines:
            if ':' in line and not line.strip().startswith('#'):
                parts = line.split(':', 1)
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    if value and not (value.startswith('"') and value.endswith('"')):
                        if not (value.startswith("'") and value.endswith("'")):
                            # Escape any quotes in the value
                            value = value.replace('"', '\\"')
                            line = f'{key}: "{value}"'
            fixed_lines.append(line)
        
        fixed_frontmatter = '\n'.join(fixed_lines)
        
        if fixed_frontmatter != frontmatter_content:
            new_content = f"---\n{fixed_frontmatter}\n---\n{body_content}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed frontmatter errors in {file_path}")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing frontmatter errors in {file_path}: {e}")
        return False

def fix_specific_files():
    """Fix specific files with known issues"""
    
    # Fix result-codes.mdx frontmatter issue
    result_codes_path = 'reference/result-codes.mdx'
    if os.path.exists(result_codes_path):
        try:
            with open(result_codes_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix the specific frontmatter issue
            content = re.sub(
                r"description: 'Interpreting the meaning behi[^']*'",
                'description: "Interpreting the meaning behind Authlete\'s API result codes"',
                content
            )
            
            with open(result_codes_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Fixed specific issue in {result_codes_path}")
            
        except Exception as e:
            print(f"Error fixing {result_codes_path}: {e}")

def fix_all_mdx_files():
    """Fix all MDX files with various errors"""
    
    # Get all MDX files
    mdx_files = glob.glob('**/*.mdx', recursive=True)
    
    # Skip node_modules and other directories
    mdx_files = [f for f in mdx_files if 'node_modules' not in f]
    
    acorn_fixed = 0
    lazy_line_fixed = 0
    frontmatter_fixed = 0
    
    for file_path in mdx_files:
        print(f"Processing {file_path}...")
        
        # Fix acorn errors
        if fix_acorn_errors(file_path):
            acorn_fixed += 1
        
        # Fix lazy line errors
        if fix_lazy_line_errors(file_path):
            lazy_line_fixed += 1
        
        # Fix frontmatter errors
        if fix_frontmatter_errors(file_path):
            frontmatter_fixed += 1
    
    # Fix specific files
    fix_specific_files()
    
    print(f"\nSummary:")
    print(f"Fixed acorn errors in {acorn_fixed} files")
    print(f"Fixed lazy line errors in {lazy_line_fixed} files")
    print(f"Fixed frontmatter errors in {frontmatter_fixed} files")

def main():
    print("Fixing all MDX parsing errors...")
    fix_all_mdx_files()
    print("All MDX files have been processed!")

if __name__ == "__main__":
    main()