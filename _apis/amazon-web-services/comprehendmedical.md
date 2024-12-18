---
aid: amazon-web-services:comprehendmedical
name: Amazon Comprehend Medical
tags:
  - Inference
  - Jobs
  - Stop
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/comprehend/medical/
overlays:
  - url: overlays/comprehendmedical-openapi-search.yml
    type: APIs.io Search
  - url: overlays/comprehendmedical-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/comprehend/medical/
    type: Documentation
  - url: properties/comprehendmedical-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/comprehend/medical/features/
    type: Features
  - url: https://aws.amazon.com/comprehend/medical/pricing/
    type: Pricing
  - url: https://aws.amazon.com/comprehend/medical/faqs/
    type: FAQ
  - url: https://aws.amazon.com/comprehend/medical/resources/
    type: Resources
  - url: https://aws.amazon.com/comprehend/medical/customers/
    type: Customers
description: >-
  The Amazon Comprehend Medical API is designed to extract structured
  information from unstructured clinical text, allowing users to gain valuable
  insights from their documents. It should be noted, however, that this API only
  detects entities in English language texts and imposes size limits on files
  for various API operations.

---