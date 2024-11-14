---
aid: stripe:stripe-country-api
name: Stripe Country API
tags:
  - Countries
  - Specs
overlays:
  - url: overlays/country-openapi-search.yml
    type: APIs.io Search
  - url: overlays/country-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/country_specs
    type: Documentation
  - url: properties/country-openapi-original.yml
    type: OpenAPI
description: >-
  Stripe needs to collect certain pieces of information about each account
  created. These requirements can differ depending on the account's country. The
  Country Specs API makes these rules available to your integration.

---