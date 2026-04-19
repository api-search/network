---
categories:
- get
- info
- microcks
- 'no'
- operation
- pagination
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Cloud Map.
layout: rules
name: Amazon Cloud Map API Rules
provider_name: Amazon Cloud Map
provider_slug: amazon-cloud-map
rule_count: 20
rules:
- description: API title must start with "Amazon Cloud Map"
  given: $.info.title
  name: info-title-prefix
  severity: error
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API must define at least one server
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: operationId must use PascalCase (AWS convention)
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationId-pascal-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon Cloud Map"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All response codes must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should document 500 internal server error
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-required
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation extension
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
- description: List operations should use NextToken pagination (AWS convention)
  given: $.paths[*].get.parameters[?(@.name == 'NextToken')]
  name: pagination-uses-next-token
  severity: info
rules_file: rules/amazon-cloud-map-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-cloud-map/refs/heads/main/rules/amazon-cloud-map-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 2
  warn: 6
slug: amazon-cloud-map-spectral-rules
tags:
- AWS
- Cloud Map
- Service Discovery
- Microservices
- DNS
- Spectral
- Linting
- API Governance
---
