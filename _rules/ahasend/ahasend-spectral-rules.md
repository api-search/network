---
categories:
- delete
- get
- idempotency
- info
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for AhaSend.
layout: rules
name: AhaSend API Rules
provider_name: AhaSend
provider_slug: ahasend
rule_count: 28
rules:
- description: API title must start with "AhaSend"
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API must have a non-empty description
  given: $.info
  name: info-description-required
  severity: error
- description: API must specify a version
  given: $.info
  name: info-version-required
  severity: error
- description: API contact email should be provided
  given: $.info.contact
  name: info-contact-email
  severity: warn
- description: Use OpenAPI 3.x
  given: $
  name: openapi-version
  severity: warn
- description: Servers array must be defined and non-empty
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Path segments must use kebab-case
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "AhaSend"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have a description
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Operations must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
- description: Schema properties should have a type defined
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: warn
- description: Security schemes must be defined
  given: $.components.securitySchemes
  name: security-schemes-defined
  severity: error
- description: Bearer auth token format should be documented
  given: $.components.securitySchemes[*][?(@.scheme == 'bearer')]
  name: security-bearer-format
  severity: info
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
- description: POST endpoints should document idempotency key header support
  given: $.paths[*].post.parameters[*]
  name: idempotency-key-documented
  severity: info
rules_file: rules/ahasend-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/ahasend/refs/heads/main/rules/ahasend-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 3
  warn: 14
slug: ahasend-spectral-rules
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
- Spectral
- Linting
- API Governance
---
