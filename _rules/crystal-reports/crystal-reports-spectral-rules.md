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
description: Spectral linting rules defining API design standards and conventions for Crystal Reports.
layout: rules
name: Crystal Reports API Rules
provider_name: Crystal Reports
provider_slug: crystal-reports
rule_count: 16
rules:
- description: ''
  given: $.info
  name: info-title-required
  severity: error
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
rules_file: rules/crystal-reports-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/crystal-reports/refs/heads/main/rules/crystal-reports-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 1
  warn: 1
slug: crystal-reports-spectral-rules
tags:
- Business Intelligence
- Crystal Reports
- Data Analytics
- Enterprise Software
- Reporting
- SAP
- Spectral
- Linting
- API Governance
---
