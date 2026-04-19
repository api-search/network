---
categories:
- info
- list
- 'no'
- openapi
- operation
- paths
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Deadline Cloud.
layout: rules
name: Amazon Deadline Cloud API Rules
provider_name: Amazon Deadline Cloud
provider_slug: amazon-deadline-cloud
rule_count: 20
rules:
- description: API title must reference "Deadline Cloud"
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
- description: Deadline Cloud API paths should include API version date prefix
  given: $.paths[*]~
  name: paths-versioned
  severity: warn
- description: Most Deadline Cloud resources are scoped under a farm
  given: $.paths[*]~
  name: paths-farm-scoped
  severity: info
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
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: List operations should return nextToken for pagination
  given: $.paths[*][get].responses.200.content.application/json.schema.properties
  name: list-has-pagination
  severity: info
rules_file: rules/amazon-deadline-cloud-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-deadline-cloud/refs/heads/main/rules/amazon-deadline-cloud-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 2
  warn: 5
slug: amazon-deadline-cloud-spectral-rules
tags:
- AWS
- Compute
- Media
- Rendering
- Visual Effects
- Spectral
- Linting
- API Governance
---
