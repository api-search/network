---
categories:
- info
- 'no'
- openapi
- operation
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon PrivateLink.
layout: rules
name: Amazon PrivateLink API Rules
provider_name: Amazon PrivateLink
provider_slug: amazon-privatelink
rule_count: 16
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: API should use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Summaries should start with Amazon PrivateLink
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-amazon-privatelink-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All operations must have a success response
  given: $.paths[*][get,post,put,delete,patch]
  name: response-success-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/amazon-privatelink-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-privatelink/refs/heads/main/rules/amazon-privatelink-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 0
  warn: 5
slug: amazon-privatelink-spectral-rules
tags:
- AWS
- Networking
- Private Connectivity
- Security
- VPC
- Zero Trust
- Endpoint Services
- Spectral
- Linting
- API Governance
---
