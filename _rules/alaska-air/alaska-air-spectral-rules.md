---
categories:
- examples
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Alaska Airlines.
layout: rules
name: Alaska Airlines API Rules
provider_name: Alaska Airlines
provider_slug: alaska-air
rule_count: 32
rules:
- description: Info title must be defined
  given: $.info
  name: info-title-required
  severity: error
- description: API title should start with 'Alaska'
  given: $.info.title
  name: info-title-alaska-prefix
  severity: warn
- description: Info description must be defined
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: Info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: Server URLs should use alaskaair.com or alaskacargo.com domains
  given: $.servers[*]
  name: servers-alaskaair-domain
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: API paths should include a version prefix
  given: $.paths[*]~
  name: paths-versioned
  severity: warn
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with 'Alaska Airlines' or 'Alaska Air'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-alaska-prefix
  severity: warn
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags should be defined at the global level
  given: $
  name: tags-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tags-description-required
  severity: warn
- description: Parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameters must have a schema
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: IATA airport code parameters should use enum or note valid format
  given: $.paths[*][*].parameters[?(@.name == 'origin' || @.name == 'destination' || @.name == 'originAirport' || @.name == 'destinationAirport')]
  name: parameter-iata-uppercase
  severity: info
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: APIs should define 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-401-required
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined
  given: $
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/alaska-air-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/rules/alaska-air-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 2
  warn: 14
slug: alaska-air-spectral-rules
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
- Spectral
- Linting
- API Governance
---
