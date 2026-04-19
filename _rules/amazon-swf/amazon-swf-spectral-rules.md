---
categories:
- info
- operation
- parameter
- response
- security
description: Spectral linting rules defining API design standards and conventions for Amazon Simple Workflow Service.
layout: rules
name: Amazon Simple Workflow Service API Rules
provider_name: Amazon Simple Workflow Service
provider_slug: amazon-swf
rule_count: 9
rules:
- description: Info title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present.
  given: $.info
  name: info-description-required
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][*]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with 'Amazon SWF'.
  given: $.paths[*][*].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][*]
  name: operation-operationId-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][*]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have at least one 2xx response.
  given: $.paths[*][*].responses
  name: response-success-required
  severity: error
- description: Security schemes must be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
rules_file: rules/amazon-swf-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/rules/amazon-swf-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 5
slug: amazon-swf-spectral-rules
tags:
- Automation
- AWS
- Task Coordination
- Workflow
- Spectral
- Linting
- API Governance
---
