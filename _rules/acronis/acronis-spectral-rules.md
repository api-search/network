---
categories:
- delete
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
- tenant
description: Spectral linting rules defining API design standards and conventions for Acronis.
layout: rules
name: Acronis API Rules
provider_name: Acronis
provider_slug: acronis
rule_count: 33
rules:
- description: OpenAPI info.title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info.description must be present
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info.version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Acronis APIs must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Acronis API servers should use acronis.com domain
  given: $.servers[*]
  name: servers-acronis-domain
  severity: info
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operation summaries should start with 'Acronis'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-acronis-prefix
  severity: info
- description: Operations should have x-microcks-operation for mock testing
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: warn
- description: All global tags should have descriptions
  given: $.tags[*]
  name: tags-description-required
  severity: warn
- description: All parameters should have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: All operations must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Protected endpoints should define 401 responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should define types
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: schema-property-example
  severity: info
- description: Security schemes must be defined
  given: $
  name: security-schemes-defined
  severity: error
- description: Acronis APIs use bearer token authentication
  given: $.components.securitySchemes[*]
  name: security-bearer-scheme
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204 No Content
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: warn
- description: Endpoints that scope to a tenant should include tenant_id parameter
  given: $.paths[*][get]
  name: tenant-id-parameter
  severity: info
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/acronis-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acronis/refs/heads/main/rules/acronis-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 7
  warn: 11
slug: acronis-spectral-rules
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
- Spectral
- Linting
- API Governance
---
