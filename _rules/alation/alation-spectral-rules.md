---
categories:
- alation
description: Spectral linting rules defining API design standards and conventions for Alation.
layout: rules
name: Alation API Rules
provider_name: Alation
provider_slug: alation
rule_count: 26
rules:
- description: Alation APIs must use bearer token authentication
  given: $.components.securitySchemes
  name: alation-auth-bearer-required
  severity: error
- description: Global security must be defined
  given: $.security[*]
  name: alation-global-security-defined
  severity: error
- description: API title must be present
  given: $.info
  name: alation-info-title
  severity: error
- description: API description must be present
  given: $.info
  name: alation-info-description
  severity: error
- description: API version must be present
  given: $.info
  name: alation-info-version
  severity: error
- description: Alation API paths must end with a trailing slash
  given: $.paths
  name: alation-path-trailing-slash
  severity: warn
- description: Paths must be lowercase
  given: $.paths
  name: alation-path-no-uppercase
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: alation-operation-id-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: alation-operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: alation-operation-description-required
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: alation-operation-tags-required
  severity: error
- description: GET operations must define a 200 response
  given: $.paths[*].get.responses
  name: alation-response-200-required
  severity: error
- description: POST operations that create resources should return 201
  given: $.paths[*].post.responses
  name: alation-response-201-post
  severity: warn
- description: APIs must document 401 Unauthorized
  given: $.paths[*][get,post,put,patch,delete].responses
  name: alation-response-401-required
  severity: warn
- description: Successful responses must specify content type
  given: $.paths[*][get,post,put,patch,delete].responses[200,201].content
  name: alation-response-content-type
  severity: error
- description: All schemas must have descriptions
  given: $.components.schemas[*]
  name: alation-schema-description
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: alation-property-description
  severity: info
- description: Reuse schemas via $ref rather than inlining
  given: $.paths[*][*].responses[*].content[*].schema
  name: alation-no-inline-schemas
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: alation-parameter-description
  severity: warn
- description: List operations should support limit parameter
  given: $.paths[*].get.parameters[*]
  name: alation-pagination-limit
  severity: info
- description: operationId must use camelCase
  given: $.paths[*][*].operationId
  name: alation-operation-id-camel-case
  severity: warn
- description: Schema names must use PascalCase
  given: $.components.schemas
  name: alation-schema-name-pascal-case
  severity: warn
- description: Request bodies must specify application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: alation-request-body-content-type
  severity: error
- description: Request bodies must have a schema
  given: $.paths[*][post,put,patch].requestBody.content.application/json
  name: alation-request-body-schema
  severity: error
- description: API must define at least one server
  given: $
  name: alation-servers-required
  severity: error
- description: All operation tags must be defined at root level
  given: $
  name: alation-tags-defined
  severity: warn
rules_file: rules/alation-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/alation/refs/heads/main/rules/alation-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 10
slug: alation-spectral-rules
tags:
- Data Catalog
- Data Governance
- Data Intelligence
- Data Lineage
- Data Quality
- Business Glossary
- Metadata Management
- AI
- Spectral
- Linting
- API Governance
---
