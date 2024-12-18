---
aid: amazon-web-services:wafv2
name: AWS WAF
tags:
  - ACL
  - Web
  - Firewalls
  - Security
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://docs.aws.amazon.com/waf/
overlays:
  - url: overlays/wafv2-openapi-search.yml
    type: APIs.io Search
  - url: overlays/wafv2-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://docs.aws.amazon.com/waf/
    type: Documentation
  - url: properties/wafv2-openapi-original.yml
    type: OpenAPI
description: >-
  AWS WAF is a powerful web application firewall designed to safeguard your AWS
  resources by monitoring and managing incoming web requests. It offers
  protection for various resources like Amazon CloudFront distributions, Amazon
  API Gateway REST APIs, Application Load Balancers, and AWS AppSync GraphQL
  APIs.

---