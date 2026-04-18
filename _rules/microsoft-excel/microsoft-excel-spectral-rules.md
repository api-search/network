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
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Microsoft Excel.
layout: rules
name: Microsoft Excel API Rules
provider_name: Microsoft Excel
provider_slug: microsoft-excel
rule_count: 24
rules:
- description: Info title must contain 'Microsoft' or 'Excel'
  given: $.info.title
  name: info-title-must-contain-microsoft-excel
  severity: error
- description: Info description is required and must be at least 20 characters
  given: $.info
  name: info-description-required
  severity: error
- description: Info version is required
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-must-be-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-required
  severity: error
- description: Paths must not end with a trailing slash
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with 'Microsoft Excel'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tag-description-required
  severity: info
- description: Parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must define a success response (2xx)
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 401 Unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-recommended
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-description
  severity: info
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations must not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $.paths[*][get,post,put,patch,delete].description
  name: no-empty-descriptions
  severity: error
rules_file: rules/microsoft-excel-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-excel/refs/heads/main/rules/microsoft-excel-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 2
  warn: 6
slug: microsoft-excel-spectral-rules
tags:
- Automation
- Data Analysis
- Microsoft
- Microsoft 365
- Office
- Spreadsheets
- Spectral
- Linting
- API Governance
---
