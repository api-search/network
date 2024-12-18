---
aid: amazon-web-services:memorydb
name: AWS MemoryDB
tags:
  - Users
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/memorydb/
overlays:
  - url: overlays/memorydb-openapi-search.yml
    type: APIs.io Search
  - url: overlays/memorydb-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/memorydb/
    type: Documentation
  - url: properties/memorydb-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/memorydb/features/
    type: Features
  - url: https://aws.amazon.com/memorydb/pricing/
    type: Pricing
  - url: https://aws.amazon.com/memorydb/resources/
    type: Resources
  - url: https://aws.amazon.com/memorydb/faqs/
    type: FAQ
  - url: https://aws.amazon.com/memorydb/sla/
    type: Sla
description: >-
  MemoryDB for Redis is a managed in-memory database that offers fast
  performance and Multi-AZ durability for microservices applications. It stores
  the entire database in-memory for low latency and high throughput access.
  Compatible with Redis, it supports Redis' data structures, APIs, and commands.

---