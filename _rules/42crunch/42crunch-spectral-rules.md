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
- post
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for 42Crunch.
layout: rules
name: 42Crunch API Rules
provider_name: 42Crunch
provider_slug: 42crunch
rule_count: 43
rules:
- description: The info object must have a non-empty title.
  given: $.info
  name: info-title-required
  severity: error
- description: API title must start with "42Crunch" to identify the provider.
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: The info object must have a description with at least 30 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: The info object must specify a version.
  given: $.info
  name: info-version-required
  severity: error
- description: The info object should include contact information.
  given: $.info
  name: info-contact-required
  severity: info
- description: All specs must use OpenAPI 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: warn
- description: Every server must have a description.
  given: $.servers[*]
  name: servers-description
  severity: info
- description: Path segments must use kebab-case (lowercase letters, numbers, hyphens).
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Paths must not contain query strings; use parameters instead.
  given: $.paths[*]~
  name: paths-no-query-string
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "42Crunch" for consistency.
  given: $.paths[*][get,post,put,patch,delete,options,head].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase format.
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-id-camel-case
  severity: warn
- description: operationId should start with a standard verb (list, get, create, update, delete, check, run, search).
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-id-verb-prefix
  severity: info
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: Operations should include x-microcks-operation for mock server compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Global tags array should be defined with descriptions.
  given: $
  name: tags-global-defined
  severity: warn
- description: Tag names must use Title Case (e.g., "Jobs", "Health", "Logs").
  given: $.tags[*].name
  name: tags-title-case
  severity: warn
- description: Each global tag should have a description.
  given: $.tags[*]
  name: tags-description-required
  severity: info
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Query parameter names should use snake_case or kebab-case.
  given: $.paths[*][*].parameters[?(@.in == 'query')].name
  name: parameter-name-kebab-case
  severity: info
- description: Request bodies should specify application/json as content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Request body schemas should include examples for documentation and mocking.
  given: $.paths[*][post,put,patch].requestBody.content.application/json
  name: request-body-examples
  severity: info
- description: Every operation must have at least one 2xx success response.
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every operation should have a 400 Bad Request response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-400-required
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Success responses should return application/json content.
  given: $.paths[*][get,post,put,patch].responses[?(@property.match(/^2/))]
  name: response-json-content
  severity: warn
- description: Error responses (4xx) should use the Error schema with an 'error' field.
  given: $.paths[*][*].responses[?(@property.match(/^4/))]
  name: response-error-schema
  severity: warn
- description: All schemas in components must have a type defined.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: All component schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-description
  severity: info
- description: Schemas should set additionalProperties to false for strict validation.
  given: $.components.schemas[*]
  name: schema-additional-properties-false
  severity: info
- description: Schema properties must not be empty objects without type or $ref.
  given: $.components.schemas[*].properties[*]
  name: schema-no-empty-properties
  severity: warn
- description: All security schemes must have descriptions.
  given: $.components.securitySchemes[*]
  name: security-schemes-described
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations should have a request body.
  given: $.paths[*].post
  name: post-has-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/42crunch-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/42crunch/refs/heads/main/rules/42crunch-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 10
  warn: 21
slug: 42crunch-spectral-rules
tags:
- API Security
- Platform
- Scanning
- Security
- OpenAPI
- DevSecOps
- Spectral
- Linting
- API Governance
---
