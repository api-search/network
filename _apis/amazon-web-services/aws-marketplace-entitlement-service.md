---
aid: amazon-web-services:aws-marketplace-entitlement-service
name: AWS Marketplace Entitlement Service
tags:
  - Entitlements
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: >-

  https://docs.aws.amazon.com/marketplace/latest/userguide/checking-entitlements.html
overlays:
  - url: overlays/entitlementmarketplace-openapi-search.yml
    type: APIs.io Search
  - url: overlays/entitlementmarketplace-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-

      https://docs.aws.amazon.com/marketplace/latest/userguide/checking-entitlements.html
    type: Documentation
  - url: openapi/entitlementmarketplace-openapi-original.yml
    type: OpenAPI
description: |-

  The AWS Marketplace Entitlement Service API documentation provides an
  overview of how to use the service to determine a customer's entitlement
  to a specific product. Entitlements represent the capacity or access a
  customer has to a particular product, such as user seats in an SaaS
  application or data capacity in a database. The GetEntitlements function
  retrieves entitlement records for a Marketplace product.

---