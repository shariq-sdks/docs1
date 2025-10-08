#!/usr/bin/env python3
"""
Fix Placeholders and Images Script
Populates placeholder pages with real content and fixes broken image links
"""

import re
import logging
from pathlib import Path
from typing import Optional, Dict
from bs4 import BeautifulSoup, Tag

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ContentFixer:
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.image_base_url = "https://storage.googleapis.com/authlete-website"
        
        # Mapping from our page names to original website paths
        self.page_mappings = {
            # Implementation pages
            'implementation/service-management': 'developers/getting_started',
            'implementation/client-management': 'developers/getting_started',
            'implementation/authentication': 'developers/getting_started',
            'implementation/token-management': 'developers/getting_started',
            'implementation/basic-oauth-flows': 'developers/getting_started',
            
            # OIDC pages
            'oidc/user-authentication': 'developers/getting_started',
            'oidc/userinfo-endpoint': 'developers/getting_started',
            'oidc/id-token-handling': 'developers/getting_started',
            'oidc/oidc-best-practices': 'developers/getting_started',
            
            # Security pages
            'security/security-best-practices': 'developers/pkce',
            'security/token-security': 'developers/pkce',
            'security/api-protection': 'developers/pkce',
            
            # FAPI pages
            'fapi/compliance-requirements': 'developers/fapi2',
            'fapi/high-assurance-security': 'developers/fapi2',
            'fapi/fapi2-overview': 'developers/fapi2',
            'fapi/fapi2-implementation': 'developers/fapi2',
            
            # Federation pages
            'federation/trust-frameworks': 'developers/oidcfed',
            'federation/step-up-authentication': 'developers/stepup_authn',
            'federation/verifiable-credentials': 'developers/oid4vci',
            'federation/oidc-federation': 'developers/oidcfed',
            
            # Production pages
            'production/infrastructure-setup': 'developers/terraform',
            'production/monitoring-logging': 'developers/terraform',
            'production/terraform-deployment': 'developers/terraform',
            'production/migration-guides': 'developers/terraform',
            'production/troubleshooting': 'developers/terraform',
            
            # Tutorial pages
            'tutorials/oauth-tutorial': 'developers/tutorial/oauth',
            'tutorials/oidc-tutorial': 'developers/tutorial/oidc',
            'tutorials/fapi-tutorial': 'developers/tutorial/fapi',
            'tutorials/java-getting-started': 'developers/tutorial/getting_started_java',
            'tutorials/aws-cognito-integration': 'developers/tutorial/cognito',
            'tutorials/financial-grade-apigateway': 'developers/tutorial/financial_grade_apigateway',
            
            # Tools pages
            'tools/management-console': 'developers/cd_console',
            'tools/api-explorer': 'developers/authlete_web_apis',
            'tools/terraform-provider': 'developers/terraform',
            
            # Concepts pages
            'concepts/security-fundamentals': 'developers/pkce',
            'concepts/authlete-architecture': 'developers/overview',
            
            # Reference pages
            'reference/definitive-guide': 'developers/definitive_guide',
            'reference/standards-compliance': 'developers/overview',
            'reference/knowledge-base': 'developers/knowledge_base',
            'reference/release-notes': 'developers/relnotes',
        }

    def extract_content_from_html(self, html_file: Path) -> Optional[Dict]:
        """Extract content from HTML file"""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract title
            title_elem = soup.find('title')
            title = title_elem.get_text().strip() if title_elem else "Untitled"
            
            # Extract description from meta tag
            desc_elem = soup.find('meta', attrs={'name': 'description'})
            description = desc_elem.get('content', '').strip() if desc_elem else ""
            
            # Find main content area
            main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
            if not main_content:
                # Fallback: look for content divs
                main_content = soup.find('div', class_='container') or soup.find('div', class_='wrapper')
            
            if not main_content:
                logger.warning(f"Could not find main content in {html_file}")
                return None
            
            # Extract the main content HTML
            content_html = str(main_content)
            
            return {
                'title': title,
                'description': description,
                'content': content_html
            }
            
        except Exception as e:
            logger.error(f"Error extracting content from {html_file}: {e}")
            return None

    def convert_html_to_mdx(self, html_content: str) -> str:
        """Convert HTML to MDX with proper formatting and image URLs"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Convert images with proper URLs
        for img in soup.find_all('img'):
            src = img.get('src', '')
            if src:
                # Handle relative URLs
                if src.startswith('/'):
                    src = f"{self.image_base_url}{src}"
                elif not src.startswith('http'):
                    src = f"{self.image_base_url}/img/developers{src}"
                
                alt = img.get('alt', '')
                title = img.get('title', '')
                
                # Create proper markdown image
                img_md = f"![{alt}]({src})"
                if title:
                    img_md = f'<img src="{src}" alt="{alt}" title="{title}" />'
                
                img.replace_with(img_md)
        
        # Convert links with proper handling
        for link in soup.find_all('a'):
            href = link.get('href', '')
            text = link.get_text().strip()
            
            if not href or not text:
                link.replace_with(text)
                continue
            
            # Handle different link types
            if href.startswith('http'):
                # External link
                link.replace_with(f"[{text}]({href})")
            elif href.startswith('/'):
                # Internal link - convert to relative path
                if '/developers/' in href:
                    # Convert to our MDX structure
                    path_parts = href.split('/developers/')[-1].split('/')
                    if len(path_parts) > 1:
                        new_path = '/'.join(path_parts[:-1])  # Remove index.html
                        link.replace_with(f"[{text}](/{new_path})")
                    else:
                        link.replace_with(f"[{text}](/{path_parts[0]})")
                else:
                    link.replace_with(f"[{text}]({href})")
            elif href.startswith('#'):
                # Anchor link
                link.replace_with(f"[{text}]({href})")
            else:
                # Relative link
                link.replace_with(f"[{text}]({href})")
        
        # Convert code blocks with proper syntax highlighting
        for code in soup.find_all('code'):
            if code.parent and code.parent.name == 'pre':
                # This is a code block
                language = ''
                if code.get('class'):
                    for cls in code.get('class', []):
                        if cls.startswith('language-'):
                            language = cls.replace('language-', '')
                            break
                
                code_text = code.get_text()
                # Preserve indentation
                code_text = '\n'.join(line.rstrip() for line in code_text.split('\n'))
                
                code.parent.replace_with(f"```{language}\n{code_text}\n```")
            else:
                # Inline code
                code_text = code.get_text()
                code.replace_with(f"`{code_text}`")
        
        # Convert tables with proper formatting
        for table in soup.find_all('table'):
            table_md = self.convert_table_to_markdown(table)
            table.replace_with(table_md)
        
        # Convert lists with proper formatting
        for ul in soup.find_all('ul'):
            ul_md = self.convert_list_to_markdown(ul, ordered=False)
            ul.replace_with(ul_md)
        
        for ol in soup.find_all('ol'):
            ol_md = self.convert_list_to_markdown(ol, ordered=True)
            ol.replace_with(ol_md)
        
        # Convert headings
        for i in range(1, 7):
            for heading in soup.find_all(f'h{i}'):
                text = heading.get_text().strip()
                if text:
                    heading.replace_with(f"{'#' * i} {text}")
        
        # Convert alerts and info boxes to Mintlify components
        for alert in soup.find_all(['div', 'section'], class_=re.compile(r'(alert|info|warning|success|note|tip|callout)')):
            alert_type = 'Info'
            classes = alert.get('class', [])
            
            if any('warning' in cls for cls in classes):
                alert_type = 'Warning'
            elif any('success' in cls for cls in classes):
                alert_type = 'Success'
            elif any('error' in cls for cls in classes):
                alert_type = 'Warning'
            elif any('note' in cls for cls in classes):
                alert_type = 'Note'
            
            content = alert.get_text().strip()
            if content:
                alert.replace_with(f"<{alert_type}>\n{content}\n</{alert_type}>")
        
        # Convert paragraphs
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if text and not text.startswith(('Sign In', 'Register', 'English', '日本語')):
                p.replace_with(f"{text}\n\n")
        
        # Get the final markdown
        markdown = soup.get_text()
        
        # Clean up extra whitespace and unwanted content
        lines = markdown.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            # Skip navigation and unwanted content
            if any(skip in line for skip in ['Sign In', 'Register', 'English', '日本語', 'Português', 'News & Blogs', 'Solutions', 'Customers', 'Developers', 'Pricing', 'Resources', 'Contact']):
                continue
            if line:
                cleaned_lines.append(line)
        
        markdown = '\n'.join(cleaned_lines)
        
        # Clean up extra whitespace
        markdown = re.sub(r'\n\s*\n\s*\n+', '\n\n', markdown)
        markdown = markdown.strip()
        
        return markdown

    def convert_table_to_markdown(self, table: Tag) -> str:
        """Convert HTML table to Markdown with proper formatting"""
        rows = []
        for tr in table.find_all('tr'):
            cells = []
            for td in tr.find_all(['td', 'th']):
                cell_text = td.get_text().strip()
                # Escape pipe characters in cell content
                cell_text = cell_text.replace('|', '\\|')
                cells.append(cell_text)
            if cells:
                rows.append('| ' + ' | '.join(cells) + ' |')
        
        if not rows:
            return ""
        
        # Add separator row for headers
        if len(rows) > 1:
            separator = '|' + '|'.join([' --- ' for _ in rows[0].split('|')[1:-1]]) + '|'
            rows.insert(1, separator)
        
        return '\n'.join(rows) + '\n\n'

    def convert_list_to_markdown(self, list_elem: Tag, ordered: bool = False) -> str:
        """Convert HTML list to Markdown with proper formatting"""
        items = []
        for li in list_elem.find_all('li', recursive=False):
            text = li.get_text().strip()
            if text:
                items.append(text)
        
        if ordered:
            return '\n'.join([f"{i+1}. {item}" for i, item in enumerate(items)]) + '\n\n'
        else:
            return '\n'.join([f"- {item}" for item in items]) + '\n\n'

    def fix_placeholder_pages(self):
        """Fix all placeholder pages with real content"""
        logger.info("Starting to fix placeholder pages...")
        
        fixed_count = 0
        failed_count = 0
        
        for page_path, source_path in self.page_mappings.items():
            try:
                # Find the HTML file
                html_file = self.source_dir / f"{source_path}/index.html"
                
                if not html_file.exists():
                    logger.warning(f"HTML file not found: {html_file}")
                    continue
                
                # Extract content
                content_data = self.extract_content_from_html(html_file)
                if not content_data:
                    logger.warning(f"No content extracted from {html_file}")
                    continue
                
                # Create target path
                target_file = self.target_dir / f"{page_path}.mdx"
                
                # Convert HTML to MDX
                mdx_content = self.convert_html_to_mdx(content_data['content'])
                
                # Create frontmatter
                frontmatter = f"""---
title: '{content_data['title']}'
description: '{content_data['description']}'
---

{mdx_content}
"""
                
                # Write file
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(frontmatter)
                
                logger.info(f"Fixed placeholder: {target_file}")
                fixed_count += 1
                    
            except Exception as e:
                logger.error(f"Failed to fix {page_path}: {e}")
                failed_count += 1
        
        logger.info(f"Fixed {fixed_count} placeholder pages, {failed_count} failed")

    def fix_broken_images(self):
        """Fix broken image links in all MDX files"""
        logger.info("Starting to fix broken image links...")
        
        fixed_count = 0
        
        for mdx_file in self.target_dir.rglob("*.mdx"):
            try:
                with open(mdx_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Fix localhost images
                content = re.sub(
                    r'https://storage\.googleapis\.com/authlete-website/img/developers/',
                    'https://storage.googleapis.com/authlete-website/img/developers/',
                    content
                )
                
                # Fix any remaining localhost references
                content = re.sub(
                    r'http://localhost:1313/',
                    'https://www.authlete.com/',
                    content
                )
                
                # Write back the fixed content
                with open(mdx_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                fixed_count += 1
                logger.info(f"Fixed images in: {mdx_file}")
                
            except Exception as e:
                logger.error(f"Failed to fix images in {mdx_file}: {e}")
        
        logger.info(f"Fixed images in {fixed_count} files")

def main():
    """Main function to fix placeholders and images"""
    source_dir = "/Users/muhammadshariqnazr/website/public"
    target_dir = "/Users/muhammadshariqnazr/Downloads/new-api-doc"
    
    fixer = ContentFixer(source_dir, target_dir)
    fixer.fix_placeholder_pages()
    fixer.fix_broken_images()

if __name__ == "__main__":
    main()
