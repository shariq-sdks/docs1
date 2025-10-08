#!/usr/bin/env python3
"""
Authlete Documentation Migration Script

This script migrates content from the existing HTML documentation to Mintlify MDX format.
It handles various content types including tutorials, concepts, API docs, and more.
"""

import os
import re
import json
import shutil
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AuthleteDocMigrator:
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.image_base_url = "https://storage.googleapis.com/authlete-website/resources/"
        
        # Content type mappings
        self.content_mappings = {
            'tutorial': 'tutorials',
            'concept': 'concepts', 
            'implementation': 'implementation',
            'security': 'security',
            'oidc': 'oidc',
            'flow': 'flows',
            'fapi': 'fapi',
            'federation': 'federation',
            'production': 'production',
            'tool': 'tools',
            'reference': 'reference'
        }
        
        # Special handling for specific pages
        self.special_pages = {
            'getting_started': 'getting-started.mdx',
            'overview': 'overview.mdx',
            'quickstart': 'quickstart.mdx'
        }

    def extract_content_from_html(self, html_file: Path) -> Dict:
        """Extract structured content from HTML file"""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract main content
            article = soup.find('article', class_='docsy-article')
            if not article:
                logger.warning(f"No article content found in {html_file}")
                return {}
            
            # Extract title
            title_elem = soup.find('h1') or article.find('h1')
            title = title_elem.get_text().strip() if title_elem else "Untitled"
            
            # Extract description from meta or first paragraph
            description = ""
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                description = meta_desc.get('content', '')
            else:
                first_p = article.find('p')
                if first_p:
                    description = first_p.get_text().strip()[:200] + "..."
            
            # Extract main content
            content_div = article.find('div', class_='docsy-article-content')
            if not content_div:
                content_div = article
            
            return {
                'title': title,
                'description': description,
                'content': content_div,
                'soup': soup
            }
        except Exception as e:
            logger.error(f"Error processing {html_file}: {e}")
            return {}

    def convert_html_to_mdx(self, content_div, soup) -> str:
        """Convert HTML content to MDX format"""
        mdx_content = []
        
        for element in content_div.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'blockquote', 'pre', 'code', 'img', 'table', 'div']):
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                level = int(element.name[1])
                text = element.get_text().strip()
                mdx_content.append(f"{'#' * level} {text}\n")
                
            elif element.name == 'p':
                text = self.process_paragraph(element)
                if text.strip():
                    mdx_content.append(f"{text}\n")
                    
            elif element.name in ['ul', 'ol']:
                mdx_content.append(self.process_list(element))
                
            elif element.name == 'blockquote':
                mdx_content.append(self.process_blockquote(element))
                
            elif element.name == 'pre':
                mdx_content.append(self.process_code_block(element))
                
            elif element.name == 'img':
                mdx_content.append(self.process_image(element))
                
            elif element.name == 'table':
                mdx_content.append(self.process_table(element))
                
            elif element.name == 'div' and element.get('class'):
                if 'alert' in element.get('class', []):
                    mdx_content.append(self.process_alert(element))
                elif 'highlight' in element.get('class', []):
                    mdx_content.append(self.process_code_block(element))
        
        return '\n'.join(mdx_content)

    def process_paragraph(self, p_elem) -> str:
        """Process paragraph content, handling links and formatting"""
        text = str(p_elem)
        
        # Convert links
        text = re.sub(r'<a href="([^"]*)"[^>]*>([^<]*)</a>', r'[\2](\1)', text)
        
        # Convert strong/bold
        text = re.sub(r'<strong>([^<]*)</strong>', r'**\1**', text)
        text = re.sub(r'<b>([^<]*)</b>', r'**\1**', text)
        
        # Convert emphasis/italic
        text = re.sub(r'<em>([^<]*)</em>', r'*\1*', text)
        text = re.sub(r'<i>([^<]*)</i>', r'*\1*', text)
        
        # Convert code spans
        text = re.sub(r'<code>([^<]*)</code>', r'`\1`', text)
        
        # Remove remaining HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        
        # Clean up whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        
        return text.strip()

    def process_list(self, list_elem) -> str:
        """Process unordered or ordered lists"""
        items = []
        for li in list_elem.find_all('li', recursive=False):
            item_text = self.process_paragraph(li)
            if item_text.strip():
                items.append(f"- {item_text}")
        
        return '\n'.join(items) + '\n'

    def process_blockquote(self, blockquote_elem) -> str:
        """Process blockquotes"""
        text = self.process_paragraph(blockquote_elem)
        return f"> {text}\n"

    def process_code_block(self, code_elem) -> str:
        """Process code blocks"""
        # Find code element
        code = code_elem.find('code')
        if not code:
            return ""
        
        # Extract language from class
        language = ""
        if code.get('class'):
            for cls in code.get('class', []):
                if cls.startswith('language-'):
                    language = cls.replace('language-', '')
                    break
        
        # Get code content
        code_text = code.get_text()
        
        return f"```{language}\n{code_text}\n```\n"

    def process_image(self, img_elem) -> str:
        """Process images"""
        src = img_elem.get('src', '')
        alt = img_elem.get('alt', '')
        
        # Convert relative URLs to absolute
        if src.startswith('/'):
            src = f"https://storage.googleapis.com/authlete-website{src}"
        elif not src.startswith('http'):
            src = f"{self.image_base_url}{src}"
        
        return f"![{alt}]({src})\n"

    def process_table(self, table_elem) -> str:
        """Process tables"""
        rows = []
        for tr in table_elem.find_all('tr'):
            cells = []
            for td in tr.find_all(['td', 'th']):
                cell_text = td.get_text().strip()
                cells.append(cell_text)
            if cells:
                rows.append('| ' + ' | '.join(cells) + ' |')
        
        if len(rows) > 1:
            # Add separator row
            separator = '|' + '|'.join([' --- ' for _ in rows[0].split('|')[1:-1]]) + '|'
            rows.insert(1, separator)
        
        return '\n'.join(rows) + '\n'

    def process_alert(self, alert_elem) -> str:
        """Process alert boxes"""
        text = self.process_paragraph(alert_elem)
        
        # Determine alert type based on classes
        classes = alert_elem.get('class', [])
        if 'alert-danger' in classes or 'alert-error' in classes:
            return f"<Warning>\n{text}\n</Warning>\n"
        elif 'alert-info' in classes:
            return f"<Info>\n{text}\n</Info>\n"
        elif 'alert-success' in classes:
            return f"<Success>\n{text}\n</Success>\n"
        else:
            return f"<Note>\n{text}\n</Note>\n"

    def create_mdx_file(self, content_data: Dict, output_path: Path) -> bool:
        """Create MDX file from content data"""
        try:
            # Create frontmatter
            frontmatter = f"""---
title: '{content_data['title']}'
description: '{content_data['description']}'
---

"""
            
            # Convert content to MDX
            mdx_content = self.convert_html_to_mdx(content_data['content'], content_data['soup'])
            
            # Combine frontmatter and content
            full_content = frontmatter + mdx_content
            
            # Write to file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            logger.info(f"Created MDX file: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error creating MDX file {output_path}: {e}")
            return False

    def determine_output_path(self, html_file: Path) -> Optional[Path]:
        """Determine the output path for an HTML file based on its content and location"""
        file_name = html_file.stem
        
        # Check for special pages
        if file_name in self.special_pages:
            return self.target_dir / self.special_pages[file_name]
        
        # Determine content type based on file path
        relative_path = html_file.relative_to(self.source_dir)
        path_parts = relative_path.parts
        
        # Map based on directory structure
        if 'tutorial' in path_parts:
            category = 'tutorials'
        elif 'concept' in path_parts or 'oauth' in path_parts or 'oidc' in path_parts:
            category = 'concepts'
        elif 'implementation' in path_parts:
            category = 'implementation'
        elif 'security' in path_parts:
            category = 'security'
        elif 'oidc' in path_parts:
            category = 'oidc'
        elif 'flow' in path_parts or 'device' in path_parts or 'ciba' in path_parts:
            category = 'flows'
        elif 'fapi' in path_parts:
            category = 'fapi'
        elif 'federation' in path_parts:
            category = 'federation'
        elif 'production' in path_parts or 'terraform' in path_parts:
            category = 'production'
        elif 'tool' in path_parts or 'mkjwk' in path_parts or 'mkjose' in path_parts:
            category = 'tools'
        elif 'reference' in path_parts or 'relnotes' in path_parts:
            category = 'reference'
        else:
            # Default to concepts for unknown content
            category = 'concepts'
        
        # Create output directory
        output_dir = self.target_dir / category
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Convert file name to kebab-case
        mdx_name = re.sub(r'[^a-zA-Z0-9\-_]', '-', file_name.lower())
        mdx_name = re.sub(r'-+', '-', mdx_name).strip('-')
        
        return output_dir / f"{mdx_name}.mdx"

    def migrate_all_docs(self):
        """Migrate all HTML documentation files"""
        logger.info("Starting documentation migration...")
        
        # Find all HTML files
        html_files = list(self.source_dir.rglob("*.html"))
        logger.info(f"Found {len(html_files)} HTML files to migrate")
        
        migrated_count = 0
        failed_count = 0
        
        for html_file in html_files:
            try:
                # Skip non-content files
                if any(skip in str(html_file) for skip in ['index.html', 'layout', 'partial', 'base']):
                    continue
                
                # Extract content
                content_data = self.extract_content_from_html(html_file)
                if not content_data:
                    continue
                
                # Determine output path
                output_path = self.determine_output_path(html_file)
                if not output_path:
                    logger.warning(f"Could not determine output path for {html_file}")
                    continue
                
                # Create MDX file
                if self.create_mdx_file(content_data, output_path):
                    migrated_count += 1
                else:
                    failed_count += 1
                    
            except Exception as e:
                logger.error(f"Failed to migrate {html_file}: {e}")
                failed_count += 1
        
        logger.info(f"Migration complete! Migrated: {migrated_count}, Failed: {failed_count}")

    def create_migration_report(self):
        """Create a report of the migration process"""
        report = {
            'timestamp': str(Path().cwd()),
            'source_directory': str(self.source_dir),
            'target_directory': str(self.target_dir),
            'migrated_files': [],
            'failed_files': []
        }
        
        # This would be populated during migration
        return report

def main():
    """Main function to run the migration"""
    source_dir = "/Users/muhammadshariqnazr/website/public/developers"
    target_dir = "/Users/muhammadshariqnazr/Downloads/new-api-doc"
    
    migrator = AuthleteDocMigrator(source_dir, target_dir)
    migrator.migrate_all_docs()

if __name__ == "__main__":
    main()
