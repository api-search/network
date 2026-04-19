---
categories:
- fraud
description: Spectral linting rules defining API design standards and conventions for Amazon Fraud Detector.
layout: rules
name: Amazon Fraud Detector API Rules
provider_name: Amazon Fraud Detector
provider_slug: amazon-fraud-detector
rule_count: 25
rules:
- description: API must include contact information
  given: $.info
  name: fraud-detector-info-contact
  severity: warn
- description: API must have a description
  given: $.info
  name: fraud-detector-info-description
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: fraud-detector-server-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-operation-description
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-operation-tags
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-operation-id
  severity: error
- description: POST operations should define 200 response
  given: $.paths[*][post]
  name: fraud-detector-response-200
  severity: warn
- description: Operations should define 400 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-response-400
  severity: warn
- description: Operations should define 500 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fraud-detector-response-500
  severity: warn
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: fraud-detector-schema-description
  severity: warn
- description: Operation tags should use Title Case
  given: $.paths[*][*].tags[*]
  name: fraud-detector-tags-title-case
  severity: warn
- description: Detector schema must reference eventTypeName
  given: $.components.schemas.Detector.required
  name: fraud-detector-detector-event-type
  severity: warn
- description: Model type should define allowed enum values
  given: $.components.schemas.Model.properties.modelType
  name: fraud-detector-model-type-enum
  severity: warn
- description: Rule schema must include outcomes
  given: $.components.schemas.Rule.required
  name: fraud-detector-rule-outcomes
  severity: warn
- description: Event prediction request must include entities
  given: $.components.schemas.GetEventPredictionRequest.required
  name: fraud-detector-prediction-entities
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: fraud-detector-parameter-description
  severity: error
- description: Path parameters must be required
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]
  name: fraud-detector-path-param-required
  severity: error
- description: Object schemas should define properties
  given: $.components.schemas[?(@.type=='object')]
  name: fraud-detector-schema-properties
  severity: warn
- description: ARN fields should be consistently named 'arn'
  given: $.components.schemas[*].properties.arn
  name: fraud-detector-arn-fields
  severity: info
- description: Event type schema must include labels field
  given: $.components.schemas.EventType.required
  name: fraud-detector-event-type-labels
  severity: warn
- description: Rule language should define DETECTORPL enum
  given: $.components.schemas.Rule.properties.language
  name: fraud-detector-rule-language-enum
  severity: info
- description: Request bodies should define application/json content
  given: $.paths[*][put,post].requestBody.content
  name: fraud-detector-request-body-json
  severity: warn
- description: Tag schema must require key field
  given: $.components.schemas.Tag.required
  name: fraud-detector-tag-key-required
  severity: warn
- description: DELETE operations should define 404 response
  given: $.paths[*].delete.responses
  name: fraud-detector-delete-not-found
  severity: warn
rules_file: rules/amazon-fraud-detector-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-fraud-detector/refs/heads/main/rules/amazon-fraud-detector-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 2
  warn: 16
slug: amazon-fraud-detector-spectral-rules
tags:
- AWS
- Financial Services
- Fraud Detection
- Machine Learning
- Security
- Spectral
- Linting
- API Governance
---
