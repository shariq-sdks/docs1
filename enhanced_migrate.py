#!/usr/bin/env python3
"""
Enhanced Authlete Documentation Migration Script

This script specifically handles the patterns found in Authlete's HTML documentation
and converts them to proper Mintlify MDX format with all the rich components.
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

class EnhancedAuthleteMigrator:
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.image_base_url = "https://storage.googleapis.com/authlete-website/resources/"
        
        # Page mappings based on the sequential learning structure
        self.page_mappings = {
            # Getting Started
            'getting_started': 'getting-started.mdx',
            'overview': 'overview.mdx',
            'quickstart': 'quickstart.mdx',
            
            # Core Concepts
            'oauth': 'concepts/oauth2-basics.mdx',
            'oidc': 'concepts/oidc-basics.mdx',
            'architecture': 'concepts/authlete-architecture.mdx',
            'security': 'concepts/security-fundamentals.mdx',
            
            # Implementation
            'service': 'implementation/service-management.mdx',
            'client': 'implementation/client-management.mdx',
            'authentication': 'implementation/authentication.mdx',
            'token': 'implementation/token-management.mdx',
            
            # Security
            'pkce': 'security/pkce.mdx',
            'api_protection': 'security/api-protection.mdx',
            'security_best_practices': 'security/security-best-practices.mdx',
            
            # OIDC
            'userinfo': 'oidc/userinfo-endpoint.mdx',
            'id_token': 'oidc/id-token-handling.mdx',
            'oidc_best_practices': 'oidc/oidc-best-practices.mdx',
            
            # Flows
            'device_flow': 'flows/device-flow.mdx',
            'ciba': 'flows/ciba.mdx',
            'nativesso': 'flows/native-sso.mdx',
            'grant_management': 'flows/grant-management.mdx',
            'token_exchange': 'flows/token-exchange.mdx',
            
            # FAPI
            'fapi': 'fapi/fapi2-overview.mdx',
            'fapi2': 'fapi/fapi2-implementation.mdx',
            'high_assurance': 'fapi/high-assurance-security.mdx',
            'compliance': 'fapi/compliance-requirements.mdx',
            
            # Federation
            'oidcfed': 'federation/oidc-federation.mdx',
            'oid4vci': 'federation/verifiable-credentials.mdx',
            'stepup_authn': 'federation/step-up-authentication.mdx',
            
            # Production
            'terraform': 'production/terraform-deployment.mdx',
            'monitoring': 'production/monitoring-logging.mdx',
            'infrastructure': 'production/infrastructure-setup.mdx',
            'troubleshooting': 'production/troubleshooting.mdx',
            'migration': 'production/migration-guides.mdx',
            
            # Tutorials
            'tutorial_oauth': 'tutorials/oauth-tutorial.mdx',
            'tutorial_oidc': 'tutorials/oidc-tutorial.mdx',
            'tutorial_fapi': 'tutorials/fapi-tutorial.mdx',
            'tutorial_java': 'tutorials/java-getting-started.mdx',
            'tutorial_aws': 'tutorials/aws-cognito-integration.mdx',
            'tutorial_financial': 'tutorials/financial-grade-apigateway.mdx',
            
            # Tools
            'mkjwk': 'tools/mkjwk-generator.mdx',
            'mkjose': 'tools/mkjose-generator.mdx',
            'cbor': 'tools/cbor-zone.mdx',
            'templates': 'tools/templates-toolkits.mdx',
            'terraform_provider': 'tools/terraform-provider.mdx',
            'api_explorer': 'tools/api-explorer.mdx',
            'management_console': 'tools/management-console.mdx',
            
            # Reference
            'relnotes': 'reference/release-notes.mdx',
            'knowledge_base': 'reference/knowledge-base.mdx',
            'definitive_guide': 'reference/definitive-guide.mdx',
            'standards': 'reference/standards-compliance.mdx'
        }

    def extract_content_from_html(self, html_file: Path) -> Dict:
        """Extract structured content from HTML file with enhanced parsing"""
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
            
            # Extract version info
            version_info = ""
            alert_elem = soup.find('div', class_='alert')
            if alert_elem and '3.0' in alert_elem.get_text():
                version_info = alert_elem.get_text().strip()
            
            return {
                'title': title,
                'description': description,
                'content': content_div,
                'soup': soup,
                'version_info': version_info
            }
        except Exception as e:
            logger.error(f"Error processing {html_file}: {e}")
            return {}

    def convert_html_to_mdx(self, content_div, soup) -> str:
        """Convert HTML content to MDX format with enhanced component handling"""
        mdx_content = []
        
        # Process each element
        for element in content_div.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'blockquote', 'pre', 'code', 'img', 'table', 'div', 'figure']):
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
                
            elif element.name == 'figure':
                mdx_content.append(self.process_figure(element))
                
            elif element.name == 'table':
                mdx_content.append(self.process_table(element))
                
            elif element.name == 'div' and element.get('class'):
                classes = element.get('class', [])
                if 'alert' in classes:
                    mdx_content.append(self.process_alert(element))
                elif 'highlight' in classes:
                    mdx_content.append(self.process_code_block(element))
                elif 'mermaid' in classes:
                    mdx_content.append(self.process_mermaid(element))
                elif 'accordion' in classes:
                    mdx_content.append(self.process_accordion(element))
                elif 'card' in classes:
                    mdx_content.append(self.process_card(element))
        
        return '\n'.join(mdx_content)

    def process_paragraph(self, p_elem) -> str:
        """Process paragraph content with enhanced link and formatting handling"""
        text = str(p_elem)
        
        # Convert links with proper handling
        text = re.sub(r'<a href="([^"]*)"[^>]*>([^<]*)</a>', self.convert_link, text)
        
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

    def convert_link(self, match) -> str:
        """Convert HTML links to Markdown format"""
        url, text = match.groups()
        
        # Handle internal links
        if url.startswith('/developers/'):
            # Convert to relative path
            path_parts = url.split('/')
            if len(path_parts) > 2:
                page_name = path_parts[-1]
                if page_name in self.page_mappings:
                    return f"[{text}](/{self.page_mappings[page_name]})"
        
        # Handle external links
        if url.startswith('http'):
            return f"[{text}]({url})"
        
        # Handle relative links
        return f"[{text}]({url})"

    def process_list(self, list_elem) -> str:
        """Process lists with enhanced formatting"""
        items = []
        is_ordered = list_elem.name == 'ol'
        
        for li in list_elem.find_all('li', recursive=False):
            item_text = self.process_paragraph(li)
            if item_text.strip():
                prefix = "1. " if is_ordered else "- "
                items.append(f"{prefix}{item_text}")
        
        return '\n'.join(items) + '\n'

    def process_blockquote(self, blockquote_elem) -> str:
        """Process blockquotes"""
        text = self.process_paragraph(blockquote_elem)
        return f"> {text}\n"

    def process_code_block(self, code_elem) -> str:
        """Process code blocks with language detection"""
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
        """Process images with proper URL handling"""
        src = img_elem.get('src', '')
        alt = img_elem.get('alt', '')
        
        # Convert relative URLs to absolute
        if src.startswith('/'):
            src = f"https://storage.googleapis.com/authlete-website{src}"
        elif not src.startswith('http'):
            src = f"{self.image_base_url}{src}"
        
        return f"![{alt}]({src})\n"

    def process_figure(self, figure_elem) -> str:
        """Process figure elements"""
        img = figure_elem.find('img')
        if img:
            return self.process_image(img)
        return ""

    def process_table(self, table_elem) -> str:
        """Process tables with enhanced formatting"""
        rows = []
        for tr in table_elem.find_all('tr'):
            cells = []
            for td in tr.find_all(['td', 'th']):
                cell_text = td.get_text().strip()
                # Handle code in cells
                cell_text = re.sub(r'`([^`]+)`', r'`\1`', cell_text)
                cells.append(cell_text)
            if cells:
                rows.append('| ' + ' | '.join(cells) + ' |')
        
        if len(rows) > 1:
            # Add separator row
            separator = '|' + '|'.join([' --- ' for _ in rows[0].split('|')[1:-1]]) + '|'
            rows.insert(1, separator)
        
        return '\n'.join(rows) + '\n'

    def process_alert(self, alert_elem) -> str:
        """Process alert boxes with proper Mintlify components"""
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

    def process_mermaid(self, mermaid_elem) -> str:
        """Process Mermaid diagrams"""
        content = mermaid_elem.get_text().strip()
        return f"```mermaid\n{content}\n```\n"

    def process_accordion(self, accordion_elem) -> str:
        """Process accordion elements"""
        # This would need to be converted to Mintlify Accordion components
        return f"<!-- Accordion content: {accordion_elem.get_text()[:100]}... -->\n"

    def process_card(self, card_elem) -> str:
        """Process card elements"""
        # This would need to be converted to Mintlify Card components
        return f"<!-- Card content: {card_elem.get_text()[:100]}... -->\n"

    def create_mdx_file(self, content_data: Dict, output_path: Path) -> bool:
        """Create MDX file with enhanced frontmatter and content"""
        try:
            # Create enhanced frontmatter
            frontmatter = f"""---
title: '{content_data['title']}'
description: '{content_data['description']}'
---

"""
            
            # Add version info if present
            if content_data.get('version_info'):
                frontmatter += f"<Info>\n{content_data['version_info']}\n</Info>\n\n"
            
            # Convert content to MDX
            mdx_content = self.convert_html_to_mdx(content_data['content'], content_data['soup'])
            
            # Combine frontmatter and content
            full_content = frontmatter + mdx_content
            
            # Write to file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            logger.info(f"Created MDX file: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error creating MDX file {output_path}: {e}")
            return False

    def determine_output_path(self, html_file: Path) -> Optional[Path]:
        """Determine output path based on file mapping"""
        # Get the parent directory name (which is the actual page name)
        parent_dir = html_file.parent.name
        file_name = html_file.stem
        
        logger.info(f"Determining output path for {parent_dir}/{file_name}")
        
        # Check direct mappings first
        if parent_dir in self.page_mappings:
            return self.target_dir / self.page_mappings[parent_dir]
        
        # Check for partial matches
        for key, path in self.page_mappings.items():
            if key in parent_dir.lower():
                return self.target_dir / path
        
        # Special handling for tutorial subdirectories
        if 'tutorial' in str(html_file):
            if 'oauth' in parent_dir:
                return self.target_dir / 'tutorials/oauth-tutorial.mdx'
            elif 'oidc' in parent_dir:
                return self.target_dir / 'tutorials/oidc-tutorial.mdx'
            elif 'fapi' in parent_dir:
                return self.target_dir / 'tutorials/fapi-tutorial.mdx'
            elif 'java' in parent_dir:
                return self.target_dir / 'tutorials/java-getting-started.mdx'
            elif 'aws' in parent_dir:
                return self.target_dir / 'tutorials/aws-cognito-integration.mdx'
            elif 'financial' in parent_dir:
                return self.target_dir / 'tutorials/financial-grade-apigateway.mdx'
            elif 'signup' in parent_dir:
                return self.target_dir / 'tutorials/signup-to-first-api.mdx'
        
        # Default fallback
        return self.target_dir / f"concepts/{parent_dir}.mdx"

    def migrate_all_docs(self):
        """Migrate all HTML documentation files"""
        logger.info("Starting enhanced documentation migration...")
        
        # Find all HTML files
        html_files = list(self.source_dir.rglob("*.html"))
        logger.info(f"Found {len(html_files)} HTML files to migrate")
        
        migrated_count = 0
        failed_count = 0
        
        for html_file in html_files:
            try:
                # Skip non-content files
                if any(skip in str(html_file) for skip in ['layout', 'partial', 'base', '404']):
                    continue
                
                # Only process index.html files in subdirectories
                if html_file.name != 'index.html':
                    continue
                
                logger.info(f"Processing {html_file}")
                
                # Extract content
                content_data = self.extract_content_from_html(html_file)
                if not content_data:
                    logger.warning(f"No content extracted from {html_file}")
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
        
        logger.info(f"Enhanced migration complete! Migrated: {migrated_count}, Failed: {failed_count}")

def main():
    """Main function to run the enhanced migration"""
    source_dir = "/Users/muhammadshariqnazr/website/public/developers"
    target_dir = "/Users/muhammadshariqnazr/Downloads/new-api-doc"
    
    migrator = EnhancedAuthleteMigrator(source_dir, target_dir)
    migrator.migrate_all_docs()

if __name__ == "__main__":
    main()
