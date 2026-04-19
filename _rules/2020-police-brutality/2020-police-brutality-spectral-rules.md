---
categories:
- get
- info
- 'no'
- openapi
- operation
- response
- schema
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for 2020 Police Brutality.
layout: rules
name: 2020 Police Brutality API Rules
provider_name: 2020 Police Brutality
provider_slug: 2020-police-brutality
rule_count: 19
rules:
- description: API info title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API info description must be present and meaningful.
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: Open data APIs should include a license.
  given: $.info
  name: info-license-required
  severity: warn
- description: Must use OpenAPI 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers array must be defined.
  given: $
  name: servers-must-be-defined
  severity: error
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Component schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schemas should define a type.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-described
  severity: info
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Global tags array should be defined for documentation.
  given: $
  name: tags-defined
  severity: info
rules_file: rules/2020-police-brutality-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/2020-police-brutality/refs/heads/main/rules/2020-police-brutality-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 2
  warn: 7
slug: 2020-police-brutality-spectral-rules
tags:
- Brutality
- Civil Rights
- Policing
- Public Data
- Spectral
- Linting
- API Governance
---
