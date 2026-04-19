---
categories:
- amazon
description: Spectral linting rules defining API design standards and conventions for Amazon Amplify.
layout: rules
name: Amazon Amplify API Rules
provider_name: Amazon Amplify
provider_slug: amazon-amplify
rule_count: 5
rules:
- description: API must have a title.
  given: $.info
  name: amazon-info-title-required
  severity: error
- description: Operations must have summaries.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-operation-summary-required
  severity: error
- description: Operations must have operationIds.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-operation-operationid-required
  severity: error
- description: GET operations must return 200.
  given: $.paths[*].get
  name: amazon-response-200-get
  severity: error
- description: Schemas should have descriptions.
  given: $.components.schemas[*]
  name: amazon-schema-description
  severity: info
rules_file: rules/amazon-amplify-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-amplify/refs/heads/main/rules/amazon-amplify-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 0
slug: amazon-amplify-spectral-rules
tags:
- AWS
- Frontend
- Full Stack
- Hosting
- Mobile Development
- Web Applications
- Spectral
- Linting
- API Governance
---
