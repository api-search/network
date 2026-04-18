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
- pagination
- parameter
- paths
- post
- request
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Circana.
layout: rules
name: Circana API Rules
provider_name: Circana
provider_slug: circana
rule_count: 41
rules:
- description: Info title must be present and non-empty
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with "Circana"
  given: $.info
  name: info-title-circana-prefix
  severity: warn
- description: Info description must be present and non-empty
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version must be 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Circana"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-circana-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags should have descriptions
  given: $.tags[*]
  name: tag-description
  severity: info
- description: Tag names should use Title Case
  given: $.tags[*].name
  name: tag-title-case
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameter names should use snake_case
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-snake-case
  severity: warn
- description: Parameters must have a schema with type
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameters should include an example value
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-example-recommended
  severity: info
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have a success response (2xx)
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should include a 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schema property names should use snake_case
  given: $.components.schemas[*].properties
  name: schema-property-snake-case
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties must define a type
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-request-body-required
  severity: info
- description: Descriptions must not be empty strings
  given: $.paths[*][get,post,put,patch,delete].description
  name: no-empty-descriptions
  severity: error
- description: Response schemas should include examples
  given: $.paths[*][get,post,put,patch,delete].responses[*].content.application/json
  name: examples-recommended
  severity: info
- description: Paginated endpoints should use offset/limit parameters
  given: $.paths[*].get.parameters[?(@.name=='offset' || @.name=='limit')]
  name: pagination-offset-limit
  severity: info
- description: Operations should include x-microcks-operation for mock compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/circana-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/circana/refs/heads/main/rules/circana-spectral-rules.yml
severity_counts:
  error: 20
  hint: 0
  info: 6
  warn: 15
slug: circana-spectral-rules
tags:
- Analytics
- Consumer Data
- Market Research
- Retail
- CPG
- Point Of Sale
- Consumer Insights
- Business Intelligence
- Spectral
- Linting
- API Governance
---
