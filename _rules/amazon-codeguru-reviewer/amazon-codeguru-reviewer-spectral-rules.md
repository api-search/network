---
categories:
- info
- 'no'
- operation
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon CodeGuru Reviewer.
layout: rules
name: Amazon CodeGuru Reviewer API Rules
provider_name: Amazon CodeGuru Reviewer
provider_slug: amazon-codeguru-reviewer
rule_count: 10
rules:
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Amazon CodeGuru Reviewer
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-company-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationId-required
  severity: error
- description: Every operation must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Every response must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema components should have a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include x-microcks-operation
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-microcks-operation
  severity: info
rules_file: rules/amazon-codeguru-reviewer-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-codeguru-reviewer/refs/heads/main/rules/amazon-codeguru-reviewer-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 4
slug: amazon-codeguru-reviewer-spectral-rules
tags:
- Amazon
- AWS
- Code Review
- Security
- DevOps
- Machine Learning
- Developer Tools
- Spectral
- Linting
- API Governance
---
