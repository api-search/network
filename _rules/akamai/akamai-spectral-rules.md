---
categories:
- delete
- get
- info
- openapi
- operation
- parameter
- paths
- response
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Akamai.
layout: rules
name: Akamai API Rules
provider_name: Akamai
provider_slug: akamai
rule_count: 21
rules:
- description: ''
  given: $.info.title
  name: info-title-akamai-prefix
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
  name: openapi-version-3
  severity: error
- description: ''
  given: $
  name: servers-defined
  severity: error
- description: ''
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: ''
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: ''
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-akamai-prefix
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-external-docs
  severity: info
- description: ''
  given: $.paths[*][get,post,put,patch,delete][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: ''
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: ''
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: ''
  given: $.paths[*].delete.responses
  name: delete-returns-no-content
  severity: info
- description: ''
  given: $.components
  name: security-schemes-defined
  severity: info
- description: ''
  given: $
  name: tags-global-defined
  severity: info
rules_file: rules/akamai-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/akamai/refs/heads/main/rules/akamai-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 4
  warn: 6
slug: akamai-spectral-rules
tags:
- CDN
- Cloud
- Edge Computing
- Networks
- Platform
- Security
- Spectral
- Linting
- API Governance
---
