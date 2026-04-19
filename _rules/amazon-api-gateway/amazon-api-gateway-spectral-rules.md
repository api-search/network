---
categories:
- amazon
description: Spectral linting rules defining API design standards and conventions for Amazon API Gateway.
layout: rules
name: Amazon API Gateway API Rules
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
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
rules_file: rules/amazon-api-gateway-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-api-gateway/refs/heads/main/rules/amazon-api-gateway-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 1
  warn: 0
slug: amazon-api-gateway-spectral-rules
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
- Spectral
- Linting
- API Governance
---
