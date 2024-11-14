---
aid: stripe:stripe-reporting-api
name: Stripe Reporting API
tags:
  - Reporting
  - Reports
  - Runs
  - Types
overlays:
  - url: overlays/reporting-openapi-search.yml
    type: APIs.io Search
  - url: overlays/reporting-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/reports/api
    type: Documentation
  - url: properties/reporting-openapi-original.yml
    type: OpenAPI
description: >-
  The financial reports in the Dashboard provide downloadable reports in CSV
  format for a variety of accounting and reconciliation tasks. These reports are
  also available through the API, so you can schedule them to run automatically
  or run them whenever you need to receive the associated report files for
  accounting purposes.

---