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
description: Spectral linting rules defining API design standards and conventions for Amazon QLDB.
layout: rules
name: Amazon QLDB API Rules
provider_name: Amazon QLDB
provider_slug: amazon-qldb
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
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: warn
- description: Paths should use RESTful resource naming
  given: $.paths
  name: paths-restful-design
  severity: info
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: Summaries should start with Amazon QLDB
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-amazon-qldb-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: All operations must have a success response
  given: $.paths[*][get,post,put,delete,patch]
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
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/amazon-qldb-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-qldb/refs/heads/main/rules/amazon-qldb-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 1
  warn: 6
slug: amazon-qldb-spectral-rules
tags:
- AWS
- Blockchain
- Database
- Ledger
- Spectral
- Linting
- API Governance
---
