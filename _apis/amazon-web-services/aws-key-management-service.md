---
aid: amazon-web-services:aws-key-management-service
name: AWS Key Management Service
tags:
  - Verify
  - Keys
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://example.com
overlays:
  - url: overlays/kms-openapi-search.yml
    type: APIs.io Search
  - url: overlays/kms-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/kms/
    type: Documentation
  - url: openapi/kms-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/kms/features/
    type: Features
  - url: https://aws.amazon.com/kms/pricing/
    type: Pricing
  - url: https://aws.amazon.com/kms/getting-started/
    type: Getting-started
  - url: https://aws.amazon.com/kms/resources/
    type: Resources
  - url: https://aws.amazon.com/kms/faqs/
    type: FAQ
description: |-

  The Key Management Service (KMS) API is an encryption and key management
  web service that allows you to programmatically call various operations.
  KMS has replaced the term customer master key (CMK) with KMS key, but the
  concept remains the same. Amazon Web Services provides SDKs for various
  programming languages and platforms to create programmatic access to KMS. 

---