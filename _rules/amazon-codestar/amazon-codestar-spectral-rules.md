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
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon CodeStar.
layout: rules
name: Amazon CodeStar API Rules
provider_name: Amazon CodeStar
provider_slug: amazon-codestar
rule_count: 25
rules:
- description: OpenAPI info must have a title matching AWS CodeStar naming pattern.
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info must have a description with at least 20 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info must have a version field.
  given: $.info
  name: info-version-required
  severity: error
- description: Specs must use OpenAPI 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-required
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Amazon CodeStar".
  given: $.paths[*][get,post,put,patch,delete,head,options].summary
  name: operation-summary-amazon-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: OperationIds should use PascalCase as per AWS convention.
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-id-pascal-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: APIs should define 400 or 4xx error responses.
  given: $.paths[*][post,put,patch,delete].responses
  name: response-4xx-defined
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema objects should have a type defined.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
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
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should have x-microcks-operation for mock server compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-codestar-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-codestar/refs/heads/main/rules/amazon-codestar-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 13
slug: amazon-codestar-spectral-rules
tags:
- AWS
- Developer Tools
- DevOps
- Project Management
- Team Collaboration
- Spectral
- Linting
- API Governance
---
