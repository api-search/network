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
description: Spectral linting rules defining API design standards and conventions for albertsons.
layout: rules
name: albertsons API Rules
provider_name: albertsons
provider_slug: albertsons
rule_count: 35
rules:
- description: Info title must be defined and start with "Albertsons".
  given: $.info.title
  name: info-title-required
  severity: error
- description: Info description must be defined with meaningful content.
  given: $.info.description
  name: info-description-required
  severity: error
- description: API version must be specified.
  given: $.info.version
  name: info-version-required
  severity: error
- description: Contact information should be provided.
  given: $.info.contact
  name: info-contact-required
  severity: warn
- description: All specs must use OpenAPI 3.x.
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $.servers
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Path segments must use kebab-case (lowercase with hyphens).
  given: $.paths[*]~
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash.
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Resource path segments should use plural nouns.
  given: $.paths[*]~
  name: paths-plural-resource-nouns
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with "Albertsons".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-albertsons-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete].description
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-required
  severity: error
- description: operationId must use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete].tags
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined.
  given: $.tags
  name: tags-global-defined
  severity: warn
- description: All global tags must have descriptions.
  given: $.tags[*].description
  name: tags-description-required
  severity: warn
- description: All parameters must have descriptions.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].description
  name: parameter-description-required
  severity: error
- description: Query and path parameter names should use camelCase or snake_case.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-snake-case
  severity: info
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-content-json
  severity: warn
- description: Request body content should have a schema with description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Secured endpoints should define a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: All responses must have descriptions.
  given: $.paths[*][get,post,put,patch,delete].responses[*].description
  name: response-description-required
  severity: error
- description: Top-level schemas must have descriptions.
  given: $.components.schemas[*].description
  name: schema-description-required
  severity: warn
- description: All schemas must define a type.
  given: $.components.schemas[*].type
  name: schema-type-required
  severity: warn
- description: Schema property names should use camelCase.
  given: $.components.schemas[*].properties[*]~
  name: schema-property-camel-case
  severity: info
- description: Security schemes must be defined in components.
  given: $.components.securitySchemes
  name: security-schemes-defined
  severity: error
- description: Bearer authentication scheme should be defined.
  given: $.components.securitySchemes.bearerAuth
  name: security-bearer-auth
  severity: warn
- description: Each operation should define security requirements.
  given: $.paths[*][get,post,put,patch,delete].security
  name: security-operation-defined
  severity: warn
- description: GET operations must not have request bodies.
  given: $.paths[*].get.requestBody
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have request bodies.
  given: $.paths[*].delete.requestBody
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/albertsons-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/albertsons/refs/heads/main/rules/albertsons-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 5
  warn: 14
slug: albertsons-spectral-rules
tags:
- Grocery
- Retail
- Retail Media
- Advertising
- Campaigns
- Analytics
- Consumer Goods
- Food
- Pharmacy
- Spectral
- Linting
- API Governance
---
