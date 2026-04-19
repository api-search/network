---
categories:
- albato
description: Spectral linting rules defining API design standards and conventions for Albato A Single No Code Platform For All Automations.
layout: rules
name: Albato A Single No Code Platform For All Automations API Rules
provider_name: Albato A Single No Code Platform For All Automations
provider_slug: albato-a-single-no-code-platform-for-all-automations
rule_count: 25
rules:
- description: Albato APIs must define API key authentication
  given: $.components.securitySchemes
  name: albato-auth-apikey-required
  severity: error
- description: Global security must be defined
  given: $.security[*]
  name: albato-global-security-defined
  severity: error
- description: API title must be present
  given: $.info
  name: albato-info-title
  severity: error
- description: API description must be present
  given: $.info
  name: albato-info-description
  severity: error
- description: API version must be present
  given: $.info
  name: albato-info-version
  severity: error
- description: Paths must not end with a trailing slash
  given: $.paths
  name: albato-path-no-trailing-slash
  severity: warn
- description: Paths must be lowercase with hyphens
  given: $.paths
  name: albato-path-lowercase
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-id-required
  severity: error
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-summary-required
  severity: error
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-description-required
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: albato-operation-tags-required
  severity: error
- description: GET operations must define a 200 response
  given: $.paths[*].get.responses
  name: albato-response-200-get
  severity: error
- description: POST create operations should return 201
  given: $.paths[*].post.responses
  name: albato-response-201-post
  severity: warn
- description: Operations should document 401 Unauthorized
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
- description: Schema properties must have types
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
- description: POST operations should have required request bodies
  given: $.paths[*].post.requestBody
  name: albato-request-body-required
  severity: warn
- description: API must define servers
  given: $
  name: albato-servers-defined
  severity: error
- description: Tags must be documented at root level
  given: $
  name: albato-tags-documented
  severity: warn
rules_file: rules/albato-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/albato-a-single-no-code-platform-for-all-automations/refs/heads/main/rules/albato-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 0
  warn: 10
slug: albato-spectral-rules
tags:
- No-Code Automation
- Workflow Automation
- App Integration
- Embedded iPaaS
- Integrations
- Webhooks
- Spectral
- Linting
- API Governance
---
