---
categories:
- delete
- examples
- get
- info
- 'no'
- oauth2
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
- tag
description: Spectral linting rules defining API design standards and conventions for Salesforce Automation.
layout: rules
name: Salesforce Automation API Rules
provider_name: Salesforce Automation
provider_slug: salesforce-automation
rule_count: 37
rules:
- description: Info object must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: Info title should start with "Salesforce".
  given: $.info.title
  name: info-title-salesforce-prefix
  severity: warn
- description: Info object must have a description.
  given: $.info
  name: info-description-required
  severity: error
- description: Info description should be at least 50 characters.
  given: $.info.description
  name: info-description-min-length
  severity: warn
- description: Info object must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: Info object should have contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: Info object should include license information.
  given: $.info
  name: info-license-required
  severity: info
- description: OpenAPI version should be 3.1.0.
  given: $
  name: openapi-version
  severity: warn
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: warn
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Paths must not include query strings.
  given: $.paths
  name: paths-no-query-strings
  severity: error
- description: Path segments should use kebab-case or camelCase (no underscores).
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: operationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-operationid-camel-case
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Salesforce".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-salesforce-prefix
  severity: warn
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags should have descriptions.
  given: $.tags[*]
  name: tag-description
  severity: info
- description: Every parameter must have a description.
  given: $.paths[*][*].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every parameter must have a schema.
  given: $.paths[*][*].parameters[*]
  name: parameter-schema-required
  severity: error
- description: Request bodies should use application/json content type.
  given: $.paths[*][post,put,patch].requestBody.content
  name: request-body-json-content
  severity: warn
- description: Every operation must have at least one success response (2xx).
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Authenticated endpoints should define a 401 response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: info
- description: Schemas must define a type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Top-level schemas should have descriptions.
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Global security must be defined.
  given: $
  name: security-defined
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: error
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
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Schema properties should include example values.
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
- description: Salesforce APIs should use OAuth 2.0 authentication.
  given: $.components.securitySchemes
  name: oauth2-security
  severity: warn
rules_file: rules/salesforce-automation-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation/refs/heads/main/rules/salesforce-automation-spectral-rules.yml
severity_counts:
  error: 18
  hint: 0
  info: 7
  warn: 12
slug: salesforce-automation-spectral-rules
tags:
- Automation
- Cloud
- CRM
- Enterprise
- Sales
- Spectral
- Linting
- API Governance
---
