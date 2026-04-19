---
categories:
- aurora
description: Spectral linting rules defining API design standards and conventions for Amazon Aurora.
layout: rules
name: Amazon Aurora API Rules
provider_name: Amazon Aurora
provider_slug: amazon-aurora
rule_count: 14
rules:
- description: All operationIds must be camelCase
  given: $.paths[*][*].operationId
  name: aurora-operation-id-camel-case
  severity: warn
- description: All operation summaries must start with Amazon Aurora
  given: $.paths[*][*].summary
  name: aurora-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][*]
  name: aurora-has-tags
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][*].responses
  name: aurora-response-200
  severity: error
- description: CreateDBClusterInput must require DBClusterIdentifier and Engine
  given: $.components.schemas.CreateDBClusterInput
  name: aurora-create-cluster-required
  severity: error
- description: Engine must use valid enum values for Aurora
  given: $.components.schemas.CreateDBClusterInput.properties.Engine
  name: aurora-engine-enum
  severity: error
- description: CreateDBClusterEndpoint EndpointType must use valid enum values
  given: $.components.schemas.CreateDBClusterEndpointInput.properties.EndpointType
  name: aurora-endpoint-type-enum
  severity: error
- description: API must use sigv4 security scheme
  given: $.security[*]
  name: aurora-security-sigv4
  severity: error
- description: Server URL must be fixed without variables
  given: $.servers[*]
  name: aurora-server-url-fixed
  severity: warn
- description: All examples must have x-microcks-default set to true
  given: $.paths[*][*].responses[*].content[*].examples.default
  name: aurora-example-microcks-default
  severity: warn
- description: DBCluster DBClusterIdentifier must be string type
  given: $.components.schemas.DBCluster.properties.DBClusterIdentifier
  name: aurora-db-cluster-identifier-string
  severity: error
- description: Filter Values must be an array
  given: $.components.schemas.Filter.properties.Values
  name: aurora-filter-values-array
  severity: error
- description: GlobalCluster GlobalClusterIdentifier must be string type
  given: $.components.schemas.GlobalCluster.properties.GlobalClusterIdentifier
  name: aurora-global-cluster-identifier-string
  severity: error
- description: DBClusterSnapshot Status must be defined
  given: $.components.schemas.DBClusterSnapshot.properties
  name: aurora-snapshot-status-defined
  severity: warn
rules_file: rules/amazon-aurora-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/rules/amazon-aurora-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 0
  warn: 6
slug: amazon-aurora-spectral-rules
tags:
- Amazon Aurora
- MySQL
- PostgreSQL
- Relational Database
- AWS
- Spectral
- Linting
- API Governance
---
