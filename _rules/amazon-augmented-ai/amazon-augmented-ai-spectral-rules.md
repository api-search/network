---
categories:
- a2i
description: Spectral linting rules defining API design standards and conventions for Amazon Augmented AI.
layout: rules
name: Amazon Augmented AI API Rules
provider_name: Amazon Augmented AI
provider_slug: amazon-augmented-ai
rule_count: 11
rules:
- description: All operationIds must be camelCase
  given: $.paths[*][*].operationId
  name: a2i-operation-id-camel-case
  severity: warn
- description: All operation summaries must start with Amazon Augmented AI
  given: $.paths[*][*].summary
  name: a2i-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][*]
  name: a2i-has-tags
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][*].responses
  name: a2i-response-200
  severity: error
- description: StartHumanLoopRequest must require HumanLoopName
  given: $.components.schemas.StartHumanLoopRequest
  name: a2i-human-loop-name-required
  severity: error
- description: HumanLoopStatus must use valid enum values
  given: $.components.schemas.HumanLoopSummary.properties.HumanLoopStatus
  name: a2i-human-loop-status-enum
  severity: error
- description: API must use sigv4 security scheme
  given: $.security[*]
  name: a2i-security-sigv4
  severity: error
- description: Server URL must be fixed without variables
  given: $.servers[*]
  name: a2i-server-url-fixed
  severity: warn
- description: All examples must have x-microcks-default set to true
  given: $.paths[*][*].responses[*].content[*].examples.default
  name: a2i-example-microcks-default
  severity: warn
- description: StartHumanLoopRequest must require HumanLoopInput
  given: $.components.schemas.StartHumanLoopRequest.required
  name: a2i-human-loop-input-required
  severity: error
- description: StartHumanLoopRequest must require FlowDefinitionArn
  given: $.components.schemas.StartHumanLoopRequest.properties.FlowDefinitionArn
  name: a2i-flow-definition-arn-required
  severity: error
rules_file: rules/amazon-augmented-ai-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/rules/amazon-augmented-ai-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 5
slug: amazon-augmented-ai-spectral-rules
tags:
- Amazon Augmented AI
- Human In The Loop
- Machine Learning
- AI Review
- AWS
- Spectral
- Linting
- API Governance
---
