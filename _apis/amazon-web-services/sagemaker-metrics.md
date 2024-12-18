---
aid: amazon-web-services:sagemaker-metrics
name: Amazon SageMaker Metrics
tags:
  - Batches
  - Metrics
  - Data
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html
overlays:
  - url: overlays/sagemaker-metrics-openapi-search.yml
    type: APIs.io Search
  - url: overlays/sagemaker-metrics-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html
    type: Documentation
  - url: properties/sagemaker-metrics-openapi-original.yml
    type: OpenAPI
description: >-
  Contains all data plane API operations and data types for Amazon SageMaker
  Metrics. Use these APIs to put and retrieve (get) features related to your
  training run.    BatchPutMetrics

---