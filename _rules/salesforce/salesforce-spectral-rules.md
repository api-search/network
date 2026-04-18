---
categories:
- http
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- response
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Salesforce.
layout: rules
name: Salesforce API Rules
provider_name: Salesforce
provider_slug: salesforce
rule_count: 21
rules:
- description: Info title must be present and non-empty
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be specified
  given: $.info
  name: info-version-required
  severity: error
- description: Contact information should be provided
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI version should be 3.x
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
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Every parameter must have a schema
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must have a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: DELETE operations must not have a request body
  given: $.paths[*].delete
  name: http-delete-no-body
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Operations should have x-microcks-operation
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
rules_file: rules/salesforce-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/rules/salesforce-spectral-rules.yml
severity_counts:
  error: 19
  hint: 0
  info: 1
  warn: 1
slug: salesforce-spectral-rules
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
- Spectral
- Linting
- API Governance
---
