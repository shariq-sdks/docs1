#!/usr/bin/env python3
import os
import re
import yaml
import glob

def fix_mdx_structure(file_path):
    """Fix MDX structure and ensure compatibility"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file is empty or has issues
        if len(content.strip()) < 100:
            print(f"Warning: {file_path} seems too short")
            return False
        
        # Fix common MDX issues
        fixed_content = content
        
        # 1. Ensure proper frontmatter
        if not content.startswith('---'):
            print(f"Adding frontmatter to {file_path}")
            fixed_content = '---\ntitle: "Untitled"\ndescription: "No description"\n---\n\n' + content
        
        # 2. Fix YAML frontmatter issues
        frontmatter_match = re.match(r'^---\n(.*?)\n---', fixed_content, re.DOTALL)
        if frontmatter_match:
            frontmatter_content = frontmatter_match.group(1)
            try:
                # Validate YAML
                yaml.safe_load(frontmatter_content)
            except yaml.YAMLError as e:
                print(f"Fixing YAML frontmatter in {file_path}: {e}")
                # Fix common YAML issues
                frontmatter_content = re.sub(r'^(\w+):\s*([^\n]+)"\s*$', r'\1: "\2"', frontmatter_content, flags=re.MULTILINE)
                fixed_content = f"---\n{frontmatter_content}\n---\n{fixed_content[frontmatter_match.end():]}"
        
        # 3. Fix markdown issues
        # Remove any problematic characters
        fixed_content = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', fixed_content)
        
        # 4. Ensure proper heading structure
        if not re.search(r'^#\s+', fixed_content, re.MULTILINE):
            print(f"Adding main heading to {file_path}")
            fixed_content = re.sub(r'^(---\n.*?\n---\n\n)', r'\1# Page Title\n\n', fixed_content)
        
        # 5. Fix code blocks
        fixed_content = re.sub(r'```(\w+)?\n(.*?)\n```', r'```\1\n\2\n```', fixed_content, flags=re.DOTALL)
        
        # 6. Ensure file ends with newline
        if not fixed_content.endswith('\n'):
            fixed_content += '\n'
        
        # Write back if changed
        if fixed_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"Fixed structure issues in {file_path}")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def create_proper_deployment_pages():
    """Create properly structured deployment pages"""
    
    # Infrastructure Setup
    infrastructure_content = '''---
title: "Infrastructure Setup"
description: "Complete guide to setting up Authlete infrastructure for production deployments"
---

# Infrastructure Setup

This guide covers the essential infrastructure components and configurations needed to deploy Authlete in production environments.

## Prerequisites

Before setting up your Authlete infrastructure, ensure you have:

- **Authlete Account** - Active service subscription
- **Domain Configuration** - Valid domain for your authorization server
- **SSL/TLS Certificates** - Valid certificates for HTTPS endpoints
- **DNS Configuration** - Proper DNS records for your domain

## Core Infrastructure Components

### 1. Authorization Server

The authorization server is the core component that handles OAuth 2.0 and OpenID Connect flows.

**Key Requirements:**
- High availability (99.9% uptime)
- Load balancing for traffic distribution
- SSL/TLS termination
- Rate limiting and DDoS protection

### 2. Token Endpoint

Secure endpoint for token issuance and refresh operations.

**Configuration:**
```yaml
endpoints:
  token: "https://auth.yourdomain.com/oauth/token"
  introspection: "https://auth.yourdomain.com/oauth/introspect"
  revocation: "https://auth.yourdomain.com/oauth/revoke"
```

### 3. UserInfo Endpoint

Provides user information for OpenID Connect implementations.

**Configuration:**
```yaml
endpoints:
  userinfo: "https://auth.yourdomain.com/oauth/userinfo"
  jwks: "https://auth.yourdomain.com/.well-known/jwks.json"
```

## Deployment Options

### Cloud Deployment

**Recommended Cloud Providers:**
- AWS (Amazon Web Services)
- Google Cloud Platform
- Microsoft Azure
- DigitalOcean

**Key Considerations:**
- Auto-scaling capabilities
- Global CDN integration
- Managed database services
- Security and compliance features

### On-Premises Deployment

For organizations requiring on-premises deployment:

**Requirements:**
- Container orchestration (Kubernetes/Docker Swarm)
- Load balancer configuration
- Database setup (PostgreSQL/MySQL)
- Monitoring and logging infrastructure

## Security Configuration

### SSL/TLS Setup

1. **Certificate Management**
   - Use Let's Encrypt for free certificates
   - Implement certificate auto-renewal
   - Configure HSTS headers

2. **Cipher Suites**
   - Use strong encryption algorithms
   - Disable weak protocols (TLS 1.0, 1.1)
   - Implement perfect forward secrecy

### Network Security

- **Firewall Rules** - Restrict access to necessary ports only
- **VPC Configuration** - Isolate services in private subnets
- **WAF Integration** - Web Application Firewall for additional protection

## Database Configuration

### Primary Database

**Requirements:**
- High availability setup
- Automated backups
- Encryption at rest
- Connection pooling

**Recommended Setup:**
```yaml
database:
  type: "postgresql"
  version: "13+"
  replicas: 3
  backup: "daily"
  encryption: "enabled"
```

### Caching Layer

Implement Redis for session and token caching:

```yaml
cache:
  type: "redis"
  cluster: "enabled"
  persistence: "aof"
  memory: "8gb"
```

## Monitoring and Alerting

### Key Metrics to Monitor

- **Performance Metrics**
  - Response times
  - Throughput (requests/second)
  - Error rates
  - Database connection pools

- **Security Metrics**
  - Failed authentication attempts
  - Suspicious activity patterns
  - Certificate expiration dates

### Alerting Configuration

Set up alerts for:
- High error rates (>5%)
- Slow response times (>2s)
- Database connection issues
- Certificate expiration (30 days)

## Next Steps

1. **Configure Service Settings** - Set up your OAuth 2.0 service
2. **Register Clients** - Add your applications
3. **Test Endpoints** - Verify all endpoints are working
4. **Set Up Monitoring** - Implement logging and alerting
5. **Go Live** - Deploy to production

## Additional Resources

- [Terraform Deployment Guide](/production/terraform-deployment)
- [Monitoring and Logging Setup](/production/monitoring-logging)
- [Troubleshooting Common Issues](/production/troubleshooting)
'''

    # Terraform Deployment
    terraform_content = '''---
title: "Terraform Deployment"
description: "Deploy and manage Authlete infrastructure using Terraform for Infrastructure as Code"
---

# Terraform Deployment

Deploy and manage your Authlete infrastructure using Terraform for consistent, repeatable, and version-controlled deployments.

## Overview

The Authlete Terraform provider allows you to:
- Define your OAuth 2.0 services as code
- Manage client applications programmatically
- Version control your authentication configuration
- Automate deployment pipelines
- Ensure consistency across environments

## Prerequisites

Before using Terraform with Authlete:

1. **Install Terraform** (v1.0+)
2. **Get Authlete Credentials** - Service API key and secret
3. **Set Up Backend** - Configure state storage
4. **Install Provider** - Add Authlete provider to your configuration

## Quick Start

### 1. Initialize Terraform

Create a new directory and initialize Terraform:

```bash
mkdir authlete-terraform
cd authlete-terraform
terraform init
```

### 2. Configure Provider

Create `main.tf`:

```hcl
terraform {
  required_providers {
    authlete = {
      source  = "authlete/authlete"
      version = "~> 1.0"
    }
  }
}

provider "authlete" {
  api_key    = var.authlete_api_key
  api_secret = var.authlete_api_secret
  base_url   = "https://api.authlete.com"
}
```

### 3. Create Variables

Create `variables.tf`:

```hcl
variable "authlete_api_key" {
  description = "Authlete API Key"
  type        = string
  sensitive   = true
}

variable "authlete_api_secret" {
  description = "Authlete API Secret"
  type        = string
  sensitive   = true
}
```

### 4. Define Service

Create `service.tf`:

```hcl
resource "authlete_service" "main" {
  service_name        = "My OAuth Service"
  issuer             = "https://auth.example.com"
  description        = "Production OAuth 2.0 Service"
  supported_grant_types = ["AUTHORIZATION_CODE", "REFRESH_TOKEN"]
  supported_response_types = ["CODE"]
  
  # Supported scopes
  supported_scopes = [
    "read",
    "write", 
    "openid",
    "profile",
    "email"
  ]
  
  # Token endpoint
  access_token_duration = 3600
  refresh_token_duration = 86400
  
  # Security settings
  pkce_required = true
  pkce_s256_required = true
}
```

### 5. Deploy

```bash
terraform plan
terraform apply
```

## Advanced Configuration

### Client Management

Create and manage OAuth clients:

```hcl
resource "authlete_client" "web_app" {
  client_name = "Web Application"
  client_type = "CONFIDENTIAL"
  redirect_uris = [
    "https://app.example.com/callback",
    "https://app.example.com/auth/callback"
  ]
  grant_types = ["AUTHORIZATION_CODE", "REFRESH_TOKEN"]
  response_types = ["CODE"]
  scopes = ["read", "write", "openid"]
  
  # Security settings
  tls_client_certificate_bound_access_tokens = true
  dpop_required = false
}

resource "authlete_client" "mobile_app" {
  client_name = "Mobile Application"
  client_type = "PUBLIC"
  redirect_uris = ["com.example.app://callback"]
  grant_types = ["AUTHORIZATION_CODE", "REFRESH_TOKEN"]
  response_types = ["CODE"]
  scopes = ["read", "openid", "profile"]
  
  # PKCE required for public clients
  pkce_required = true
  pkce_s256_required = true
}
```

## State Management

### Remote State

Store Terraform state remotely:

```hcl
terraform {
  backend "s3" {
    bucket = "my-authlete-terraform-state"
    key    = "authlete/terraform.tfstate"
    region = "us-west-2"
  }
}
```

### State Locking

Enable state locking to prevent concurrent modifications:

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "authlete/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}
```

## Environment Management

### Development Environment

```hcl
# environments/dev/main.tf
module "authlete" {
  source = "../../modules/authlete"
  
  environment = "dev"
  service_name = "Dev OAuth Service"
  issuer = "https://dev-auth.example.com"
}
```

### Production Environment

```hcl
# environments/prod/main.tf
module "authlete" {
  source = "../../modules/authlete"
  
  environment = "prod"
  service_name = "Production OAuth Service"
  issuer = "https://auth.example.com"
  
  # Production-specific settings
  access_token_duration = 1800  # 30 minutes
  refresh_token_duration = 2592000  # 30 days
}
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Deploy Authlete Infrastructure

on:
  push:
    branches: [main]
    paths: ['terraform/**']

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v2
        with:
          terraform_version: 1.5.0
          
      - name: Terraform Init
        run: terraform init
        working-directory: ./terraform
        
      - name: Terraform Plan
        run: terraform plan
        working-directory: ./terraform
        env:
          TF_VAR_authlete_api_key: ${{ secrets.AUTHLETE_API_KEY }}
          TF_VAR_authlete_api_secret: ${{ secrets.AUTHLETE_API_SECRET }}
          
      - name: Terraform Apply
        run: terraform apply -auto-approve
        working-directory: ./terraform
        env:
          TF_VAR_authlete_api_key: ${{ secrets.AUTHLETE_API_KEY }}
          TF_VAR_authlete_api_secret: ${{ secrets.AUTHLETE_API_SECRET }}
```

## Best Practices

### 1. Use Modules

Organize your configuration into reusable modules:

```hcl
# modules/authlete-service/main.tf
resource "authlete_service" "main" {
  service_name = var.service_name
  issuer      = var.issuer
  # ... other configuration
}
```

### 2. Environment Variables

Use environment variables for sensitive data:

```bash
export TF_VAR_authlete_api_key="your-api-key"
export TF_VAR_authlete_api_secret="your-api-secret"
```

### 3. State Management

- Always use remote state storage
- Enable state locking
- Regular state backups
- Separate state per environment

### 4. Security

- Never commit secrets to version control
- Use Terraform Cloud or similar for sensitive operations
- Rotate API keys regularly
- Use least privilege access

## Troubleshooting

### Common Issues

1. **Provider Authentication**
   ```bash
   # Verify credentials
   terraform plan
   ```

2. **State Conflicts**
   ```bash
   # Refresh state
   terraform refresh
   ```

3. **Resource Dependencies**
   ```hcl
   # Use explicit dependencies
   resource "authlete_client" "app" {
     depends_on = [authlete_service.main]
   }
   ```

## Additional Resources

- [Terraform Provider Documentation](https://registry.terraform.io/providers/authlete/authlete)
- [Infrastructure Setup Guide](/production/infrastructure-setup)
- [Monitoring and Logging](/production/monitoring-logging)
'''

    # Monitoring and Logging
    monitoring_content = '''---
title: "Monitoring and Logging"
description: "Set up comprehensive monitoring and logging for your Authlete deployment"
---

# Monitoring and Logging

Comprehensive monitoring and logging are essential for maintaining the health, security, and performance of your Authlete deployment in production.

## Overview

Effective monitoring helps you:
- Track system performance and availability
- Identify security threats and anomalies
- Debug issues quickly
- Ensure compliance requirements
- Optimize resource usage

## Key Metrics to Monitor

### Performance Metrics

**Response Times**
- Authorization endpoint response time
- Token endpoint response time
- UserInfo endpoint response time
- Database query performance

**Throughput**
- Requests per second (RPS)
- Concurrent user sessions
- Token issuance rate
- API call volume

**Error Rates**
- 4xx client errors
- 5xx server errors
- Authentication failures
- Token validation errors

### Security Metrics

**Authentication Events**
- Successful logins
- Failed authentication attempts
- Account lockouts
- Suspicious login patterns

**Authorization Events**
- Token grants and revocations
- Scope usage patterns
- Client access patterns
- Unusual access patterns

**Security Alerts**
- Brute force attacks
- Invalid token usage
- Unauthorized access attempts
- Certificate expiration warnings

## Logging Configuration

### Application Logs

**Log Levels**
```yaml
logging:
  level: "INFO"
  authlete: "DEBUG"
  security: "WARN"
  performance: "INFO"
```

**Log Format**
```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "INFO",
  "service": "authlete",
  "endpoint": "/oauth/token",
  "client_id": "12345",
  "user_id": "user@example.com",
  "duration_ms": 150,
  "status": 200,
  "message": "Token issued successfully"
}
```

### Security Logs

**Authentication Logs**
- Login attempts (success/failure)
- Password changes
- MFA events
- Account lockouts

**Authorization Logs**
- Token requests
- Scope grants
- Resource access
- Permission changes

**Audit Logs**
- Configuration changes
- Admin actions
- Data access
- System events

## Monitoring Tools

### Application Performance Monitoring (APM)

**Recommended Tools:**
- **New Relic** - Full-stack monitoring
- **Datadog** - Infrastructure and application monitoring
- **AppDynamics** - Enterprise APM
- **Elastic APM** - Open-source monitoring

**Key Dashboards:**
- Response time trends
- Error rate monitoring
- User activity patterns
- Resource utilization

### Infrastructure Monitoring

**System Metrics:**
- CPU usage
- Memory consumption
- Disk I/O
- Network traffic
- Database performance

**Cloud Monitoring:**
- AWS CloudWatch
- Google Cloud Monitoring
- Azure Monitor
- DigitalOcean Monitoring

### Log Management

**Centralized Logging:**
- **ELK Stack** (Elasticsearch, Logstash, Kibana)
- **Splunk** - Enterprise log analysis
- **Fluentd** - Log collection and forwarding
- **Grafana Loki** - Log aggregation system

## Alerting Configuration

### Critical Alerts

**System Health**
- Service availability < 99.9%
- Response time > 2 seconds
- Error rate > 5%
- Database connection failures

**Security Alerts**
- Multiple failed login attempts
- Unusual access patterns
- Invalid token usage spikes
- Certificate expiration (30 days)

**Performance Alerts**
- High CPU usage (>80%)
- Memory usage (>90%)
- Disk space (<10% free)
- Database slow queries

### Alert Channels

**Notification Methods:**
- Email notifications
- Slack integration
- PagerDuty for critical alerts
- SMS for emergency issues

**Alert Escalation:**
- Level 1: Immediate notification
- Level 2: Escalate after 5 minutes
- Level 3: Escalate after 15 minutes

## Compliance and Audit

### Audit Requirements

**Data Retention:**
- Authentication logs: 1 year
- Authorization logs: 6 months
- System logs: 3 months
- Security logs: 2 years

**Compliance Standards:**
- SOC 2 Type II
- ISO 27001
- GDPR compliance
- HIPAA (if applicable)

### Log Analysis

**Security Analysis:**
- Threat detection
- Anomaly detection
- Pattern analysis
- Forensic investigation

**Performance Analysis:**
- Trend analysis
- Capacity planning
- Optimization opportunities
- User behavior insights

## Implementation Guide

### 1. Set Up Logging Infrastructure

```yaml
# docker-compose.yml
version: '3.8'
services:
  authlete:
    image: authlete/service:latest
    environment:
      - LOG_LEVEL=INFO
      - LOG_FORMAT=json
    volumes:
      - ./logs:/app/logs
  
  elasticsearch:
    image: elasticsearch:8.8.0
    environment:
      - discovery.type=single-node
    ports:
      - "9200:9200"
  
  kibana:
    image: kibana:8.8.0
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch
```

### 2. Configure Monitoring

```yaml
# monitoring.yml
monitoring:
  metrics:
    enabled: true
    port: 9090
    path: /metrics
  
  health_checks:
    enabled: true
    port: 8080
    path: /health
  
  alerts:
    enabled: true
    webhook_url: "https://hooks.slack.com/your-webhook"
```

### 3. Set Up Dashboards

**Grafana Dashboard:**
- System metrics
- Application performance
- Security events
- User activity

**Custom Dashboards:**
- OAuth flow metrics
- Token usage patterns
- Client performance
- Error analysis

## Best Practices

### 1. Log Management

- Use structured logging (JSON format)
- Include correlation IDs
- Set appropriate log levels
- Implement log rotation
- Secure log storage

### 2. Monitoring Strategy

- Monitor from user perspective
- Set realistic thresholds
- Use multiple data sources
- Regular review and tuning
- Document alert procedures

### 3. Security Considerations

- Encrypt log data at rest
- Secure log transmission
- Access control for logs
- Regular security reviews
- Incident response procedures

## Troubleshooting

### Common Issues

**High Log Volume:**
- Adjust log levels
- Implement log filtering
- Use log sampling
- Optimize log storage

**Missing Metrics:**
- Check instrumentation
- Verify configuration
- Test monitoring tools
- Review data retention

**Alert Fatigue:**
- Tune alert thresholds
- Group related alerts
- Use alert suppression
- Regular alert review

## Additional Resources

- [Infrastructure Setup Guide](/production/infrastructure-setup)
- [Terraform Deployment](/production/terraform-deployment)
- [Troubleshooting Guide](/production/troubleshooting)
'''

    # Migration Guides
    migration_content = '''---
title: "Migration Guides"
description: "Comprehensive guides for migrating to Authlete from other OAuth 2.0 and OpenID Connect solutions"
---

# Migration Guides

This section provides step-by-step migration guides for moving from other OAuth 2.0 and OpenID Connect solutions to Authlete.

## Overview

Migrating to Authlete offers several benefits:
- **Simplified Implementation** - Reduce development time and complexity
- **Enhanced Security** - Built-in security best practices
- **Better Performance** - Optimized for high-scale deployments
- **Comprehensive Support** - Full OAuth 2.0 and OpenID Connect compliance
- **Easy Maintenance** - Managed service with automatic updates

## Migration Strategies

### 1. Big Bang Migration

Migrate everything at once during a maintenance window.

**Pros:**
- Clean cutover
- No dual-system complexity
- Immediate benefits

**Cons:**
- Higher risk
- Requires extensive testing
- Longer maintenance window

### 2. Gradual Migration

Migrate components incrementally over time.

**Pros:**
- Lower risk
- Easier rollback
- Continuous operation

**Cons:**
- Longer timeline
- Temporary complexity
- Resource overhead

### 3. Parallel Migration

Run both systems simultaneously during transition.

**Pros:**
- Zero downtime
- Easy comparison
- Safe rollback

**Cons:**
- Higher costs
- Data synchronization
- Complex testing

## Common Migration Scenarios

### From Custom OAuth 2.0 Implementation

**Challenges:**
- Custom code maintenance
- Security vulnerabilities
- Compliance issues
- Performance bottlenecks

**Migration Steps:**
1. **Audit Current Implementation**
   - Document existing flows
   - Identify custom features
   - Assess security gaps

2. **Plan Authlete Configuration**
   - Map existing scopes
   - Configure grant types
   - Set up clients

3. **Implement Gradual Migration**
   - Start with new clients
   - Migrate existing clients
   - Update applications

4. **Validate and Test**
   - Test all OAuth flows
   - Verify token compatibility
   - Check client functionality

### From Identity Provider Solutions

**From Auth0:**

```yaml
# Auth0 Configuration
AUTH0_DOMAIN: "your-domain.auth0.com"
AUTH0_CLIENT_ID: "your-client-id"
AUTH0_CLIENT_SECRET: "your-client-secret"

# Authlete Configuration
AUTHLETE_SERVICE_API_KEY: "your-service-key"
AUTHLETE_SERVICE_API_SECRET: "your-service-secret"
AUTHLETE_BASE_URL: "https://api.authlete.com"
```

**Migration Checklist:**
- [ ] Export user data
- [ ] Map user attributes
- [ ] Configure scopes
- [ ] Set up clients
- [ ] Test authentication flows
- [ ] Update application code

**From Okta:**

```yaml
# Okta Configuration
OKTA_DOMAIN: "your-domain.okta.com"
OKTA_CLIENT_ID: "your-client-id"
OKTA_CLIENT_SECRET: "your-client-secret"

# Authlete Configuration
AUTHLETE_SERVICE_API_KEY: "your-service-key"
AUTHLETE_SERVICE_API_SECRET: "your-service-secret"
AUTHLETE_BASE_URL: "https://api.authlete.com"
```

**Migration Checklist:**
- [ ] Export user profiles
- [ ] Map group memberships
- [ ] Configure custom attributes
- [ ] Set up authorization servers
- [ ] Test SSO flows
- [ ] Update application integrations

### From Open Source Solutions

**From Keycloak:**

```yaml
# Keycloak Configuration
KEYCLOAK_URL: "https://keycloak.example.com"
KEYCLOAK_REALM: "your-realm"
KEYCLOAK_CLIENT_ID: "your-client-id"

# Authlete Configuration
AUTHLETE_SERVICE_API_KEY: "your-service-key"
AUTHLETE_SERVICE_API_SECRET: "your-service-secret"
AUTHLETE_BASE_URL: "https://api.authlete.com"
```

**Migration Steps:**
1. **Export Keycloak Configuration**
   - Realm settings
   - Client configurations
   - User data
   - Role mappings

2. **Configure Authlete Service**
   - Set up service settings
   - Configure endpoints
   - Import user data

3. **Update Applications**
   - Change OAuth endpoints
   - Update client credentials
   - Test authentication flows

## Data Migration

### User Data Migration

**Export from Source:**
```json
{
  "users": [
    {
      "id": "user123",
      "email": "user@example.com",
      "name": "John Doe",
      "attributes": {
        "department": "Engineering",
        "role": "Developer"
      }
    }
  ]
}
```

**Import to Authlete:**
```bash
# Using Authlete API
curl -X POST "https://api.authlete.com/api/user/import" \\
  -H "Authorization: Bearer $AUTHLETE_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d @users.json
```

### Client Configuration Migration

**Export Client Data:**
```json
{
  "clients": [
    {
      "client_id": "app123",
      "client_secret": "secret456",
      "redirect_uris": ["https://app.example.com/callback"],
      "grant_types": ["authorization_code", "refresh_token"],
      "scopes": ["read", "write", "openid"]
    }
  ]
}
```

**Import to Authlete:**
```bash
# Using Authlete API
curl -X POST "https://api.authlete.com/api/client/create" \\
  -H "Authorization: Bearer $AUTHLETE_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d @clients.json
```

## Testing and Validation

### Pre-Migration Testing

**Test Environment Setup:**
1. Create Authlete test service
2. Configure test clients
3. Set up test users
4. Run comprehensive tests

**Test Scenarios:**
- OAuth 2.0 authorization code flow
- OpenID Connect authentication
- Token refresh
- Token revocation
- UserInfo endpoint
- JWKS endpoint

### Post-Migration Validation

**Validation Checklist:**
- [ ] All OAuth flows working
- [ ] Token format compatibility
- [ ] User authentication successful
- [ ] Client applications functional
- [ ] Performance meets requirements
- [ ] Security policies enforced

## Rollback Planning

### Rollback Triggers

**Critical Issues:**
- Authentication failures
- Token validation errors
- Performance degradation
- Security vulnerabilities
- Data loss

### Rollback Procedures

**Immediate Rollback:**
1. Switch DNS/load balancer
2. Revert application configuration
3. Monitor system health
4. Investigate issues

**Gradual Rollback:**
1. Stop new client migrations
2. Revert problematic clients
3. Monitor remaining clients
4. Plan next migration phase

## Best Practices

### 1. Planning

- **Thorough Assessment** - Understand current implementation
- **Detailed Testing** - Test all scenarios
- **Stakeholder Communication** - Keep teams informed
- **Rollback Plan** - Prepare for issues

### 2. Execution

- **Phased Approach** - Migrate incrementally
- **Monitoring** - Watch for issues
- **Documentation** - Record all changes
- **Support** - Have experts available

### 3. Post-Migration

- **Validation** - Verify all functionality
- **Optimization** - Tune performance
- **Training** - Educate teams
- **Monitoring** - Watch for issues

## Common Challenges

### Technical Challenges

**Token Format Differences:**
- JWT structure variations
- Claim naming differences
- Signature algorithms
- Key management

**Endpoint Differences:**
- URL variations
- Parameter differences
- Response format changes
- Error handling

### Business Challenges

**User Experience:**
- Login flow changes
- UI/UX updates
- Error messages
- Help documentation

**Integration Complexity:**
- Multiple applications
- Different client types
- Legacy systems
- Third-party integrations

## Support and Resources

### Migration Support

- **Documentation** - Comprehensive guides
- **Examples** - Code samples and tutorials
- **Support Team** - Expert assistance
- **Community** - User forums and discussions

### Additional Resources

- [Infrastructure Setup](/production/infrastructure-setup)
- [Terraform Deployment](/production/terraform-deployment)
- [Monitoring and Logging](/production/monitoring-logging)
- [Troubleshooting Guide](/production/troubleshooting)
'''

    # Troubleshooting
    troubleshooting_content = '''---
title: "Troubleshooting"
description: "Common issues and solutions for Authlete deployments"
---

# Troubleshooting Guide

This guide helps you diagnose and resolve common issues with Authlete deployments.

## Quick Diagnostics

### Health Check Endpoints

**Service Health:**
```bash
curl -X GET "https://api.authlete.com/health"
```

**Service Status:**
```bash
curl -X GET "https://api.authlete.com/api/service/status" \\
  -H "Authorization: Bearer $AUTHLETE_API_KEY"
```

### Common Error Codes

| Error Code | Description | Solution |
|------------|-------------|----------|
| A004001 | Invalid request parameters | Check request format and required fields |
| A004002 | Authentication required | Verify API credentials |
| A004003 | Insufficient permissions | Check API key permissions |
| A004004 | Resource not found | Verify resource exists |
| A004005 | Internal server error | Contact support |
| A050001 | Token request successful | Normal operation |
| A050002 | Invalid client | Check client credentials |
| A050003 | Invalid grant | Verify authorization code |
| A050004 | Unsupported grant type | Check grant type configuration |

## Authentication Issues

### Invalid Client Credentials

**Symptoms:**
- 401 Unauthorized errors
- "Invalid client" error messages
- Authentication failures

**Diagnosis:**
```bash
# Check client configuration
curl -X GET "https://api.authlete.com/api/client/get/$CLIENT_ID" \\
  -H "Authorization: Bearer $AUTHLETE_API_KEY"
```

**Solutions:**
1. **Verify Client ID**
   - Check client ID format
   - Ensure client exists
   - Verify client is active

2. **Check Client Secret**
   - Verify secret is correct
   - Check for encoding issues
   - Ensure secret is not expired

3. **Client Type Mismatch**
   - Public clients don't need secrets
   - Confidential clients require secrets
   - Check client type configuration

### Invalid Grant Type

**Symptoms:**
- "Unsupported grant type" errors
- Token request failures
- Authorization code issues

**Diagnosis:**
```bash
# Check service configuration
curl -X GET "https://api.authlete.com/api/service/get/$SERVICE_ID" \\
  -H "Authorization: Bearer $AUTHLETE_API_KEY"
```

**Solutions:**
1. **Enable Grant Type**
   - Add grant type to service settings
   - Check client grant type configuration
   - Verify grant type is supported

2. **Check Grant Type Format**
   - Use correct grant type names
   - Check for typos
   - Verify case sensitivity

### Invalid Redirect URI

**Symptoms:**
- "Invalid redirect URI" errors
- Authorization failures
- Redirect mismatches

**Solutions:**
1. **Exact Match Required**
   - Redirect URI must match exactly
   - Check for trailing slashes
   - Verify protocol (http vs https)

2. **Wildcard Support**
   - Use wildcards for subdomains
   - Check wildcard configuration
   - Verify wildcard placement

## Token Issues

### Token Validation Failures

**Symptoms:**
- "Invalid token" errors
- Token rejection
- Authentication failures

**Diagnosis:**
```bash
# Validate token
curl -X POST "https://api.authlete.com/api/auth/introspection" \\
  -H "Authorization: Bearer $AUTHLETE_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{"token": "$ACCESS_TOKEN"}'
```

**Solutions:**
1. **Check Token Format**
   - Verify JWT structure
   - Check token encoding
   - Validate token signature

2. **Token Expiration**
   - Check token expiration time
   - Verify system clock
   - Refresh expired tokens

3. **Token Revocation**
   - Check if token is revoked
   - Verify revocation status
   - Generate new token if needed

### Token Refresh Issues

**Symptoms:**
- Refresh token failures
- "Invalid refresh token" errors
- Token renewal problems

**Solutions:**
1. **Refresh Token Validity**
   - Check refresh token expiration
   - Verify refresh token format
   - Ensure refresh token is not revoked

2. **Client Configuration**
   - Enable refresh token grant type
   - Check client secret
   - Verify client permissions

## Configuration Issues

### Service Configuration Problems

**Symptoms:**
- Service not responding
- Configuration errors
- Endpoint failures

**Diagnosis:**
```bash
# Check service configuration
curl -X GET "https://api.authlete.com/api/service/get/$SERVICE_ID" \\
  -H "Authorization: Bearer $AUTHLETE_API_KEY"
```

**Solutions:**
1. **Verify Service Settings**
   - Check service configuration
   - Verify endpoint URLs
   - Ensure service is active

2. **Check Service Limits**
   - Verify rate limits
   - Check quota usage
   - Monitor service status

### Client Configuration Issues

**Symptoms:**
- Client authentication failures
- Scope permission errors
- Redirect URI mismatches

**Solutions:**
1. **Client Settings**
   - Verify client configuration
   - Check redirect URIs
   - Ensure client is active

2. **Scope Configuration**
   - Check scope permissions
   - Verify scope names
   - Ensure scopes are enabled

## Performance Issues

### Slow Response Times

**Symptoms:**
- High latency
- Timeout errors
- Slow token issuance

**Diagnosis:**
```bash
# Check service metrics
curl -X GET "https://api.authlete.com/api/service/metrics/$SERVICE_ID" \\
  -H "Authorization: Bearer $AUTHLETE_API_KEY"
```

**Solutions:**
1. **Database Performance**
   - Check database connections
   - Monitor query performance
   - Optimize database queries

2. **Caching Issues**
   - Check cache configuration
   - Monitor cache hit rates
   - Optimize cache settings

3. **Network Issues**
   - Check network latency
   - Verify DNS resolution
   - Monitor bandwidth usage

### High Error Rates

**Symptoms:**
- Increased error responses
- Service degradation
- User complaints

**Solutions:**
1. **Monitor Error Logs**
   - Check application logs
   - Monitor error patterns
   - Identify root causes

2. **Rate Limiting**
   - Check rate limit configuration
   - Monitor request patterns
   - Adjust rate limits if needed

3. **Resource Limits**
   - Check resource usage
   - Monitor memory/CPU
   - Scale resources if needed

## Security Issues

### Certificate Problems

**Symptoms:**
- SSL/TLS errors
- Certificate validation failures
- HTTPS issues

**Solutions:**
1. **Certificate Validity**
   - Check certificate expiration
   - Verify certificate chain
   - Update expired certificates

2. **Certificate Configuration**
   - Check certificate format
   - Verify private key
   - Ensure proper key usage

### Security Vulnerabilities

**Symptoms:**
- Security warnings
- Vulnerability alerts
- Compliance issues

**Solutions:**
1. **Update Dependencies**
   - Update libraries
   - Patch vulnerabilities
   - Monitor security advisories

2. **Security Configuration**
   - Review security settings
   - Enable security features
   - Implement best practices

## Debugging Tools

### Log Analysis

**Enable Debug Logging:**
```yaml
logging:
  level: DEBUG
  authlete: DEBUG
  security: INFO
  performance: INFO
```

**Log Analysis Commands:**
```bash
# Filter error logs
grep "ERROR" /var/log/authlete/app.log

# Monitor real-time logs
tail -f /var/log/authlete/app.log | grep "ERROR"

# Analyze performance logs
grep "duration" /var/log/authlete/app.log | sort -n
```

### API Testing

**Test Authorization Endpoint:**
```bash
curl -X GET "https://auth.example.com/oauth/authorize" \\
  -G -d "response_type=code" \\
  -d "client_id=$CLIENT_ID" \\
  -d "redirect_uri=$REDIRECT_URI" \\
  -d "scope=openid profile" \\
  -d "state=random_state"
```

**Test Token Endpoint:**
```bash
curl -X POST "https://auth.example.com/oauth/token" \\
  -H "Content-Type: application/x-www-form-urlencoded" \\
  -d "grant_type=authorization_code" \\
  -d "code=$AUTHORIZATION_CODE" \\
  -d "redirect_uri=$REDIRECT_URI" \\
  -d "client_id=$CLIENT_ID" \\
  -d "client_secret=$CLIENT_SECRET"
```

### Monitoring Commands

**Check Service Status:**
```bash
# Service health
curl -X GET "https://api.authlete.com/health"

# Service metrics
curl -X GET "https://api.authlete.com/api/service/metrics/$SERVICE_ID" \\
  -H "Authorization: Bearer $AUTHLETE_API_KEY"

# Client status
curl -X GET "https://api.authlete.com/api/client/get/$CLIENT_ID" \\
  -H "Authorization: Bearer $AUTHLETE_API_KEY"
```

## Getting Help

### Self-Service Resources

- **Documentation** - Comprehensive guides and references
- **API Reference** - Complete API documentation
- **Code Examples** - Sample implementations
- **Community Forums** - User discussions and solutions

### Support Channels

- **Email Support** - [support@authlete.com](mailto:support@authlete.com)
- **Priority Support** - For enterprise customers
- **Emergency Support** - For critical issues
- **Community Support** - User forums and discussions

### Escalation Process

1. **Level 1** - Self-service resources
2. **Level 2** - Email support
3. **Level 3** - Priority support
4. **Level 4** - Emergency support

## Additional Resources

- [Infrastructure Setup](/production/infrastructure-setup)
- [Terraform Deployment](/production/terraform-deployment)
- [Monitoring and Logging](/production/monitoring-logging)
- [Migration Guides](/production/migration-guides)
'''

    # Write all files
    files_to_create = [
        ('production/infrastructure-setup.mdx', infrastructure_content),
        ('production/terraform-deployment.mdx', terraform_content),
        ('production/monitoring-logging.mdx', monitoring_content),
        ('production/migration-guides.mdx', migration_content),
        ('production/troubleshooting.mdx', troubleshooting_content)
    ]
    
    for file_path, content in files_to_create:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created/updated {file_path}")

def main():
    print("Fixing deployment pages...")
    
    # First, create properly structured files
    create_proper_deployment_pages()
    
    # Then fix any remaining structural issues
    production_files = glob.glob('production/*.mdx')
    
    fixed_count = 0
    for file_path in production_files:
        if fix_mdx_structure(file_path):
            fixed_count += 1
    
    print(f"Fixed {fixed_count} files")
    print("Deployment pages should now be properly structured and compatible!")

if __name__ == "__main__":
    main()
