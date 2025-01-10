---
aid: amazon-web-services:amazon-opensearch-ingestion
name: Amazon OpenSearch Ingestion
tags:
  - Blueprints
  - Change
  - Names
  - Pipelines
  - Progress
  - Resources
  - Stop
  - Tags
  - Untag
  - Validate
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: >-

  https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html
overlays:
  - url: overlays/osis-openapi-search.yml
    type: APIs.io Search
  - url: overlays/osis-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-

      https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html
    type: Documentation
  - url: openapi/osis-openapi-original.yml
    type: OpenAPI
description: |-

  The Amazon OpenSearch Ingestion API is a fully managed, serverless data
  collection tool designed to deliver real-time log, metric, and trace data
  to Amazon OpenSearch Service domains and OpenSearch Serverless
  collections. With OpenSearch Ingestion, there is no longer a need for
  third-party solutions like Logstash or Jaeger to ingest data into your
  OpenSearch Service domains and OpenSearch Serverless collections. 

---