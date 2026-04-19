---
categories:
- info
- microcks
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Amazon Health Dashboard.
layout: rules
name: Amazon Health Dashboard API Rules
provider_name: Amazon Health Dashboard
provider_slug: amazon-health-dashboard
rule_count: 7
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
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-health-dashboard-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-health-dashboard/refs/heads/main/rules/amazon-health-dashboard-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 2
slug: amazon-health-dashboard-spectral-rules
tags:
- AWS
- Health Monitoring
- Notifications
- Operations
- Service Status
- Spectral
- Linting
- API Governance
---
