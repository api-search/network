---
api_count: 1
apis:
- description: REST runtime API for Amazon Augmented AI covering human loops for human review of machine learning predictions.
  name: Amazon Augmented AI API
  slug: amazon-augmented-ai-api
capabilities:
- description: Workflow capability for managing human-in-the-loop review of machine learning predictions using Amazon Augmented AI.
  name: Human Review Workflow
  slug: human-review-workflow
common: []
created: '2026-03-16'
description: Amazon Augmented AI (Amazon A2I) is a machine learning service that makes it easy to build the workflows required for human review of ML predictions. Amazon A2I brings human review to all developers, removing the undifferentiated heavy lifting associated with building human review systems or managing large numbers of human reviewers.
features:
- Human review integration for Amazon Rekognition and Amazon Textract
- Custom flow definitions for any ML use case
- Built-in worker task templates for common review tasks
- Integration with Amazon SageMaker Ground Truth for workforce management
- Private, vendor, and Amazon Mechanical Turk workforce support
- Automatic routing based on ML confidence scores
- Audit trail with evidence of human review decisions
- Scalable workforce management across thousands of reviewers
- Pre-built UI templates for image and text review tasks
- Compliance support with PII content classifiers
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- Amazon SageMaker
- Amazon Rekognition
- Amazon Textract
- Amazon S3
- Amazon SageMaker Ground Truth
- Amazon Mechanical Turk
- AWS IAM
- Amazon CloudWatch
- AWS Lambda
- Amazon SNS
jsonld:
- class_count: 4
  name: Amazon Augmented Ai Context
  property_count: 0
  slug: amazon-augmented-ai-context
layout: provider
modified: '2026-04-19'
name: Amazon Augmented AI
rules:
- name: Amazon Augmented AI API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 5
  slug: amazon-augmented-ai-spectral-rules
skills: []
slug: amazon-augmented-ai
solutions: []
tags:
- Amazon Augmented AI
- Human In The Loop
- Machine Learning
- AI Review
- AWS
url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/apis.yml
use_cases:
- Review low-confidence document text extraction results
- Validate image classification predictions before deployment
- Moderate user-generated content with human reviewers
- Ensure accuracy of medical record processing
- Verify identity document data extraction results
- Build training datasets with human-verified labels
---
