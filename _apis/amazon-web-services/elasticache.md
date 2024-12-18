---
aid: amazon-web-services:elasticache
name: Amazon ElastiCache
tags:
  - Migrations
  - Tests
  - Cache
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/elasticache/
overlays:
  - url: overlays/elasticache-openapi-search.yml
    type: APIs.io Search
  - url: overlays/elasticache-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/elasticache/
    type: Documentation
  - url: properties/elasticache-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/elasticache/features/
    type: Features
  - url: https://aws.amazon.com/elasticache/pricing/
    type: Pricing
  - url: https://aws.amazon.com/elasticache/resources/
    type: Resources
  - url: https://aws.amazon.com/elasticache/migrations/
    type: Migrations
  - url: https://aws.amazon.com/elasticache/faqs/
    type: FAQ
  - url: https://aws.amazon.com/elasticache/customers/
    type: Customers
description: >-
  Amazon ElastiCache is a convenient web service that simplifies the process of
  setting up, operating, and expanding a distributed cache in the cloud. By
  utilizing ElastiCache, users can enjoy the advantages of a high-performance,
  in-memory cache without the extensive administrative tasks typically
  associated with launching and maintaining a distributed cache. The service
  streamlines setup, scaling, and cluster failure management compared to a
  self-managed cache deployment. Additionally, Amazon ElastiCache offers
  integration with Amazon CloudWatch, providing users with increased visibility
  into the important performance metrics of their cache and the ability to
  receive alerts if any parts of their cache become overloaded.

---