#!/usr/bin/env python3
"""
Fix All Broken Titles Script
Aggressively finds and fixes ALL title/description issues throughout the project
"""

import re
from pathlib import Path

def fix_file_aggressive(file_path):
    """Aggressively fix all frontmatter issues in a single file"""
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
        
        # Store original for comparison
        original_frontmatter = frontmatter_content
        
        # Fix ALL possible broken patterns - be very aggressive
        
        # Pattern 1: title with extra quotes and line breaks (most common)
        frontmatter_content = re.sub(
            r"title: '\s*'([^']+)'\s*'\s*\n\s*description: '([^']+)'",
            r"title: '\1'\ndescription: '\2'",
            frontmatter_content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        # Pattern 2: title with extra quotes only
        frontmatter_content = re.sub(
            r"title: '\s*'([^']+)'\s*'",
            r"title: '\1'",
            frontmatter_content
        )
        
        # Pattern 3: description with extra quotes only
        frontmatter_content = re.sub(
            r"description: '\s*'([^']+)'\s*'",
            r"description: '\1'",
            frontmatter_content
        )
        
        # Pattern 4: Fix any remaining broken patterns with multiline
        frontmatter_content = re.sub(
            r"title: '\s*([^']*)\s*'\s*\n\s*description: '\s*([^']*)\s*'\s*'",
            r"title: '\1'\ndescription: '\2'",
            frontmatter_content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        # Pattern 5: Fix any remaining quotes issues
        frontmatter_content = re.sub(r"title: '\s*([^']*)\s*'\s*$", r"title: '\1'", frontmatter_content, flags=re.MULTILINE)
        frontmatter_content = re.sub(r"description: '\s*([^']*)\s*'\s*$", r"description: '\1'", frontmatter_content, flags=re.MULTILINE)
        
        # Pattern 6: Fix any remaining broken patterns
        frontmatter_content = re.sub(
            r"title: '\s*'([^']+)'\s*'\s*\n\s*description: '\s*'([^']+)'\s*'",
            r"title: '\1'\ndescription: '\2'",
            frontmatter_content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        # Clean up any extra whitespace
        frontmatter_content = re.sub(r'\n\s*\n', '\n', frontmatter_content)
        frontmatter_content = frontmatter_content.strip()
        
        # Check if we made any changes
        if frontmatter_content != original_frontmatter:
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
    
    print("🔧 AGGRESSIVELY fixing ALL frontmatter issues throughout the entire project...")
    
    # Find all MDX files
    mdx_files = list(base_dir.rglob("*.mdx"))
    
    print(f"📁 Found {len(mdx_files)} MDX files")
    
    fixed_count = 0
    broken_files = []
    
    for file_path in mdx_files:
        # First check if file has broken patterns
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for broken patterns
            has_broken_patterns = (
                re.search(r"title: '\s*'[^']+'\s*'", content) or
                re.search(r"description: '\s*'[^']+'\s*'", content) or
                re.search(r"title: '\s*'[^']+'\s*'\s*\n\s*description:", content)
            )
            
            if has_broken_patterns:
                broken_files.append(file_path.name)
                print(f"🔍 Found broken patterns in: {file_path.name}")
                
                if fix_file_aggressive(file_path):
                    print(f"✅ Fixed: {file_path.name}")
                    fixed_count += 1
                else:
                    print(f"❌ Failed to fix: {file_path.name}")
        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {e}")
    
    print(f"\n🎉 Fixed {fixed_count} files out of {len(broken_files)} files with issues")
    
    if broken_files:
        print(f"\n📋 Files that had broken patterns:")
        for file_name in broken_files:
            print(f"   - {file_name}")
    
    # Final verification
    print("\n🔍 Final verification...")
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
