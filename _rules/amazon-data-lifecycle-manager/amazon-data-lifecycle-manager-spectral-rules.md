---
categories:
- arn
- info
- 'no'
- openapi
- operation
- paths
- policy
- response
- schema
- security
- servers
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon Data Lifecycle Manager.
layout: rules
name: Amazon Data Lifecycle Manager API Rules
provider_name: Amazon Data Lifecycle Manager
provider_slug: amazon-data-lifecycle-manager
rule_count: 21
rules:
- description: API title must start with "Amazon Data Lifecycle Manager"
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x
  given: $
  name: openapi-version-3x
  severity: error
- description: Servers array must be defined
  given: $
  name: servers-defined
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https-only
  severity: error
- description: DLM API paths should reference /policies or /tags resources
  given: $.paths[*]~
  name: paths-resource-based
  severity: info
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: Tags array should be defined globally
  given: $
  name: tags-defined
  severity: warn
- description: Each tag must have a description
  given: $.tags[*]
  name: tag-description-required
  severity: warn
- description: All operations must have at least one 2xx response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Top-level schemas should have a description
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-defined
  severity: error
- description: Descriptions must not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: error
- description: Policy State field should use standard enum values
  given: $.components.schemas.*.properties.State
  name: policy-state-enum
  severity: info
- description: ARN fields should have descriptions documenting them as unique identifiers
  given: $.components.schemas[*].properties[?(@property =~ /Arn/)].description
  name: arn-fields-documented
  severity: info
rules_file: rules/amazon-data-lifecycle-manager-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-data-lifecycle-manager/refs/heads/main/rules/amazon-data-lifecycle-manager-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 3
  warn: 5
slug: amazon-data-lifecycle-manager-spectral-rules
tags:
- AWS
- Backup
- EBS Snapshots
- Lifecycle Management
- Storage
- Automation
- Compliance
- Spectral
- Linting
- API Governance
---
