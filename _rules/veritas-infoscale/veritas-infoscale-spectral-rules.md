---
categories:
- delete
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- post
- request
- response
- schema
- security
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Veritas InfoScale.
layout: rules
name: Veritas InfoScale API Rules
provider_name: Veritas InfoScale
provider_slug: veritas-infoscale
rule_count: 39
rules:
- description: Info object must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Title should start with "Veritas InfoScale"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Info object should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version should be 3.0.x
  given: $.openapi
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Paths must not end with a trailing slash
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not contain query strings
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Path segments should use lowercase
  given: $.paths
  name: paths-lowercase
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Veritas InfoScale"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: Each global tag should have a description
  given: $.tags[*]
  name: tag-description
  severity: info
- description: Every parameter must have a description
  given: $..parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema with a type
  given: $..parameters[*]
  name: parameter-schema-required
  severity: error
- description: Path parameters must be required
  given: $..parameters[?(@.in == 'path')]
  name: parameter-path-required
  severity: error
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
- description: Every operation must define a success response (2xx)
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should define a 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-defined
  severity: info
- description: All schemas must define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: error
- description: Schema properties should use camelCase (Veritas convention)
  given: $.components.schemas[*].properties
  name: schema-properties-camel-case
  severity: info
- description: Global security must be defined
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Bearer token security scheme should be defined for InfoScale APIs
  given: $.components.securitySchemes
  name: security-bearer-scheme
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations must not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: error
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-request-body
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Operations should have x-microcks-operation for mock compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/veritas-infoscale-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/veritas-infoscale/refs/heads/main/rules/veritas-infoscale-spectral-rules.yml
severity_counts:
  error: 23
  hint: 0
  info: 6
  warn: 10
slug: veritas-infoscale-spectral-rules
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
- Spectral
- Linting
- API Governance
---
