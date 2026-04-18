---
categories:
- get
- info
- openapi
- operation
- parameter
- response
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Microsoft Visio.
layout: rules
name: Microsoft Visio API Rules
provider_name: Microsoft Visio
provider_slug: microsoft-visio
rule_count: 16
rules:
- description: Info title must contain 'Microsoft' or 'Visio'
  given: $.info.title
  name: info-title-must-contain-microsoft-visio
  severity: error
- description: Info description is required
  given: $.info
  name: info-description-required
  severity: error
- description: Info version is required
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-must-be-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with 'Microsoft Visio'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must define a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-recommended
  severity: warn
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
rules_file: rules/microsoft-visio-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-visio/refs/heads/main/rules/microsoft-visio-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 0
  warn: 4
slug: microsoft-visio-spectral-rules
tags:
- Business Process
- Diagramming
- Flowcharts
- Microsoft 365
- Visualization
- Spectral
- Linting
- API Governance
---
