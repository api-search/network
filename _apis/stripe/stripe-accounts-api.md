---
aid: stripe:stripe-accounts-api
name: Stripe Accounts API
tags:
  - Accounts
  - Bank
  - Capabilities
  - External
  - Links
  - Login
  - People
  - Person
  - Persons
  - Reject
  - Sessions
overlays:
  - url: overlays/accounts-openapi-search.yml
    type: APIs.io Search
  - url: overlays/accounts-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/accounts
    type: Documentation
  - url: properties/accounts-openapi-original.yml
    type: OpenAPI
description: >-
  This is an object representing a Stripe account. You can retrieve it to see
  properties on the account like its current requirements or if the account is
  enabled to make live charges or receive payouts.

---