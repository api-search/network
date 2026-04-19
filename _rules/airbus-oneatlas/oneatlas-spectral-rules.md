---
categories:
- oneatlas
description: Spectral linting rules defining API design standards and conventions for Airbus OneAtlas.
layout: rules
name: Airbus OneAtlas API Rules
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
rule_count: 12
rules:
- description: All operation summaries must use Title Case
  given: $.paths[*][get,post,put,patch,delete]
  name: oneatlas-operation-summary-title-case
  severity: warn
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: oneatlas-require-operation-id
  severity: error
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: oneatlas-require-operation-tags
  severity: warn
- description: GET operations must define a 200 response
  given: $.paths[*].get
  name: oneatlas-require-response-200
  severity: error
- description: Component schemas must have a title
  given: $.components.schemas[*]
  name: oneatlas-schema-title-required
  severity: warn
- description: All operations must include API key security
  given: $
  name: oneatlas-require-api-key-security
  severity: error
- description: API must define at least one server
  given: $
  name: oneatlas-require-server-url
  severity: error
- description: API info must have a description
  given: $.info
  name: oneatlas-require-info-description
  severity: warn
- description: API should reference external documentation
  given: $
  name: oneatlas-require-external-docs
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: oneatlas-require-operation-description
  severity: warn
- description: Geometry schemas must specify a type field
  given: $.components.schemas[?(@.description =~ /.*[Gg]eometr.*/)]
  name: oneatlas-geometry-type-required
  severity: warn
- description: CatalogItem schema must include id and geometry
  given: $.components.schemas.CatalogItem.properties
  name: oneatlas-catalog-item-required-fields
  severity: warn
rules_file: rules/oneatlas-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airbus-oneatlas/refs/heads/main/rules/oneatlas-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 0
  warn: 8
slug: oneatlas-spectral-rules
tags:
- Imagery
- Satellites
- Spectral
- Linting
- API Governance
---
