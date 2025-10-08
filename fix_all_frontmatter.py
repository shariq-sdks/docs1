#!/usr/bin/env python3
"""
Fix All Frontmatter Script
Comprehensively fixes title/description issues throughout the entire project
"""

import re
import os
from pathlib import Path

def fix_frontmatter_comprehensive(file_path):
    """Fix frontmatter comprehensively for a single file"""
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
        
        # Fix all possible broken patterns
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
    
    print("🔧 Fixing ALL frontmatter issues throughout the project...")
    
    # Find all MDX files
    mdx_files = list(base_dir.rglob("*.mdx"))
    
    print(f"📁 Found {len(mdx_files)} MDX files")
    
    fixed_count = 0
    broken_files = []
    
    for file_path in mdx_files:
        if fix_frontmatter_comprehensive(file_path):
            print(f"✅ Fixed: {file_path.name}")
            fixed_count += 1
        else:
            # Check if file still has issues
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if re.search(r"title: '\s*'[^']+'\s*'", content) or re.search(r"description: '\s*'[^']+'\s*'", content):
                    broken_files.append(file_path.name)
            except:
                pass
    
    print(f"\n🎉 Fixed {fixed_count} files")
    
    if broken_files:
        print(f"\n⚠️  Still found issues in {len(broken_files)} files:")
        for file_name in broken_files:
            print(f"   - {file_name}")
    else:
        print("\n✅ No more frontmatter issues found!")

if __name__ == "__main__":
    main()
