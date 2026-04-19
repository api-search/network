---
categories:
- external
- get
- info
- 'no'
- openapi
- operation
- post
- response
- schema
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon DMS.
layout: rules
name: Amazon DMS API Rules
provider_name: Amazon DMS
provider_slug: amazon-dms
rule_count: 18
rules:
- description: API title should include "DMS" or "Database Migration"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-id-required
  severity: error
- description: OperationIds should use PascalCase (AWS DMS convention)
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-id-pascal-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: POST operations should have a request body
  given: $.paths[*].post
  name: post-should-have-request-body
  severity: info
- description: Operations must have at least one 2xx response
  given: $.paths[*][get,post,put,delete,patch].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,delete,patch].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: API should reference external documentation
  given: $
  name: external-docs-encouraged
  severity: info
rules_file: rules/amazon-dms-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-dms/refs/heads/main/rules/amazon-dms-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 3
  warn: 4
slug: amazon-dms-spectral-rules
tags:
- AWS
- Data Replication
- Database
- Database Migration
- Migration
- Spectral
- Linting
- API Governance
---
