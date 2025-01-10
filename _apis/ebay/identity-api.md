---
aid: ebay:identity-api
name: Identity API
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.ebay.com/api-docs/commerce/identity/overview.html
properties:
  - url: https://developer.ebay.com/api-docs/commerce/identity/overview.html
    type: Documentation
  - url: openapi/ebay-identity-openapi-original.yml
    type: OpenAPI
  - url: https://developer.ebay.com/api-docs/commerce/identity/release-notes.html
    type: Release Notes
description: >-
  The Identity API returns data for an authenticated user (user access token)
  based on the OAuth scopes provided. Non-confidential information, such as eBay
  userID is returned using the default scope. Confidential data for an
  individual, such as address, email, phone, etc. are returned based on the
  OAuth scope you use in the call. 

---