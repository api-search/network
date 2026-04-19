---
categories:
- info
- microcks
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Amazon GuardDuty.
layout: rules
name: Amazon GuardDuty API Rules
provider_name: Amazon GuardDuty
provider_slug: amazon-guardduty
rule_count: 8
rules:
- description: ''
  given: $.info.title
  name: info-title-format
  severity: warn
- description: ''
  given: $.info
  name: info-description-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-company-prefix
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: ''
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-guardduty-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-guardduty/refs/heads/main/rules/amazon-guardduty-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 2
slug: amazon-guardduty-spectral-rules
tags:
- Anomaly Detection
- AWS
- Compliance
- Machine Learning
- Monitoring
- Security
- Threat Detection
- Spectral
- Linting
- API Governance
---
