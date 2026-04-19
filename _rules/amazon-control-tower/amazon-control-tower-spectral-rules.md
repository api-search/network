---
categories:
- arn
- async
- info
- 'no'
- openapi
- operation
- paths
- request
- response
- schema
- security
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Control Tower.
layout: rules
name: Amazon Control Tower API Rules
provider_name: Amazon Control Tower
provider_slug: amazon-control-tower
rule_count: 27
rules:
- description: API title must start with "AWS Control Tower"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
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
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: AWS Control Tower API paths use POST for all non-tag operations
  given: $.paths[*]~
  name: paths-post-convention
  severity: info
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "AWS Control Tower"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-aws-prefix
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
- description: Tags array should be defined globally
  given: $
  name: tags-defined
  severity: warn
- description: Each tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: POST request bodies should support application/json
  given: $.paths[*].post.requestBody.content
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
- description: Error response schemas should include a message field
  given: $.components.schemas.Error.properties
  name: response-error-has-message
  severity: warn
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Asynchronous operations (create, update, delete, reset, enable, disable) should return an operationIdentifier
  given: $.paths[?(@ =~ /create|update|delete|reset|enable|disable/)].post.responses.200.content.application/json.schema.properties
  name: async-operation-identifier-in-response
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have examples in request bodies
  given: $.paths[*][*].requestBody.content[*]
  name: operation-examples-encouraged
  severity: info
- description: Control Tower uses ARNs as resource identifiers - document them consistently
  given: $.paths[*][*].requestBody.content.application/json.schema.properties[?(@ =~ /Identifier|Arn/)].description
  name: arn-as-identifier-convention
  severity: info
rules_file: rules/amazon-control-tower-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-control-tower/refs/heads/main/rules/amazon-control-tower-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 4
  warn: 10
slug: amazon-control-tower-spectral-rules
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
- Spectral
- Linting
- API Governance
---
