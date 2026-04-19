---
categories:
- info
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AmTrust Financial Services.
layout: rules
name: AmTrust Financial Services API Rules
provider_name: AmTrust Financial Services
provider_slug: amtrust-financial-services
rule_count: 10
rules:
- description: API title must include AmTrust Financial Services
  given: $.info.title
  name: info-title-amtrust
  severity: warn
- description: Info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: All servers must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: All operations must have summaries
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations must have operationIds
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All operations must have success responses
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Schema properties should have explicit types
  given: $.components.schemas[*].properties[*]
  name: schema-properties-typed
  severity: warn
rules_file: rules/amtrust-financial-services-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/rules/amtrust-financial-services-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 0
  warn: 3
slug: amtrust-financial-services-spectral-rules
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
- Spectral
- Linting
- API Governance
---
