---
categories:
- actions
- delete
- get
- hal
- info
- 'no'
- openapi
- operation
- parameter
- paths
- post
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Acquia.
layout: rules
name: Acquia API Rules
provider_name: Acquia
provider_slug: acquia
rule_count: 32
rules:
- description: OpenAPI info.title must be present and non-empty
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info.description must be present
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info.version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Acquia APIs must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Acquia Cloud API server should use cloud.acquia.com domain
  given: $.servers[*]
  name: servers-acquia-cloud-domain
  severity: info
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: Resource identifiers in paths should use UUID suffix pattern
  given: $.paths[*]~
  name: paths-uuid-format
  severity: info
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operation summaries should start with 'Acquia'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-acquia-prefix
  severity: info
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: warn
- description: All parameters should have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: UUID path parameters should end with 'Uuid' suffix
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in == 'path')]
  name: parameter-uuid-naming
  severity: info
- description: All operations must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Protected endpoints should define 401 Unauthorized responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-unauthorized
  severity: warn
- description: Protected endpoints should define 403 Forbidden responses
  given: $.paths[*][post,put,patch,delete].responses
  name: response-403-forbidden
  severity: warn
- description: Schema components should define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: error
- description: Acquia Cloud API uses OAuth2 authentication
  given: $.components.securitySchemes[*]
  name: security-oauth2-scheme
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations creating resources should have a request body
  given: $.paths[*].post
  name: post-has-request-body
  severity: info
- description: Action endpoints should follow /resources/{id}/actions/{action-name} pattern
  given: $.paths[*~\/actions\/]~
  name: actions-paths-pattern
  severity: info
- description: Acquia Cloud API responses use application/hal+json content type
  given: $.paths[*][get,post,put,patch,delete].responses[*].content
  name: hal-json-content-type
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/acquia-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/rules/acquia-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 8
  warn: 10
slug: acquia-spectral-rules
tags:
- Content
- Experience
- Spectral
- Linting
- API Governance
---
