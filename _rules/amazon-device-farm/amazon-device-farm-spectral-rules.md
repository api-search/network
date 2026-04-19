---
categories:
- external
- get
- info
- 'no'
- openapi
- operation
- parameter
- post
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Device Farm.
layout: rules
name: Amazon Device Farm API Rules
provider_name: Amazon Device Farm
provider_slug: amazon-device-farm
rule_count: 24
rules:
- description: API title should include "Device Farm"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationIds should use PascalCase (AWS Device Farm convention)
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-id-pascal-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-schema-required
  severity: error
- description: POST operations should typically have a request body
  given: $.paths[*].post
  name: post-should-have-request-body
  severity: info
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: error
- description: Operations should document 4xx error responses
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-error-4xx
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Schemas should have a type defined
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: Security schemes should be defined in components
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: API should reference external documentation
  given: $
  name: external-docs-encouraged
  severity: info
rules_file: rules/amazon-device-farm-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-device-farm/refs/heads/main/rules/amazon-device-farm-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 4
  warn: 8
slug: amazon-device-farm-spectral-rules
tags:
- Application Testing
- AWS
- Device Testing
- Mobile Testing
- Quality Assurance
- Spectral
- Linting
- API Governance
---
