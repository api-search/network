---
categories:
- get
- info
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- server
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Panorama.
layout: rules
name: Amazon Panorama API Rules
provider_name: Amazon Panorama
provider_slug: amazon-panorama
rule_count: 21
rules:
- description: API title should start with "Amazon Panorama"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version should be 3.x
  given: $.openapi
  name: openapi-version-3
  severity: warn
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: server-https-required
  severity: error
- description: Path segments should use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths should not have a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Amazon Panorama"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-company-prefix
  severity: warn
- description: Operations must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: OperationIds should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: Parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must have a success response (2xx)
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Response objects must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined in components
  given: $.components
  name: security-scheme-defined
  severity: error
- description: GET operations should not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Operations should include examples
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: operation-examples-encouraged
  severity: info
rules_file: rules/amazon-panorama-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-panorama/refs/heads/main/rules/amazon-panorama-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 1
  warn: 10
slug: amazon-panorama-spectral-rules
tags:
- AWS
- Cameras
- Computer Vision
- Edge ML
- Industrial IoT
- Spectral
- Linting
- API Governance
---
