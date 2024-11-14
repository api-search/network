---
aid: adyen:adyen-configuration-webhooks-api
name: Adyen Configuration Webhooks API
tags: []
overlays:
  - url: overlays/configuration-webhooks-openapi-search.yml
    type: APIs.io Search
  - url: overlays/configuration-webhooks-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
description: >-
  Adyen sends webhooks to inform your system about events that occur in your
  platform. These events include, for example, when an account holders
  capabilities are updated, or when a sweep configuration is created or updated.
  When an event occurs, Adyen makes an HTTP POST request to a URL on your server
  and includes the details of the event in the request body. You can use these
  webhooks to build your implementation.

---