#!/usr/bin/env python3
"""
Fix Remaining Frontmatter Issues
Fixes the remaining files with broken frontmatter patterns
"""

import re
from pathlib import Path

def fix_file(file_path):
    """Fix a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix the specific pattern we found
        content = re.sub(
            r"title: '\s*'([^']+)'\s*'\s*\n\s*description: '([^']+)'\s*'",
            r"title: '\1'\ndescription: '\2'",
            content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Fix remaining files"""
    files_to_fix = [
        "/Users/muhammadshariqnazr/Downloads/new-api-doc/federation/step-up-authentication.mdx",
        "/Users/muhammadshariqnazr/Downloads/new-api-doc/federation/verifiable-credentials.mdx",
        "/Users/muhammadshariqnazr/Downloads/new-api-doc/concepts/oid4vci.mdx",
        "/Users/muhammadshariqnazr/Downloads/new-api-doc/concepts/stepup_authn.mdx",
        "/Users/muhammadshariqnazr/Downloads/new-api-doc/flows/grant-management.mdx"
    ]
    
    print("🔧 Fixing remaining frontmatter issues...")
    
    fixed_count = 0
    
    for file_path in files_to_fix:
        if fix_file(file_path):
            print(f"✅ Fixed: {Path(file_path).name}")
            fixed_count += 1
    
    print(f"\n🎉 Fixed {fixed_count} files")

if __name__ == "__main__":
    main()
