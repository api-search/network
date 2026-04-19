---
categories:
- examples
- http
- info
- 'no'
- openapi
- operation
- parameter
- paths
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Managed Grafana.
layout: rules
name: Amazon Managed Grafana API Rules
provider_name: Amazon Managed Grafana
provider_slug: amazon-managed-grafana
rule_count: 18
rules:
- description: Info title must be present
  given: $.info
  name: info-title-required
  severity: error
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: warn
- description: API version must be defined
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.0.x
  given: $
  name: openapi-version
  severity: error
- description: Servers must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs should use HTTPS
  given: $.servers[*]
  name: servers-https
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: warn
- description: Operation summaries should start with "Amazon Managed Grafana"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: info
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-required
  severity: error
- description: GET operations should not have request bodies
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: Schema properties should include examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/amazon-managed-grafana-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-grafana/refs/heads/main/rules/amazon-managed-grafana-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 4
  warn: 7
slug: amazon-managed-grafana-spectral-rules
tags:
- AWS
- Dashboards
- Monitoring
- Observability
- Visualization
- Spectral
- Linting
- API Governance
---
