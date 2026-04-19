---
categories:
- delete
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
description: Spectral linting rules defining API design standards and conventions for Amazon CodeArtifact.
layout: rules
name: Amazon CodeArtifact API Rules
provider_name: Amazon CodeArtifact
provider_slug: amazon-codeartifact
rule_count: 23
rules:
- description: API title should identify CodeArtifact service
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $.openapi
  name: openapi-version
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with Amazon CodeArtifact
  given: $.paths[*][get,post,put,delete,patch].summary
  name: operation-summary-amazon-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,delete,patch,head,options]
  name: operation-operationId-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,delete,patch].operationId
  name: operation-operationId-camelcase
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must define at least one 2xx response
  given: $.paths[*][get,post,put,delete,patch]
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema components should have a type defined
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include examples for Microcks compatibility
  given: $.paths[*][get,post,put,delete,patch]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-codeartifact-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-codeartifact/refs/heads/main/rules/amazon-codeartifact-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 2
  warn: 10
slug: amazon-codeartifact-spectral-rules
tags:
- Amazon
- AWS
- Artifact Repository
- Package Management
- DevOps
- Software Supply Chain
- npm
- Maven
- PyPI
- NuGet
- Spectral
- Linting
- API Governance
---
