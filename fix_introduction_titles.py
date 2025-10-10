#!/usr/bin/env python3
"""
Fix Introduction Titles Script
Fixes files that have generic "Introduction" titles and sets proper descriptive titles
"""

import os
import re
from pathlib import Path

def get_proper_title(file_path):
    """Get a proper title based on the file path and content"""
    relative_path = str(file_path).replace('/Users/muhammadshariqnazr/Downloads/new-api-doc/', '')
    
    # Title mapping based on file paths
    title_mapping = {
        'concepts/oidcfed.mdx': 'OIDC Federation',
        'concepts/cd_console.mdx': 'Client Developer Console',
        'concepts/so_console.mdx': 'Service Owner Console',
        'flows/token-exchange.mdx': 'Token Exchange',
        'flows/grant-management.mdx': 'Grant Management',
        'reference/terraform-intro.mdx': 'Terraform Introduction',
    }
    
    if relative_path in title_mapping:
        return title_mapping[relative_path]
    
    # Try to extract title from content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for the first meaningful heading after frontmatter
        lines = content.split('\n')
        in_frontmatter = False
        frontmatter_end = 0
        
        for i, line in enumerate(lines):
            if line.strip() == '---':
                if in_frontmatter:
                    frontmatter_end = i
                    break
                else:
                    in_frontmatter = True
            elif in_frontmatter and line.strip() == '---':
                frontmatter_end = i
                break
        
        # Look for headings after frontmatter
        for i in range(frontmatter_end + 1, len(lines)):
            line = lines[i].strip()
            if line.startswith('# '):
                title = line[2:].strip()
                # Skip generic titles
                if title not in ['Introduction', 'Overview', 'Getting Started', 'Documentation']:
                    return title
            elif line.startswith('## '):
                title = line[3:].strip()
                if title not in ['Introduction', 'Overview', 'Getting Started', 'Documentation']:
                    return title
        
        # Fallback to file name
        file_name = Path(file_path).stem
        return file_name.replace('-', ' ').replace('_', ' ').title()
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return "Untitled"

def fix_file_title(file_path):
    """Fix the title in a single file"""
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
        rest_content = content[content.find('---', 3) + 3:]
        
        # Check if title is "Introduction" or similar
        title_match = re.search(r"title:\s*['\"](.*?)['\"]", '\n'.join(frontmatter_lines))
        if not title_match:
            return False
        
        current_title = title_match.group(1)
        if current_title not in ['Introduction', '1. Introduction', 'Overview', 'Getting Started']:
            return False
        
        # Get proper title
        proper_title = get_proper_title(file_path)
        
        # Replace the title
        new_frontmatter = re.sub(
            r"title:\s*['\"].*?['\"]",
            f"title: \"{proper_title}\"",
            '\n'.join(frontmatter_lines)
        )
        
        # Reconstruct content
        new_content = f"---\n{new_frontmatter}\n---{rest_content}"
        
        # Write back if changed
        if new_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to fix all Introduction titles"""
    print("🔧 Fixing Introduction titles...")
    print("=" * 50)
    
    # Get all MDX files
    mdx_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.mdx'):
                mdx_files.append(os.path.join(root, file))
    
    total_files = len(mdx_files)
    files_fixed = 0
    
    for file_path in sorted(mdx_files):
        if fix_file_title(file_path):
            files_fixed += 1
            print(f"✅ Fixed title in {file_path}")
    
    print("=" * 50)
    print(f"📊 Results:")
    print(f"   Total files processed: {total_files}")
    print(f"   Files fixed: {files_fixed}")
    print("🎉 All Introduction titles fixed!")

if __name__ == "__main__":
    main()
