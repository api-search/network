---
categories:
- delete
- get
- info
- operation
- parameter
- post
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amadeus Reservations.
layout: rules
name: Amadeus Reservations API Rules
provider_name: Amadeus Reservations
provider_slug: amadeus-reservations
rule_count: 20
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API title must reference Amadeus.
  given: $.info.title
  name: info-title-amadeus-prefix
  severity: warn
- description: API must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be present.
  given: $.info
  name: info-version-required
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-required
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
- description: Every operation must have a description.
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
  severity: error
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Booking operations should define a 401 response.
  given: $.paths[*][post].responses
  name: response-401-booking
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-recommended
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204 No Content.
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
- description: POST operations for booking creation should have a request body.
  given: $.paths[*].post
  name: post-has-request-body
  severity: warn
rules_file: rules/amadeus-reservations-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/rules/amadeus-reservations-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 2
  warn: 7
slug: amadeus-reservations-spectral-rules
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
- Spectral
- Linting
- API Governance
---
