---
categories:
- amazon
description: Spectral linting rules defining API design standards and conventions for Amazon App Studio.
layout: rules
name: Amazon App Studio API Rules
provider_name: Amazon App Studio
provider_slug: amazon-app-studio
rule_count: 3
rules:
- description: API must have a title.
  given: $.info
  name: amazon-info-title
  severity: error
- description: Operations must have summaries.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-operation-summary
  severity: error
- description: Operations must have operationIds.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-operation-id
  severity: error
rules_file: rules/amazon-app-studio-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-app-studio/refs/heads/main/rules/amazon-app-studio-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 0
slug: amazon-app-studio-spectral-rules
tags:
- AWS
- Generative AI
- Internal Tools
- Low-Code
- No-Code
- Spectral
- Linting
- API Governance
---
