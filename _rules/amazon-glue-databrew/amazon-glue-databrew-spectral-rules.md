---
categories:
- info
- microcks
- 'no'
- operation
- response
description: Spectral linting rules defining API design standards and conventions for Amazon Glue DataBrew.
layout: rules
name: Amazon Glue DataBrew API Rules
provider_name: Amazon Glue DataBrew
provider_slug: amazon-glue-databrew
rule_count: 7
rules:
- description: API title must reference Amazon Glue DataBrew
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
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: ''
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/amazon-glue-databrew-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-glue-databrew/refs/heads/main/rules/amazon-glue-databrew-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 1
slug: amazon-glue-databrew-spectral-rules
tags:
- AWS
- Data Analytics
- Data Preparation
- ETL
- Machine Learning
- Spectral
- Linting
- API Governance
---
