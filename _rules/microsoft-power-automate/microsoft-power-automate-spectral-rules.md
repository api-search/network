---
categories:
- delete
- get
- info
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Microsoft Power Automate.
layout: rules
name: Microsoft Power Automate API Rules
provider_name: Microsoft Power Automate
provider_slug: microsoft-power-automate
rule_count: 23
rules:
- description: Info object must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with Microsoft Power Automate
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
- description: OpenAPI version must be 3.0.x
  given: $
  name: openapi-version
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should be camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with Microsoft Power Automate
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: info
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Operations must define a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Operations should define a 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined
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
rules_file: rules/microsoft-power-automate-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-automate/refs/heads/main/rules/microsoft-power-automate-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 1
  warn: 7
slug: microsoft-power-automate-spectral-rules
tags:
- Automation
- Business Process
- Integration
- Low-Code
- Microsoft
- Power Platform
- RPA
- Workflow
- Spectral
- Linting
- API Governance
---
