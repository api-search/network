---
aid: plaid:plaid-fdx-api
name: Plaid FDX API
tags:
  - Fdx
  - Notifications
  - Receiver
  - Webhooks
score: 43
baseURL: https://production.plaid.com
humanURL: https://plaid.github.io/core-exchange/api-versions/six-dot-zero
overlays:
  - url: overlays/plaid-fdx--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-fdx--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-fdx--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.github.io/core-exchange/api-versions/six-dot-zero
    type: Documentation
description: >-
  The Core Exchange API specifications are a subset of the Financial Data
  Exchange (FDX) API specification, the usage thereof (or any part thereof)
  constitutes acceptance of the FDX API License Agreement, which can be found at
  https://financialdataexchange.org/.

---