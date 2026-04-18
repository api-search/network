---
categories:
- delete
- deprecated
- external
- get
- info
- 'no'
- openapi
- operation
- parameter
- patch
- paths
- post
- put
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Google Analytics.
layout: rules
name: Google Analytics API Rules
provider_name: Google Analytics
provider_slug: google-analytics
rule_count: 66
rules:
- description: API title must be present and non-empty.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should follow the pattern "Google Analytics [Name]".
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API description must be present and meaningful.
  given: $.info
  name: info-description-required
  severity: error
- description: API description should be at least 50 characters to be meaningful.
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: API version must be specified.
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Contact name should be provided.
  given: $.info.contact
  name: info-contact-name
  severity: info
- description: Contact URL should be provided.
  given: $.info.contact
  name: info-contact-url
  severity: info
- description: License information should be provided.
  given: $.info
  name: info-license-required
  severity: warn
- description: Terms of service URL should be provided.
  given: $.info
  name: info-terms-of-service
  severity: info
- description: OpenAPI version must be 3.0.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Server entries should have descriptions.
  given: $.servers[*]
  name: servers-description
  severity: info
- description: Server URLs should use googleapis.com or google-analytics.com domains.
  given: $.servers[*].url
  name: servers-google-domain
  severity: info
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not contain query strings.
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Paths should include a version prefix (e.g., /v1beta/, /v1/, /v3/).
  given: $.paths
  name: paths-version-prefix
  severity: info
- description: Path segments (excluding parameters and custom actions) should use lowercase.
  given: $.paths
  name: paths-no-uppercase-in-segments
  severity: info
- description: Path parameters should use camelCase.
  given: $.paths
  name: paths-path-params-camelcase
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Operation descriptions should be at least 20 characters.
  given: $.paths[*][get,post,put,patch,delete].description
  name: operation-description-min-length
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs must be unique across the API.
  given: $
  name: operation-operationid-unique
  severity: error
- description: Operation IDs should use dot-notation (service.resource.action) or camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-format
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operations should have exactly one tag for clean grouping.
  given: $.paths[*][get,post,put,patch,delete].tags
  name: operation-tags-single
  severity: info
- description: Global tags array should be defined.
  given: $
  name: tags-defined
  severity: warn
- description: Tag names should use Title Case (e.g., "Account Summaries", "Data Streams").
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Query parameters should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='query')]
  name: parameter-query-camelcase
  severity: warn
- description: Path parameters should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]
  name: parameter-path-camelcase
  severity: warn
- description: Parameters must have a schema with a type defined.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].schema
  name: parameter-schema-type-required
  severity: error
- description: Pagination limit parameters should be named pageSize.
  given: $.paths[*].get.parameters[?(@.in=='query')]
  name: parameter-pagination-page-size
  severity: info
- description: Pagination cursor parameters should be named pageToken.
  given: $.paths[*].get.parameters[?(@.in=='query')]
  name: parameter-pagination-page-token
  severity: info
- description: API keys should be passed in headers, not query parameters.
  given: $.components.securitySchemes[?(@.type=='apiKey')]
  name: parameter-no-api-key-in-query
  severity: info
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Request bodies should have a description.
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: info
- description: Every operation must define a success response (2xx).
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Success responses with bodies should use application/json content type.
  given: $.paths[*][get,post,put,patch].responses.200.content
  name: response-success-json-content
  severity: warn
- description: Success responses with JSON content should have a schema defined.
  given: $.paths[*][get,post,put,patch].responses.200.content.application/json
  name: response-success-schema
  severity: warn
- description: Operations with security should define a 401 Unauthorized response.
  given: $.paths[*][get,post,put,patch,delete][?(@.security)]
  name: response-401-defined
  severity: info
- description: Operations with security should define a 403 Forbidden response.
  given: $.paths[*][get,post,put,patch,delete][?(@.security)]
  name: response-403-defined
  severity: info
- description: POST operations should define a 400 Bad Request response.
  given: $.paths[*].post.responses
  name: response-400-for-post
  severity: info
- description: Schema names should use PascalCase.
  given: $.components.schemas
  name: schema-names-pascalcase
  severity: warn
- description: Schemas should have a type defined.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should use snake_case or camelCase consistently.
  given: $.components.schemas[*].properties
  name: schema-properties-snake-case
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-top-level
  severity: info
- description: Enum values should use UPPER_CASE_WITH_UNDERSCORES.
  given: $.components.schemas[*].properties[*].enum[*]
  name: schema-enum-uppercase
  severity: info
- description: Global security should be defined or operations should have individual security.
  given: $
  name: security-global-defined
  severity: warn
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: Security schemes should have descriptions.
  given: $.components.securitySchemes[*]
  name: security-scheme-description
  severity: info
- description: OAuth2 security schemes should have properly defined flows.
  given: $.components.securitySchemes[?(@.type=='oauth2')]
  name: security-oauth2-flows
  severity: error
- description: OAuth2 flows should define scopes.
  given: $.components.securitySchemes[?(@.type=='oauth2')].flows[*]
  name: security-oauth2-scopes
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
  name: post-request-body
  severity: info
- description: PUT operations should have a request body.
  given: $.paths[*].put
  name: put-request-body
  severity: info
- description: PATCH operations should have a request body.
  given: $.paths[*].patch
  name: patch-request-body
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: External documentation link should be provided.
  given: $
  name: external-docs-encouraged
  severity: info
- description: External documentation should have a URL.
  given: $.externalDocs
  name: external-docs-url
  severity: warn
- description: Deprecated operations should explain the deprecation in their description.
  given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]
  name: deprecated-description
  severity: warn
- description: Deprecated schema properties should explain the deprecation.
  given: $.components.schemas[*].properties[?(@.deprecated==true)]
  name: schema-deprecated-description
  severity: info
- description: Success responses should include examples.
  given: $.paths[*][get,post,put,patch].responses.200.content.application/json
  name: response-examples-encouraged
  severity: info
rules_file: rules/google-analytics-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/rules/google-analytics-spectral-rules.yml
severity_counts:
  error: 18
  hint: 0
  info: 26
  warn: 22
slug: google-analytics-spectral-rules
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
- Spectral
- Linting
- API Governance
---
