---
categories:
- get
- info
- 'no'
- openapi
- operation
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon IoT Greengrass.
layout: rules
name: Amazon IoT Greengrass API Rules
provider_name: Amazon IoT Greengrass
provider_slug: amazon-iot-greengrass
rule_count: 14
rules:
- description: Info title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API version must be specified.
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-only
  severity: error
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with 'Amazon IoT Greengrass'.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Every response must have a description.
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: warn
- description: Schemas should define an explicit type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: info
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
rules_file: rules/amazon-iot-greengrass-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-greengrass/refs/heads/main/rules/amazon-iot-greengrass-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 1
  warn: 5
slug: amazon-iot-greengrass-spectral-rules
tags:
- AWS
- Edge Computing
- IoT
- Lambda
- Machine Learning
- Real-Time Processing
- Spectral
- Linting
- API Governance
---
