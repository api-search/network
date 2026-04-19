---
categories:
- absentify
description: Spectral linting rules defining API design standards and conventions for Absentify.
layout: rules
name: Absentify API Rules
provider_name: Absentify
provider_slug: absentify
rule_count: 15
rules:
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: absentify-operation-must-have-summary
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: absentify-operation-must-have-description
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: absentify-operation-must-have-operation-id
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: absentify-operation-must-have-tags
  severity: warn
- description: Operation summaries should be in Title Case
  given: $.paths[*][get,post,put,patch,delete].summary
  name: absentify-summary-title-case
  severity: warn
- description: All parameters must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: absentify-parameters-must-have-description
  severity: warn
- description: Request body content must define a schema
  given: $.paths[*][post,put,patch].requestBody.content[*]
  name: absentify-request-body-must-have-schema
  severity: error
- description: Successful responses should define a schema
  given: $.paths[*][get,post,put,patch,delete].responses[200,201]
  name: absentify-response-must-have-schema
  severity: warn
- description: Operations should use ApiKeyAuth security
  given: $.paths[*][get,post,put,patch,delete]
  name: absentify-security-must-use-api-key
  severity: warn
- description: Schema properties must define a type
  given: $.components.schemas[*].properties[*]
  name: absentify-schema-properties-must-have-type
  severity: warn
- description: API info must have contact information
  given: $.info
  name: absentify-info-must-have-contact
  severity: warn
- description: API info must have license information
  given: $.info
  name: absentify-info-must-have-license
  severity: info
- description: At least one server must be defined
  given: $
  name: absentify-server-must-be-defined
  severity: error
- description: Components section should define reusable schemas
  given: $.components
  name: absentify-components-schemas-must-exist
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: absentify-paths-must-use-kebab-case
  severity: info
rules_file: rules/absentify-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/absentify/refs/heads/main/rules/absentify-spectral-rules.yml
severity_counts:
  error: 4
  hint: 0
  info: 2
  warn: 9
slug: absentify-spectral-rules
tags:
- Absence Management
- HR
- Leave Management
- Microsoft Teams
- Human Resources
- Spectral
- Linting
- API Governance
---
