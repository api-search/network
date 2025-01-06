---
aid: plaid:plaid-sandbox-api
name: Plaid Sandbox API
tags: []
score: 635
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/sandbox/
overlays:
  - url: overlays/plaid-sandbox--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-sandbox--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: openapi/plaid-sandbox--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/sandbox/
    type: Documentation
description: >-
  The Plaid Sandbox API is a tool that allows developers to easily test and
  experiment with the Plaid platform in a simulated environment. This API
  enables users to create and access fake financial accounts, transactions, and
  user profiles, allowing them to simulate real-world scenarios and interactions
  with the Plaid API. By using the Sandbox API, developers can quickly build and
  test applications that interact with financial data without the need for live,
  sensitive information. This API provides a safe and secure way for developers
  to familiarize themselves with the Plaid platform and streamline the
  development process.

---