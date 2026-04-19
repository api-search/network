---
categories:
- agromonitoring
description: Spectral linting rules defining API design standards and conventions for Agromonitoring.
layout: rules
name: Agromonitoring API Rules
provider_name: Agromonitoring
provider_slug: agromonitoring
rule_count: 20
rules:
- description: Operation summaries must use Title Case
  given: $.paths[*][*].summary
  name: agromonitoring-operation-summary-title-case
  severity: warn
- description: Operation summaries should start with a verb
  given: $.paths[*][*].summary
  name: agromonitoring-operation-summary-prefix
  severity: warn
- description: OperationId must use camelCase
  given: $.paths[*][*].operationId
  name: agromonitoring-operationid-camelcase
  severity: error
- description: All operations must require the appid query parameter for authentication
  given: $.paths[*][get,post,put,delete,patch]
  name: agromonitoring-appid-query-required
  severity: error
- description: All operations must define a 200 response
  given: $.paths[*][*].responses
  name: agromonitoring-response-200-defined
  severity: error
- description: All operations should define a 400 error response
  given: $.paths[*][*].responses
  name: agromonitoring-response-400-defined
  severity: warn
- description: All operations should define a 401 unauthorized response
  given: $.paths[*][*].responses
  name: agromonitoring-response-401-defined
  severity: warn
- description: Response schemas should use $ref to components/schemas
  given: $.paths[*][*].responses[*].content[*].schema
  name: agromonitoring-schema-ref-components
  severity: warn
- description: API info must include contact details
  given: $.info
  name: agromonitoring-info-contact
  severity: warn
- description: API info must include version
  given: $.info
  name: agromonitoring-info-version
  severity: error
- description: All operations must have at least one tag
  given: $.paths[*][*]
  name: agromonitoring-tags-defined
  severity: warn
- description: Schema properties should use snake_case
  given: $.components.schemas[*].properties
  name: agromonitoring-property-snake-case
  severity: warn
- description: Polygon schema must include an id field
  given: $.components.schemas.Polygon.properties
  name: agromonitoring-polygon-id-field
  severity: error
- description: GeoJson schema must include coordinates field
  given: $.components.schemas.GeoJson.properties
  name: agromonitoring-geo-json-coordinates
  severity: error
- description: NDVI values should include minimum/maximum bounds
  given: $.components.schemas.NdviRecord.properties.ndvi
  name: agromonitoring-ndvi-value-range
  severity: warn
- description: WeatherData schema must include temp field
  given: $.components.schemas.WeatherData.properties
  name: agromonitoring-weather-temp-field
  severity: error
- description: SoilData schema must include moisture field
  given: $.components.schemas.SoilData.properties
  name: agromonitoring-soil-moisture-field
  severity: error
- description: API must define at least one server URL
  given: $.servers
  name: agromonitoring-server-url-defined
  severity: error
- description: API must define an API key security scheme
  given: $.components.securitySchemes
  name: agromonitoring-security-scheme-apikey
  severity: error
- description: Path segments should use lowercase
  given: $.paths
  name: agromonitoring-path-lowercase
  severity: warn
rules_file: rules/agromonitoring-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/agromonitoring/refs/heads/main/rules/agromonitoring-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 0
  warn: 10
slug: agromonitoring-spectral-rules
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
- Spectral
- Linting
- API Governance
---
