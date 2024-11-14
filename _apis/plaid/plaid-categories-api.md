---
aid: plaid:plaid-categories-api
name: Plaid Categories API
tags: []
score: 44
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/api/products/transactions/#categoriesget
overlays:
  - url: overlays/plaid-categories--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-categories--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-categories--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/api/products/transactions/
    type: Documentation
description: >-
  To access detailed information on categories returned by Plaid, simply make a
  request to the /categories/get endpoint of the API.

---