---
categories:
- http
- info
- openapi
- operation
- pagination
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Activepieces.
layout: rules
name: Activepieces API Rules
provider_name: Activepieces
provider_slug: activepieces
rule_count: 25
rules:
- description: API title should start with "Activepieces"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must include a version
  given: $.info
  name: info-version-required
  severity: error
- description: Should use OpenAPI 3.x
  given: $.openapi
  name: openapi-version
  severity: warn
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All servers should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summary should start with "Activepieces"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationId-camelCase
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: List endpoints should support limit parameter
  given: $.paths[*].get.parameters[*]
  name: pagination-limit-param
  severity: info
- description: Every operation must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should document 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: API should use Bearer authentication
  given: $.components.securitySchemes[*]
  name: security-bearer-auth
  severity: warn
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: http-get-no-request-body
  severity: error
- description: DELETE operations should return 204
  given: $.paths[*].delete.responses
  name: http-delete-returns-204
  severity: info
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should define types
  given: $.components.schemas[*].properties[*]
  name: schema-properties-have-types
  severity: warn
rules_file: rules/activepieces-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/activepieces/refs/heads/main/rules/activepieces-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 4
  warn: 11
slug: activepieces-spectral-rules
tags:
- Automation
- No-Code
- Open Source
- Workflow
- AI Agents
- MCP
- Spectral
- Linting
- API Governance
---
