---
categories:
- info
- microcks
- 'no'
- operation
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Global Accelerator.
layout: rules
name: Amazon Global Accelerator API Rules
provider_name: Amazon Global Accelerator
provider_slug: amazon-global-accelerator
rule_count: 14
rules:
- description: API title must reference Amazon Global Accelerator
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with Amazon Global Accelerator
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-company-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Operations must have at least one success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Security schemes should be defined in components
  given: $
  name: security-schemes-defined
  severity: warn
- description: Schema properties should have types
  given: $.components.schemas[*].properties[*]
  name: schema-properties-typed
  severity: info
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-global-accelerator-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-global-accelerator/refs/heads/main/rules/amazon-global-accelerator-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 2
  warn: 5
slug: amazon-global-accelerator-spectral-rules
tags:
- Availability
- AWS
- CDN
- Global
- Load Balancing
- Networking
- Performance
- Spectral
- Linting
- API Governance
---
