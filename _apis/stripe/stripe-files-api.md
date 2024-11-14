---
aid: stripe:stripe-files-api
name: Stripe Files API
tags:
  - Files
  - File
overlays:
  - url: overlays/files-openapi-search.yml
    type: APIs.io Search
  - url: overlays/files-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://stripe.com/docs/api/files
    type: Documentation
  - url: properties/files-openapi-original.yml
    type: OpenAPI
description: >-
  This object represents files hosted on Stripe's servers. You can upload files
  with the create file request (for example, when uploading dispute evidence).
  Stripe also creates files independently (for example, the results of a Sigma
  scheduled query).

---