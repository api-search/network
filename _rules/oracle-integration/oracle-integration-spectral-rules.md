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
- tag
description: Spectral linting rules defining API design standards and conventions for Oracle Integration.
layout: rules
name: Oracle Integration API Rules
provider_name: Oracle Integration
provider_slug: oracle-integration
rule_count: 36
rules:
- description: Info title must start with "Oracle Integration".
  given: $.info.title
  name: info-title-must-start-with-oracle
  severity: error
- description: Info description is required and must be at least 50 characters.
  given: $.info
  name: info-description-required
  severity: error
- description: Info version is required.
  given: $.info
  name: info-version-required
  severity: error
- description: Info contact information is required.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info license information is required.
  given: $.info
  name: info-license-required
  severity: warn
- description: OpenAPI version must be 3.0.x.
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-required
  severity: error
- description: Each server must have a description.
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments should use kebab-case or camelCase consistently.
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Paths must not have a trailing slash.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not contain query strings.
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Oracle Integration".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags should have descriptions.
  given: $.tags[*]
  name: tag-description-required
  severity: info
- description: Tag names should use Title Case.
  given: $.tags[*].name
  name: tag-title-case
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema with a type.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: info
- description: Every operation must have a 2xx success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should include a 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-recommended
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schema property names should use camelCase.
  given: $.components.schemas[*].properties
  name: schema-properties-camelcase
  severity: warn
- description: Schemas must have a type defined.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: error
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-description-recommended
  severity: info
- description: Global security must be defined.
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations should not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $.paths[*][get,post,put,patch,delete].description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
- description: Operations should include x-microcks-operation for mock server compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-extension-recommended
  severity: info
rules_file: rules/oracle-integration-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/oracle-integration/refs/heads/main/rules/oracle-integration-spectral-rules.yml
severity_counts:
  error: 19
  hint: 0
  info: 6
  warn: 11
slug: oracle-integration-spectral-rules
tags:
- API Management
- Automation
- B2B Integration
- Cloud Integration
- Enterprise Integration
- Integration
- iPaaS
- Process Automation
- Spectral
- Linting
- API Governance
---
