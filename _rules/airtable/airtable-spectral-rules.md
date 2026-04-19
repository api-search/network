---
categories:
- airtable
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- post
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Airtable.
layout: rules
name: Airtable API Rules
provider_name: Airtable
provider_slug: airtable
rule_count: 29
rules:
- description: Info title must be defined.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be defined.
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version must be 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https
  severity: warn
- description: Airtable API servers should use api.airtable.com.
  given: $.servers[*]
  name: servers-api-airtable-base
  severity: info
- description: Airtable API paths typically start with /v0/.
  given: $.paths[*]~
  name: paths-v0-prefix
  severity: info
- description: Path segments should use kebab-case or base IDs.
  given: $.paths[*]~
  name: paths-kebab-or-base-id
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationId-camelCase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with "Airtable".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-starts-with-airtable
  severity: info
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Authorization should use Bearer token scheme.
  given: $.components.securitySchemes[*]
  name: parameter-authorization-header
  severity: info
- description: Every operation must have a success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Operations with request bodies should document 422 validation errors.
  given: $.paths[*][post,put,patch].responses
  name: response-422-for-validation
  severity: info
- description: Schema properties in Airtable APIs use camelCase.
  given: $.components.schemas[*].properties[*]~
  name: schema-property-camelCase
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes must be defined.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Airtable APIs use Bearer token authentication.
  given: $.components.securitySchemes[*]
  name: security-bearer-required
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: List operations should support cursor or offset pagination.
  given: $.paths[*].get
  name: post-list-uses-offset
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include x-microcks-operation for mock compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
- description: Rate limits should be documented in the API info.
  given: $.info
  name: airtable-rate-limit-documented
  severity: info
rules_file: rules/airtable-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/rules/airtable-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 11
  warn: 9
slug: airtable-spectral-rules
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
- Spectral
- Linting
- API Governance
---
