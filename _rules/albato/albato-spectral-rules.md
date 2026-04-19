---
categories:
- albato
description: Spectral linting rules defining API design standards and conventions for Albato.
layout: rules
name: Albato API Rules
provider_name: Albato
provider_slug: albato
rule_count: 24
rules:
- description: Albato APIs must define API key authentication
  given: $.components.securitySchemes
  name: albato-auth-apikey-required
  severity: error
- description: Global security must be defined
  given: $
  name: albato-global-security
  severity: error
- description: API must have a title
  given: $.info
  name: albato-info-title
  severity: error
- description: API must have a description
  given: $.info
  name: albato-info-description
  severity: error
- description: API must have a version
  given: $.info
  name: albato-info-version
  severity: error
- description: Paths must be lowercase
  given: $.paths
  name: albato-path-lowercase
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-id
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-description
  severity: warn
- description: Operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-tags
  severity: error
- description: GET operations must return 200
  given: $.paths[*].get.responses
  name: albato-response-200-get
  severity: error
- description: POST operations should return 201
  given: $.paths[*].post.responses
  name: albato-response-201-post
  severity: warn
- description: Operations should document 401
  given: $.paths[*].get.responses
  name: albato-response-401
  severity: warn
- description: Responses must use application/json
  given: $.paths[*][get,post,put].responses[200,201].content
  name: albato-response-json
  severity: error
- description: Schemas must have descriptions
  given: $.components.schemas[*]
  name: albato-schema-description
  severity: warn
- description: Properties must have types
  given: $.components.schemas[*].properties[*]
  name: albato-property-type
  severity: error
- description: Parameters should have descriptions
  given: $.paths[*][*].parameters[*]
  name: albato-parameter-description
  severity: warn
- description: Path parameters must have schemas
  given: $.paths[*][*].parameters[?(@.in=='path')]
  name: albato-path-param-schema
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][*].operationId
  name: albato-operation-id-camel-case
  severity: warn
- description: Schema names must use PascalCase
  given: $.components.schemas
  name: albato-schema-pascal-case
  severity: warn
- description: Request bodies must use application/json
  given: $.paths[*][post,put,patch].requestBody.content
  name: albato-request-body-json
  severity: error
- description: POST request bodies should be required
  given: $.paths[*].post.requestBody
  name: albato-request-body-required
  severity: warn
- description: API must define servers
  given: $
  name: albato-servers-defined
  severity: error
- description: Tags must be documented at root
  given: $
  name: albato-tags-at-root
  severity: warn
rules_file: rules/albato-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/albato/refs/heads/main/rules/albato-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 0
  warn: 9
slug: albato-spectral-rules
tags:
- No-Code Automation
- Workflow Automation
- Embedded iPaaS
- App Integration
- Integrations
- Webhooks
- White-Label
- Spectral
- Linting
- API Governance
---
