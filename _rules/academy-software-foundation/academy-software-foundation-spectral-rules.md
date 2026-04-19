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
- servers
description: Spectral linting rules defining API design standards and conventions for Academy Software Foundation.
layout: rules
name: Academy Software Foundation API Rules
provider_name: Academy Software Foundation
provider_slug: academy-software-foundation
rule_count: 21
rules:
- description: Info title must be present and start with "Academy Software Foundation"
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present and be descriptive
  given: $.info
  name: info-description-required
  severity: error
- description: Info version must be present
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Servers should have descriptions
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Path segments should use kebab-case or snake_case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with the provider name
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Path and query parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameters should have example values
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-example-recommended
  severity: info
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-property-description-recommended
  severity: info
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/academy-software-foundation-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/academy-software-foundation/refs/heads/main/rules/academy-software-foundation-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 2
  warn: 5
slug: academy-software-foundation-spectral-rules
tags:
- Animation
- Color Management
- Film
- Linux Foundation
- Open Source
- Rendering
- Standards
- Visual Effects
- VFX
- Spectral
- Linting
- API Governance
---
