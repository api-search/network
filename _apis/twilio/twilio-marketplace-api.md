---
aid: twilio:twilio-marketplace-api
name: Twilio Marketplace API
tags:
  - Available
  - Marketplace
  - Extensions
  - 'On'
  - Installed
overlays:
  - url: overlays/marketplace-openapi-search.yml
    type: APIs.io Search
  - url: overlays/marketplace-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://www.twilio.com/docs/add-ons/marketplace
    type: Documentation
  - url: properties/marketplace-openapi-original.yml
    type: OpenAPI
description: >-
  Add-ons are available through the Twilio Marketplace. At a functional level,
  Add-ons package a publisher's APIs and annotate the content that Twilio
  provides by tapping into the publisher's data sources or by using the
  publisher's technology to analyze the content.

---