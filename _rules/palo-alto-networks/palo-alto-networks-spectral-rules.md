---
categories:
- components
- delete
- deprecated
- error
- external
- get
- info
- 'no'
- openapi
- operation
- pagination
- parameter
- paths
- post
- put
- request
- response
- schema
- security
- server
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Palo Alto Networks.
layout: rules
name: Palo Alto Networks API Rules
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
rule_count: 69
rules:
- description: Every API must have a title in the info object.
  given: $.info
  name: info-title-required
  severity: error
- description: Titles should start with "Palo Alto Networks" for portfolio consistency.
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: The info object must include a description explaining the API purpose.
  given: $.info
  name: info-description-required
  severity: error
- description: Info descriptions should be at least 50 characters to be meaningful.
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: A version string is required in the info object.
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information must be provided in the info object.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Contact should include a name field.
  given: $.info.contact
  name: info-contact-name
  severity: warn
- description: Contact should include a URL (e.g. https://pan.dev/).
  given: $.info.contact
  name: info-contact-url
  severity: warn
- description: License information must be provided in the info object.
  given: $.info
  name: info-license-required
  severity: warn
- description: APIs should use OpenAPI 3.1.0 or later.
  given: $
  name: openapi-version-3-1
  severity: warn
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: server-url-https
  severity: error
- description: Each server should have a description.
  given: $.servers[*]
  name: server-description-required
  severity: warn
- description: Path segments should use kebab-case (lowercase with hyphens), not camelCase, PascalCase, or snake_case.
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not end with a trailing slash.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not contain query strings — use parameters instead.
  given: $.paths
  name: paths-no-query-string
  severity: error
- description: Paths should include a version prefix (e.g. /v1/, /v2/).
  given: $.paths
  name: paths-version-prefix
  severity: info
- description: Resource collection paths should use plural nouns (e.g. /addresses not /address).
  given: $.paths
  name: paths-plural-resources
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Palo Alto Networks" for consistency.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Operation summaries should be concise — under 80 characters.
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-max-length
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs must use camelCase (e.g. listAddresses, getIncident).
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Operation IDs should start with a standard verb (get, list, create, update, delete, search, submit, start, stop, run, commit, isolate, scan, dismiss, reopen).
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-verb-prefix
  severity: info
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operations should have exactly one tag for clean documentation grouping.
  given: $.paths[*][get,post,put,patch,delete].tags
  name: operation-tags-one-only
  severity: info
- description: Global tags array must be defined.
  given: $
  name: tags-defined
  severity: warn
- description: Each global tag should have a description.
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: Tag names should use Title Case (e.g., "Network Security", "Cloud NGFW").
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: Tag names should use PascalCase or Title Case (e.g. Alerts, SecurityRules).
  given: $.tags[*].name
  name: tag-name-pascal-case
  severity: info
- description: Every parameter must have a description.
  given: $..parameters[*]
  name: parameter-description-required
  severity: warn
- description: Parameter names should use snake_case for consistency.
  given: $..parameters[*].name
  name: parameter-name-snake-case
  severity: warn
- description: API keys should be passed in headers, not query parameters.
  given: $..parameters[?(@.in=='query')]
  name: parameter-query-no-api-key
  severity: error
- description: Offset-based pagination should use "offset" as the parameter name.
  given: $..parameters[?(@.in=='query')]
  name: pagination-offset-name
  severity: info
- description: Limit-based pagination should use "limit" as the parameter name.
  given: $..parameters[?(@.in=='query')]
  name: pagination-limit-name
  severity: info
- description: Request bodies should support application/json.
  given: $..requestBody.content
  name: request-body-json
  severity: warn
- description: Request bodies should have a description.
  given: $..requestBody
  name: request-body-description
  severity: info
- description: Every operation must define at least one success response (2xx).
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-defined
  severity: error
- description: Operations with security should define a 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-401-defined
  severity: warn
- description: Operations should define a 403 Forbidden response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-403-defined
  severity: info
- description: GET operations with path parameters should define a 404 Not Found response.
  given: $.paths[*/{*}].get.responses
  name: response-error-404-on-get
  severity: info
- description: POST operations should define a 400 Bad Request response.
  given: $.paths[*].post.responses
  name: response-error-400-on-post
  severity: info
- description: Operations should define a 500 Internal Server Error response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-500-defined
  severity: info
- description: Every response must have a description.
  given: $..responses[*]
  name: response-description-required
  severity: error
- description: Success responses (except 204) should return application/json content.
  given: $.paths[*][get,post,put,patch,delete].responses[200,201,202].content
  name: response-json-content
  severity: warn
- description: Schema properties should use snake_case for consistency across the portfolio.
  given: $..properties
  name: schema-property-snake-case
  severity: warn
- description: Top-level schemas in components should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Schema properties must define a type or use a reference.
  given: $..properties[*]
  name: schema-property-type-defined
  severity: error
- description: Identifier properties should use "id" or be suffixed with "_id" (not "Id", "ID", or "identifier").
  given: $..properties
  name: schema-id-property-name
  severity: info
- description: Timestamp properties should use snake_case with standard suffixes (_at, _time, _timestamp).
  given: $..properties
  name: schema-timestamp-property-name
  severity: info
- description: A global security requirement should be defined.
  given: $
  name: security-defined-globally
  severity: warn
- description: At least one security scheme must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Security schemes should have a description explaining how to authenticate.
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: warn
- description: API key header names should use X- prefix convention (e.g. X-PAN-KEY, X-API-KEY).
  given: $.components.securitySchemes[?(@.type=='apiKey' && @.in=='header')]
  name: security-api-key-header-naming
  severity: info
- description: APIs should define reusable schemas in components.
  given: $.components
  name: components-schemas-defined
  severity: info
- description: Error responses (4xx, 5xx) should include a message or error field in the schema.
  given: $.paths[*][get,post,put,patch,delete].responses[400,401,403,404,409,500].content.application/json.schema
  name: error-response-has-message
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Custom headers in parameters should be moved to security schemes where possible.
  given: $..parameters[?(@.in=='header')].name
  name: no-x-headers-in-parameters
  severity: info
- description: Schemas with additionalProperties false should also define properties.
  given: $..schema[?(@.additionalProperties===false)]
  name: schema-no-additional-properties-false-alone
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: POST operations should have a request body.
  given: $.paths[*].post
  name: post-request-body-required
  severity: info
- description: PUT operations should have a request body.
  given: $.paths[*].put
  name: put-request-body-required
  severity: info
- description: DELETE operations should return 204 No Content on success.
  given: $.paths[*].delete.responses
  name: delete-response-204
  severity: info
- description: Top-level request/response schemas should include examples.
  given: $.paths[*][get,post,put,patch,delete]..content.application/json.schema
  name: schema-examples-defined
  severity: info
- description: Deprecated operations must include a description explaining the deprecation.
  given: $.paths[*][get,post,put,patch,delete][?(@.deprecated===true)]
  name: deprecated-operations-documented
  severity: warn
- description: APIs should link to external documentation (e.g. pan.dev).
  given: $
  name: external-docs-defined
  severity: info
- description: External docs must include a URL.
  given: $.externalDocs
  name: external-docs-url
  severity: warn
rules_file: rules/palo-alto-networks-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/rules/palo-alto-networks-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 24
  warn: 29
slug: palo-alto-networks-spectral-rules
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- Spectral
- Linting
- API Governance
---
