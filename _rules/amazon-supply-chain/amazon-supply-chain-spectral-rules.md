---
categories:
- get
- info
- 'no'
- openapi
- operation
- paths
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Supply Chain.
layout: rules
name: Amazon Supply Chain API Rules
provider_name: Amazon Supply Chain
provider_slug: amazon-supply-chain
rule_count: 18
rules:
- description: API title must start with "Amazon" or "AWS"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info must have description
  given: $.info
  name: info-description-required
  severity: error
- description: Info must have version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Summary must start with "Amazon" or "AWS"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-amazon-prefix
  severity: warn
- description: Every operation must have operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationId must use PascalCase
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-id-pascal-case
  severity: warn
- description: Operations must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Operations must have 2xx response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Responses must have descriptions
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined
  given: $
  name: security-schemes-defined
  severity: error
- description: GET must not have request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Tags should use Title Case
  given: $.tags[*].name
  name: tags-title-case
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Object schemas should have descriptions
  given: $.components.schemas[?(@.type == 'object')]
  name: schema-description-on-objects
  severity: info
rules_file: rules/amazon-supply-chain-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-supply-chain/refs/heads/main/rules/amazon-supply-chain-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 2
  warn: 5
slug: amazon-supply-chain-spectral-rules
tags:
- AWS
- ERP Integration
- Logistics
- Machine Learning
- Supply Chain
- Spectral
- Linting
- API Governance
---
