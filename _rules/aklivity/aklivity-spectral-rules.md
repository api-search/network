---
categories:
- get
- info
- operation
- paths
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Aklivity.
layout: rules
name: Aklivity API Rules
provider_name: Aklivity
provider_slug: aklivity
rule_count: 11
rules:
- description: ''
  given: $.info
  name: info-title-required
  severity: error
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
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
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
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: ''
  given: $.components.schemas[*].properties[*]
  name: schema-type-defined
  severity: warn
rules_file: rules/aklivity-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/aklivity/refs/heads/main/rules/aklivity-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 1
  warn: 2
slug: aklivity-spectral-rules
tags:
- API Gateway
- Apache Kafka
- Event-Driven
- IoT
- Kafka Proxy
- Multi-Protocol
- Real-Time
- Spectral
- Linting
- API Governance
---
