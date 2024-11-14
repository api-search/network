---
aid: plaid:plaid-auth-api
name: Plaid Auth API
tags: []
score: 218
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/api/products/auth/
overlays:
  - url: overlays/plaid-auth--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-auth--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-auth--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/api/products/auth/
    type: Documentation
description: >+
  Retrieve bank account information to set up electronic funds transfers, such
  as ACH payments in the US, EFT payments in Canada, BACS payments in the UK,
  and IBAN / SIC payments in the EU.


---