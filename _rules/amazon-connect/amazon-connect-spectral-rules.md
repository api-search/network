---
categories:
- delete
- get
- info
- instance
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
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Connect.
layout: rules
name: Amazon Connect API Rules
provider_name: Amazon Connect
provider_slug: amazon-connect
rule_count: 36
rules:
- description: API title must start with "Amazon Connect"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description of at least 50 characters
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version field
  given: $.info
  name: info-version-required
  severity: error
- description: Info object should have a contact
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: Servers array must be defined and non-empty
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Each server must have a description
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments must use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summary must start with "Amazon Connect"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amazon-connect-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags array should be defined at the global level
  given: $
  name: tags-defined
  severity: warn
- description: Each global tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Query and header parameter names should use camelCase (AWS convention)
  given: $.paths[*][*].parameters[?(@.in == 'query')].name
  name: parameter-name-snake-case
  severity: info
- description: Request body should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Request body should support application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: All operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: POST operations should return a 400 Bad Request response
  given: $.paths[*].post.responses
  name: response-400-on-post
  severity: warn
- description: Error response schemas should include a message field
  given: $.components.schemas.Error.properties
  name: response-error-has-message
  severity: warn
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have a type defined
  given: $.components.schemas[*].properties[*]
  name: schema-properties-type-required
  severity: warn
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Operations should have examples in responses
  given: $.paths[*][*].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations using InstanceId path parameter should document it consistently
  given: $.paths[*][*].parameters[?(@.name == 'InstanceId')]
  name: instance-id-path-param
  severity: info
rules_file: rules/amazon-connect-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-connect/refs/heads/main/rules/amazon-connect-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 3
  warn: 17
slug: amazon-connect-spectral-rules
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
- Spectral
- Linting
- API Governance
---
