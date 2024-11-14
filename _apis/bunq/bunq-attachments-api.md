---
aid: bunq:bunq-attachments-api
name: Bunq Attachments API
tags:
  - Attachments
  - Items
  - Users
  - Content
baseURL: https://public-api.sandbox.bunq.com/
humanURL: https://doc.bunq.com/#/attachment
overlays:
  - url: overlays/bunq-user-userid-attachment-openapi-search.yml
    type: OpenAPI
properties:
  - url: properties/bunq-user-userid-attachment-openapi-original.yml
    type: OpenAPI
  - url: https://doc.bunq.com/
    type: Documentation
description: An API for managing attachments associated with a Bunq account.

---