---
aid: amazon-web-services:aws-marketplace-metering-service
name: AWS Marketplace Metering Service
tags:
  - Customers
  - Resolve
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://docs.aws.amazon.com/marketplace/
overlays:
  - url: overlays/meteringmarketplace-openapi-search.yml
    type: APIs.io Search
  - url: overlays/meteringmarketplace-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://docs.aws.amazon.com/marketplace/
    type: Documentation
  - url: openapi/meteringmarketplace-openapi-original.yml
    type: OpenAPI
  - url: https://docs.aws.amazon.com/marketplace/latest/userguide/index.html
    type: Seller Guide
  - url: https://docs.aws.amazon.com/marketplace/latest/buyerguide/index.html
    type: Buyer Guide
description: |-

  The AWS Marketplace Metering Service API allows AWS Marketplace sellers to
  submit usage data for custom usage dimensions. This reference provides
  detailed descriptions of the low-level API functions available for use.

---