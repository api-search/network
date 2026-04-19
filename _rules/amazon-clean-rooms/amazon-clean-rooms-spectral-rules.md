---
categories:
- delete
- get
- info
- microcks
- 'no'
- openapi
- operation
- pagination
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Clean Rooms.
layout: rules
name: Amazon Clean Rooms API Rules
provider_name: Amazon Clean Rooms
provider_slug: amazon-clean-rooms
rule_count: 29
rules:
- description: API title must start with "Amazon Clean Rooms"
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
- description: API must have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: API must define at least one server
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
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
- description: Operation summaries must start with "Amazon Clean Rooms"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Path and query parameters should use camelCase (AWS convention)
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-camel-case
  severity: warn
- description: Every operation must have a success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All response codes must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should document 400 bad request
  given: $.paths[*][post,put,patch].responses
  name: response-400-required
  severity: warn
- description: Operations should document 403 access denied
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-403-required
  severity: warn
- description: Operations should document 500 internal server error
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-required
  severity: warn
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-on-top-level
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 200 or 204
  given: $.paths[*].delete.responses
  name: delete-returns-200-or-204
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation extension
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
- description: List operations should use nextToken for pagination (AWS convention)
  given: $.paths[*].get.parameters[?(@.name == 'nextToken')]
  name: pagination-uses-next-token
  severity: info
rules_file: rules/amazon-clean-rooms-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-clean-rooms/refs/heads/main/rules/amazon-clean-rooms-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 13
slug: amazon-clean-rooms-spectral-rules
tags:
- AWS
- Clean Rooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
- Spectral
- Linting
- API Governance
---
