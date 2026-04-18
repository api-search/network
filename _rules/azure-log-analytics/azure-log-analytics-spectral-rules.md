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
- post
- request
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Azure Log Analytics.
layout: rules
name: Azure Log Analytics API Rules
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
rule_count: 41
rules:
- description: Info object must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: Info title must start with "Azure Log Analytics".
  given: $.info.title
  name: info-title-prefix
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
- description: Info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info should include license information.
  given: $.info
  name: info-license-required
  severity: info
- description: OpenAPI version must be 3.0.x.
  given: $.openapi
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
  severity: info
- description: Path segments should use kebab-case or camelCase.
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not include query strings.
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Azure Log Analytics".
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
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags should have descriptions.
  given: $.tags[*]
  name: tag-description
  severity: info
- description: Tag names should use Title Case.
  given: $.tags[*].name
  name: tag-title-case
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema with type.
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameter names should use camelCase.
  given: $.paths[*][*].parameters[*].name
  name: parameter-camelcase
  severity: info
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Operations with security should include a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-401
  severity: info
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas must define a type.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: error
- description: Schema property names should use camelCase or PascalCase.
  given: $.components.schemas[*].properties
  name: schema-property-camelcase
  severity: info
- description: Global security must be defined.
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions.
  given: $.components.securitySchemes[*]
  name: security-scheme-description
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
  name: post-request-body-required
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should include examples.
  given: $.paths[*][get,post,put,patch].responses.200.content.application/json
  name: examples-encouraged
  severity: info
- description: Operations should include x-microcks-operation extension.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/azure-log-analytics-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/azure-log-analytics/refs/heads/main/rules/azure-log-analytics-spectral-rules.yml
severity_counts:
  error: 20
  hint: 0
  info: 10
  warn: 11
slug: azure-log-analytics-spectral-rules
tags:
- Analytics
- Azure
- Cloud
- Logging
- Monitoring
- Spectral
- Linting
- API Governance
---
