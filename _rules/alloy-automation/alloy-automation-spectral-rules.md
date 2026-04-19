---
categories:
- alloy
description: Spectral linting rules defining API design standards and conventions for Alloy Automation.
layout: rules
name: Alloy Automation API Rules
provider_name: Alloy Automation
provider_slug: alloy-automation
rule_count: 16
rules:
- description: All operation summaries must start with "Alloy"
  given: $.paths[*][*].summary
  name: alloy-operation-summary-prefix
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][*]
  name: alloy-operation-tags
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][*]
  name: alloy-operation-id
  severity: error
- description: All operations must have a description
  given: $.paths[*][*]
  name: alloy-operation-description
  severity: warn
- description: All operations must document 401 Unauthorized response
  given: $.paths[*][*].responses
  name: alloy-error-response-401
  severity: error
- description: API must use bearer API key security
  given: $.components.securitySchemes
  name: alloy-api-key-security
  severity: error
- description: API version should be specified in server URL or via x-api-version header
  given: $.servers[0].url
  name: alloy-api-version-header
  severity: info
- description: All schemas must have a title
  given: $.components.schemas[*]
  name: alloy-schema-title
  severity: warn
- description: All schemas must have a description
  given: $.components.schemas[*]
  name: alloy-schema-description
  severity: warn
- description: All schema properties must have a description
  given: $.components.schemas[*].properties[*]
  name: alloy-property-description
  severity: warn
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: alloy-property-example
  severity: info
- description: All operations should have x-microcks-operation extension
  given: $.paths[*][*]
  name: alloy-microcks-operation
  severity: info
- description: User ID fields should follow usr_ prefix pattern
  given: $.components.schemas[*].properties.userId.example
  name: alloy-user-id-pattern
  severity: info
- description: POST operations should return 201 (created) or 200
  given: $.paths[*].post.responses
  name: alloy-post-201-or-200
  severity: warn
- description: Error responses must reference ErrorResponse schema
  given: $.paths[*][*].responses[4XX,5XX].content.application/json.schema.$ref
  name: alloy-error-response-schema
  severity: warn
- description: Connector IDs should use kebab-case
  given: $.components.schemas[*].properties.connectorId.example
  name: alloy-connector-id-kebab-case
  severity: info
rules_file: rules/alloy-automation-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/alloy-automation/refs/heads/main/rules/alloy-automation-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 5
  warn: 7
slug: alloy-automation-spectral-rules
tags:
- Automation
- Embedded Integrations
- Integrations
- iPaaS
- Unified API
- Workflows
- Spectral
- Linting
- API Governance
---
