---
categories:
- healthlake
description: Spectral linting rules defining API design standards and conventions for Amazon HealthLake.
layout: rules
name: Amazon HealthLake API Rules
provider_name: Amazon HealthLake
provider_slug: amazon-healthlake
rule_count: 8
rules:
- description: All operations must have a summary
  given: $.paths.*[get,post,put,patch,delete]
  name: healthlake-operation-summary
  severity: error
- description: All operations must have an operationId
  given: $.paths.*[get,post,put,patch,delete]
  name: healthlake-operation-id
  severity: error
- description: All operations should have tags
  given: $.paths.*[get,post,put,patch,delete]
  name: healthlake-operation-tags
  severity: warn
- description: All operations should have a 200 response
  given: $.paths.*[get,post,put,patch,delete].responses
  name: healthlake-response-200
  severity: warn
- description: Schema components should have descriptions
  given: $.components.schemas.*
  name: healthlake-schema-description
  severity: info
- description: FHIR datastore operations should follow naming conventions
  given: $.paths.*[get,post,put,patch,delete]
  name: healthlake-fhir-datastore
  severity: info
- description: HIPAA-eligible service must document security requirements
  given: $.components.securitySchemes
  name: healthlake-hipaa-security
  severity: error
- description: Job operations should have consistent naming patterns
  given: $.paths.*[get,post,put,patch,delete][?(@property == 'operationId' && @.match('Job'))]
  name: healthlake-job-operations
  severity: info
rules_file: rules/amazon-healthlake-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-healthlake/refs/heads/main/rules/amazon-healthlake-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 3
  warn: 2
slug: amazon-healthlake-spectral-rules
tags:
- AWS
- FHIR
- Health Data
- Healthcare
- HIPAA
- Cloud Computing
- Spectral
- Linting
- API Governance
---
