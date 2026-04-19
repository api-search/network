---
categories:
- healthomics
description: Spectral linting rules defining API design standards and conventions for Amazon HealthOmics.
layout: rules
name: Amazon HealthOmics API Rules
provider_name: Amazon HealthOmics
provider_slug: amazon-healthomics
rule_count: 8
rules:
- description: All operations must have a summary
  given: $.paths.*[get,post,put,patch,delete]
  name: healthomics-operation-summary
  severity: error
- description: All operations must have an operationId
  given: $.paths.*[get,post,put,patch,delete]
  name: healthomics-operation-id
  severity: error
- description: All operations should have tags
  given: $.paths.*[get,post,put,patch,delete]
  name: healthomics-operation-tags
  severity: warn
- description: All operations should have a 200 response
  given: $.paths.*[get,post,put,patch,delete].responses
  name: healthomics-response-200
  severity: warn
- description: Schema components should have descriptions
  given: $.components.schemas.*
  name: healthomics-schema-description
  severity: info
- description: Workflow operations should follow consistent naming
  given: $.paths.*[get,post,put,patch,delete]
  name: healthomics-workflow-operations
  severity: info
- description: Store operations should reference appropriate schemas
  given: $.paths.*[get,post,put,patch,delete][?(@property == 'operationId' && @.match('Store'))]
  name: healthomics-store-naming
  severity: info
- description: HealthOmics must document security requirements
  given: $.components.securitySchemes
  name: healthomics-security
  severity: error
rules_file: rules/amazon-healthomics-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-healthomics/refs/heads/main/rules/amazon-healthomics-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 3
  warn: 2
slug: amazon-healthomics-spectral-rules
tags:
- AWS
- Bioinformatics
- Genomics
- Healthcare
- Life Sciences
- Cloud Computing
- Spectral
- Linting
- API Governance
---
