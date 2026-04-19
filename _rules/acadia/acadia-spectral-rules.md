---
categories:
- delete
- get
- info
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Acadia.
layout: rules
name: Acadia API Rules
provider_name: Acadia
provider_slug: acadia
rule_count: 25
rules:
- description: Info title must start with "Acadia"
  given: $.info
  name: info-title-acadia-prefix
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Info version must be present
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: Path segments must use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Operation summaries must start with "Acadia"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: List endpoints should support page parameter
  given: $.paths[*].get.parameters[?(@.name == "page")]
  name: parameter-pagination-page
  severity: info
- description: List endpoints should support limit parameter
  given: $.paths[*].get.parameters[?(@.name == "limit")]
  name: parameter-pagination-limit
  severity: info
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Protected operations should document 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas must have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema properties should have example values
  given: $.components.schemas[*].properties[*]
  name: schema-property-example
  severity: info
- description: Security schemes must be defined
  given: $
  name: security-schemes-required
  severity: error
- description: Acadia uses Bearer JWT authentication
  given: $.components.securitySchemes[*][?(@.type == "http")]
  name: security-bearer-jwt
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 200 or 204
  given: $.paths[*].delete.responses
  name: delete-returns-200-or-204
  severity: warn
rules_file: rules/acadia-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acadia/refs/heads/main/rules/acadia-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 4
  warn: 8
slug: acadia-spectral-rules
tags:
- Connected Worker
- Knowledge Management
- Manufacturing
- Skills Management
- Training
- Workforce Development
- Spectral
- Linting
- API Governance
---
