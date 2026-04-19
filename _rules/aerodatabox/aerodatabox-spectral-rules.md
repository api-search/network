---
categories:
- get
- info
- microcks
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AeroDataBox.
layout: rules
name: AeroDataBox API Rules
provider_name: AeroDataBox
provider_slug: aerodatabox
rule_count: 22
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
- description: Path must not have a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Path must not contain a query string.
  given: $.paths[*]~
  name: paths-no-query-string
  severity: error
- description: Path segments should use kebab-case.
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "AeroDataBox".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-aerodatabox-prefix
  severity: warn
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must have at least one response.
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Each operation should have x-microcks-operation for mock server support.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
rules_file: rules/aerodatabox-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/rules/aerodatabox-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 3
  warn: 8
slug: aerodatabox-spectral-rules
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
- Spectral
- Linting
- API Governance
---
