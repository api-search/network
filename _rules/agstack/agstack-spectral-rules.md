---
categories:
- agstack
description: Spectral linting rules defining API design standards and conventions for AgStack Foundation.
layout: rules
name: AgStack Foundation API Rules
provider_name: AgStack Foundation
provider_slug: agstack
rule_count: 16
rules:
- description: Operation summaries should use Title Case
  given: $.paths[*][*].summary
  name: agstack-operation-summary-title-case
  severity: warn
- description: All operations must define an operationId
  given: $.paths[*][get,post,put,delete,patch]
  name: agstack-operationid-defined
  severity: error
- description: All operations must define a successful response
  given: $.paths[*][*].responses
  name: agstack-response-200-defined
  severity: error
- description: FastAPI operations should document 422 validation errors
  given: $.paths[*][get,post].responses
  name: agstack-response-422-validation-error
  severity: warn
- description: Protected operations must declare Bearer security
  given: $.paths[*][post,put,delete,patch]
  name: agstack-security-bearer-defined
  severity: warn
- description: API must define a version
  given: $.info
  name: agstack-info-version
  severity: error
- description: API must include a description
  given: $.info
  name: agstack-info-description
  severity: warn
- description: API must define at least one server URL
  given: $.servers
  name: agstack-server-url-defined
  severity: error
- description: Schema components must define a type
  given: $.components.schemas[*]
  name: agstack-schema-type-defined
  severity: warn
- description: POST/PUT request bodies should specify application/json content type
  given: $.paths[*][post,put].requestBody.content
  name: agstack-request-body-content-type
  severity: warn
- description: All operations should have tags for grouping
  given: $.paths[*][*]
  name: agstack-tags-on-operations
  severity: warn
- description: Geo ID fields should follow AgStack's 16-character alphanumeric format
  given: $.components.schemas[*].properties.geo_id
  name: agstack-geo-id-format
  severity: warn
- description: API must use OpenAPI 3.x
  given: $.openapi
  name: agstack-openapi-version-3
  severity: error
- description: Operation descriptions should be meaningful (min 10 chars)
  given: $.paths[*][*].description
  name: agstack-description-field-length
  severity: warn
- description: GeoJSON schemas must include a type field
  given: $.components.schemas.GeoJSONOut.properties
  name: agstack-geojson-type-field
  severity: error
- description: API paths should use lowercase and hyphens
  given: $.paths
  name: agstack-paths-lowercase
  severity: warn
rules_file: rules/agstack-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/agstack/refs/heads/main/rules/agstack-spectral-rules.yml
severity_counts:
  error: 6
  hint: 0
  info: 0
  warn: 10
slug: agstack-spectral-rules
tags:
- Agriculture
- Linux Foundation
- Open Source
- Geospatial
- Precision Agriculture
- Linked Data
- Spectral
- Linting
- API Governance
---
