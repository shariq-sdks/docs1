#!/usr/bin/env python3
"""
Knowledge Base Migration Script
Migrates Knowledge Base content to fill gaps in the simplified structure
"""

import re
import logging
from pathlib import Path
from typing import Optional, Dict
from bs4 import BeautifulSoup, Tag

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class KBMigrator:
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.image_base_url = "https://storage.googleapis.com/authlete-website"
        
        # Mapping from KB paths to our reference structure
        self.kb_mappings = {
            # Deployment & Operations - Infrastructure
            'deployment/on-premises/kubernetes-deployment-installation-guide': 'reference/kubernetes-deployment',
            'deployment/on-premises/aws-ecs-deployment-installation-guide': 'reference/aws-ecs-deployment',
            'deployment/on-premises/on-premises-packaging': 'reference/on-premises-packaging',
            'deployment/on-premises/v2/on-premises-packaging': 'reference/on-premises-packaging-v2',
            'deployment/on-premises/v2/https-settings-for-authlete-api-servers': 'reference/https-settings',
            
            # Performance & Monitoring
            'deployment/performance/caching-introspection-responses': 'reference/caching-introspection',
            
            # Migration & Troubleshooting
            'deployment/migration-from-existing-system/migrate-from-old-version': 'reference/migrate-from-old-version',
            'deployment/migration-from-existing-system/migrating-access-tokens': 'reference/migrating-access-tokens',
            'deployment/migration-from-existing-system/preserving-existing-client-id': 'reference/preserving-client-id',
            
            # Security & Networking
            'deployment/security/jwk-set-for-service': 'reference/jwk-set-for-service',
            'deployment/security/jwk-set-for-client': 'reference/jwk-set-for-client',
            'deployment/security/providing-user-attributes': 'reference/providing-user-attributes',
            'deployment/security/v2/jwk-set-for-service': 'reference/jwk-set-for-service-v2',
            'deployment/security/v2/jwk-set-for-client': 'reference/jwk-set-for-client-v2',
            'deployment/networking/proxy-server': 'reference/proxy-server',
            
            # Integration
            'deployment/integration-with-api-gateways/amazon-api-gateway': 'reference/amazon-api-gateway',
            'deployment/integration-with-api-gateways/api-gateway-products': 'reference/api-gateway-products',
            
            # Operations
            'operations/service-configuration/service-settings': 'reference/service-settings',
            'operations/service-configuration/v2/service-settings': 'reference/service-settings-v2',
            'deployment/developer-console/login-to-developer-console-as-service-owner': 'reference/developer-console-login',
            'deployment/developer-console/multiple-developer-accounts': 'reference/multiple-developer-accounts',
            
            # Developer Tools
            'deployment/developer-console': 'reference/developer-console',
            
            # Standards & Compliance - OAuth & OIDC Standards
            'oauth-and-openid-connect/client-authentication/client-authentication': 'reference/client-authentication',
            'oauth-and-openid-connect/client-authentication/client-secret-jwt': 'reference/client-secret-jwt',
            'oauth-and-openid-connect/client-authentication/client-auth-private-key-jwt': 'reference/client-private-key-jwt',
            'oauth-and-openid-connect/client-authentication/tls-client-auth': 'reference/tls-client-auth',
            'oauth-and-openid-connect/scopes/scope-attributes': 'reference/scopes',
            'oauth-and-openid-connect/introspection/two-introspection-apis': 'reference/introspection',
            'oauth-and-openid-connect/authorization-requests/request-objects': 'reference/authorization-requests',
            'oauth-and-openid-connect/authorization-requests/pushed-authorization-requests': 'reference/pushed-authorization-requests',
            'oauth-and-openid-connect/authorization-requests/rich-authorization-requests': 'reference/rich-authorization-requests',
            'oauth-and-openid-connect/authorization-requests/jar': 'reference/jar',
            'oauth-and-openid-connect/authorization-requests/resource-indicator': 'reference/resource-indicator',
            
            # Token Types
            'oauth-and-openid-connect/access-tokens/jwt-based-access-token': 'reference/access-tokens',
            'oauth-and-openid-connect/access-tokens/single-access-token-per-subject': 'reference/single-access-token',
            'oauth-and-openid-connect/access-tokens/extra-properties': 'reference/access-token-properties',
            'oauth-and-openid-connect/access-tokens/auth-token-get-list': 'reference/access-token-list',
            'oauth-and-openid-connect/refresh-tokens/how-to-enable-refresh-token-grant-type': 'reference/refresh-tokens',
            'oauth-and-openid-connect/tokens/token-duration-per-client': 'reference/token-management',
            'oauth-and-openid-connect/tokens/token-duration-per-scope': 'reference/token-duration-scope',
            'oauth-and-openid-connect/tokens/changing-token-durations': 'reference/token-duration-change',
            'oauth-and-openid-connect/tokens/token-revocation-policy': 'reference/token-revocation',
            'oauth-and-openid-connect/proof-of-possession-pop-tokens/certificate-bound-access-tokens': 'reference/proof-of-possession-tokens',
            'oauth-and-openid-connect/proof-of-possession-pop-tokens/dpop': 'reference/dpop',
            
            # Error Handling
            'oauth-and-openid-connect/error-handling/fail-api': 'reference/error-handling',
            'oauth-and-openid-connect/error-handling/flags-in-authlete': 'reference/flags-in-authlete',
            'oauth-and-openid-connect/error-handling/result-code-in-authlete': 'reference/result-codes',
            'oauth-and-openid-connect/error-handling/suppressing-error-details-in-responsecontent': 'reference/suppressing-error-details',
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
        """Convert HTML content to MDX format"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Convert images
        for img in soup.find_all('img'):
            src = img.get('src', '')
            if src.startswith('/'):
                src = f"{self.image_base_url}{src}"
            elif not src.startswith('http'):
                src = f"{self.image_base_url}/img/kb{src}"
            
            alt = img.get('alt', '')
            img.replace_with(f"![{alt}]({src})")
        
        # Convert links
        for link in soup.find_all('a'):
            href = link.get('href', '')
            text = link.get_text().strip()
            if href.startswith('http'):
                link.replace_with(f"[{text}]({href})")
            else:
                link.replace_with(text)
        
        # Convert code blocks
        for code in soup.find_all('code'):
            if code.parent.name == 'pre':
                # This is a code block
                language = code.get('class', [''])[0].replace('language-', '') if code.get('class') else ''
                code_text = code.get_text()
                code.parent.replace_with(f"```{language}\n{code_text}\n```")
            else:
                # Inline code
                code_text = code.get_text()
                code.replace_with(f"`{code_text}`")
        
        # Convert tables
        for table in soup.find_all('table'):
            table_md = self.convert_table_to_markdown(table)
            table.replace_with(table_md)
        
        # Convert alerts and info boxes
        for alert in soup.find_all(['div', 'section'], class_=re.compile(r'(alert|info|warning|success|note|tip)')):
            alert_type = 'Info'
            if 'warning' in alert.get('class', []):
                alert_type = 'Warning'
            elif 'success' in alert.get('class', []):
                alert_type = 'Success'
            elif 'error' in alert.get('class', []):
                alert_type = 'Warning'
            
            content = alert.get_text().strip()
            alert.replace_with(f"<{alert_type}>\n{content}\n</{alert_type}>")
        
        # Convert headings
        for i in range(1, 7):
            for heading in soup.find_all(f'h{i}'):
                text = heading.get_text().strip()
                heading.replace_with(f"{'#' * i} {text}")
        
        # Convert lists
        for ul in soup.find_all('ul'):
            ul_md = self.convert_list_to_markdown(ul, ordered=False)
            ul.replace_with(ul_md)
        
        for ol in soup.find_all('ol'):
            ol_md = self.convert_list_to_markdown(ol, ordered=True)
            ol.replace_with(ol_md)
        
        # Convert paragraphs
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if text:
                p.replace_with(f"{text}\n\n")
        
        # Get the final markdown
        markdown = soup.get_text()
        
        # Clean up extra whitespace
        markdown = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown)
        markdown = markdown.strip()
        
        return markdown

    def convert_table_to_markdown(self, table: Tag) -> str:
        """Convert HTML table to Markdown"""
        rows = []
        for tr in table.find_all('tr'):
            cells = []
            for td in tr.find_all(['td', 'th']):
                cell_text = td.get_text().strip()
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
        """Convert HTML list to Markdown"""
        items = []
        for li in list_elem.find_all('li', recursive=False):
            text = li.get_text().strip()
            if text:
                items.append(text)
        
        if ordered:
            return '\n'.join([f"{i+1}. {item}" for i, item in enumerate(items)]) + '\n\n'
        else:
            return '\n'.join([f"- {item}" for item in items]) + '\n\n'

    def create_mdx_file(self, content_data: Dict, output_path: Path) -> bool:
        """Create MDX file with content"""
        try:
            # Ensure directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
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
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter)
            
            logger.info(f"Created MDX file: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error creating MDX file {output_path}: {e}")
            return False

    def migrate_kb_content(self):
        """Migrate Knowledge Base content"""
        logger.info("Starting Knowledge Base migration...")
        
        migrated_count = 0
        failed_count = 0
        
        for kb_path, target_path in self.kb_mappings.items():
            try:
                # Find the HTML file
                html_file = self.source_dir / f"{kb_path}/index.html"
                
                if not html_file.exists():
                    logger.warning(f"HTML file not found: {html_file}")
                    continue
                
                # Extract content
                content_data = self.extract_content_from_html(html_file)
                if not content_data:
                    logger.warning(f"No content extracted from {html_file}")
                    continue
                
                # Create target path
                target_file = self.target_dir / f"{target_path}.mdx"
                
                # Create MDX file
                if self.create_mdx_file(content_data, target_file):
                    migrated_count += 1
                else:
                    failed_count += 1
                    
            except Exception as e:
                logger.error(f"Failed to migrate {kb_path}: {e}")
                failed_count += 1
        
        logger.info(f"Knowledge Base migration complete! Migrated: {migrated_count}, Failed: {failed_count}")

def main():
    """Main function to run the Knowledge Base migration"""
    source_dir = "/Users/muhammadshariqnazr/website/public/kb"
    target_dir = "/Users/muhammadshariqnazr/Downloads/new-api-doc"
    
    migrator = KBMigrator(source_dir, target_dir)
    migrator.migrate_kb_content()

if __name__ == "__main__":
    main()
