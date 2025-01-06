---
aid: amazon-web-services:amazon-neptune
name: Amazon Neptune
tags:
  - DBCluster
  - Stop
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/neptune/
overlays:
  - url: overlays/neptune-openapi-search.yml
    type: APIs.io Search
  - url: overlays/neptune-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/neptune/
    type: Documentation
  - url: openapi/neptune-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/neptune/pricing/
    type: Pricing
  - url: https://aws.amazon.com/neptune/faqs/
    type: FAQ
  - url: https://aws.amazon.com/neptune/features/
    type: Features
  - url: https://aws.amazon.com/neptune/global-database/
    type: Global-database
  - url: https://aws.amazon.com/neptune/machine-learning/
    type: Machine-learning
  - url: https://aws.amazon.com/neptune/serverless/
    type: Serverless
  - url: https://aws.amazon.com/neptune/getting-started/
    type: Getting-started
description: |-

  Amazon Neptune Amazon Neptune is a fast, reliable, fully-managed graph
  database service that makes it easy to build and run applications that
  work with highly connected datasets. The core of Amazon Neptune is a
  purpose-built, high-performance graph database engine optimized for
  storing billions of relationships and querying the graph with milliseconds
  latency.

---