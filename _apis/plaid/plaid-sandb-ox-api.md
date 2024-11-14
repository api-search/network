---
aid: plaid:plaid-sandb-ox-api
name: Plaid Sandb ox API
tags:
  - Login
  - Payments
  - Profiles
  - Reset
  - Sandbox
score: 120
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/sandbox/
overlays:
  - url: overlays/plaid-payment-profile--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-payment-profile--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-payment-profile--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/payment-initiation/add-to-app/
    type: Documentation
description: >-
  The Plaid Sandbox is a free and fully-featured environment for application
  development and testing. All Plaid functionality of both the Plaid API and
  Plaid Link is supported in the Sandbox environment. 

---