---
aid: amazon-web-services:aws-marketplace
name: AWS Marketplace
tags:
  - Resources
  - Untag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/mediastore/
overlays:
  - url: overlays/mediastore-openapi-search.yml
    type: APIs.io Search
  - url: overlays/mediastore-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/mediastore/
    type: Documentation
  - url: openapi/mediastore-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/mediastore/features/
    type: Features
  - url: https://aws.amazon.com/mediastore/pricing/
    type: Pricing
  - url: https://aws.amazon.com/mediastore/getting-started/
    type: Getting-started
  - url: https://aws.amazon.com/mediastore/resources/
    type: Resources
  - url: https://aws.amazon.com/mediastore/faqs/
    type: FAQ
description: |-

  The AWS Elemental MediaStore API is designed to provide high-performance
  storage specifically tailored for media content, offering reliable
  consistency and minimal latency to support the seamless delivery of live
  streaming video content.

---