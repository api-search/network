---
categories:
- info
- 'no'
- openapi
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Private CA.
layout: rules
name: Amazon Private CA API Rules
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
rule_count: 19
rules:
- description: API must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: API should use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All operations must have a summary
  given: $.paths[*][post,get,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Summaries should start with Amazon Private CA
  given: $.paths[*][post,get,put,delete,patch].summary
  name: operation-summary-amazon-private-ca-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][post,get,put,delete,patch]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][post,get,put,delete,patch]
  name: operation-id-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][post,get,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All operations must have a success response
  given: $.paths[*][post,get,put,delete,patch]
  name: response-success-required
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Consider adding examples to operation responses
  given: $.paths[*][*].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-private-ca-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-private-ca/refs/heads/main/rules/amazon-private-ca-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 2
  warn: 5
slug: amazon-private-ca-spectral-rules
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
- Spectral
- Linting
- API Governance
---
