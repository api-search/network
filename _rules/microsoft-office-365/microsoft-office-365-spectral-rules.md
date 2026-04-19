---
categories:
- info
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Microsoft Office 365.
layout: rules
name: Microsoft Office 365 API Rules
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
rule_count: 7
rules:
- description: Info title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/microsoft-office-365-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-office-365/refs/heads/main/rules/microsoft-office-365-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 0
slug: microsoft-office-365-spectral-rules
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
- Spectral
- Linting
- API Governance
---
