---
categories:
- delete
- examples
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
description: Spectral linting rules defining API design standards and conventions for Amazon IAM Access Analyzer.
layout: rules
name: Amazon IAM Access Analyzer API Rules
provider_name: Amazon IAM Access Analyzer
provider_slug: amazon-iam-access-analyzer
rule_count: 23
rules:
- description: Info title must be present and non-empty.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present and have at least 20 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be specified in info.version.
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x specification.
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
- description: Every operation must have a non-empty summary.
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-summary-required
  severity: error
- description: Every operation summary must start with 'Amazon IAM Access Analyzer'.
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-id-required
  severity: error
- description: operationId should use PascalCase (e.g. ListAnalyzers, CreateAnalyzer).
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,delete,patch,head,options].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must define a schema.
  given: $.paths[*][get,post,put,delete,patch,head,options].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must define at least one 2xx success response.
  given: $.paths[*][get,post,put,delete,patch,head,options].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,delete,patch,head,options].responses[*]
  name: response-description-required
  severity: warn
- description: Top-level component schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: Schemas should define an explicit type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: info
- description: Security schemes must be defined in components if security is used.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/amazon-iam-access-analyzer-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-access-analyzer/refs/heads/main/rules/amazon-iam-access-analyzer-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 3
  warn: 10
slug: amazon-iam-access-analyzer-spectral-rules
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
- Spectral
- Linting
- API Governance
---
