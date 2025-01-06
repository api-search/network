---
aid: amazon-web-services:aws-price-list
name: AWS Price List
tags:
  - Prices
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/pricing/
overlays:
  - url: overlays/pricing-openapi-search.yml
    type: APIs.io Search
  - url: overlays/pricing-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/pricing/
    type: Documentation
  - url: openapi/pricing-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/pricing/cost-optimization/
    type: Cost-optimization
description: |-

  The Amazon Web Services Price List API is a user-friendly tool that allows
  you to access Amazon Web Services' services, products, and pricing
  information through programmatic queries. The API utilizes standardized
  product attributes like Location, Storage Class, and Operating System, and
  provides pricing at the SKU level. 

---