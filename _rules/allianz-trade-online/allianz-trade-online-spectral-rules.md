---
categories:
- allianz
description: Spectral linting rules defining API design standards and conventions for Allianz Trade.
layout: rules
name: Allianz Trade API Rules
provider_name: Allianz Trade
provider_slug: allianz-trade-online
rule_count: 22
rules:
- description: All operation summaries must start with "Allianz Trade"
  given: $.paths[*][*].summary
  name: allianz-trade-operation-summary-prefix
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][*]
  name: allianz-trade-operation-tags
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][*]
  name: allianz-trade-operation-id
  severity: error
- description: All operations must have a description
  given: $.paths[*][*]
  name: allianz-trade-operation-description
  severity: warn
- description: List operations must support pageSize query parameter
  given: $.paths[*].get
  name: allianz-trade-pagination-page-size
  severity: warn
- description: List operations must support page query parameter
  given: $.paths[*].get
  name: allianz-trade-pagination-page
  severity: warn
- description: List operations must support totalRequired query parameter
  given: $.paths[*].get
  name: allianz-trade-pagination-total-required
  severity: warn
- description: Write operations (POST/PATCH/DELETE) must return 202 for async processing
  given: $.paths[*][post,patch,delete]
  name: allianz-trade-async-202
  severity: warn
- description: 202 responses must reference JobResponse schema
  given: $.paths[*][post,patch,delete].responses.202.content.application/json.schema.$ref
  name: allianz-trade-async-job-response
  severity: warn
- description: All operations must document 401 Unauthorized response
  given: $.paths[*][*].responses
  name: allianz-trade-error-response-401
  severity: error
- description: ErrorResponse must have a code property
  given: $.components.schemas.ErrorResponse.properties
  name: allianz-trade-error-schema-code
  severity: warn
- description: ErrorResponse must have a message property
  given: $.components.schemas.ErrorResponse.properties
  name: allianz-trade-error-schema-message
  severity: warn
- description: API must use OAuth2 security scheme
  given: $.components.securitySchemes
  name: allianz-trade-oauth2-security
  severity: error
- description: OAuth2 must use client credentials flow
  given: $.components.securitySchemes.OAuth2.flows
  name: allianz-trade-oauth2-client-credentials
  severity: error
- description: All schemas must have a title
  given: $.components.schemas[*]
  name: allianz-trade-schema-title
  severity: warn
- description: All schemas must have a description
  given: $.components.schemas[*]
  name: allianz-trade-schema-description
  severity: warn
- description: All schema properties must have a description
  given: $.components.schemas[*].properties[*]
  name: allianz-trade-property-description
  severity: warn
- description: Schema properties should have examples
  given: $.components.schemas[*].properties[*]
  name: allianz-trade-property-example
  severity: info
- description: All operations should have x-microcks-operation extension
  given: $.paths[*][*]
  name: allianz-trade-microcks-operation
  severity: info
- description: Identifier fields should follow Allianz Trade ID pattern (PREFIX-NNNNNN)
  given: $.components.schemas[*].properties[?(@property.endsWith('Id'))].example
  name: allianz-trade-id-pattern
  severity: info
- description: Currency properties must use ISO 4217 format
  given: $.components.schemas[*].properties.currency.description
  name: allianz-trade-currency-iso
  severity: warn
- description: Date properties must specify date format
  given: $.components.schemas[*].properties[?(@property.endsWith('Date') || @property.endsWith('date'))].format
  name: allianz-trade-date-format
  severity: warn
rules_file: rules/allianz-trade-online-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/allianz-trade-online/refs/heads/main/rules/allianz-trade-online-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 3
  warn: 14
slug: allianz-trade-online-spectral-rules
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
- Spectral
- Linting
- API Governance
---
