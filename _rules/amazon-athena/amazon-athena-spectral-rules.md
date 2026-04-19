---
categories:
- athena
description: Spectral linting rules defining API design standards and conventions for Amazon Athena.
layout: rules
name: Amazon Athena API Rules
provider_name: Amazon Athena
provider_slug: amazon-athena
rule_count: 19
rules:
- description: StartQueryExecution must require QueryString
  given: $.components.schemas.StartQueryExecutionInput
  name: athena-query-string-required
  severity: error
- description: All operationIds must be camelCase
  given: $.paths[*][*].operationId
  name: athena-operation-id-camel-case
  severity: warn
- description: All operation summaries must start with Amazon Athena
  given: $.paths[*][*].summary
  name: athena-summary-prefix
  severity: warn
- description: All operations must have tags
  given: $.paths[*][*]
  name: athena-has-tags
  severity: warn
- description: Server URL must be fixed without variables
  given: $.servers[*]
  name: athena-server-url-fixed
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][*].responses
  name: athena-response-200
  severity: error
- description: POST operations must have a request body
  given: $.paths[*].post
  name: athena-request-body-required
  severity: error
- description: QueryExecutionId must be of type string
  given: $.components.schemas[*].properties.QueryExecutionId
  name: athena-query-execution-id-string
  severity: error
- description: NamedQueryId must be of type string
  given: $.components.schemas[*].properties.NamedQueryId
  name: athena-named-query-id-string
  severity: error
- description: WorkGroup State must use valid enum values
  given: $.components.schemas.WorkGroup.properties.State
  name: athena-work-group-state-enum
  severity: error
- description: DataCatalog Type must use valid enum values
  given: $.components.schemas.DataCatalog.properties.Type
  name: athena-data-catalog-type-enum
  severity: error
- description: QueryExecutionStatus State must use valid enum values
  given: $.components.schemas.QueryExecutionStatus.properties.State
  name: athena-query-status-state-enum
  severity: error
- description: Tag schema must define Key property
  given: $.components.schemas.Tag.properties
  name: athena-tag-key-defined
  severity: error
- description: Tag schema must define Value property
  given: $.components.schemas.Tag.properties
  name: athena-tag-value-defined
  severity: error
- description: ResultConfiguration must have OutputLocation
  given: $.components.schemas.ResultConfiguration.properties
  name: athena-result-configuration-output-location
  severity: warn
- description: EngineVersion schema must be defined
  given: $.components.schemas
  name: athena-engine-version-defined
  severity: warn
- description: ColumnInfo must define Name property
  given: $.components.schemas.ColumnInfo.properties
  name: athena-column-info-name-defined
  severity: error
- description: All examples must have x-microcks-default set to true
  given: $.paths[*][*].requestBody.content[*].examples.default
  name: athena-example-microcks-default
  severity: warn
- description: API must use sigv4 security scheme
  given: $.security[*]
  name: athena-security-sigv4
  severity: error
rules_file: rules/amazon-athena-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/rules/amazon-athena-spectral-rules.yml
severity_counts:
  error: 12
  hint: 0
  info: 0
  warn: 7
slug: amazon-athena-spectral-rules
tags:
- Amazon Athena
- SQL
- Analytics
- Serverless
- AWS
- Spectral
- Linting
- API Governance
---
