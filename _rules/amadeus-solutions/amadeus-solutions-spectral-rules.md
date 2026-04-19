---
categories:
- get
- info
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amadeus Solutions.
layout: rules
name: Amadeus Solutions API Rules
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
rule_count: 15
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be present.
  given: $.info
  name: info-version-required
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amadeus".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amadeus-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations should define a 401 response.
  given: $.paths[*][get,post].responses
  name: response-401-required
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Security schemes should be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
rules_file: rules/amadeus-solutions-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/rules/amadeus-solutions-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 1
  warn: 4
slug: amadeus-solutions-spectral-rules
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
- Spectral
- Linting
- API Governance
---
