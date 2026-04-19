---
categories:
- get
- info
- 'no'
- openapi
- operation
- parameter
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon SimpleDB.
layout: rules
name: Amazon SimpleDB API Rules
provider_name: Amazon SimpleDB
provider_slug: amazon-simpledb
rule_count: 19
rules:
- description: API title must start with "Amazon" or "AWS"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
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
- description: Operation summary must start with "Amazon" or "AWS"
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-amazon-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationId must use PascalCase
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-id-pascal-case
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,delete,patch].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have a 2xx or 200 response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: error
- description: Object schemas should have descriptions
  given: $.components.schemas[?(@.type == 'object')]
  name: schema-description-on-objects
  severity: info
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Tags should use Title Case
  given: $.tags[*].name
  name: tags-title-case
  severity: warn
rules_file: rules/amazon-simpledb-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-simpledb/refs/heads/main/rules/amazon-simpledb-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 1
  warn: 7
slug: amazon-simpledb-spectral-rules
tags:
- AWS
- Cloud Storage
- Data Storage
- Database
- NoSQL
- Spectral
- Linting
- API Governance
---
