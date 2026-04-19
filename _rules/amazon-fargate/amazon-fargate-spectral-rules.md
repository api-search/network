---
categories:
- info
- 'no'
- openapi
- operation
- request
- response
- schema
- security
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Fargate.
layout: rules
name: Amazon Fargate API Rules
provider_name: Amazon Fargate
provider_slug: amazon-fargate
rule_count: 29
rules:
- description: API must have a title in info
  given: $.info
  name: info-title-required
  severity: error
- description: API title must start with Amazon Fargate
  given: $.info.title
  name: info-title-amazon-fargate-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.1.x
  given: $
  name: openapi-version-3-1
  severity: warn
- description: Must define at least one server
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationid-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summary must start with Amazon Fargate
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amazon-fargate-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: Global tags array must be defined
  given: $
  name: tags-defined
  severity: warn
- description: Each tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: Request bodies should use application/x-amz-json-1.1 or application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content-type
  severity: warn
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should have a 400 error response
  given: $.paths[*][post,put,patch].responses
  name: response-error-400
  severity: warn
- description: Operations should document 500 server errors
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-500
  severity: warn
- description: Component schemas must have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema properties must define a type
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: Should use AWS Signature V4 authentication
  given: $.components.securitySchemes
  name: security-aws-sig-v4
  severity: info
- description: Amazon API operations should use application/x-amz-json-1.1 content type
  given: $.paths[*][post].requestBody.content
  name: operation-amz-json-content-type
  severity: info
- description: Operations should have x-microcks-operation extension for mock support
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/amazon-fargate-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-fargate/refs/heads/main/rules/amazon-fargate-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 4
  warn: 15
slug: amazon-fargate-spectral-rules
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
- Spectral
- Linting
- API Governance
---
