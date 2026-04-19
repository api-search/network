---
categories:
- delete
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
- tag
description: Spectral linting rules defining API design standards and conventions for 3M.
layout: rules
name: 3M API Rules
provider_name: 3M
provider_slug: 3m
rule_count: 32
rules:
- description: API info title should follow "3M ..." pattern.
  given: $.info.title
  name: info-title-pattern
  severity: warn
- description: API info description must be present and at least 50 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined and non-empty.
  given: $
  name: servers-must-be-defined
  severity: error
- description: Production server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: Each server must have a description.
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments should use kebab-case or camelCase, not underscores.
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash.
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every summary should start with "3M".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: OperationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags must have descriptions.
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameters should include example values.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-example-encouraged
  severity: info
- description: Request bodies should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Every operation must define at least one success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Authenticated APIs must define 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: error
- description: Component schemas must have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should define a type.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-described
  severity: info
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-examples
  severity: info
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security should be defined.
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty.
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/3m-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/3m/refs/heads/main/rules/3m-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 3
  warn: 16
slug: 3m-spectral-rules
tags:
- Industrial
- Manufacturing
- Supply Chain
- Spectral
- Linting
- API Governance
---
