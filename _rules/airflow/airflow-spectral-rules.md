---
categories:
- dag
- delete
- get
- info
- microcks
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Apache Airflow.
layout: rules
name: Apache Airflow API Rules
provider_name: Apache Airflow
provider_slug: airflow
rule_count: 24
rules:
- description: Info title must be defined.
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be defined.
  given: $.info
  name: info-description-required
  severity: warn
- description: Info version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: OpenAPI version must be 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: Servers must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Stable API paths should start with /api/v2/.
  given: $.paths[*]~
  name: paths-api-v2-prefix
  severity: info
- description: Path segments should use snake_case or kebab-case.
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with "Airflow".
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-starts-with-airflow
  severity: info
- description: All parameters should have a description.
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have at least one success response.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Operations should document 401 Unauthorized responses.
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-documented
  severity: info
- description: Top-level schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-recommended
  severity: info
- description: Schema property names should use snake_case.
  given: $.components.schemas[*].properties[*]~
  name: schema-properties-snake-case
  severity: info
- description: Security schemes should be defined.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations should not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should return 204 No Content.
  given: $.paths[*].delete.responses
  name: delete-returns-204
  severity: info
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include x-microcks-operation for mock compatibility.
  given: $.paths[*][get,post,put,patch,delete]
  name: microcks-operation-extension
  severity: info
- description: DAG endpoints are core to Airflow — they must be documented.
  given: $.paths
  name: dag-resource-required
  severity: info
rules_file: rules/airflow-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/rules/airflow-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 9
  warn: 7
slug: airflow-spectral-rules
tags:
- Workflow Orchestration
- Data Pipeline
- Open Source
- Apache
- DAG
- Scheduling
- ETL
- Data Engineering
- Spectral
- Linting
- API Governance
---
