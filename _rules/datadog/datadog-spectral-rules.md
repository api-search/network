---
categories:
- get
- info
- 'no'
- operation
- parameter
- paths
- response
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Datadog.
layout: rules
name: Datadog API Rules
provider_name: Datadog
provider_slug: datadog
rule_count: 19
rules:
- description: ''
  given: $.info
  name: info-title-required
  severity: error
- description: ''
  given: $.info.title
  name: info-title-format
  severity: warn
- description: ''
  given: $.info
  name: info-description-required
  severity: error
- description: ''
  given: $.info
  name: info-version-required
  severity: error
- description: ''
  given: $
  name: servers-defined
  severity: error
- description: ''
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: ''
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: ''
  given: $.paths
  name: paths-version-prefix
  severity: info
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: ''
  given: $
  name: operation-operationid-unique
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: ''
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: ''
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: ''
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: ''
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: ''
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/datadog-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/rules/datadog-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 3
slug: datadog-spectral-rules
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
- Spectral
- Linting
- API Governance
---
