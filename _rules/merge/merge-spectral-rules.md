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
- remote
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Merge.
layout: rules
name: Merge API Rules
provider_name: Merge
provider_slug: merge
rule_count: 37
rules:
- description: Info object must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with "Merge".
  given: $.info.title
  name: info-title-merge-prefix
  severity: warn
- description: Info object must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters.
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: Info object must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: Info object should have contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version should be 3.x.
  given: $
  name: openapi-version-3
  severity: warn
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Server URL should be on api.merge.dev.
  given: $.servers[*].url
  name: servers-merge-api-domain
  severity: info
- description: Path segments should use kebab-case.
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Resource paths should use plural nouns.
  given: $.paths
  name: paths-plural-resources
  severity: info
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Merge".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-merge-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameter names should use snake_case.
  given: $.paths[*][*].parameters[*].name
  name: parameter-snake-case
  severity: warn
- description: Merge APIs use cursor-based pagination with cursor parameter.
  given: $.paths[*].get.parameters
  name: parameter-pagination-cursor
  severity: info
- description: Request bodies should use application/json.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
- description: Every operation must have a success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should use snake_case naming.
  given: $.components.schemas[*].properties
  name: schema-property-snake-case
  severity: warn
- description: Schemas must define a type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Global security must be defined.
  given: $
  name: security-defined
  severity: error
- description: Merge APIs should use Bearer token authentication.
  given: $.components.securitySchemes
  name: security-bearer-auth
  severity: warn
- description: Merge APIs require X-Account-Token header.
  given: $.components.securitySchemes
  name: security-account-token-header
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: List endpoints should return paginated responses with next/previous/results.
  given: $.paths[*].get.responses.200.content.application/json.schema
  name: pagination-response-format
  severity: info
- description: Merge schemas should include remote_was_deleted field for soft delete tracking.
  given: $.components.schemas[?(@.type=='object' && !@.title.match(/Paginated|Request|Error/))]
  name: remote-was-deleted-field
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/merge-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/rules/merge-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 7
  warn: 15
slug: merge-spectral-rules
tags:
- Integrations
- Platform
- Unified API
- Spectral
- Linting
- API Governance
---
