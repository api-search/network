---
categories:
- info
- openapi
- operation
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Application Discovery Service.
layout: rules
name: Amazon Application Discovery Service API Rules
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
rule_count: 21
rules:
- description: API title must start with "Amazon Application Discovery Service"
  given: $.info
  name: info-title-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must have a version field
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: error
- description: Path segments must use kebab-case or camelCase with /v1/ prefix
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Amazon Application Discovery Service"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every operation must have a 200 success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 500 error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-500-defined
  severity: warn
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Global security must be defined
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Operations should have x-microcks-operation for mock server compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: POST operations should have request/response examples
  given: $.paths[*][post].requestBody.content.application/json
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-application-discovery-service-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-application-discovery-service/refs/heads/main/rules/amazon-application-discovery-service-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 2
  warn: 6
slug: amazon-application-discovery-service-spectral-rules
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
- Spectral
- Linting
- API Governance
---
