#!/usr/bin/env python3
"""
Auto-generate models.mdx from speakeasy.yaml
This script extracts schemas from the OpenAPI spec and generates a models.mdx file
"""

import yaml
import os
from pathlib import Path
from typing import Dict, List, Any

def extract_schema_info(schema: Dict[str, Any], schema_name: str) -> Dict[str, Any]:
    """Extract relevant information from a schema"""
    info = {
        'name': schema_name,
        'type': schema.get('type', 'object'),
        'description': schema.get('description', ''),
        'properties': {},
        'required': schema.get('required', []),
        'enum': schema.get('enum', []),
        'items': schema.get('items', {}),
        'allOf': schema.get('allOf', [])
    }
    
    # Extract properties
    if 'properties' in schema:
        for prop_name, prop_def in schema['properties'].items():
            info['properties'][prop_name] = {
                'type': prop_def.get('type', 'string'),
                'description': prop_def.get('description', ''),
                'enum': prop_def.get('enum', []),
                'items': prop_def.get('items', {}),
                'format': prop_def.get('format', '')
            }
    
    return info

def format_property(prop_name: str, prop_info: Dict[str, Any], is_required: bool = False) -> str:
    """Format a single property for YAML output"""
    required_marker = " # Required" if is_required else ""
    
    lines = [f"    {prop_name}:{required_marker}"]
    
    if prop_info['type']:
        lines.append(f"      type: {prop_info['type']}")
    
    if prop_info['description']:
        # Handle multi-line descriptions
        desc = prop_info['description'].strip()
        if '\n' in desc:
            lines.append(f"      description: |")
            for line in desc.split('\n'):
                lines.append(f"        {line}")
        else:
            lines.append(f"      description: {desc}")
    
    if prop_info['enum']:
        lines.append(f"      enum:")
        for enum_val in prop_info['enum']:
            lines.append(f"        - {enum_val}")
    
    if prop_info['items'] and prop_info['items'].get('type'):
        lines.append(f"      items:")
        lines.append(f"        type: {prop_info['items']['type']}")
    
    if prop_info['format']:
        lines.append(f"      format: {prop_info['format']}")
    
    return '\n'.join(lines)

def generate_schema_yaml(schema_info: Dict[str, Any]) -> str:
    """Generate YAML representation of a schema"""
    lines = [f"{schema_info['name']}:"]
    
    if schema_info['type']:
        lines.append(f"  type: {schema_info['type']}")
    
    if schema_info['description']:
        desc = schema_info['description'].strip()
        if '\n' in desc:
            lines.append(f"  description: |")
            for line in desc.split('\n'):
                lines.append(f"    {line}")
        else:
            lines.append(f"  description: {desc}")
    
    if schema_info['enum']:
        lines.append(f"  enum:")
        for enum_val in schema_info['enum']:
            lines.append(f"    - {enum_val}")
    
    if schema_info['properties']:
        if schema_info['required']:
            lines.append(f"  required:")
            for req_prop in schema_info['required']:
                lines.append(f"    - {req_prop}")
        
        lines.append(f"  properties:")
        for prop_name, prop_info in schema_info['properties'].items():
            is_required = prop_name in schema_info['required']
            prop_yaml = format_property(prop_name, prop_info, is_required)
            lines.append(prop_yaml)
    
    return '\n'.join(lines)

def categorize_schemas(schemas: Dict[str, Dict[str, Any]]) -> Dict[str, List[str]]:
    """Categorize schemas by type"""
    categories = {
        'core': [],
        'requests': [],
        'responses': [],
        'errors': [],
        'enums': [],
        'utilities': []
    }
    
    for schema_name, schema_info in schemas.items():
        schema_name_lower = schema_name.lower()
        
        if schema_name_lower in ['client', 'service', 'user', 'scope']:
            categories['core'].append(schema_name)
        elif schema_name_lower.endswith('request'):
            categories['requests'].append(schema_name)
        elif schema_name_lower.endswith('response'):
            categories['responses'].append(schema_name)
        elif schema_name_lower in ['errorresponse', 'badrequest', 'unauthorized', 'forbidden', 'notfound', 'internalservererror']:
            categories['errors'].append(schema_name)
        elif schema_info.get('enum') or schema_name_lower in ['granttype', 'responsetype', 'clienttype', 'applicationtype', 'display', 'prompt']:
            categories['enums'].append(schema_name)
        else:
            categories['utilities'].append(schema_name)
    
    return categories

def generate_models_mdx(spec_path: str, output_path: str):
    """Generate models.mdx from OpenAPI spec"""
    print(f"🔍 Reading OpenAPI spec from {spec_path}")
    
    with open(spec_path, 'r', encoding='utf-8') as f:
        spec = yaml.safe_load(f)
    
    if 'components' not in spec or 'schemas' not in spec['components']:
        print("❌ No schemas found in the OpenAPI spec")
        return
    
    schemas = spec['components']['schemas']
    print(f"📊 Found {len(schemas)} schemas")
    
    # Extract schema information
    schema_infos = {}
    for schema_name, schema_def in schemas.items():
        schema_infos[schema_name] = extract_schema_info(schema_def, schema_name)
    
    # Categorize schemas
    categories = categorize_schemas(schema_infos)
    
    # Generate MDX content
    mdx_content = '''---
title: "API Models"
description: "Data models and schemas used in the Authlete API"
---

# API Models

This page contains the data models and schemas used throughout the Authlete API. These models define the structure of requests, responses, and data objects.

*This page is automatically generated from the OpenAPI specification.*

'''
    
    # Core Models
    if categories['core']:
        mdx_content += "## Core Models\n\n"
        for schema_name in sorted(categories['core']):
            schema_info = schema_infos[schema_name]
            mdx_content += f"### {schema_name}\n\n"
            mdx_content += f"The {schema_name} model represents "
            if schema_name.lower() == 'client':
                mdx_content += "an OAuth 2.0 client application.\n\n"
            elif schema_name.lower() == 'service':
                mdx_content += "an OAuth 2.0 authorization server.\n\n"
            else:
                mdx_content += f"a {schema_name.lower()} entity.\n\n"
            
            mdx_content += "<CodeGroup>\n\n"
            mdx_content += f"```yaml {schema_name} Schema\n"
            mdx_content += generate_schema_yaml(schema_info)
            mdx_content += "\n```\n\n"
            mdx_content += "</CodeGroup>\n\n"
    
    # Request Models
    if categories['requests']:
        mdx_content += "## Request Models\n\n"
        for schema_name in sorted(categories['requests']):
            schema_info = schema_infos[schema_name]
            mdx_content += f"### {schema_name}\n\n"
            mdx_content += f"Request model for {schema_name.lower().replace('request', '')} operations.\n\n"
            
            mdx_content += "<CodeGroup>\n\n"
            mdx_content += f"```yaml {schema_name} Schema\n"
            mdx_content += generate_schema_yaml(schema_info)
            mdx_content += "\n```\n\n"
            mdx_content += "</CodeGroup>\n\n"
    
    # Response Models
    if categories['responses']:
        mdx_content += "## Response Models\n\n"
        for schema_name in sorted(categories['responses']):
            schema_info = schema_infos[schema_name]
            mdx_content += f"### {schema_name}\n\n"
            mdx_content += f"Response model for {schema_name.lower().replace('response', '')} operations.\n\n"
            
            mdx_content += "<CodeGroup>\n\n"
            mdx_content += f"```yaml {schema_name} Schema\n"
            mdx_content += generate_schema_yaml(schema_info)
            mdx_content += "\n```\n\n"
            mdx_content += "</CodeGroup>\n\n"
    
    # Error Models
    if categories['errors']:
        mdx_content += "## Error Models\n\n"
        for schema_name in sorted(categories['errors']):
            schema_info = schema_infos[schema_name]
            mdx_content += f"### {schema_name}\n\n"
            mdx_content += f"Error response model for {schema_name.lower()} scenarios.\n\n"
            
            mdx_content += "<CodeGroup>\n\n"
            mdx_content += f"```yaml {schema_name} Schema\n"
            mdx_content += generate_schema_yaml(schema_info)
            mdx_content += "\n```\n\n"
            mdx_content += "</CodeGroup>\n\n"
    
    # Enums
    if categories['enums']:
        mdx_content += "## Enums\n\n"
        for schema_name in sorted(categories['enums']):
            schema_info = schema_infos[schema_name]
            mdx_content += f"### {schema_name}\n\n"
            mdx_content += f"Supported {schema_name.lower()} values.\n\n"
            
            mdx_content += "<CodeGroup>\n\n"
            mdx_content += f"```yaml {schema_name} Enum\n"
            mdx_content += generate_schema_yaml(schema_info)
            mdx_content += "\n```\n\n"
            mdx_content += "</CodeGroup>\n\n"
    
    # Utility Models
    if categories['utilities']:
        mdx_content += "## Utility Models\n\n"
        for schema_name in sorted(categories['utilities']):
            schema_info = schema_infos[schema_name]
            mdx_content += f"### {schema_name}\n\n"
            mdx_content += f"Utility model for {schema_name.lower()} operations.\n\n"
            
            mdx_content += "<CodeGroup>\n\n"
            mdx_content += f"```yaml {schema_name} Schema\n"
            mdx_content += generate_schema_yaml(schema_info)
            mdx_content += "\n```\n\n"
            mdx_content += "</CodeGroup>\n\n"
    
    # Add footer
    mdx_content += '''## Additional Resources

For more detailed information about these models and their usage, refer to:

- [OAuth 2.0 RFC 6749](https://tools.ietf.org/html/rfc6749)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
- [OAuth 2.0 Dynamic Client Registration Protocol (RFC 7591)](https://tools.ietf.org/html/rfc7591)
- [OAuth 2.0 Token Exchange (RFC 8693)](https://tools.ietf.org/html/rfc8693)

---

*This page was automatically generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} from the OpenAPI specification.*
'''
    
    # Write the file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(mdx_content)
    
    print(f"✅ Generated models.mdx with {len(schema_infos)} schemas")
    print(f"📁 Output saved to: {output_path}")

def main():
    """Main function"""
    import argparse
    from datetime import datetime
    
    parser = argparse.ArgumentParser(description='Generate models.mdx from OpenAPI spec')
    parser.add_argument('--spec', default='app/specs/shared/3.0.15/speakeasy.yaml', 
                       help='Path to OpenAPI spec file')
    parser.add_argument('--output', default='reference/models.mdx', 
                       help='Output path for models.mdx')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.spec):
        print(f"❌ Spec file not found: {args.spec}")
        return
    
    generate_models_mdx(args.spec, args.output)

if __name__ == "__main__":
    main()
