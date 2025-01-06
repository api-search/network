---
aid: adyen:adyen-configuration-webhooks-api
name: Adyen Configuration Webhooks API
tags:
  - Configuraton
  - Webhooks
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/1/overview
properties:
  - url: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/1/overview
    type: Documentation
  - url: openapi/configuration-webhooks-openapi-original.yml
    type: OpenAPI
description: >-
  Adyen sends webhooks to inform your system about events that occur in your
  platform. These events include, for example, when an account holders
  capabilities are updated, or when a sweep configuration is created or updated.
  When an event occurs, Adyen makes an HTTP POST request to a URL on your server
  and includes the details of the event in the request body. You can use these
  webhooks to build your implementation.

---