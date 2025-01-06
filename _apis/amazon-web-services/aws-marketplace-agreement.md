---
aid: amazon-web-services:aws-marketplace-agreement
name: AWS Marketplace Agreement
tags:
  - Agreements
  - Search
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: >-

  https://docs.aws.amazon.com/marketplace-agreements/latest/api-reference/welcome.html
overlays:
  - url: overlays/marketplace-agreement-openapi-search.yml
    type: APIs.io Search
  - url: overlays/marketplace-agreement-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-

      https://docs.aws.amazon.com/marketplace-agreements/latest/api-reference/welcome.html
    type: Documentation
  - url: openapi/marketplace-agreement-openapi-original.yml
    type: OpenAPI
description: |-

  The AWS Marketplace API enables sellers to manage product-related
  agreements, including listing, searching, and filtering agreements. To use
  this API, sellers must ensure that their AWS IAM policies and roles are
  properly configured. Users must have the necessary permissions to carry
  out actions such as describing agreements, getting agreement terms, and
  searching through all agreements.

---