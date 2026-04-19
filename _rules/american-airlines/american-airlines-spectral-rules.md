---
categories:
- get
- info
- operation
- parameter
- paths
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for American Airlines.
layout: rules
name: American Airlines API Rules
provider_name: American Airlines
provider_slug: american-airlines
rule_count: 12
rules:
- description: API title must start with "American Airlines"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operations must have a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Parameters should have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
rules_file: rules/american-airlines-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/american-airlines/refs/heads/main/rules/american-airlines-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 1
  warn: 3
slug: american-airlines-spectral-rules
tags:
- Airlines
- Aviation
- Flights
- Travel
- Booking
- Developer Experience
- Spectral
- Linting
- API Governance
---
