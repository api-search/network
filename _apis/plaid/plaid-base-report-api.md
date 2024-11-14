---
aid: plaid:plaid-base-report-api
name: Plaid Base Report API
tags:
  - Accounts
  - Applicants
  - Applications
  - Bank
  - Base
  - CRA
  - Cash
  - Data
  - Decisions
  - Flows
  - Income
  - Information
  - Insights
  - Loan
  - Loans
  - Partners
  - Register
  - Reports
  - Unregister
  - Used
  - Verification
score: 213
baseURL: https://production.plaid.com
humanURL: https://plaid.com/docs/check/api/
overlays:
  - url: overlays/plaid-cra--openapi-search.yml
    type: OpenAPI
  - url: overlays/plaid-cra--openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: properties/plaid-cra--openapi-original.yml
    type: OpenAPI
description: API for retrieving a base report for an account.

---