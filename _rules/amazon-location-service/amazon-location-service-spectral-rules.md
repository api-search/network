---
categories:
- info
- openapi
- operation
- parameter
- paths
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Location Service.
layout: rules
name: Amazon Location Service API Rules
provider_name: Amazon Location Service
provider_slug: amazon-location-service
rule_count: 16
rules:
- description: API title must start with "Amazon Location Service"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Summaries must start with "Amazon Location Service"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationid-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-required
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-required
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
rules_file: rules/amazon-location-service-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-location-service/refs/heads/main/rules/amazon-location-service-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 0
  warn: 7
slug: amazon-location-service-spectral-rules
tags:
- AWS
- Geocoding
- Geofencing
- Location
- Maps
- Routing
- Spectral
- Linting
- API Governance
---
