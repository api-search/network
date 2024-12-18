---
aid: amazon-web-services:waf
name: AWS WAF Classic
tags:
  - Match
  - Sets
  - Firewalls
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html
overlays:
  - url: overlays/waf-openapi-search.yml
    type: APIs.io Search
  - url: overlays/waf-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-
      https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html
    type: Documentation
  - url: properties/waf-openapi-original.yml
    type: OpenAPI
description: >-
  AWS WAF Classic is a web application firewall that allows you to monitor HTTP
  and HTTPS requests directed towards Amazon API Gateway API, Amazon CloudFront,
  or an Application Load Balancer. Additionally, AWS WAF Classic enables you to
  manage access to your content by setting conditions such as originating IP
  addresses or query string values. 

---