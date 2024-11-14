---
aid: adyen:adyen-notification-webhooks-api
name: Adyen Notification Webhooks API
tags: []
overlays:
  - url: overlays/notification-webhooks-openapi-search.yml
    type: APIs.io Search
  - url: overlays/notification-webhooks-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
description: >-
  Adyen sends notifications through webhooks to inform your system about events
  that occur in the balance platform. These events include, for example, a card
  user making a payment, or a merchant starting a refund. When an event occurs,
  Adyen makes an HTTP POST request to a URL on your server and includes the
  details of the event in the request body. You can use the webhooks to build
  your implementation. For example, you can use this information to update
  balances in your own dashboards or to keep track of incoming funds.

---