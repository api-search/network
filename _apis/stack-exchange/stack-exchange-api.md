---
aid: stack-exchange:stack-exchange-api
name: Stack Exchange API
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
contact:
  - FN: Stack Exchange
    url: http://stackapps.com/
    email: team+api@stackexchange.com
humanURL: https://api.stackexchange.com/
overlays:
  - url: >-
      overlays/https://raw.githubusercontent.com/openapis/api-specs/master/stackexchange/stackexchange-api-v2.2_swagger-v2.0.yaml-openapi-search.yml
    type: APIs.io Search
properties:
  - url: https://api.stackexchange.com/docs
    type: Documentation
  - url: properties/stack-exchange-openapi-original.yml
    type: OpenAPI
description: >-
  This is the documentation for the v2.3 Stack Exchange API (with both
  authentication and write support). If you have additional questions, or
  believe you have encountered a bug, don't hesitate to post a question on Stack
  Apps.

---