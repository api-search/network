---
categories:
- info
- 'no'
- openai
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AIMLAPI.
layout: rules
name: AIMLAPI API Rules
provider_name: AIMLAPI
provider_slug: aimlapi
rule_count: 15
rules:
- description: Title should start with AIMLAPI
  given: $.info.title
  name: info-title-aimlapi
  severity: warn
- description: Operation summaries must start with "AIMLAPI"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation should have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Operations must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Parameters should have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description
  severity: warn
- description: Schema properties should have types defined
  given: $.components.schemas[*].properties[*]
  name: schema-property-type
  severity: warn
- description: Bearer auth security scheme should be defined
  given: $.components.securitySchemes
  name: security-bearer-defined
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Chat completion operations should have a model parameter
  given: $.paths['/chat/completions'].post
  name: openai-compatible-model-param
  severity: info
rules_file: rules/aimlapi-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aimlapi/refs/heads/main/rules/aimlapi-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 1
  warn: 8
slug: aimlapi-spectral-rules
tags:
- Artificial Intelligence
- Machine Learning
- AI Models
- LLM
- Image Generation
- Video Generation
- Speech
- Embeddings
- API Gateway
- Developer Tools
- Spectral
- Linting
- API Governance
---
