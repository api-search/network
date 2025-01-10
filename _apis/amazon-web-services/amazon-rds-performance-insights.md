---
aid: amazon-web-services:amazon-rds-performance-insights
name: Amazon RDS Performance Insights
tags:
  - Resources
  - Untag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/rds/performance-insights/
overlays:
  - url: overlays/pi-openapi-search.yml
    type: APIs.io Search
  - url: overlays/pi-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/rds/performance-insights/
    type: Documentation
  - url: openapi/pi-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/rds/performance-insights/pricing/
    type: Pricing
  - url: https://aws.amazon.com/rds/performance-insights/faqs/
    type: FAQ
  - url: https://aws.amazon.com/rds/performance-insights/customers/
    type: Customers
description: |-

  The Amazon RDS Performance Insights API allows you to monitor and analyze
  various aspects of database load by capturing data from a running DB
  instance. This guide provides detailed information on Performance Insights
  data types, parameters, and errors. With Performance Insights enabled, the
  API offers visibility into the performance of your DB instance. Amazon
  CloudWatch serves as the source for monitoring metrics, while Performance
  Insights provides a specialized view of DB load, measured in average
  active sessions. 

---