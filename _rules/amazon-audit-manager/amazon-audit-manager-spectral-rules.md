---
categories:
- audit
description: Spectral linting rules defining API design standards and conventions for Amazon Audit Manager.
layout: rules
name: Amazon Audit Manager API Rules
provider_name: Amazon Audit Manager
provider_slug: amazon-audit-manager
rule_count: 15
rules:
- description: All operationIds must be camelCase
  given: $.paths[*][*].operationId
  name: audit-manager-operation-id-camel-case
  severity: warn
- description: All operation summaries must start with Amazon Audit Manager
  given: $.paths[*][*].summary
  name: audit-manager-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][*]
  name: audit-manager-has-tags
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][*].responses
  name: audit-manager-response-200
  severity: error
- description: CreateAssessmentRequest must require name
  given: $.components.schemas.CreateAssessmentRequest
  name: audit-manager-assessment-name-required
  severity: error
- description: AssessmentMetadata Status must use valid enum values
  given: $.components.schemas.AssessmentMetadata.properties.status
  name: audit-manager-assessment-status-enum
  severity: error
- description: AssessmentReport status must use valid enum values
  given: $.components.schemas.AssessmentReport.properties.status
  name: audit-manager-assessment-report-status-enum
  severity: error
- description: Framework type must use valid enum values
  given: $.components.schemas.Framework.properties.type
  name: audit-manager-framework-type-enum
  severity: error
- description: Control type must use valid enum values
  given: $.components.schemas.Control.properties.type
  name: audit-manager-control-type-enum
  severity: error
- description: Role roleType must use valid enum values
  given: $.components.schemas.Role.properties.roleType
  name: audit-manager-role-type-enum
  severity: error
- description: AssessmentReportsDestination type must use valid enum values
  given: $.components.schemas.AssessmentReportsDestination.properties.destinationType
  name: audit-manager-destination-type-enum
  severity: error
- description: API must use sigv4 security scheme
  given: $.security[*]
  name: audit-manager-security-sigv4
  severity: error
- description: Server URL must be fixed without variables
  given: $.servers[*]
  name: audit-manager-server-url-fixed
  severity: warn
- description: All examples must have x-microcks-default set to true
  given: $.paths[*][*].responses[*].content[*].examples.default
  name: audit-manager-example-microcks-default
  severity: warn
- description: Delegation status must use valid enum values
  given: $.components.schemas.Delegation.properties.status
  name: audit-manager-delegation-status-enum
  severity: error
rules_file: rules/amazon-audit-manager-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-audit-manager/refs/heads/main/rules/amazon-audit-manager-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 0
  warn: 5
slug: amazon-audit-manager-spectral-rules
tags:
- Amazon Audit Manager
- Compliance
- Audit
- Risk Management
- AWS
- Spectral
- Linting
- API Governance
---
