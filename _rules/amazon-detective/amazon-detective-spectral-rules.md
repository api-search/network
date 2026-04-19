---
categories:
- delete
- external
- get
- info
- 'no'
- openapi
- operation
- operations
- parameter
- paths
- post
- request
- response
- schema
- security
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Detective.
layout: rules
name: Amazon Detective API Rules
provider_name: Amazon Detective
provider_slug: amazon-detective
rule_count: 39
rules:
- description: API title should start with "Amazon Detective"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description of at least 50 characters
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information
  given: $.info
  name: info-contact-required
  severity: warn
- description: API info should include license information
  given: $.info
  name: info-license-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments should use kebab-case or camelCase (AWS Detective uses camelCase in some paths)
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Paths must not end with a trailing slash
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Amazon Detective"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationIds should use camelCase
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-global-defined
  severity: warn
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tag-description-required
  severity: info
- description: All parameters must have a description
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: error
- description: Operations should include a 400 error response
  given: $.paths[*][post,put,patch].responses
  name: response-error-400
  severity: info
- description: Operations should include a 500 error response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-error-500
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should have a type defined
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Amazon Detective schema properties use PascalCase naming
  given: $.components.schemas[*].properties
  name: schema-property-pascal-case
  severity: info
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Security schemes should have descriptions
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations typically should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body-unless-needed
  severity: info
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-should-have-request-body
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation for mock support
  given: $.paths[*][get,post,put,delete,patch]
  name: operations-microcks-extension
  severity: info
- description: API should reference external documentation
  given: $
  name: external-docs-encouraged
  severity: info
rules_file: rules/amazon-detective-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-detective/refs/heads/main/rules/amazon-detective-spectral-rules.yml
severity_counts:
  error: 18
  hint: 0
  info: 9
  warn: 12
slug: amazon-detective-spectral-rules
tags:
- AWS
- Forensics
- Investigation
- Security
- Spectral
- Linting
- API Governance
---
