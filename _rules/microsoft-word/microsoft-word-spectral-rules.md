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
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Microsoft Word.
layout: rules
name: Microsoft Word API Rules
provider_name: Microsoft Word
provider_slug: microsoft-word
rule_count: 39
rules:
- description: Info title must be present and non-empty.
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with 'Microsoft Word'.
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info description must be present.
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters.
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: Info version must be present.
  given: $.info
  name: info-version-required
  severity: error
- description: Info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info should include license information.
  given: $.info
  name: info-license-required
  severity: info
- description: OpenAPI version must be 3.0.x.
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case.
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with 'Microsoft Word'.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
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
- description: Global tags array should be defined.
  given: $
  name: tags-defined
  severity: warn
- description: Each tag should have a description.
  given: $.tags[*]
  name: tags-description
  severity: info
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema with a type.
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should specify application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations should include a 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: GET operations should include a 404 Not Found response.
  given: $.paths[*].get.responses
  name: response-404-for-get
  severity: warn
- description: All schemas must have a type defined.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should use camelCase naming.
  given: $.components.schemas[*].properties
  name: schema-properties-camelcase
  severity: warn
- description: Global security must be defined.
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: OAuth2 security scheme should be defined for Microsoft Graph APIs.
  given: $.components.securitySchemes
  name: security-schemes-oauth2
  severity: warn
- description: GET operations must not have a request body.
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
- description: Operations should include x-microcks-operation extension.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/microsoft-word-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/rules/microsoft-word-spectral-rules.yml
severity_counts:
  error: 18
  hint: 0
  info: 4
  warn: 17
slug: microsoft-word-spectral-rules
tags:
- Documents
- Microsoft 365
- Office
- Productivity
- Word Processing
- Spectral
- Linting
- API Governance
---
