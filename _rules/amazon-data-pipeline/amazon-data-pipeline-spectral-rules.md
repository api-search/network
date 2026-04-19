---
categories:
- action
- all
- info
- 'no'
- openapi
- operation
- pipeline
- request
- response
- schema
- security
- servers
- tags
- validation
description: Spectral linting rules defining API design standards and conventions for Amazon Data Pipeline.
layout: rules
name: Amazon Data Pipeline API Rules
provider_name: Amazon Data Pipeline
provider_slug: amazon-data-pipeline
rule_count: 22
rules:
- description: API title must start with "AWS Data Pipeline"
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
- description: AWS Data Pipeline uses Action-based path conventions with ?Action= query parameter
  given: $.paths[*]~
  name: action-based-paths
  severity: info
- description: AWS Data Pipeline uses POST for all operations
  given: $.paths[*][get,put,patch,delete]
  name: all-operations-use-post
  severity: info
- description: All operations must have a summary
  given: $.paths[*][post]
  name: operation-summary-required
  severity: error
- description: All operations must have a description
  given: $.paths[*][post]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][post]
  name: operation-id-required
  severity: error
- description: OperationId must use camelCase
  given: $.paths[*][post].operationId
  name: operation-id-camel-case
  severity: warn
- description: All operations must have tags
  given: $.paths[*][post]
  name: operation-tags-required
  severity: error
- description: All POST operations should support application/json
  given: $.paths[*].post.requestBody.content
  name: request-body-json-content
  severity: warn
- description: Tags array should be defined globally
  given: $
  name: tags-defined
  severity: warn
- description: All operations must have a 200 response
  given: $.paths[*][post].responses
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
- description: Pipeline operations should reference pipelineId in request body
  given: $.components.schemas[?(@ =~ /Request/)].properties
  name: pipeline-id-in-operations
  severity: info
- description: Validation operation responses should include errored field
  given: $.components.schemas.PutPipelineDefinitionOutput.properties
  name: validation-output-has-errored
  severity: info
rules_file: rules/amazon-data-pipeline-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-data-pipeline/refs/heads/main/rules/amazon-data-pipeline-spectral-rules.yml
severity_counts:
  error: 13
  hint: 0
  info: 4
  warn: 5
slug: amazon-data-pipeline-spectral-rules
tags:
- AWS
- Data Processing
- ETL
- Workflows
- Data Pipeline
- Automation
- Spectral
- Linting
- API Governance
---
