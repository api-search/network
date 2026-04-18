---
categories:
- get
- info
- 'no'
- operation
- parameter
- paths
- response
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Microsoft Azure Functions.
layout: rules
name: Microsoft Azure Functions API Rules
provider_name: Microsoft Azure Functions
provider_slug: microsoft-azure-functions
rule_count: 19
rules:
- description: API title must be present.
  given: $.info
  name: info-title-required
  severity: error
- description: API description must be present.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be specified.
  given: $.info
  name: info-version-required
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS.
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: Paths must not have trailing slashes.
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Path segments should use camelCase (Azure convention).
  given: $.paths
  name: paths-camelcase
  severity: info
- description: Every operation must have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operation IDs must be unique.
  given: $
  name: operation-operationid-unique
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Tag names should use Title Case.
  given: $.tags[*].name
  name: tags-title-case
  severity: info
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Azure APIs should include api-version as a query parameter.
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.name=='api-version')]
  name: parameter-api-version
  severity: info
- description: Every operation must define a success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes should be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions must not be empty.
  given: $..description
  name: no-empty-descriptions
  severity: error
rules_file: rules/azure-functions-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-functions/refs/heads/main/rules/azure-functions-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 3
  warn: 2
slug: azure-functions-spectral-rules
tags:
- Azure
- Cloud
- Compute
- Event-Driven
- Microsoft
- Serverless
- Spectral
- Linting
- API Governance
---
