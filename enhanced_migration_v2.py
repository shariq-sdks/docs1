#!/usr/bin/env python3
"""
Enhanced Migration Script V2
Properly migrates all content with correct formatting, hyperlinks, media, and code samples
"""

import re
import logging
from pathlib import Path
from typing import Optional, Dict, List
from bs4 import BeautifulSoup, Tag
import urllib.parse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class EnhancedMigratorV2:
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.image_base_url = "https://storage.googleapis.com/authlete-website"
        self.site_base_url = "https://www.authlete.com"
        
        # Skip patterns for navigation and unwanted content
        self.skip_patterns = [
            'navbar', 'navigation', 'header', 'footer', 'sidebar',
            'breadcrumb', 'menu', 'nav', 'logo', 'sign-in', 'register',
            'language-selector', 'locale-switcher'
        ]
        
        # Content selectors for different page types
        self.content_selectors = [
            'main', 'article', '.content', '.main-content', 
            '.page-content', '.post-content', '.entry-content',
            '#content', '.container .row', '.wrapper'
        ]

    def should_skip_element(self, element: Tag) -> bool:
        """Check if element should be skipped"""
        if not element.name:
            return False
            
        # Check class names
        classes = element.get('class', [])
        for class_name in classes:
            if any(pattern in class_name.lower() for pattern in self.skip_patterns):
                return True
        
        # Check ID
        element_id = element.get('id', '')
        if any(pattern in element_id.lower() for pattern in self.skip_patterns):
            return True
        
        return False

    def extract_main_content(self, soup: BeautifulSoup) -> Optional[Tag]:
        """Extract main content area, skipping navigation and unwanted elements"""
        # Try different selectors to find main content
        for selector in self.content_selectors:
            content = soup.select_one(selector)
            if content and not self.should_skip_element(content):
                return content
        
        # Fallback: find the largest content div
        content_divs = soup.find_all('div', class_=re.compile(r'content|main|article|post'))
        if content_divs:
            # Return the div with most text content
            return max(content_divs, key=lambda x: len(x.get_text().strip()))
        
        return None

    def clean_and_convert_html_to_mdx(self, html_content: str, base_path: str = "") -> str:
        """Convert HTML to MDX with proper formatting and link handling"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove unwanted elements
        for element in soup.find_all():
            if self.should_skip_element(element):
                element.decompose()
        
        # Convert images with proper URLs
        for img in soup.find_all('img'):
            src = img.get('src', '')
            if src:
                # Handle relative URLs
                if src.startswith('/'):
                    src = f"{self.image_base_url}{src}"
                elif not src.startswith('http'):
                    src = f"{self.image_base_url}/img/kb{src}"
                
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
                elif '/kb/' in href:
                    # Knowledge base link
                    path_parts = href.split('/kb/')[-1].split('/')
                    if len(path_parts) > 1:
                        new_path = f"reference/{path_parts[0]}"
                        link.replace_with(f"[{text}](/{new_path})")
                    else:
                        link.replace_with(f"[{text}](/reference/{path_parts[0]})")
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
            if not self.should_skip_element(ul):
                ul_md = self.convert_list_to_markdown(ul, ordered=False)
                ul.replace_with(ul_md)
        
        for ol in soup.find_all('ol'):
            if not self.should_skip_element(ol):
                ol_md = self.convert_list_to_markdown(ol, ordered=True)
                ol.replace_with(ol_md)
        
        # Convert headings
        for i in range(1, 7):
            for heading in soup.find_all(f'h{i}'):
                if not self.should_skip_element(heading):
                    text = heading.get_text().strip()
                    if text:
                        heading.replace_with(f"{'#' * i} {text}")
        
        # Convert alerts and info boxes to Mintlify components
        for alert in soup.find_all(['div', 'section'], class_=re.compile(r'(alert|info|warning|success|note|tip|callout)')):
            if not self.should_skip_element(alert):
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
            if not self.should_skip_element(p):
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

    def extract_content_from_html(self, html_file: Path) -> Optional[Dict]:
        """Extract clean content from HTML file"""
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
            main_content = self.extract_main_content(soup)
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

    def create_mdx_file(self, content_data: Dict, output_path: Path) -> bool:
        """Create properly formatted MDX file"""
        try:
            # Ensure directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Convert HTML to MDX with proper formatting
            mdx_content = self.clean_and_convert_html_to_mdx(content_data['content'])
            
            # Create frontmatter
            frontmatter = f"""---
title: '{content_data['title']}'
description: '{content_data['description']}'
---

{mdx_content}
"""
            
            # Write file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter)
            
            logger.info(f"Created MDX file: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error creating MDX file {output_path}: {e}")
            return False

    def migrate_all_remaining_pages(self):
        """Migrate all remaining pages that haven't been migrated yet"""
        logger.info("Starting comprehensive migration of all remaining pages...")
        
        # Get all HTML files
        all_html_files = []
        all_html_files.extend(list(self.source_dir.rglob("developers/*/index.html")))
        all_html_files.extend(list(self.source_dir.rglob("kb/*/index.html")))
        
        logger.info(f"Found {len(all_html_files)} HTML files to migrate")
        
        migrated_count = 0
        failed_count = 0
        skipped_count = 0
        
        for html_file in all_html_files:
            try:
                # Skip if already migrated
                relative_path = html_file.relative_to(self.source_dir)
                if 'developers/' in str(relative_path):
                    # Developers content
                    page_name = relative_path.parts[1]  # Get directory name
                    if page_name in ['index.html']:
                        continue
                    
                    # Map to our structure
                    if page_name in ['getting_started', 'overview', 'quickstart']:
                        target_path = self.target_dir / f"{page_name}.mdx"
                    elif page_name in ['pkce', 'device_flow', 'ciba', 'nativesso', 'grant_management', 'token_exchange']:
                        target_path = self.target_dir / f"flows/{page_name.replace('_', '-')}.mdx"
                    elif page_name in ['fapi', 'fapi2']:
                        target_path = self.target_dir / f"fapi/{page_name}-overview.mdx"
                    else:
                        target_path = self.target_dir / f"concepts/{page_name}.mdx"
                
                elif 'kb/' in str(relative_path):
                    # Knowledge base content
                    kb_path = str(relative_path).replace('kb/', '').replace('/index.html', '')
                    
                    # Map to reference structure
                    if 'deployment/' in kb_path:
                        ref_name = kb_path.split('/')[-1].replace('-', '-')
                        target_path = self.target_dir / f"reference/{ref_name}.mdx"
                    elif 'oauth-and-openid-connect/' in kb_path:
                        ref_name = kb_path.split('/')[-1].replace('-', '-')
                        target_path = self.target_dir / f"reference/{ref_name}.mdx"
                    else:
                        ref_name = kb_path.split('/')[-1].replace('-', '-')
                        target_path = self.target_dir / f"reference/{ref_name}.mdx"
                
                else:
                    skipped_count += 1
                    continue
                
                # Skip if target already exists and is not empty
                if target_path.exists() and target_path.stat().st_size > 500:
                    skipped_count += 1
                    continue
                
                # Extract content
                content_data = self.extract_content_from_html(html_file)
                if not content_data:
                    logger.warning(f"No content extracted from {html_file}")
                    failed_count += 1
                    continue
                
                # Create MDX file
                if self.create_mdx_file(content_data, target_path):
                    migrated_count += 1
                else:
                    failed_count += 1
                    
            except Exception as e:
                logger.error(f"Failed to migrate {html_file}: {e}")
                failed_count += 1
        
        logger.info(f"Migration complete! Migrated: {migrated_count}, Failed: {failed_count}, Skipped: {skipped_count}")

def main():
    """Main function to run the enhanced migration"""
    source_dir = "/Users/muhammadshariqnazr/website/public"
    target_dir = "/Users/muhammadshariqnazr/Downloads/new-api-doc"
    
    migrator = EnhancedMigratorV2(source_dir, target_dir)
    migrator.migrate_all_remaining_pages()

if __name__ == "__main__":
    main()
