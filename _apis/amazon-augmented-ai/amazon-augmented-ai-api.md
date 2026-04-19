---
aid: amazon-augmented-ai:amazon-augmented-ai-api
baseURL: https://a2i-runtime.sagemaker.us-east-1.amazonaws.com
description: REST runtime API for Amazon Augmented AI covering human loops for human review of machine learning predictions.
humanURL: https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/Welcome.html
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Amazon Augmented AI API
properties:
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/openapi/amazon-augmented-ai-openapi.yml
- type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/rules/amazon-augmented-ai-spectral-rules.yml
- type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/capabilities/shared/a2i-api.yaml
- type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/capabilities/human-review-workflow.yaml
- type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/vocabulary/amazon-augmented-ai-vocabulary.yaml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/json-schema/a2i-human-loop-summary-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/json-schema/a2i-start-human-loop-request-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/json-structure/a2i-human-loop-summary-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/json-structure/a2i-describe-human-loop-response-structure.json
- type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/json-ld/amazon-augmented-ai-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/examples/a2i-start-human-loop-request-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/examples/a2i-describe-human-loop-response-example.json
provider_name: Amazon Augmented AI
provider_slug: amazon-augmented-ai
slug: amazon-augmented-ai-api
tags:
- Amazon Augmented AI
- Human In The Loop
- Machine Learning
- AI Review
- AWS
---
