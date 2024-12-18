---
aid: amazon-web-services:trustedadvisor
name: AWS TrustedAdvisor
tags:
  - Organizations
  - Recommendations
  - Checks
  - Accounts
  - Resources
  - Lifecycle
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/
overlays:
  - url: overlays/trustedadvisor-openapi-search.yml
    type: APIs.io Search
  - url: overlays/trustedadvisor-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/
    type: Documentation
  - url: properties/trustedadvisor-openapi-original.yml
    type: OpenAPI
description: >-
  The AWS Trusted Advisor API offers a comprehensive solution to help users
  optimize costs, enhance performance, bolster security and resilience, and
  effectively operate in the cloud at scale. By continuously assessing your AWS
  environment against industry best practices in categories like cost
  optimization, performance, resilience, security, operational excellence, and
  service limits, Trusted Advisor provides actionable recommendations to address
  any areas of concern.

---