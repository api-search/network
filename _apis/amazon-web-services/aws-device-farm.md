---
aid: amazon-web-services:aws-device-farm
name: AWS Device Farm
tags:
  - Configurations
  - VPCE
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/device-farm/
overlays:
  - url: overlays/devicefarm-openapi-search.yml
    type: APIs.io Search
  - url: overlays/devicefarm-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/device-farm/
    type: Documentation
  - url: openapi/devicefarm-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/device-farm/device-list/
    type: Device List
  - url: https://aws.amazon.com/device-farm/pricing/
    type: Pricing
  - url: https://aws.amazon.com/device-farm/resources/
    type: Resources
  - url: https://aws.amazon.com/device-farm/faqs/
    type: FAQ
description: |-

  Explore the AWS Device Farm API documentation, offering APIs for two main
  testing services: desktop browser testing and real mobile device testing.
  Use Device Farm to test your web applications on desktop browsers with
  Selenium through the TestGrid-named APIs. 

---