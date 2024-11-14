---
aid: plaid:plaid-profile-api
name: Plaid Profile API
tags: []
score: 218
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/
overlays:
  - url: overlays/plaid-profile--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-profile--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-profile--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/
    type: Documentation
description: Use to manage Plaid profile data.

---