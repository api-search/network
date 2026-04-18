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
description: Spectral linting rules defining API design standards and conventions for GitHub.
layout: rules
name: GitHub API Rules
provider_name: GitHub
provider_slug: github
rule_count: 20
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
- description: Path segments should use kebab-case or snake_case.
  given: $.paths
  name: paths-kebab-case
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
- description: Parameter names should use snake_case (GitHub convention).
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-snake-case
  severity: info
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
rules_file: rules/github-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/github/refs/heads/main/rules/github-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 3
  warn: 3
slug: github-spectral-rules
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
- Spectral
- Linting
- API Governance
---
