---
categories:
- get
- info
- operation
- parameter
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Amadeus Traveler Media.
layout: rules
name: Amadeus Traveler Media API Rules
provider_name: Amadeus Traveler Media
provider_slug: amadeus-traveler-media
rule_count: 12
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
- description: Operation summaries must start with Amadeus.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amadeus-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have tags.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Parameters should have descriptions.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Responses must have descriptions.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: GET operations must not have request bodies.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description
  severity: info
rules_file: rules/amadeus-traveler-media-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amadeus-traveler-media/refs/heads/main/rules/amadeus-traveler-media-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 1
  warn: 2
slug: amadeus-traveler-media-spectral-rules
tags:
- Content
- Destination
- Media
- Photos
- Points of Interest
- Tourism
- Travel
- Spectral
- Linting
- API Governance
---
