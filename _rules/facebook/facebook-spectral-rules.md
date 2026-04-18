---
categories:
- delete
- examples
- get
- info
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
description: Spectral linting rules defining API design standards and conventions for Facebook.
layout: rules
name: Facebook API Rules
provider_name: Facebook
provider_slug: facebook
rule_count: 30
rules:
- description: Info title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with Facebook.
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info description must be present.
  given: $.info
  name: info-description-required
  severity: error
- description: Info version must be present.
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided.
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version should be 3.0.x.
  given: $
  name: openapi-version
  severity: warn
- description: Servers array must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Paths should not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Facebook.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have tags.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: OperationId should be camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameter names should use snake_case or kebab-case.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-snake-case
  severity: info
- description: Operations must have a success response (2xx).
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Schema property names should use snake_case.
  given: $.components.schemas[*].properties
  name: schema-properties-snake-case
  severity: info
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas must have a type defined.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: error
- description: Global security must be defined.
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Bearer authentication should be used.
  given: $.components.securitySchemes[*]
  name: security-bearer-scheme
  severity: info
- description: GET operations should not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
- description: Pagination should use cursor-based pagination with before/after.
  given: $.components.schemas.Paging
  name: pagination-cursor-pattern
  severity: info
rules_file: rules/facebook-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/rules/facebook-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 5
  warn: 12
slug: facebook-spectral-rules
tags:
- Advertising
- Content Publishing
- Messaging
- Social Media
- Social Networking
- Spectral
- Linting
- API Governance
---
