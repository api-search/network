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
- paths
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for 1Password.
layout: rules
name: 1Password API Rules
provider_name: 1Password
provider_slug: 1password
rule_count: 30
rules:
- description: Info title should follow "1Password ..." pattern.
  given: $.info.title
  name: info-title-pattern
  severity: warn
- description: Info description must be present and at least 50 characters.
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided.
  given: $.info
  name: info-contact-required
  severity: info
- description: Must use OpenAPI 3.0.x or 3.1.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined and non-empty.
  given: $
  name: servers-must-be-defined
  severity: error
- description: Production server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: Paths must not end with a trailing slash.
  given: $.paths
  name: paths-no-trailing-slash
  severity: warn
- description: Path segments should use kebab-case.
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-description-required
  severity: warn
- description: Every operation summary should start with "1Password".
  given: $.paths[*][get,post,put,patch,delete,options,head].summary
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-operationid-required
  severity: error
- description: OperationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete,options,head].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,options,head]
  name: operation-tags-required
  severity: error
- description: Every parameter must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][get,post,put,patch,delete,options,head].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies must define content type.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-content-required
  severity: error
- description: Every operation must define at least one success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete,options,head].responses[*]
  name: response-description-required
  severity: error
- description: Authenticated APIs should define a 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-for-authenticated-apis
  severity: warn
- description: Component schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Schema properties should have explicit types.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-typed
  severity: warn
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Bearer token security should use HTTP Bearer scheme.
  given: $.components.securitySchemes[?(@.type == 'http' && @.scheme == 'bearer')]
  name: security-bearer-format
  severity: info
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204 No Content.
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
- description: Descriptions must not be empty.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-on-schemas
  severity: info
- description: Global tags should use Title Case naming.
  given: $.tags[*].name
  name: tags-title-case
  severity: warn
rules_file: rules/1password-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/rules/1password-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 6
  warn: 11
slug: 1password-spectral-rules
tags:
- Password Manager
- Passwords
- Security
- Secrets
- Spectral
- Linting
- API Governance
---
