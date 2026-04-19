---
categories:
- get
- info
- list
- openapi
- operation
- parameter
- paths
- response
- responses
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Allianz Engagement Survey.
layout: rules
name: Allianz Engagement Survey API Rules
provider_name: Allianz Engagement Survey
provider_slug: allianz-engagement-survey
rule_count: 24
rules:
- description: API title must start with "Allianz"
  given: $.info.title
  name: info-title-allianz-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must define a version
  given: $.info
  name: info-version-required
  severity: error
- description: Specs must use OpenAPI 3.x
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Path segments must use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Summaries must start with "Allianz Engagement Survey"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-allianz-prefix
  severity: warn
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: operationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
- description: Parameter names should use snake_case
  given: $.paths[*][get,post,put,patch,delete].parameters[*].name
  name: parameter-snake-case
  severity: warn
- description: List operations should support limit and offset parameters
  given: $.paths[*].get.operationId
  name: list-operations-pagination
  severity: info
- description: Every operation must define a success response
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Operations should define a 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Response descriptions should note anonymization for response endpoints
  given: $.paths[*].get.description
  name: responses-anonymized
  severity: info
rules_file: rules/allianz-engagement-survey-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/allianz-engagement-survey/refs/heads/main/rules/allianz-engagement-survey-spectral-rules.yml
severity_counts:
  error: 15
  hint: 0
  info: 2
  warn: 7
slug: allianz-engagement-survey-spectral-rules
tags:
- Analytics
- Enterprise
- Human Resources
- Insurance
- Surveys
- Employee Experience
- Spectral
- Linting
- API Governance
---
