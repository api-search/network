---
categories:
- delete
- examples
- get
- info
- microcks
- 'no'
- openapi
- operation
- pagination
- parameter
- paths
- request
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Abacus.
layout: rules
name: Abacus API Rules
provider_name: Abacus
provider_slug: abacus
rule_count: 39
rules:
- description: API info must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API title should start with "Abacus"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Should use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case or snake_case with underscores
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths should not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Abacus"
  given: $.paths[*][get,post,put,patch,delete,options,head].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: Tags used in operations should be defined at the global level
  given: $.tags
  name: tag-global-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tag-description
  severity: info
- description: All parameters must have a description
  given: $..parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameter names should use snake_case
  given: $.paths[*][*].parameters[*].name
  name: parameter-snake-case
  severity: warn
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-json
  severity: info
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Endpoints should document 401 Unauthorized responses
  given: $.paths[*][get,post,put,delete].responses
  name: response-401-for-auth
  severity: warn
- description: Endpoints with path parameters should document 404 responses
  given: $.paths[*][get,put,delete].responses
  name: response-404-for-resource-endpoints
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema property names should use snake_case
  given: $.components.schemas[*].properties
  name: schema-property-snake-case
  severity: warn
- description: Security schemes should be defined in components
  given: $.components.securitySchemes
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: OAuth2 scopes should be defined
  given: $.components.securitySchemes[?(@.type == 'oauth2')]
  name: security-oauth2-scopes
  severity: info
- description: GET operations should not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should have examples for better DX
  given: $.components.schemas[*].properties[*]
  name: examples-on-schemas
  severity: info
- description: Operations should have x-microcks-operation for mock compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
- description: Paginated endpoints should use standard page/per_page parameters
  given: $.paths[*].get.parameters[*].name
  name: pagination-params-standard
  severity: info
rules_file: rules/abacus-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/rules/abacus-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 7
  warn: 19
slug: abacus-spectral-rules
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
- Spectral
- Linting
- API Governance
---
