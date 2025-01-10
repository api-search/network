---
aid: amazon-web-services:aws-cost-explorer
name: AWS  Cost Explorer
tags:
  - Categories
  - Cost
  - Definitions
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://ce.us-east-1.amazonaws.com
humanURL: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/
overlays:
  - url: overlays/ce-openapi-search.yml
    type: APIs.io Search
  - url: overlays/ce-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/
    type: Documentation
  - url: openapi/ce-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/features/
    type: Features
  - url: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/
    type: Pricing
  - url: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/faqs/
    type: FAQ
  - url: >-

      https://aws.amazon.com/aws-cost-management/aws-cost-explorer/getting-started/
    type: Getting Started
description: |-

  The Cost Explorer API allows you to access your cost and usage data
  programmatically. You can retrieve aggregated information like total
  monthly costs or daily usage, as well as more detailed data such as
  specific operations for services like Amazon DynamoDB. The service
  endpoint for the Cost Explorer API is https://ce.us-east-1.amazonaws.com.
  For pricing details, refer to Amazon Web Services Cost Management Pricing.

---