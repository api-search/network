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
  - url: openapi/plaid-payment-profile--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/payment-initiation/add-to-app/
    type: Documentation
description: >-
  Plaid Sandbox API is a tool provided by Plaid that allows developers to test
  and experiment with their applications in a simulated environment. The API
  provides access to a variety of fake financial data, such as bank account
  information, transactions, and balances, that can be used to simulate
  real-world scenarios without affecting actual user accounts. This allows
  developers to quickly and easily test the functionality of their applications,
  identify bugs and issues, and make necessary adjustments before deploying
  their products in a production environment. Overall, the Plaid Sandbox API
  helps developers streamline the development process and ensure the reliability
  and security of their applications.

---