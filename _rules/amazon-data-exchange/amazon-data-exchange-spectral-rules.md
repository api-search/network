---
categories:
- arn
- create
- delete
- get
- info
- list
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
- update
description: Spectral linting rules defining API design standards and conventions for Amazon Data Exchange.
layout: rules
name: Amazon Data Exchange API Rules
provider_name: Amazon Data Exchange
provider_slug: amazon-data-exchange
rule_count: 30
rules:
- description: API title must start with "AWS Data Exchange"
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
- description: AWS Data Exchange API paths should include version prefix /v1/
  given: $.paths[*]~
  name: paths-versioned
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
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
- description: Create operations should use POST method
  given: $.paths[*][post].operationId
  name: create-uses-post
  severity: info
- description: Get/List operations should use GET method
  given: $.paths[*][get].operationId
  name: get-uses-get-method
  severity: info
- description: Update operations should use PATCH method
  given: $.paths[*][patch].operationId
  name: update-uses-patch
  severity: info
- description: Delete/Cancel operations should use DELETE method
  given: $.paths[*][delete].operationId
  name: delete-uses-delete-method
  severity: info
- description: Tags array should be defined globally
  given: $
  name: tags-defined
  severity: warn
- description: Each tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: POST/PATCH request bodies should support application/json
  given: $.paths[*][post,patch].requestBody.content
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
- description: List operations should support pagination via NextToken
  given: $.paths[*][get].responses.200.content.application/json.schema.properties
  name: list-response-has-next-token
  severity: info
- description: ARN fields should have descriptions documenting them as unique identifiers
  given: $.components.schemas[*].properties.Arn.description
  name: arn-field-documented
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have examples in request/response bodies
  given: $.paths[*][*].requestBody.content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-data-exchange-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-data-exchange/refs/heads/main/rules/amazon-data-exchange-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 7
  warn: 10
slug: amazon-data-exchange-spectral-rules
tags:
- AWS
- Data Exchange
- Data Marketplace
- Third-Party Data
- Analytics
- Subscriptions
- Spectral
- Linting
- API Governance
---
