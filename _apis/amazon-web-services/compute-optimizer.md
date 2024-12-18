---
aid: amazon-web-services:compute-optimizer
name: AWS Compute Optimizer
tags:
  - Enrollment
  - Status
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/compute-optimizer/
overlays:
  - url: overlays/compute-optimizer-openapi-search.yml
    type: APIs.io Search
  - url: overlays/compute-optimizer-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/compute-optimizer/
    type: Documentation
  - url: properties/compute-optimizer-openapi-original.yml
    type: OpenAPI
  - url: https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html
    type: Metrics
  - url: https://aws.amazon.com/compute-optimizer/faqs/
    type: FAQ
  - url: https://aws.amazon.com/compute-optimizer/getting-started/
    type: Getting Started
  - url: https://aws.amazon.com/compute-optimizer/pricing/
    type: Pricing
description: >-
  Compute Optimizer is an API that evaluates the configuration and usage metrics
  of your AWS compute resources, including EC2 instances, Auto Scaling groups,
  Lambda functions, EBS volumes, and ECS services on Fargate. It provides
  optimization recommendations to enhance performance and reduce costs, based on
  current and projected utilization data.

---