---
aid: amazon-web-services:sts
name: AWS Security Token Service
tags:
  - Sessions
  - Tokens
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html
overlays:
  - url: overlays/sts-openapi-search.yml
    type: APIs.io Search
  - url: overlays/sts-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html
    type: Documentation
  - url: properties/sts-openapi-original.yml
    type: OpenAPI
description: >-
  Introducing the Security Token Service (STS) API, which allows you to
  conveniently request temporary, restricted-access credentials for your users.
  This documentation offers comprehensive explanations of the STS API
  functionality, with detailed instructions on how to utilize this service
  effectively. For further insights on using temporary security credentials,
  refer to the resources on Temporary Security Credentials.

---