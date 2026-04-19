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
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AccuWeather.
layout: rules
name: AccuWeather API Rules
provider_name: AccuWeather
provider_slug: accuweather
rule_count: 24
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
  name: servers-https-only
  severity: error
- description: ''
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: ''
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-starts-with-accuweather
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: ''
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: ''
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: ''
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-401
  severity: info
- description: ''
  given: $.components.schemas[*].properties[*]
  name: schema-properties-described
  severity: info
- description: ''
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
- description: ''
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: ''
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: ''
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/accuweather-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/rules/accuweather-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 3
  warn: 10
slug: accuweather-spectral-rules
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
- Spectral
- Linting
- API Governance
---
