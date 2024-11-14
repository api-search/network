---
aid: walmart:walmart-marketplace-notifications-api
name: Walmart Marketplace Notifications API
tags:
  - Notifications
  - Tests
  - Webhooks
  - Subscriptions
  - Events
  - Types
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.walmart.com/doc/us/mp/us-mp-notifications/
overlays: []
properties:
  - url: https://developer.walmart.com/doc/us/mp/us-mp-notifications/
    type: Documentation
  - url: properties/walmart-marketplace-notifications-openapi-original.yml
    type: OpenAPI
description: >-
  Push notifications or Web Hooks trigger alerts to seller applications when
  specific events occur, such as an item is unpublished, a new purchase order is
  created, an item's inventory is out of stock, etc. Whenever the trigger event
  occurs, Walmart will send a notification payload with event details to the
  seller-defined destination URL. Web Hooks help to optimize integration,
  automate workflows and reduce the number of times your application has to poll
  Walmart APIs within the throttle limits to determine if an event has occurred.

---