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
- response
- schema
- security
- server
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Abortion Policy API.
layout: rules
name: Abortion Policy API API Rules
provider_name: Abortion Policy API
provider_slug: abortion-policy-api
rule_count: 32
rules:
- description: API info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should follow the "Abortion Policy API ..." naming pattern.
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
- description: Each server should have a description.
  given: $.servers[*]
  name: server-description-required
  severity: warn
- description: Path segments should use kebab-case or underscore_case.
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Abortion Policy API".
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
- description: Tag names should use Title Case.
  given: $.tags[*].name
  name: tag-name-title-case
  severity: warn
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
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
  name: schema-property-description
  severity: warn
- description: All schemas should have a type defined.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions.
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: Every operation should have security defined.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-security-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations must not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have examples for better developer experience.
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: examples-encouraged
  severity: info
rules_file: rules/abortion-policy-api-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/abortion-policy-api/refs/heads/main/rules/abortion-policy-api-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 1
  warn: 15
slug: abortion-policy-api-spectral-rules
tags:
- Abortion
- Policies
- Healthcare
- Government
- Spectral
- Linting
- API Governance
---
