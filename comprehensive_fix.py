#!/usr/bin/env python3
"""
Comprehensive Fix Script
Fixes all sidebar title issues and broken image links in one go
"""

import re
import os
from pathlib import Path

def fix_file_titles_and_images(file_path):
    """Fix titles and images in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix common title issues
        title_fixes = {
            # OIDC pages
            'oidc/user-authentication.mdx': ('Getting Started - Authlete', 'User Authentication'),
            'oidc/userinfo-endpoint.mdx': ('Getting Started - Authlete', 'UserInfo Endpoint'),
            'oidc/id-token-handling.mdx': ('Getting Started - Authlete', 'ID Token Handling'),
            'oidc/oidc-best-practices.mdx': ('Getting Started - Authlete', 'OIDC Best Practices'),
            
            # Implementation pages
            'implementation/basic-oauth-flows.mdx': ('Getting Started - Authlete', 'Basic OAuth Flows'),
            
            # Reference pages
            'reference/getting-started.mdx': ('Getting Started - Authlete', 'Getting Started Reference'),
        }
        
        # Get relative path for title matching
        relative_path = str(file_path).replace('/Users/muhammadshariqnazr/Downloads/new-api-doc/', '')
        
        # Fix titles
        if relative_path in title_fixes:
            old_title, new_title = title_fixes[relative_path]
            content = re.sub(
                rf"title: '{re.escape(old_title)}'",
                f"title: '{new_title}'",
                content
            )
        
        # Fix localhost links
        content = re.sub(r'http://localhost:1313/', 'https://www.authlete.com/', content)
        content = re.sub(r'http://localhost:1314/', 'https://www.authlete.com/', content)
        
        # Fix broken image URLs
        content = re.sub(
            r'https://storage\.googleapis\.com/authlete-website/img/developers/',
            'https://storage.googleapis.com/authlete-website/img/developers/',
            content
        )
        
        # Fix any remaining localhost in image URLs
        content = re.sub(
            r'http://localhost:1313/img/',
            'https://storage.googleapis.com/authlete-website/img/',
            content
        )
        
        # Fix relative image paths
        content = re.sub(
            r'!\[([^\]]*)\]\(/img/([^)]+)\)',
            r'![\1](https://storage.googleapis.com/authlete-website/img/\2)',
            content
        )
        
        # Fix any remaining relative paths in images
        content = re.sub(
            r'!\[([^\]]*)\]\(img/([^)]+)\)',
            r'![\1](https://storage.googleapis.com/authlete-website/img/\2)',
            content
        )
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Main function to fix all issues"""
    base_dir = Path("/Users/muhammadshariqnazr/Downloads/new-api-doc")
    
    print("🔍 Scanning for issues...")
    
    # Find all MDX files
    mdx_files = list(base_dir.rglob("*.mdx"))
    
    print(f"📁 Found {len(mdx_files)} MDX files")
    
    fixed_count = 0
    
    for file_path in mdx_files:
        if fix_file_titles_and_images(file_path):
            print(f"✅ Fixed: {file_path.name}")
            fixed_count += 1
    
    print(f"\n🎉 Fixed {fixed_count} files")
    
    # Check for remaining issues
    print("\n🔍 Checking for remaining issues...")
    
    # Check for remaining "Getting Started - Authlete" titles
    remaining_titles = []
    for file_path in mdx_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if "Getting Started - Authlete" in content:
                    remaining_titles.append(str(file_path))
        except:
            pass
    
    if remaining_titles:
        print(f"⚠️  Still found 'Getting Started - Authlete' in {len(remaining_titles)} files:")
        for file_path in remaining_titles:
            print(f"   - {file_path}")
    else:
        print("✅ No more 'Getting Started - Authlete' titles found")
    
    # Check for remaining localhost links
    remaining_localhost = []
    for file_path in mdx_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if "localhost:1313" in content or "localhost:1314" in content:
                    remaining_localhost.append(str(file_path))
        except:
            pass
    
    if remaining_localhost:
        print(f"⚠️  Still found localhost links in {len(remaining_localhost)} files:")
        for file_path in remaining_localhost:
            print(f"   - {file_path}")
    else:
        print("✅ No more localhost links found")

if __name__ == "__main__":
    main()
