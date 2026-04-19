---
categories:
- actor
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
description: Spectral linting rules defining API design standards and conventions for Actor Model.
layout: rules
name: Actor Model API Rules
provider_name: Actor Model
provider_slug: actor-model
rule_count: 24
rules:
- description: API title should start with "Actor Model"
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
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summary should start with "Actor Model"
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
- description: List endpoints should support cursor and limit parameters for seek-based pagination
  given: $.paths[*][get]
  name: pagination-cursor-limit
  severity: info
- description: Every operation must have a 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should document 401 Unauthorized
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Actor system management APIs should use bearer token authentication
  given: $.components.securitySchemes[*].scheme
  name: security-bearer
  severity: warn
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: http-get-no-request-body
  severity: error
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have example values
  given: $.components.schemas[*].properties[*]
  name: schema-property-examples
  severity: info
- description: Actor paths should follow hierarchical format starting with /
  given: $.paths[/actors/**]~
  name: actor-path-format
  severity: info
rules_file: rules/actor-model-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/actor-model/refs/heads/main/rules/actor-model-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 3
  warn: 12
slug: actor-model-spectral-rules
tags:
- Actor Model
- Concurrency
- Distributed Systems
- Spectral
- Linting
- API Governance
---
