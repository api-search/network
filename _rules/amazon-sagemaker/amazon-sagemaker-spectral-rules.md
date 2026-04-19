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
description: Spectral linting rules defining API design standards and conventions for Amazon SageMaker.
layout: rules
name: Amazon SageMaker API Rules
provider_name: Amazon SageMaker
provider_slug: amazon-sagemaker
rule_count: 23
rules:
- description: Info title must be present and start with "Amazon SageMaker"
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present with at least 30 characters
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be present
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https-only
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon SageMaker"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amazon-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use PascalCase (SageMaker convention)
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-pascal-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Request bodies must define content
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-content-required
  severity: error
- description: Every operation must have a 200 or 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Schema properties should have a type defined
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: warn
- description: Top-level component schemas must have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes should be defined in components
  given: $
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
  severity: warn
- description: Operations should have x-microcks-operation for mock support
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-present
  severity: info
rules_file: rules/amazon-sagemaker-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-sagemaker/refs/heads/main/rules/amazon-sagemaker-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 11
slug: amazon-sagemaker-spectral-rules
tags:
- AI
- AWS
- Inference
- Machine Learning
- MLOps
- Training
- Spectral
- Linting
- API Governance
---
