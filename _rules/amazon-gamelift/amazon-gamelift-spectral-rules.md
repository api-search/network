---
categories:
- info
- microcks
- 'no'
- openapi
- operation
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon GameLift.
layout: rules
name: Amazon GameLift API Rules
provider_name: Amazon GameLift
provider_slug: amazon-gamelift
rule_count: 18
rules:
- description: API title must start with "Amazon GameLift"
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
- description: Must use OpenAPI 3.0.x
  given: $.openapi
  name: openapi-version
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with Amazon GameLift
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-company-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Operations must have at least one success (2xx) response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Request bodies should have descriptions
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Security schemes should be defined in components
  given: $
  name: security-schemes-defined
  severity: warn
- description: Schema properties should have types defined
  given: $.components.schemas[*].properties[*]
  name: schema-properties-typed
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation for mock support
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-gamelift-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-gamelift/refs/heads/main/rules/amazon-gamelift-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 3
  warn: 8
slug: amazon-gamelift-spectral-rules
tags:
- AWS
- Cloud Computing
- Game Servers
- Gaming
- Multiplayer
- Matchmaking
- FlexMatch
- FleetIQ
- Spectral
- Linting
- API Governance
---
