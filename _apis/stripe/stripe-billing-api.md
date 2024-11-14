---
aid: stripe:stripe-billing-api
name: Stripe Billing API
tags:
  - Billing
  - Configurations
  - Portals
  - Sessions
overlays:
  - url: overlays/billing-openapi-search.yml
    type: APIs.io Search
  - url: overlays/billing-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/billing
    type: Documentation
  - url: properties/billing-openapi-original.yml
    type: OpenAPI
description: Create and manage subscriptions, recurring payments, and recurring revenue.

---