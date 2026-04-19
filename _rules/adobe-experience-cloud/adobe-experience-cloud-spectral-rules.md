---
categories:
- delete
- examples
- get
- info
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
description: Spectral linting rules defining API design standards and conventions for Adobe Experience Cloud.
layout: rules
name: Adobe Experience Cloud API Rules
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
rule_count: 31
rules:
- description: API title must start with "Adobe"
  given: $.info.title
  name: info-title-adobe-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API must declare a version
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact details
  given: $.info
  name: info-contact-required
  severity: warn
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3
  severity: error
- description: API must define servers
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-required
  severity: error
- description: Each server should have a description
  given: $.servers[*]
  name: servers-description-required
  severity: warn
- description: Paths must not end with a trailing slash
  given: $.paths[*]~
  name: paths-no-trailing-slash
  severity: warn
- description: Paths should use valid URL characters
  given: $.paths[*]~
  name: paths-valid-chars
  severity: info
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with an Adobe product name
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-adobe-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camelcase
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: API should define global tags
  given: $
  name: tags-defined
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: error
- description: All parameters must have a schema
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should have descriptions
  given: $.paths[*][post,put,patch].requestBody
  name: request-body-description
  severity: warn
- description: Every operation must define at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Authenticated operations should define 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-error-401
  severity: warn
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level component schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: warn
- description: Schemas should define a type
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: API must define security schemes in components
  given: $.components
  name: security-schemes-defined
  severity: error
- description: API should define global security
  given: $
  name: security-global-required
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Responses should include examples
  given: $.paths[*][get,post,put,patch,delete].responses[*].content[*]
  name: examples-encouraged
  severity: info
rules_file: rules/adobe-experience-cloud-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/rules/adobe-experience-cloud-spectral-rules.yml
severity_counts:
  error: 16
  hint: 0
  info: 2
  warn: 13
slug: adobe-experience-cloud-spectral-rules
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
- Spectral
- Linting
- API Governance
---
