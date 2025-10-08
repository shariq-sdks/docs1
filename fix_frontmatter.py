#!/usr/bin/env python3
import os
import re
import glob

def fix_frontmatter_quotes(file_path):
    """Fix frontmatter YAML quote issues"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix the common pattern: description: 'text'"
        # Replace with: description: 'text'
        content = re.sub(r"description: '([^']*)'\"\n---", r"description: '\1'\n---", content)
        
        # Fix other similar patterns
        content = re.sub(r"title: '([^']*)'\"\n---", r"title: '\1'\n---", content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed: {file_path}")
        return True
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def fix_openapi_quotes(file_path):
    """Fix OpenAPI frontmatter with backticks"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix openapi: "delete /api/{\`serviceId}/..." patterns
        # Replace backticks with proper escaping
        content = re.sub(r'openapi: "([^"]*)\\\`([^"]*)\\\`([^"]*)"', r'openapi: "\1{\2}\3"', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed OpenAPI: {file_path}")
        return True
    except Exception as e:
        print(f"Error fixing OpenAPI {file_path}: {e}")
        return False

def main():
    # Fix all MDX files with frontmatter issues
    mdx_files = glob.glob('**/*.mdx', recursive=True)
    
    fixed_count = 0
    for file_path in mdx_files:
        if fix_frontmatter_quotes(file_path):
            fixed_count += 1
    
    # Fix OpenAPI files specifically
    openapi_files = [
        'api-reference/client-management/delete-client-tokens.mdx',
        'api-reference/client-management/delete-client-⚡.mdx',
        'api-reference/client-management/delete-granted-scopes.mdx',
        'api-reference/client-management/delete-requestable-scopes.mdx',
        'api-reference/client-management/get-authorized-applications.mdx',
        'api-reference/client-management/get-client.mdx',
        'api-reference/client-management/get-granted-scopes.mdx',
        'api-reference/client-management/get-requestable-scopes.mdx',
        'api-reference/client-management/rotate-client-secret.mdx',
        'api-reference/client-management/update-client-lock.mdx',
        'api-reference/client-management/update-client-secret.mdx',
        'api-reference/client-management/update-client-tokens.mdx',
        'api-reference/client-management/update-client.mdx',
        'api-reference/client-management/update-requestable-scopes.mdx',
        'api-reference/hardware-security-key/delete-security-key.mdx',
        'api-reference/hardware-security-key/get-security-key.mdx',
        'api-reference/token-operations/delete-access-token.mdx'
    ]
    
    for file_path in openapi_files:
        if os.path.exists(file_path):
            if fix_openapi_quotes(file_path):
                fixed_count += 1
    
    print(f"Fixed {fixed_count} files")

if __name__ == "__main__":
    main()
