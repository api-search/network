---
categories:
- delete
- get
- info
- microcks
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
description: Spectral linting rules defining API design standards and conventions for Oracle Cloud Infrastructure.
layout: rules
name: Oracle Cloud Infrastructure API Rules
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
rule_count: 25
rules:
- description: Info title must start with "Oracle Cloud"
  given: $.info.title
  name: info-title-format
  severity: error
- description: Info description is required
  given: $.info
  name: info-description-required
  severity: error
- description: API version is required
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version must be 3.0.x
  given: $
  name: openapi-version
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: server-https
  severity: error
- description: Path segments should use camelCase (OCI convention)
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Oracle Cloud"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: OperationId should use camelCase
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Operations must define at least one success response (2xx)
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: Schema property names should use camelCase (OCI convention)
  given: $.components.schemas[*].properties
  name: schema-properties-camel-case
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
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
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should include x-microcks-operation extension
  given: $.paths[*][get,post,put,delete,patch]
  name: microcks-operation-extension
  severity: info
rules_file: rules/oracle-cloud-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/rules/oracle-cloud-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 3
  warn: 8
slug: oracle-cloud-spectral-rules
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
- Spectral
- Linting
- API Governance
---
