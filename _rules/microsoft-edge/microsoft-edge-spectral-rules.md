---
categories:
- delete
- get
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Microsoft Edge.
layout: rules
name: Microsoft Edge API Rules
provider_name: Microsoft Edge
provider_slug: microsoft-edge
rule_count: 27
rules:
- description: Info title must start with "Microsoft Edge"
  given: $.info.title
  name: info-title-prefix
  severity: error
- description: Info description is required
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: Info version is required
  given: $.info
  name: info-version-required
  severity: error
- description: Info contact is required
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version should be 3.0.x
  given: $.openapi
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summary should start with "Microsoft Edge"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags should use Title Case
  given: $.paths[*][get,post,put,patch,delete].tags[*]
  name: tags-title-case
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must have a success response (2xx)
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should have a type defined
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes should be defined when security is used
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/microsoft-edge-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-edge/refs/heads/main/rules/microsoft-edge-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 0
  warn: 12
slug: microsoft-edge-spectral-rules
tags:
- Browser
- Chromium
- Developer Tools
- Edge
- Extensions
- Microsoft
- Progressive Web Apps
- Web Development
- WebView
- Spectral
- Linting
- API Governance
---
