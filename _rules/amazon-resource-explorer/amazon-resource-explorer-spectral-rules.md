---
categories:
- delete
- get
- info
- openapi
- operation
- parameter
- response
- schema
- security
- server
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Resource Explorer.
layout: rules
name: Amazon Resource Explorer API Rules
provider_name: Amazon Resource Explorer
provider_slug: amazon-resource-explorer
rule_count: 19
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: warn
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*]
  name: server-https
  severity: warn
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operations must have a description
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-camel-case
  severity: warn
- description: Operations must have tags
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must have a success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: warn
- description: Schema properties should have types
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes should be defined
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
rules_file: rules/amazon-resource-explorer-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-resource-explorer/refs/heads/main/rules/amazon-resource-explorer-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 1
  warn: 10
slug: amazon-resource-explorer-spectral-rules
tags:
- AWS
- Discovery
- Inventory
- Operations
- Resource Management
- Spectral
- Linting
- API Governance
---
