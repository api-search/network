---
aid: factset:factset-benchmarks-api
name: FactSet Benchmarks API
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://developer.factset.com/api-catalog/factset-benchmarks-api
overlays:
  - url: overlays/benchmarks-openapi-search.yml
    type: APIs.io Search
  - url: overlays/benchmarks-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://developer.factset.com/api-catalog/factset-benchmarks-api#overview
    type: Documentation
  - url: >-
      https://developer.factset.com/api-catalog/factset-benchmarks-api#sdkLibrary
    type: SDKs
  - url: https://developer.factset.com/api-catalog/factset-benchmarks-api#notebooks
    type: Jupyter Notebooks
  - url: >-
      https://developer.factset.com/api-catalog/factset-benchmarks-api#codeSnippet
    type: Code Snippets
  - url: https://developer.factset.com/api-catalog/factset-benchmarks-api#changelog
    type: Change Log
  - url: properties/benchmarks-openapi-original.yml
    type: OpenAPI
description: >-
  Returns Benchmark Constituent data including weights, price, and market value
  for a specified date.

---