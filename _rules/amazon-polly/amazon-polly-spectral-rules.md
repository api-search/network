---
categories:
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Polly.
layout: rules
name: Amazon Polly API Rules
provider_name: Amazon Polly
provider_slug: amazon-polly
rule_count: 22
rules:
- description: API title must reference Amazon Polly
  given: $.info.title
  name: info-title-contains-amazon-polly
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: API should use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Path segments must use kebab-case or camelCase
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: All paths should start with /v1/
  given: $.paths
  name: paths-v1-prefix
  severity: info
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Summaries must begin with 'Amazon Polly'
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-amazon-polly-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All operations must have a success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schemas must define a type
  given: $.components.schemas[*]
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
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should provide examples
  given: $.paths[*][*].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-polly-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-polly/refs/heads/main/rules/amazon-polly-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 3
  warn: 7
slug: amazon-polly-spectral-rules
tags:
- AI
- AWS
- Machine Learning
- Speech Synthesis
- Text-To-Speech
- TTS
- Voice
- SSML
- Neural Engine
- Generative AI
- Spectral
- Linting
- API Governance
---
