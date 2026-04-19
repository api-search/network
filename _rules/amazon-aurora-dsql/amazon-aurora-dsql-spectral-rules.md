---
categories:
- aurora
description: Spectral linting rules defining API design standards and conventions for Amazon Aurora DSQL.
layout: rules
name: Amazon Aurora DSQL API Rules
provider_name: Amazon Aurora DSQL
provider_slug: amazon-aurora-dsql
rule_count: 10
rules:
- description: All operationIds must be camelCase
  given: $.paths[*][*].operationId
  name: aurora-dsql-operation-id-camel-case
  severity: warn
- description: All operation summaries must start with Amazon Aurora DSQL
  given: $.paths[*][*].summary
  name: aurora-dsql-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][*]
  name: aurora-dsql-has-tags
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][*].responses
  name: aurora-dsql-response-200
  severity: error
- description: ClusterStatus must use valid enum values
  given: $.components.schemas.ClusterStatus
  name: aurora-dsql-cluster-status-enum
  severity: error
- description: API must use sigv4 security scheme
  given: $.security[*]
  name: aurora-dsql-security-sigv4
  severity: error
- description: Server URL must be fixed without variables
  given: $.servers[*]
  name: aurora-dsql-server-url-fixed
  severity: warn
- description: All examples must have x-microcks-default set to true
  given: $.paths[*][*].responses[*].content[*].examples.default
  name: aurora-dsql-example-microcks-default
  severity: warn
- description: CreateMultiRegionClustersInput must require linkedRegionList
  given: $.components.schemas.CreateMultiRegionClustersInput
  name: aurora-dsql-multi-region-linked-list-required
  severity: error
- description: ClusterSummary identifier must be string type
  given: $.components.schemas.ClusterSummary.properties.identifier
  name: aurora-dsql-cluster-identifier-string
  severity: error
rules_file: rules/amazon-aurora-dsql-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/rules/amazon-aurora-dsql-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 0
  warn: 5
slug: amazon-aurora-dsql-spectral-rules
tags:
- Amazon Aurora DSQL
- Distributed SQL
- PostgreSQL
- Serverless
- AWS
- Spectral
- Linting
- API Governance
---
