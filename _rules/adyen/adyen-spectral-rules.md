---
categories:
- delete
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Adyen.
layout: rules
name: Adyen API Rules
provider_name: Adyen
provider_slug: adyen
rule_count: 32
rules:
- description: API info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: API info must have a description.
  given: $.info
  name: info-description-required
  severity: warn
- description: API info must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: APIs should use OpenAPI 3.x specification.
  given: $
  name: openapi-version-3
  severity: warn
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-only
  severity: error
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description-required
  severity: info
- description: Path must not have a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Path must not contain a query string.
  given: $.paths[*]~
  name: paths-no-query-string
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Adyen".
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-adyen-prefix
  severity: warn
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-schema-required
  severity: error
- description: API keys should be passed in headers, not query parameters.
  given: $.components.securitySchemes[?(@.type=='apiKey')]
  name: parameter-api-key-in-header
  severity: warn
- description: Request body should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Request body should support application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-json
  severity: warn
- description: Every operation must have at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations with authentication should define a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Schema properties should define a type.
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Security schemes should have a description.
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: info
- description: Adyen API key header should be named X-API-Key.
  given: $.components.securitySchemes[?(@.type=='apiKey')]
  name: security-api-key-header-name
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..[description]
  name: no-empty-descriptions
  severity: warn
- description: Each operation should have x-microcks-operation for mock server support.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
rules_file: rules/adyen-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/rules/adyen-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 6
  warn: 14
slug: adyen-spectral-rules
tags:
- Payments
- Financial Services
- Fintech
- Spectral
- Linting
- API Governance
---
