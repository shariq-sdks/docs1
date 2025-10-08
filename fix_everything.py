#!/usr/bin/env python3
"""
Fix Everything Script
Comprehensively fixes all frontmatter issues throughout the entire project
"""

import re
from pathlib import Path

def fix_file(file_path):
    """Fix all frontmatter issues in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Check if file has frontmatter
        if not content.startswith('---'):
            return False
        
        # Find the end of frontmatter
        lines = content.split('\n')
        if len(lines) < 3 or lines[0] != '---':
            return False
        
        # Find the closing ---
        end_index = -1
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                end_index = i
                break
        
        if end_index == -1:
            return False
        
        # Extract frontmatter
        frontmatter_lines = lines[1:end_index]
        frontmatter_content = '\n'.join(frontmatter_lines)
        
        # Fix ALL possible broken patterns
        fixes_applied = False
        
        # Pattern 1: title with extra quotes and line breaks
        if re.search(r"title: '\s*'[^']+'\s*'\s*\n\s*description:", frontmatter_content):
            frontmatter_content = re.sub(
                r"title: '\s*'([^']+)'\s*'\s*\n\s*description: '([^']+)'",
                r"title: '\1'\ndescription: '\2'",
                frontmatter_content,
                flags=re.MULTILINE | re.DOTALL
            )
            fixes_applied = True
        
        # Pattern 2: title with extra quotes only
        if re.search(r"title: '\s*'[^']+'\s*'", frontmatter_content):
            frontmatter_content = re.sub(
                r"title: '\s*'([^']+)'\s*'",
                r"title: '\1'",
                frontmatter_content
            )
            fixes_applied = True
        
        # Pattern 3: description with extra quotes only
        if re.search(r"description: '\s*'[^']+'\s*'", frontmatter_content):
            frontmatter_content = re.sub(
                r"description: '\s*'([^']+)'\s*'",
                r"description: '\1'",
                frontmatter_content
            )
            fixes_applied = True
        
        # Pattern 4: Fix any remaining broken patterns with multiline
        if re.search(r"title: '\s*([^']*)\s*'\s*\n\s*description: '\s*([^']*)\s*'\s*'", frontmatter_content):
            frontmatter_content = re.sub(
                r"title: '\s*([^']*)\s*'\s*\n\s*description: '\s*([^']*)\s*'\s*'",
                r"title: '\1'\ndescription: '\2'",
                frontmatter_content,
                flags=re.MULTILINE | re.DOTALL
            )
            fixes_applied = True
        
        # Pattern 5: Fix any remaining quotes issues
        frontmatter_content = re.sub(r"title: '\s*([^']*)\s*'\s*$", r"title: '\1'", frontmatter_content, flags=re.MULTILINE)
        frontmatter_content = re.sub(r"description: '\s*([^']*)\s*'\s*$", r"description: '\1'", frontmatter_content, flags=re.MULTILINE)
        
        # Clean up any extra whitespace
        frontmatter_content = re.sub(r'\n\s*\n', '\n', frontmatter_content)
        frontmatter_content = frontmatter_content.strip()
        
        if fixes_applied or frontmatter_content != '\n'.join(lines[1:end_index]):
            # Rebuild the file
            new_content = '---\n' + frontmatter_content + '\n---\n' + '\n'.join(lines[end_index + 1:])
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Fix all MDX files with frontmatter issues"""
    base_dir = Path("/Users/muhammadshariqnazr/Downloads/new-api-doc")
    
    print("🔧 Fixing ALL frontmatter issues throughout the entire project...")
    
    # Find all MDX files
    mdx_files = list(base_dir.rglob("*.mdx"))
    
    print(f"📁 Found {len(mdx_files)} MDX files")
    
    fixed_count = 0
    
    for file_path in mdx_files:
        if fix_file(file_path):
            print(f"✅ Fixed: {file_path.name}")
            fixed_count += 1
    
    print(f"\n🎉 Fixed {fixed_count} files")
    
    # Final check for remaining issues
    print("\n🔍 Final check for remaining issues...")
    remaining_issues = 0
    
    for file_path in mdx_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for any remaining broken patterns
            if (re.search(r"title: '\s*'[^']+'\s*'", content) or 
                re.search(r"description: '\s*'[^']+'\s*'", content) or
                re.search(r"title: '\s*'[^']+'\s*'\s*\n\s*description:", content)):
                print(f"⚠️  Still broken: {file_path.name}")
                remaining_issues += 1
        except:
            pass
    
    if remaining_issues == 0:
        print("✅ ALL frontmatter issues fixed! No more broken patterns found!")
    else:
        print(f"⚠️  Found {remaining_issues} files still with issues")

if __name__ == "__main__":
    main()
