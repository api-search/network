---
categories:
- forecast
description: Spectral linting rules defining API design standards and conventions for Amazon Forecast.
layout: rules
name: Amazon Forecast API Rules
provider_name: Amazon Forecast
provider_slug: amazon-forecast
rule_count: 25
rules:
- description: API must include contact information
  given: $.info
  name: forecast-info-contact
  severity: warn
- description: API must have a description
  given: $.info
  name: forecast-info-description
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: forecast-server-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-operation-description
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-operation-tags
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-operation-id
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: forecast-operation-id-camel-case
  severity: warn
- description: POST operations should define 200 response
  given: $.paths[*][post]
  name: forecast-response-200
  severity: warn
- description: Operations should define 400 response
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-response-400
  severity: warn
- description: Operations should define 500 response
  given: $.paths[*][get,post,put,patch,delete]
  name: forecast-response-500
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: forecast-parameter-description
  severity: error
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: forecast-schema-description
  severity: warn
- description: Operation tags should use Title Case
  given: $.paths[*][*].tags[*]
  name: forecast-tags-title-case
  severity: warn
- description: Collection GET operationIds should start with 'list'
  given: $.paths[*~'[^}]$'].get.operationId
  name: forecast-list-operation-prefix
  severity: warn
- description: POST operationIds should start with 'create'
  given: $.paths[*].post.operationId
  name: forecast-create-post-prefix
  severity: warn
- description: Dataset schema should define Domain enum values
  given: $.components.schemas.Dataset.properties.Domain
  name: forecast-dataset-domain-documented
  severity: warn
- description: Predictor schema should include ForecastHorizon
  given: $.components.schemas.Predictor.properties
  name: forecast-predictor-horizon-documented
  severity: warn
- description: Object schemas should define properties
  given: $.components.schemas[?(@.type=='object')]
  name: forecast-schema-properties-defined
  severity: warn
- description: POST request bodies must define content
  given: $.paths[*].post.requestBody
  name: forecast-request-body-content
  severity: error
- description: ARN fields should follow consistent naming (ResourceArn pattern)
  given: $.components.schemas[*].properties[*~'Arn$']
  name: forecast-arn-fields-consistent
  severity: info
- description: ForecastTypes should be an array of quantile strings
  given: $.components.schemas.Forecast.properties.ForecastTypes
  name: forecast-forecast-types-array
  severity: info
- description: Resources should document Status field
  given: $.components.schemas[*].properties.Status
  name: forecast-status-field-documented
  severity: info
- description: Tag schema should be defined
  given: $.components.schemas
  name: forecast-tag-schema-documented
  severity: warn
- description: Export job request should require Destination
  given: $.components.schemas.CreateForecastExportJobRequest.required
  name: forecast-export-job-destination
  severity: warn
rules_file: rules/amazon-forecast-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-forecast/refs/heads/main/rules/amazon-forecast-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 3
  warn: 15
slug: amazon-forecast-spectral-rules
tags:
- AWS
- Forecasting
- Machine Learning
- Predictive Analytics
- Time Series
- Spectral
- Linting
- API Governance
---
