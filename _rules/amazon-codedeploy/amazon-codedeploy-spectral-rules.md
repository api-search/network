---
categories:
- info
- 'no'
- operation
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon CodeDeploy.
layout: rules
name: Amazon CodeDeploy API Rules
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
rule_count: 9
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
- description: Operation summaries should start with Amazon CodeDeploy
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-company-prefix
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-operationId-required
  severity: error
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
rules_file: rules/amazon-codedeploy-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-codedeploy/refs/heads/main/rules/amazon-codedeploy-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 3
slug: amazon-codedeploy-spectral-rules
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
- Spectral
- Linting
- API Governance
---
