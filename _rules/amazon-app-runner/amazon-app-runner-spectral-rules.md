---
categories:
- amazon
description: Spectral linting rules defining API design standards and conventions for Amazon App Runner.
layout: rules
name: Amazon App Runner API Rules
provider_name: Amazon App Runner
provider_slug: amazon-app-runner
rule_count: 3
rules:
- description: API must have a title.
  given: $.info
  name: amazon-app-runner-info-title
  severity: error
- description: Operations must have summaries.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-app-runner-operation-summary
  severity: error
- description: Operations must have operationIds.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-app-runner-operation-id
  severity: error
rules_file: rules/amazon-app-runner-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-app-runner/refs/heads/main/rules/amazon-app-runner-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 0
slug: amazon-app-runner-spectral-rules
tags:
- AWS
- CI/CD
- Containers
- Deployment
- Managed Service
- Serverless
- Web Applications
- Spectral
- Linting
- API Governance
---
