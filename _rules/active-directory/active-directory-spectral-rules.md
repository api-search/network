---
categories:
- ad
description: Spectral linting rules defining API design standards and conventions for Microsoft Active Directory.
layout: rules
name: Microsoft Active Directory API Rules
provider_name: Microsoft Active Directory
provider_slug: active-directory
rule_count: 33
rules:
- description: Microsoft Graph APIs must use graph.microsoft.com as the server URL
  given: $.servers[*].url
  name: ad-graph-server-url
  severity: error
- description: All Microsoft Graph servers must use HTTPS
  given: $.servers[*].url
  name: ad-https-only
  severity: error
- description: Every operation must have a non-empty summary
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-operation-summary-required
  severity: error
- description: Operation summaries must use Title Case (each word capitalized)
  given: $.paths[*][get,post,patch,put,delete].summary
  name: ad-operation-summary-title-case
  severity: warn
- description: Operation summaries must be prefixed with 'Active Directory'
  given: $.paths[*][get,post,patch,put,delete].summary
  name: ad-operation-summary-prefix
  severity: warn
- description: Every operation should have a detailed description
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-operation-description-required
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-operation-id-required
  severity: error
- description: Operation IDs must use kebab-case
  given: $.paths[*][get,post,patch,put,delete].operationId
  name: ad-operation-id-kebab-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-operation-tags-required
  severity: warn
- description: All tags used in operations must be declared in the global tags list
  given: $.paths[*][get,post,patch,put,delete].tags[*]
  name: ad-tags-defined
  severity: warn
- description: APIs must declare an OAuth2 security scheme
  given: $.components.securitySchemes
  name: ad-oauth2-security-scheme
  severity: error
- description: Every operation must declare security requirements
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-security-required
  severity: error
- description: GET operations must return a 200 response
  given: $.paths[*].get
  name: ad-get-200-response
  severity: error
- description: POST operations creating resources should return 201
  given: $.paths[*].post
  name: ad-post-201-response
  severity: warn
- description: DELETE operations must return 204 No Content
  given: $.paths[*].delete
  name: ad-delete-204-response
  severity: error
- description: PATCH operations must return 204 No Content
  given: $.paths[*].patch
  name: ad-patch-204-response
  severity: warn
- description: All operations must define a 401 Unauthorized response
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-401-response
  severity: warn
- description: List operations should support $filter OData parameter
  given: $.paths[?(!@property.match(/{[^}]+}$/))].get
  name: ad-list-filter-param
  severity: warn
- description: List operations should support $top pagination parameter
  given: $.paths[*].get.parameters[*]
  name: ad-list-top-param
  severity: info
- description: POST operations must define a request body
  given: $.paths[*].post
  name: ad-post-request-body
  severity: error
- description: PATCH operations must define a request body
  given: $.paths[*].patch
  name: ad-patch-request-body
  severity: error
- description: Request bodies must use application/json content type
  given: $.paths[*][post,patch,put].requestBody.content
  name: ad-request-body-json
  severity: error
- description: ID properties should be documented as UUID format
  given: $.components.schemas[*].properties.id
  name: ad-schema-id-uuid
  severity: warn
- description: All schemas must have descriptions
  given: $.components.schemas[*]
  name: ad-schemas-have-descriptions
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: ad-properties-have-descriptions
  severity: info
- description: API paths must use lowercase letters
  given: $.paths[*]~
  name: ad-path-lowercase
  severity: error
- description: API paths must not end with a trailing slash
  given: $.paths[*]~
  name: ad-path-no-trailing-slash
  severity: error
- description: Path parameters for resource IDs should use descriptive names ending in 'Id'
  given: $.paths[*][get,patch,delete].parameters[?(@.in=='path')].name
  name: ad-path-id-parameter
  severity: warn
- description: API info must include a contact object
  given: $.info
  name: ad-info-contact
  severity: warn
- description: API info must include license information
  given: $.info
  name: ad-info-license
  severity: warn
- description: API info should include terms of service URL
  given: $.info
  name: ad-info-terms-of-service
  severity: info
- description: Successful responses must include application/json content type
  given: $.paths[*][get,post].responses[200,201].content
  name: ad-response-json-content
  severity: error
- description: Operations should include x-microcks-operation for mock generation
  given: $.paths[*][get,post,patch,put,delete]
  name: ad-microcks-operation
  severity: info
rules_file: rules/active-directory-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/active-directory/refs/heads/main/rules/active-directory-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 4
  warn: 15
slug: active-directory-spectral-rules
tags:
- Active Directory
- Authentication
- Authorization
- Directory Services
- Identity Management
- Microsoft Entra
- Zero Trust
- Spectral
- Linting
- API Governance
---
