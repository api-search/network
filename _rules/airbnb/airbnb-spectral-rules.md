---
categories:
- airbnb
description: Spectral linting rules defining API design standards and conventions for airbnb.
layout: rules
name: airbnb API Rules
provider_name: airbnb
provider_slug: airbnb
rule_count: 15
rules:
- description: All operation summaries must use Title Case
  given: $.paths[*][get,post,put,patch,delete]
  name: airbnb-operation-summary-title-case
  severity: warn
- description: Operation IDs must use camelCase
  given: $.paths[*][get,post,put,patch,delete]
  name: airbnb-operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: airbnb-require-operation-tags
  severity: error
- description: GET operations must define a 200 response
  given: $.paths[*].get
  name: airbnb-require-response-200
  severity: error
- description: All component schemas must have a title
  given: $.components.schemas[*]
  name: airbnb-schema-title-required
  severity: warn
- description: All operations must require OAuth2 security
  given: $.paths[*][get,post,put,patch,delete]
  name: airbnb-require-oauth2-security
  severity: error
- description: Listing status must use defined enum values
  given: $.components.schemas.Listing.properties.status
  name: airbnb-listing-status-enum
  severity: warn
- description: List operations should support pagination parameters
  given: $.paths[*].get
  name: airbnb-require-pagination-params
  severity: warn
- description: Reservation schema must include check_in and check_out
  given: $.components.schemas.Reservation.properties
  name: airbnb-reservation-required-dates
  severity: error
- description: API must define at least one server URL
  given: $
  name: airbnb-require-server-url
  severity: error
- description: API info must include contact information
  given: $.info
  name: airbnb-require-contact-info
  severity: warn
- description: Path responses should reference component schemas, not inline
  given: $.paths[*][*].responses[*].content[*].schema
  name: airbnb-no-inline-schemas-in-paths
  severity: warn
- description: Schemas with price fields should include currency
  given: $.components.schemas[*].properties
  name: airbnb-currency-field-present
  severity: warn
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: airbnb-require-description-on-paths
  severity: warn
- description: API should include externalDocs pointing to developer portal
  given: $
  name: airbnb-require-external-docs
  severity: warn
rules_file: rules/airbnb-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airbnb/refs/heads/main/rules/airbnb-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 10
slug: airbnb-spectral-rules
tags:
- Spectral
- Linting
- API Governance
---
