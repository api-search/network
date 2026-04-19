---
categories:
- delete
- examples
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Aladdin Studio.
layout: rules
name: Aladdin Studio API Rules
provider_name: Aladdin Studio
provider_slug: aladdin-studio
rule_count: 36
rules:
- description: Info title must be defined
  given: $.info
  name: info-title-required
  severity: error
- description: API title should start with 'Aladdin'
  given: $.info.title
  name: info-title-aladdin-prefix
  severity: warn
- description: Info description must be defined and non-empty
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: Info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info should include license information
  given: $.info
  name: info-license-required
  severity: warn
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: Server URLs should use api.blackrock.com domain
  given: $.servers[*]
  name: servers-blackrock-domain
  severity: warn
- description: Path segments should use kebab-case (not camelCase or snake_case)
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: API paths should include a version prefix
  given: $.paths[*]~
  name: paths-versioned
  severity: warn
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with 'Aladdin Studio'
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-aladdin-prefix
  severity: warn
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationid-required
  severity: error
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Tags should be defined at the global level
  given: $
  name: tags-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tags-description-required
  severity: warn
- description: Parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameters must have a schema definition
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have a description
  given: $.paths[*][*].requestBody
  name: request-body-description
  severity: warn
- description: Operations must have at least one success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: APIs should define 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-401-required
  severity: warn
- description: Resource endpoints should define 404 Not Found
  given: $.paths[*][get]
  name: response-404-for-resource-endpoints
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: error
- description: OAuth2 should be the primary authentication scheme
  given: $.components.securitySchemes
  name: security-oauth2-preferred
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should have examples for developer experience
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/aladdin-studio-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aladdin-studio/refs/heads/main/rules/aladdin-studio-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 3
  warn: 17
slug: aladdin-studio-spectral-rules
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
- Spectral
- Linting
- API Governance
---
