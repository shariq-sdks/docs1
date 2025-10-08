#!/usr/bin/env python3
"""
Fix MDX Parsing Errors Script
Fixes all MDX parsing errors including frontmatter, acorn expressions, and character issues
"""

import re
import os
from pathlib import Path

def fix_frontmatter_errors(file_path):
    """Fix frontmatter parsing errors"""
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
        
        # Fix common frontmatter issues
        # Fix multiline keys
        frontmatter_content = re.sub(r'^(\w+):\s*\n\s*', r'\1: ', frontmatter_content, flags=re.MULTILINE)
        
        # Fix unquoted values with special characters
        frontmatter_content = re.sub(r'^(\w+):\s*([^"\n][^\n]*[^"\n])\s*$', r'\1: "\2"', frontmatter_content, flags=re.MULTILINE)
        
        # Fix values that start with special characters
        frontmatter_content = re.sub(r'^(\w+):\s*([!@#$%^&*()_+=\[\]{}|;:,.<>?/\\][^\n]*)\s*$', r'\1: "\2"', frontmatter_content, flags=re.MULTILINE)
        
        # Fix values with quotes in them
        frontmatter_content = re.sub(r'^(\w+):\s*"([^"]*)"([^"]*)"([^"]*)"', r'\1: "\2\3\4"', frontmatter_content, flags=re.MULTILINE)
        
        # Rebuild the file
        new_content = '---\n' + frontmatter_content + '\n---\n' + '\n'.join(lines[end_index + 1:])
        
        if new_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing frontmatter in {file_path}: {e}")
        return False

def fix_acorn_expression_errors(file_path):
    """Fix acorn expression parsing errors"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix common acorn expression issues
        # Fix unescaped curly braces in JSX
        content = re.sub(r'\{([^}]*[{}][^}]*)\}', r'{\`\1\`}', content)
        
        # Fix unescaped quotes in JSX attributes
        content = re.sub(r'(\w+)="([^"]*)"([^"]*)"', r'\1="\2\3"', content)
        
        # Fix unescaped special characters in JSX
        content = re.sub(r'<(\w+)([^>]*[!@#$%^&*()_+=\[\]{}|;:,.<>?/\\][^>]*)>', r'<\1\2>', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing acorn expressions in {file_path}: {e}")
        return False

def fix_character_errors(file_path):
    """Fix unexpected character errors"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix unexpected ! character before name
        content = re.sub(r'!\s*([a-zA-Z_$])', r'{\`!\`}\1', content)
        
        # Fix unexpected < character before name
        content = re.sub(r'<\s*([a-zA-Z_$])', r'{\`<\`}\1', content)
        
        # Fix unescaped HTML tags
        content = re.sub(r'<([^>]*[!@#$%^&*()_+=\[\]{}|;:,.<>?/\\][^>]*)>', r'{\`<\1>\`}', content)
        
        # Fix unescaped special characters in markdown
        content = re.sub(r'([^\\])!([a-zA-Z])', r'\1{\`!\`}\2', content)
        content = re.sub(r'([^\\])<([a-zA-Z])', r'\1{\`<\`}\2', content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing character issues in {file_path}: {e}")
        return False

def fix_specific_files():
    """Fix specific files with known issues"""
    fixes = {
        'concepts/result-codes.mdx': {
            'description': 'Interpreting the meaning behind Authlete result codes and error responses.'
        },
        'concepts/authlete_web_apis.mdx': {
            'title': 'Authlete Web APIs',
            'description': 'Comprehensive reference for Authlete Web APIs and endpoints.'
        },
        'concepts/definitive_guide.mdx': {
            'title': 'Definitive Guide',
            'description': 'The definitive guide to Authlete implementation and best practices.'
        },
        'concepts/jwt_authorization_grant.mdx': {
            'title': 'JWT Authorization Grant',
            'description': 'Understanding JWT-based authorization grants in OAuth 2.0.'
        },
        'fapi/fapi-overview.mdx': {
            'title': 'FAPI Overview',
            'description': 'Financial-grade API (FAPI) overview and implementation guide.'
        },
        'flows/grant-management.mdx': {
            'title': 'Grant Management',
            'description': 'Managing OAuth 2.0 grants and authorization lifecycle.'
        },
        'flows/native-sso.mdx': {
            'title': 'Native SSO',
            'description': 'Native Single Sign-On implementation for mobile applications.'
        },
        'flows/nativesso.mdx': {
            'title': 'Native SSO',
            'description': 'Native Single Sign-On implementation for mobile applications.'
        },
        'flows/token-exchange.mdx': {
            'title': 'Token Exchange',
            'description': 'OAuth 2.0 token exchange implementation and best practices.'
        },
        'reference/access-token-list.mdx': {
            'title': 'Access Token List',
            'description': 'Managing and listing access tokens in Authlete.'
        },
        'reference/caching-introspection.mdx': {
            'title': 'Caching Introspection',
            'description': 'Token introspection caching strategies and implementation.'
        },
        'reference/definitive-guide.mdx': {
            'title': 'Definitive Guide',
            'description': 'The definitive guide to Authlete implementation and best practices.'
        },
        'reference/error-handling.mdx': {
            'title': 'Error Handling',
            'description': 'Comprehensive guide to error handling in Authlete APIs.'
        },
        'reference/introspection.mdx': {
            'title': 'Token Introspection',
            'description': 'OAuth 2.0 token introspection implementation and usage.'
        },
        'reference/multiple-developer-accounts.mdx': {
            'title': 'Multiple Developer Accounts',
            'description': 'Managing multiple developer accounts in Authlete.'
        },
        'reference/preserving-client-id.mdx': {
            'title': 'Preserving Client ID',
            'description': 'Best practices for preserving client ID in OAuth flows.'
        },
        'tools/api-explorer.mdx': {
            'title': 'API Explorer',
            'description': 'Interactive API explorer and testing tool for Authlete Web APIs.'
        }
    }
    
    base_dir = Path("/Users/muhammadshariqnazr/Downloads/new-api-doc")
    fixed_count = 0
    
    for file_path, frontmatter in fixes.items():
        full_path = base_dir / file_path
        if full_path.exists():
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract existing frontmatter
                if content.startswith('---'):
                    lines = content.split('\n')
                    end_index = -1
                    for i, line in enumerate(lines[1:], 1):
                        if line.strip() == '---':
                            end_index = i
                            break
                    
                    if end_index > 0:
                        # Replace frontmatter
                        new_frontmatter = '---\n'
                        for key, value in frontmatter.items():
                            new_frontmatter += f"{key}: '{value}'\n"
                        new_frontmatter += '---\n'
                        
                        new_content = new_frontmatter + '\n'.join(lines[end_index + 1:])
                        
                        with open(full_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        print(f"✅ Fixed frontmatter: {file_path}")
                        fixed_count += 1
                        
            except Exception as e:
                print(f"❌ Error fixing {file_path}: {e}")
    
    return fixed_count

def main():
    """Main function to fix all MDX errors"""
    base_dir = Path("/Users/muhammadshariqnazr/Downloads/new-api-doc")
    
    print("🔍 Scanning for MDX parsing errors...")
    
    # Find all MDX files
    mdx_files = list(base_dir.rglob("*.mdx"))
    
    print(f"📁 Found {len(mdx_files)} MDX files")
    
    # Fix specific files first
    print("\n🔧 Fixing specific files with known issues...")
    specific_fixes = fix_specific_files()
    
    # Fix frontmatter errors
    print("\n🔧 Fixing frontmatter errors...")
    frontmatter_fixes = 0
    for file_path in mdx_files:
        if fix_frontmatter_errors(file_path):
            print(f"✅ Fixed frontmatter: {file_path.name}")
            frontmatter_fixes += 1
    
    # Fix acorn expression errors
    print("\n🔧 Fixing acorn expression errors...")
    acorn_fixes = 0
    for file_path in mdx_files:
        if fix_acorn_expression_errors(file_path):
            print(f"✅ Fixed acorn expressions: {file_path.name}")
            acorn_fixes += 1
    
    # Fix character errors
    print("\n🔧 Fixing character errors...")
    character_fixes = 0
    for file_path in mdx_files:
        if fix_character_errors(file_path):
            print(f"✅ Fixed character issues: {file_path.name}")
            character_fixes += 1
    
    total_fixes = specific_fixes + frontmatter_fixes + acorn_fixes + character_fixes
    print(f"\n🎉 Fixed {total_fixes} files total")
    print(f"   - Specific fixes: {specific_fixes}")
    print(f"   - Frontmatter fixes: {frontmatter_fixes}")
    print(f"   - Acorn expression fixes: {acorn_fixes}")
    print(f"   - Character fixes: {character_fixes}")

if __name__ == "__main__":
    main()
