---
aid: amazon-web-services:identitystore
name: AWS  Identity Store
tags:
  - Users
  - Identity
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: >-
  https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html
overlays:
  - url: overlays/identitystore-openapi-search.yml
    type: APIs.io Search
  - url: overlays/identitystore-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-
      https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html
    type: Documentation
  - url: properties/identitystore-openapi-original.yml
    type: OpenAPI
description: >-
  The API for the Identity Store service within IAM Identity Center is a central
  hub for accessing all user and group identities. You can find detailed
  information on how to use this service in the IAM Identity Center User Guide,
  which outlines the available identity store operations that can be accessed
  programmatically. The API utilizes the sso and identitystore namespaces for
  seamless integration with your systems.

---