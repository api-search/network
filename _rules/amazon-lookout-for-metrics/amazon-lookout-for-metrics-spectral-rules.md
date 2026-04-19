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
description: Spectral linting rules defining API design standards and conventions for Amazon Lookout for Metrics.
layout: rules
name: Amazon Lookout for Metrics API Rules
provider_name: Amazon Lookout for Metrics
provider_slug: amazon-lookout-for-metrics
rule_count: 24
rules:
- description: Info title must be present and start with "Amazon Lookout for Metrics"
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
- description: Operation summaries should start with "Amazon Lookout for Metrics"
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: info
- description: Every operation should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Path segments should use PascalCase (AWS convention for action-based paths)
  given: $.paths
  name: paths-kebab-case
  severity: info
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must have at least one 2xx response
  given: $.paths[*][post]
  name: response-success-required
  severity: error
- description: All responses must have a description
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: warn
- description: Operations should document 401 Unauthorized responses
  given: $.paths[*][post]
  name: response-error-401
  severity: info
- description: Top-level schemas in components should have descriptions
  given: $.components.schemas[*]
  name: schema-description
  severity: info
- description: Schema properties should define a type
  given: $.components.schemas[*].properties[*]
  name: schema-property-type
  severity: warn
- description: Security schemes must be defined
  given: $.components
  name: security-schemes-required
  severity: error
- description: AWS Signature Version 4 security should be documented
  given: $.components.securitySchemes
  name: security-aws-sigv4
  severity: warn
- description: GET operations should not have request bodies
  given: $.paths[*].get
  name: http-get-no-body
  severity: error
- description: DELETE operations should not have request bodies
  given: $.paths[*].delete
  name: http-delete-no-body
  severity: warn
- description: Descriptions should not be empty strings
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Schema properties should include examples
  given: $.components.schemas[*].properties[*]
  name: examples-encouraged
  severity: info
rules_file: rules/amazon-lookout-for-metrics-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-lookout-for-metrics/refs/heads/main/rules/amazon-lookout-for-metrics-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 5
  warn: 11
slug: amazon-lookout-for-metrics-spectral-rules
tags:
- Anomaly Detection
- AWS
- Business Intelligence
- Machine Learning
- Metrics
- Monitoring
- Spectral
- Linting
- API Governance
---
