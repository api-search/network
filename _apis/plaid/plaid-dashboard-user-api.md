---
aid: plaid:plaid-dashboard-user-api
name: Plaid Dashboard User API
tags:
  - Dashboard
  - Users
score: 58
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/account/activity/
overlays:
  - url: overlays/plaid-dashboard-user--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-dashboard-user--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-dashboard-user--openapi-original.yml
    type: OpenAPI
  - url: https://plaid.com/docs/account/activity/
    type: Documentation
description: >-
  The Plaid Dashboard Activity Log shows the past 14 days of API activity. Using
  the dashboard, you can see a record of all requests and responses, as well as
  all webhooks sent by the Plaid API, and all Link events.

---