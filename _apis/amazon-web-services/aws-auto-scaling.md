---
aid: amazon-web-services:aws-auto-scaling
name: AWS Auto Scaling
tags:
  - Plan
  - Scaling
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/autoscaling/
overlays:
  - url: overlays/autoscaling-plans-openapi-search.yml
    type: APIs.io Search
  - url: overlays/autoscaling-plans-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/autoscaling/
    type: Documentation
  - url: openapi/autoscaling-plans-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/autoscaling/features/
    type: Features
  - url: https://aws.amazon.com/autoscaling/pricing/
    type: Pricing
  - url: https://aws.amazon.com/autoscaling/resources/
    type: Resources
  - url: https://aws.amazon.com/autoscaling/faqs/
    type: FAQ
description: |-

  This API allows you to easily create and manage scaling plans for your
  applications using AWS Auto Scaling. With this service, you can define
  target tracking scaling policies to automatically scale your AWS resources
  based on utilization, as well as scale Amazon EC2 Auto Scaling groups
  using predictive scaling and dynamic scaling to quickly adjust your
  capacity. You can also set minimum and maximum capacity limits, retrieve
  information on existing scaling plans, and access forecast data for up to
  56 days previous.

---