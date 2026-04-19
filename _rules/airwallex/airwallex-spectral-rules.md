---
categories:
- airwallex
description: Spectral linting rules defining API design standards and conventions for Airwallex.
layout: rules
name: Airwallex API Rules
provider_name: Airwallex
provider_slug: airwallex
rule_count: 29
rules:
- description: Payment intent must include id, amount, currency, and status.
  given: $.components.schemas.PaymentIntent.required
  name: airwallex-payment-intent-required-fields
  severity: error
- description: Transfer object must include id, source_amount, source_currency, and status.
  given: $.components.schemas.Transfer.required
  name: airwallex-transfer-required-fields
  severity: error
- description: Every API operation must have a non-empty summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: airwallex-operation-summary-exists
  severity: error
- description: Operation summaries must be in Title Case.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: airwallex-operation-summary-title-case
  severity: warn
- description: Every API operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: airwallex-operation-description-exists
  severity: warn
- description: Every operation must be tagged for grouping and documentation.
  given: $.paths[*][get,post,put,patch,delete]
  name: airwallex-operation-tags-exist
  severity: error
- description: Every operation must have a unique operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: airwallex-operation-id-exists
  severity: error
- description: operationId must be in camelCase format.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: airwallex-operation-id-camel-case
  severity: warn
- description: Every GET operation must define a 200 success response.
  given: $.paths[*].get
  name: airwallex-response-200-exists
  severity: error
- description: Operations accepting request bodies should document 400 errors.
  given: $.paths[*][post,put]
  name: airwallex-response-400-documented
  severity: warn
- description: Currency fields must be ISO 4217 three-letter uppercase codes.
  given: $.components.schemas[*].properties[*currency*]
  name: airwallex-currency-iso4217-format
  severity: warn
- description: Amount fields must be typed as number.
  given: $.components.schemas[*].properties[*amount*]
  name: airwallex-amount-type-number
  severity: warn
- description: Status fields must use an enum of allowed values.
  given: $.components.schemas[*].properties.status
  name: airwallex-status-enum-defined
  severity: warn
- description: All schema components must include a description.
  given: $.components.schemas[*]
  name: airwallex-schema-description-exists
  severity: warn
- description: All schema properties should include descriptions.
  given: $.components.schemas[*].properties[*]
  name: airwallex-property-description-exists
  severity: info
- description: Timestamp fields must use date-time format.
  given: $.components.schemas[*].properties[*_at]
  name: airwallex-datetime-format
  severity: warn
- description: All operations should include x-microcks-operation for mock support.
  given: $.paths[*][get,post,put,patch,delete]
  name: airwallex-microcks-operation-extension
  severity: info
- description: API must define security schemes for authentication.
  given: $
  name: airwallex-security-defined
  severity: error
- description: Airwallex APIs must use Bearer token authentication.
  given: $.components.securitySchemes[*]
  name: airwallex-bearer-auth-scheme
  severity: warn
- description: API paths must be lowercase and use hyphens for word separation.
  given: $.paths[*]~
  name: airwallex-path-lowercase
  severity: warn
- description: API paths must not end with a trailing slash.
  given: $.paths[*]~
  name: airwallex-no-trailing-slash
  severity: warn
- description: API info block must include a title.
  given: $.info
  name: airwallex-info-title-exists
  severity: error
- description: API info block must include a version.
  given: $.info
  name: airwallex-info-version-exists
  severity: error
- description: API info block should include a description.
  given: $.info
  name: airwallex-info-description-exists
  severity: warn
- description: API info should include contact information.
  given: $.info
  name: airwallex-contact-info-exists
  severity: info
- description: API must define at least one server URL.
  given: $
  name: airwallex-servers-defined
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*].url
  name: airwallex-server-https
  severity: error
- description: List endpoints should support a limit query parameter.
  given: $.paths[*].get.parameters[*][?(@.in == 'query' && @.name == 'limit')]
  name: airwallex-pagination-limit-param
  severity: info
- description: Request bodies must specify application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: airwallex-request-body-content-type
  severity: warn
rules_file: rules/airwallex-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airwallex/refs/heads/main/rules/airwallex-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 4
  warn: 14
slug: airwallex-spectral-rules
tags:
- Cross-Border Payments
- FinTech
- Foreign Exchange
- Payments
- Global
- Embedded Finance
- Multi-Currency
- Spectral
- Linting
- API Governance
---
