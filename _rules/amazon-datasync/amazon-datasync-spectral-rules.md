---
categories:
- arn
- info
- 'no'
- openapi
- operation
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon DataSync.
layout: rules
name: Amazon DataSync API Rules
provider_name: Amazon DataSync
provider_slug: amazon-datasync
rule_count: 18
rules:
- description: API title must reference "DataSync"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags array should be defined globally
  given: $
  name: tags-defined
  severity: warn
- description: All operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: ARN fields should have descriptions identifying them as unique resource identifiers
  given: $.components.schemas[*].properties[?(@property =~ /Arn/)].description
  name: arn-fields-documented
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/amazon-datasync-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-datasync/refs/heads/main/rules/amazon-datasync-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 1
  warn: 4
slug: amazon-datasync-spectral-rules
tags:
- AWS
- Data Transfer
- Migration
- Storage
- Automation
- Hybrid Cloud
- Spectral
- Linting
- API Governance
---
