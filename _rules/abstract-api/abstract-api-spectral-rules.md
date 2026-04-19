---
categories:
- delete
- generated
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
description: Spectral linting rules defining API design standards and conventions for Abstract API.
layout: rules
name: Abstract API API Rules
provider_name: Abstract API
provider_slug: abstract-api
rule_count: 34
rules:
- description: Info title must be present and start with "Abstract API"
  given: $.info
  name: info-title-required
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
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https-only
  severity: error
- description: Server URLs should be under abstractapi.com domain
  given: $.servers[*]
  name: servers-abstractapi-domain
  severity: warn
- description: Path segments must use kebab-case (lowercase with hyphens)
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes (except root /)
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summary must start with "Abstract API"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-title-case
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
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operations should have x-microcks-operation extension for mock server compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Tags should use Title Case
  given: $.tags[*]
  name: tags-title-case
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Abstract API uses api_key as the query parameter name for authentication
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name == "api_key")]
  name: parameter-api-key-query
  severity: warn
- description: Every parameter must have a schema with type
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameters should have example values
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-example-recommended
  severity: info
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations secured with API key should document 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Rate-limited APIs should document 429 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-429-recommended
  severity: info
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema properties should have example values
  given: $.components.schemas[*].properties[*]
  name: schema-property-example
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-top-level-description
  severity: warn
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: error
- description: Abstract API uses apiKey security scheme
  given: $.components.securitySchemes[*]
  name: security-api-key-scheme
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Generated specs should be marked with x-generated-from
  given: $.info
  name: generated-from-docs-marked
  severity: info
rules_file: rules/abstract-api-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/rules/abstract-api-spectral-rules.yml
severity_counts:
  error: 17
  hint: 0
  info: 6
  warn: 11
slug: abstract-api-spectral-rules
tags:
- Avatars
- Company Enrichment
- Contacts
- Currencies
- Email Validation
- Exchange Rates
- IBAN Validation
- Image Processing
- IP Geolocation
- IP Intelligence
- Phone Validation
- Public Holidays
- Screenshots
- Timezones
- VAT Validation
- Web Scraping
- Spectral
- Linting
- API Governance
---
