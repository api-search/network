---
aid: amazon-web-services:codestar-connections
name: AWS CodeStar Connections
tags:
  - Configurations
  - Sync
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html
overlays:
  - url: overlays/codestar-connections-openapi-search.yml
    type: APIs.io Search
  - url: overlays/codestar-connections-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-
      https://docs.aws.amazon.com/codeconnections/latest/APIReference/Welcome.html
    type: Documentation
  - url: properties/codestar-connections-openapi-original.yml
    type: OpenAPI
description: >-
  AWS CodeStar Connections is an API provided by Amazon Web Services that allows
  you to work with connections and installations. Connections are configurations
  used to connect AWS resources to external code repositories, allowing services
  like CodePipeline to trigger actions based on changes in third-party code
  repositories.

---