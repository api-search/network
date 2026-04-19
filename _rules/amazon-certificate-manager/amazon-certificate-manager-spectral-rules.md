---
categories:
- delete
- external
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Certificate Manager.
layout: rules
name: Amazon Certificate Manager API Rules
provider_name: Amazon Certificate Manager
provider_slug: amazon-certificate-manager
rule_count: 29
rules:
- description: API title must start with "Amazon Certificate Manager"
  given: $.info.title
  name: info-title-prefix
  severity: error
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API must have contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: API must define at least one server
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: All servers must have a description
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationId-required
  severity: error
- description: operationId must use PascalCase (matches AWS convention)
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-operationId-pascal-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon Certificate Manager"
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All response codes must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should include 400 bad request response
  given: $.paths[*][post,put,patch,delete].responses
  name: response-401-for-secured
  severity: warn
- description: Operations should document 500 internal server error
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-required
  severity: info
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-on-top-level
  severity: warn
- description: Schema properties must define a type
  given: $.components.schemas[*].properties[*]
  name: schema-properties-have-types
  severity: warn
- description: Security schemes must be defined if security is referenced
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: APIs should have external documentation links
  given: $
  name: external-docs-encouraged
  severity: info
- description: Operations should have x-microcks-operation extension for mock server support
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
rules_file: rules/amazon-certificate-manager-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-certificate-manager/refs/heads/main/rules/amazon-certificate-manager-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 3
  warn: 11
slug: amazon-certificate-manager-spectral-rules
tags:
- AWS
- Certificates
- Encryption
- Security
- SSL
- TLS
- Spectral
- Linting
- API Governance
---
