---
categories:
- info
- operation
- parameter
- security
description: Spectral linting rules defining API design standards and conventions for Amazon WAF.
layout: rules
name: Amazon WAF API Rules
provider_name: Amazon WAF
provider_slug: amazon-waf
rule_count: 8
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
- description: Operation summaries must start with 'Amazon WAF'.
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
- description: Security schemes must be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
rules_file: rules/amazon-waf-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-waf/refs/heads/main/rules/amazon-waf-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 5
slug: amazon-waf-spectral-rules
tags:
- AWS
- Bot Management
- Ddos Protection
- Security
- WAF
- Web Application Firewall
- Spectral
- Linting
- API Governance
---
