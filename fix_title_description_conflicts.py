#!/usr/bin/env python3
import os
import re
import yaml

def fix_title_description_conflicts(file_path):
    """Fix cases where title and description are too similar"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not frontmatter_match:
            return False
        
        frontmatter_content = frontmatter_match.group(1)
        body_content = content[frontmatter_match.end():]
        
        # Parse frontmatter
        try:
            frontmatter = yaml.safe_load(frontmatter_content)
        except yaml.YAMLError:
            return False
        
        # Check if title and description are too similar
        title = frontmatter.get('title', '').strip()
        description = frontmatter.get('description', '').strip()
        
        # Remove common words and punctuation for comparison
        title_clean = re.sub(r'[^\w\s]', '', title.lower())
        desc_clean = re.sub(r'[^\w\s]', '', description.lower())
        
        # If they're too similar, create a better description
        if title_clean == desc_clean or (len(title_clean) > 10 and title_clean in desc_clean):
            # Generate a more descriptive description based on content
            after_h1 = body_content.split('# ')[1] if '# ' in body_content else body_content
            first_para = re.search(r'^([^\n]+)', after_h1.split('\n\n')[0] if '\n\n' in after_h1 else after_h1, re.MULTILINE)
            
            if first_para:
                new_desc = first_para.group(1).strip()
                # Clean up the description
                new_desc = re.sub(r'[^\w\s.,!?-]', '', new_desc)  # Remove special chars
                new_desc = new_desc[:120] + '...' if len(new_desc) > 120 else new_desc
                
                if new_desc and new_desc != description:
                    frontmatter['description'] = new_desc
                    print(f"Fixed conflict in {file_path}: '{title}' vs '{description}' -> '{new_desc}'")
        
        # Specific fixes for known problematic files
        if 'api-reference' in file_path:
            frontmatter['title'] = 'API Reference'
            frontmatter['description'] = 'Complete API reference for Authlete services with interactive documentation and examples.'
        elif 'overview' in file_path:
            frontmatter['title'] = 'Overview'
            frontmatter['description'] = 'Learn about Authlete, a BaaS solution for implementing OAuth 2.0 and OpenID Connect.'
        elif 'security-fundamentals' in file_path:
            frontmatter['title'] = 'PKCE (Proof Key for Code Exchange)'
            frontmatter['description'] = 'Learn about PKCE implementation for OAuth 2.0 security and authorization code protection.'
        
        # Reconstruct the file
        new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        new_content = f"---\n{new_frontmatter}---\n{body_content}"
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    # Fix specific problematic files
    files_to_fix = [
        'api-reference.mdx',
        'overview.mdx', 
        'concepts/security-fundamentals.mdx'
    ]
    
    fixed_count = 0
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            if fix_title_description_conflicts(file_path):
                fixed_count += 1
    
    print(f"Fixed {fixed_count} title/description conflicts")

if __name__ == "__main__":
    main()
