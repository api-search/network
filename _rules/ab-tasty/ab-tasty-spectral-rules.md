---
categories:
- delete
- examples
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
description: Spectral linting rules defining API design standards and conventions for AB Tasty.
layout: rules
name: AB Tasty API Rules
provider_name: AB Tasty
provider_slug: ab-tasty
rule_count: 40
rules:
- description: API info must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API title should start with "AB Tasty"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API description should be meaningful (at least 30 characters)
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: API info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Should use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: warn
- description: Servers must be defined
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
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths should not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "AB Tasty"
  given: $.paths[*][get,post,put,patch,delete,options,head].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: Tags used in operations should be defined at the global level
  given: $.tags
  name: tag-global-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tag-description
  severity: info
- description: All parameters must have a description
  given: $..parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters should have a schema with type defined
  given: $..parameters[*].schema
  name: parameter-schema-type
  severity: warn
- description: API keys should be passed in headers, not query parameters
  given: $.components.securitySchemes[?(@.type == 'apiKey')]
  name: parameter-api-key-in-header
  severity: warn
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-type
  severity: warn
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Secured endpoints should document 401 responses
  given: $.paths[*][post,get,put,delete].responses
  name: response-401-for-secured-endpoints
  severity: warn
- description: APIs with rate limits should document 429 responses
  given: $.paths[*][post].responses
  name: response-429-rate-limit
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have types defined
  given: $.components.schemas[*].properties[*]
  name: schema-property-type
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Security schemes should be defined in components
  given: $.components.securitySchemes
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations should not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations should have request bodies
  given: $.paths[*].post
  name: post-should-have-request-body
  severity: warn
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
- description: Operations should have x-microcks-operation extension for mock compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/ab-tasty-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/rules/ab-tasty-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 5
  warn: 22
slug: ab-tasty-spectral-rules
tags:
- Aggregation
- Experimentation
- Feature Flags
- Personalization
- A/B Testing
- Spectral
- Linting
- API Governance
---
