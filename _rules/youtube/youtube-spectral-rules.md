---
categories:
- deprecated
- http
- info
- list
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- request
- response
- schema
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Youtube.
layout: rules
name: Youtube API Rules
provider_name: Youtube
provider_slug: youtube
rule_count: 55
rules:
- description: Info title must be present and non-empty
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with "YouTube"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided
  given: $.info
  name: info-contact-required
  severity: warn
- description: Terms of service URL should be provided
  given: $.info
  name: info-terms-of-service
  severity: info
- description: OpenAPI version should be 3.0.x or 3.1.x
  given: $
  name: openapi-version
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Server URLs should use googleapis.com domain
  given: $.servers[*].url
  name: servers-googleapis-domain
  severity: info
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not include query strings
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: YouTube paths use camelCase for resource names
  given: $.paths
  name: paths-camel-case
  severity: warn
- description: Resource paths should use plural nouns
  given: $.paths
  name: paths-plural-resources
  severity: info
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: OperationId should follow youtube.resource.action or youtubeAnalytics.resource.action format
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-format
  severity: warn
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Youtube" prefix
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: warn
- description: Operation summaries should use Title Case
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-title-case
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Operations should have exactly one tag
  given: $.paths[*][get,post,put,patch,delete].tags
  name: operation-single-tag
  severity: info
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: Each tag should have a description
  given: $.tags[*]
  name: tags-description
  severity: warn
- description: Tag names should use PascalCase (YouTube convention)
  given: $.tags[*].name
  name: tags-pascal-case
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Parameter names should use camelCase (YouTube convention)
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-camel-case
  severity: warn
- description: Parameters should have example values
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-example
  severity: info
- description: Pagination should use pageToken and maxResults (YouTube convention)
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name=='page' || @.name=='offset' || @.name=='cursor')]
  name: parameter-pagination-naming
  severity: info
- description: Request bodies should use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json
  severity: warn
- description: Every operation must have a 2xx success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Success responses should use application/json
  given: $.paths[*][get,post,put,patch].responses[?(@property >= 200 && @property < 300)].content
  name: response-json-content
  severity: warn
- description: Responses should include named examples for Microcks compatibility
  given: $.paths[*][get,post,put,patch,delete].responses[*].content.application/json
  name: response-examples
  severity: info
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: warn
- description: Schema properties must define a type
  given: $.components.schemas[*].properties[*]
  name: schema-type-required
  severity: error
- description: Schema property names should use camelCase (YouTube convention)
  given: $.components.schemas[*].properties
  name: schema-property-camel-case
  severity: warn
- description: YouTube resource schemas should include a kind property
  given: $.components.schemas[?(@.properties.etag)].properties
  name: schema-kind-property
  severity: info
- description: YouTube resource schemas should include an etag property
  given: $.components.schemas[?(@.properties.kind)].properties
  name: schema-etag-property
  severity: info
- description: Schema properties should have example values
  given: $.components.schemas[*].properties[*]
  name: schema-property-example
  severity: info
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: Security schemes must be defined in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: YouTube APIs should use OAuth 2.0 authentication
  given: $.components.securitySchemes
  name: security-oauth2-scheme
  severity: warn
- description: YouTube APIs should support API key authentication for read operations
  given: $.components.securitySchemes
  name: security-api-key-scheme
  severity: info
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: DELETE operations must not have a request body
  given: $.paths[*].delete
  name: http-delete-no-body
  severity: error
- description: POST operations should have a request body
  given: $.paths[*].post
  name: http-post-has-body
  severity: warn
- description: PUT operations should have a request body
  given: $.paths[*].put
  name: http-put-has-body
  severity: warn
- description: Operations should have x-microcks-operation for mock server compatibility
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Deprecated operations should have a description explaining the deprecation
  given: $.paths[*][get,post,put,patch,delete][?(@.deprecated==true)]
  name: deprecated-documented
  severity: warn
- description: List responses should contain an items array (YouTube convention)
  given: $.components.schemas[?(@.properties.nextPageToken)].properties
  name: list-response-items-array
  severity: info
rules_file: rules/youtube-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/youtube/refs/heads/main/rules/youtube-spectral-rules.yml
severity_counts:
  error: 22
  hint: 0
  info: 13
  warn: 20
slug: youtube-spectral-rules
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
- Spectral
- Linting
- API Governance
---
