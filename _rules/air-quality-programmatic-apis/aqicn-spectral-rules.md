---
categories:
- info
- operation
- parameter
- response
- servers
- token
description: Spectral linting rules defining API design standards and conventions for Air Quality Programmatic APIs.
layout: rules
name: Air Quality Programmatic APIs API Rules
provider_name: Air Quality Programmatic APIs
provider_slug: air-quality-programmatic-apis
rule_count: 10
rules:
- description: API title should start with "Air Quality" or "AQICN"
  given: $.info.title
  name: info-title-aqicn
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: API token query parameter should be documented on all operations
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name == 'token')]
  name: token-parameter-required
  severity: warn
- description: Operations must define a 200 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-200-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: All parameters should have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
rules_file: rules/aqicn-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/air-quality-programmatic-apis/refs/heads/main/rules/aqicn-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 5
slug: aqicn-spectral-rules
tags:
- Air Quality
- Environment
- EPA
- Open Data
- Public Health
- IoT
- Government Data
- Real-Time Data
- Spectral
- Linting
- API Governance
---
