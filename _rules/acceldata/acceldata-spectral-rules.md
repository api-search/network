---
categories:
- acceldata
description: Spectral linting rules defining API design standards and conventions for Acceldata.
layout: rules
name: Acceldata API Rules
provider_name: Acceldata
provider_slug: acceldata
rule_count: 25
rules:
- description: All operations must require the X-API-Key security scheme
  given: $.paths[*][get,post,put,patch,delete]
  name: acceldata-require-api-key-security
  severity: error
- description: API key must use X-API-Key header name
  given: $.components.securitySchemes[*][?(@.in == 'header')]
  name: acceldata-api-key-header-name
  severity: error
- description: API paths must use kebab-case
  given: $.paths[*]~
  name: acceldata-path-kebab-case
  severity: warn
- description: API paths must not have trailing slashes
  given: $.paths[*]~
  name: acceldata-no-trailing-slash
  severity: warn
- description: GET operations must define a 200 response
  given: $.paths[*].get.responses
  name: acceldata-require-200-response
  severity: error
- description: Operations must define a 400 error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: acceldata-require-400-response
  severity: warn
- description: Operations must define a 401 unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: acceldata-require-401-response
  severity: warn
- description: Operations must define a 500 server error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: acceldata-require-500-response
  severity: warn
- description: All schema components must have a description
  given: $.components.schemas[*]
  name: acceldata-schema-require-description
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: acceldata-schema-properties-require-description
  severity: info
- description: Resource schemas should include an id property
  given: $.components.schemas[?(@.type == 'object' && !@.properties.total)]
  name: acceldata-require-id-property
  severity: info
- description: Timestamp fields must use date-time format
  given: $.components.schemas[*].properties[?(@.description =~ /time|date|at$/i)]
  name: acceldata-timestamp-format
  severity: error
- description: List/collection schemas must include a total count property
  given: $.components.schemas[?(@.title =~ /List$/)]
  name: acceldata-list-schema-require-total
  severity: warn
- description: List/collection schemas must include page and pageSize for pagination
  given: $.components.schemas[?(@.title =~ /List$/)]
  name: acceldata-list-schema-require-page
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: acceldata-operations-require-tags
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: acceldata-operations-require-summary
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: acceldata-operations-require-operation-id
  severity: error
- description: OperationIds must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: acceldata-operation-id-camel-case
  severity: warn
- description: List operations should support page and pageSize query parameters
  given: $.paths[?(!@~.match(/\{.*\}/))].get.parameters[*]
  name: acceldata-list-operations-support-pagination
  severity: info
- description: Request bodies must use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: acceldata-require-json-content-type
  severity: error
- description: Success responses must return application/json
  given: $.paths[*][get,post,put,patch,delete].responses[200,201].content
  name: acceldata-response-require-json-content-type
  severity: error
- description: API info must include a version
  given: $.info
  name: acceldata-info-require-version
  severity: error
- description: API info must include a description
  given: $.info
  name: acceldata-info-require-description
  severity: error
- description: Alert and rule severity must use standard values
  given: $.components.schemas[*].properties.severity
  name: acceldata-severity-values
  severity: warn
- description: Alert status must use standard values
  given: $.components.schemas[*].properties.status
  name: acceldata-status-values
  severity: warn
rules_file: rules/acceldata-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acceldata/refs/heads/main/rules/acceldata-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 3
  warn: 12
slug: acceldata-spectral-rules
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
- Spectral
- Linting
- API Governance
---
