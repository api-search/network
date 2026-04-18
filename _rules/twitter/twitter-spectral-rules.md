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
- paths
- post
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for X (Twitter).
layout: rules
name: X (Twitter) API Rules
provider_name: X (Twitter)
provider_slug: twitter
rule_count: 53
rules:
- description: API title must be present and non-empty.
  given: $.info
  name: info-title-required
  severity: error
- description: API title should follow the pattern "X API" or "X [Name] API".
  given: $.info.title
  name: info-title-format
  severity: warn
- description: API description must be present and meaningful.
  given: $.info
  name: info-description-required
  severity: error
- description: API description should be at least 50 characters.
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
- description: License information should be provided.
  given: $.info
  name: info-license-required
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
- description: Server URLs should use api.x.com or ads-api.x.com domains.
  given: $.servers[*].url
  name: servers-x-domain
  severity: info
- description: Paths should start with a version prefix (e.g., /2/).
  given: $.paths
  name: paths-version-prefix
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not contain query strings.
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Path segments should use snake_case (the dominant X API convention).
  given: $.paths
  name: paths-snake-case
  severity: info
- description: Path parameters should use snake_case.
  given: $.paths
  name: paths-path-params-snake-case
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs must be unique across the API.
  given: $
  name: operation-operationid-unique
  severity: error
- description: Operation IDs should use camelCase with verb prefixes (e.g., getTweets, createPost, deleteUser).
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Global tags array should be defined.
  given: $
  name: tags-defined
  severity: warn
- description: Tag names should use Title Case (e.g., "Direct Messages", "Community Notes").
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameter names should use snake_case (the dominant X API convention).
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-snake-case
  severity: warn
- description: Parameters must have a schema with a type defined.
  given: $.paths[*][get,post,put,patch,delete].parameters[*].schema
  name: parameter-schema-type
  severity: error
- description: Pagination limit parameters should be named max_results.
  given: $.paths[*].get.parameters[?(@.in=='query')]
  name: parameter-pagination-max-results
  severity: info
- description: Pagination cursor parameters should use next_token or pagination_token.
  given: $.paths[*].get.parameters[?(@.in=='query')]
  name: parameter-pagination-token
  severity: info
- description: Expansion parameters should be named expansions for including related objects.
  given: $.paths[*].get.parameters[?(@.in=='query')]
  name: parameter-expansions
  severity: info
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must define a success response (2xx).
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should define a default error response for unexpected errors.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-default-error
  severity: info
- description: Success responses should use application/json content type.
  given: $.paths[*][get,post,put,patch].responses.200.content
  name: response-success-json
  severity: warn
- description: Schema names should use PascalCase.
  given: $.components.schemas
  name: schema-names-pascalcase
  severity: warn
- description: Schemas should have a type defined.
  given: $.components.schemas[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should use snake_case (the dominant X API convention).
  given: $.components.schemas[*].properties
  name: schema-properties-snake-case
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-top-level
  severity: info
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: A BearerToken security scheme should be defined for app-only auth.
  given: $.components.securitySchemes
  name: security-bearer-token
  severity: info
- description: An OAuth2UserToken security scheme should be defined for user context auth.
  given: $.components.securitySchemes
  name: security-oauth2-user
  severity: info
- description: Every operation should define its security requirements.
  given: $.paths[*][get,post,put,patch,delete]
  name: security-operation-defined
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
- description: Success responses should use a data wrapper object for consistency.
  given: $.paths[*][get,post].responses.200.content.application/json.schema.properties
  name: response-data-wrapper
  severity: info
- description: Error responses should include an errors array.
  given: $.components.schemas[?(@.properties.errors)]
  name: response-errors-array
  severity: info
- description: Field selection parameters should use dot notation (e.g., tweet.fields, user.fields, media.fields).
  given: $.paths[*].get.parameters[?(@.name)]
  name: parameter-fields-dot-notation
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: External documentation link should be provided.
  given: $
  name: external-docs-encouraged
  severity: info
- description: Deprecated operations should explain the deprecation in their description.
  given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]
  name: deprecated-description
  severity: warn
rules_file: rules/twitter-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/twitter/refs/heads/main/rules/twitter-spectral-rules.yml
severity_counts:
  error: 17
  hint: 0
  info: 18
  warn: 18
slug: twitter-spectral-rules
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
- Spectral
- Linting
- API Governance
---
