---
categories:
- examples
- id
- info
- list
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- server
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Absence.io.
layout: rules
name: Absence.io API Rules
provider_name: Absence.io
provider_slug: absence-io
rule_count: 30
rules:
- description: API info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should follow the "Absence.io ..." naming pattern.
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API info must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: API must use OpenAPI 3.x.
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: server-https-required
  severity: error
- description: Path segments should use lowercase with optional underscores.
  given: $.paths
  name: paths-lowercase
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Absence.io".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: OperationIds must use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined.
  given: $
  name: tags-array-defined
  severity: warn
- description: Each global tag should have a description.
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every operation must have at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every authenticated operation should have a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: All schemas should have a type defined.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Schema property names should use snake_case or camelCase.
  given: $.components.schemas[*].properties
  name: schema-properties-snake-case
  severity: info
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Every operation should have security defined.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-security-defined
  severity: warn
- description: Absence.io uses POST for list operations (not GET). This is a provider-specific pattern.
  given: $.paths
  name: list-operations-use-post
  severity: info
- description: List request bodies should include skip and limit for pagination.
  given: $.paths[*].post.requestBody.content.application/json.schema.properties
  name: list-request-skip-limit
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have examples for better developer experience.
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: examples-encouraged
  severity: info
- description: Absence.io uses MongoDB-style _id fields (not id). Ensure IDs follow this convention.
  given: $.components.schemas[*].properties
  name: id-field-naming
  severity: info
rules_file: rules/absence-io-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/absence-io/refs/heads/main/rules/absence-io-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 5
  warn: 11
slug: absence-io-spectral-rules
tags:
- Absences
- Employees
- Leave Management
- HR
- Spectral
- Linting
- API Governance
---
