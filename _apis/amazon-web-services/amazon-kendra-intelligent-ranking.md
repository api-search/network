---
aid: amazon-web-services:amazon-kendra-intelligent-ranking
name: Amazon Kendra Intelligent Ranking
tags:
  - Execution
  - Plan
  - Rescore
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://docs.aws.amazon.com/kendra/latest/dg/intelligent-rerank.html
overlays:
  - url: overlays/kendra-ranking-openapi-search.yml
    type: APIs.io Search
  - url: overlays/kendra-ranking-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://docs.aws.amazon.com/kendra/latest/dg/intelligent-rerank.html
    type: Documentation
  - url: openapi/kendra-ranking-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/kendra/intelligent-ranking-pricing/
    type: Pricing
description: |-

  Amazon Kendra Intelligent Ranking leverages the advanced semantic search
  capabilities of Amazon Kendra to intelligently re-prioritize the search
  results provided by a search service.

---