---
categories:
- client
- info
- 'no'
- operation
- path
- paths
- response
- schema
- security
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Fault Injection Simulator.
layout: rules
name: Amazon Fault Injection Simulator API Rules
provider_name: Amazon Fault Injection Simulator
provider_slug: amazon-fault-injection-simulator
rule_count: 28
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Title must start with AWS Fault Injection Simulator
  given: $.info.title
  name: info-title-aws-fis-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: API must define servers
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Operations must have summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Summaries must start with AWS Fault Injection Simulator
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-aws-fis-prefix
  severity: warn
- description: Operations must have description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operations should have x-microcks-operation
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-microcks-extension
  severity: info
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Operations must have a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Mutating operations should document 400
  given: $.paths[*][post,put,patch].responses
  name: response-error-400
  severity: warn
- description: Operations on specific resources should document 404
  given: $.paths[*][get,patch,delete].responses
  name: response-error-404
  severity: warn
- description: Operations should document 500
  given: $.paths[*][*].responses
  name: response-error-500
  severity: warn
- description: Component schemas must have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties should define type
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: Path parameters should have descriptions
  given: $.paths[*][*].parameters[*][?(@.in=="path")]
  name: path-parameters-described
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Global tags must be defined
  given: $
  name: tags-defined
  severity: warn
- description: Each tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: Create operations should include clientToken for idempotency
  given: $.paths[*][post].requestBody.content
  name: client-token-in-create
  severity: info
rules_file: rules/amazon-fis-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-fault-injection-simulator/refs/heads/main/rules/amazon-fis-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 16
slug: amazon-fis-spectral-rules
tags:
- AWS
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
- Spectral
- Linting
- API Governance
---
