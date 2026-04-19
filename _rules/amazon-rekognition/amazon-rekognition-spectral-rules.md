---
categories:
- info
- operation
- post
- response
- schema
- security
- servers
- tag
description: Spectral linting rules defining API design standards and conventions for Amazon Rekognition.
layout: rules
name: Amazon Rekognition API Rules
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
rule_count: 18
rules:
- description: Info title must start with Amazon Rekognition
  given: $.info.title
  name: info-title-prefix
  severity: warn
- description: Info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-required
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: All operations must have a summary
  given: $.paths[*][*]
  name: operation-summary-required
  severity: error
- description: Operation summaries must start with Amazon Rekognition
  given: $.paths[*][*].summary
  name: operation-summary-prefix
  severity: warn
- description: All operations must have a description
  given: $.paths[*][*]
  name: operation-description-required
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][*]
  name: operation-operationid-required
  severity: error
- description: OperationIds must use camelCase
  given: $.paths[*][*].operationId
  name: operation-operationid-camelcase
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][*]
  name: operation-tags-required
  severity: warn
- description: All operations should specify security
  given: $.paths[*][*]
  name: operation-security-required
  severity: warn
- description: Operations must have a 2xx success response
  given: $.paths[*][*].responses
  name: response-success-required
  severity: error
- description: Operations should have a 400 error response
  given: $.paths[*][*].responses
  name: response-400-recommended
  severity: warn
- description: Top-level schemas should have descriptions
  given: $.components.schemas[*]
  name: schema-description-required
  severity: warn
- description: Security schemes must be defined in components
  given: $
  name: security-schemes-defined
  severity: warn
- description: POST operations should use AWS JSON content type
  given: $.paths[*].post.requestBody.content
  name: post-must-use-amz-json
  severity: info
- description: Global tags should have descriptions
  given: $.tags[*]
  name: tag-descriptions-required
  severity: info
rules_file: rules/amazon-rekognition-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-rekognition/refs/heads/main/rules/amazon-rekognition-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 2
  warn: 8
slug: amazon-rekognition-spectral-rules
tags:
- AWS
- Celebrity Recognition
- Computer Vision
- Content Moderation
- Custom Labels
- Deep Learning
- Face Liveness
- Facial Recognition
- Image Analysis
- Machine Learning
- Object Detection
- Text Detection
- Video Analysis
- Spectral
- Linting
- API Governance
---
