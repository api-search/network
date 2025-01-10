---
aid: amazon-web-services:amazon-cognito-user-pools
name: Amazon Cognito User Pools
tags:
  - Attributes
  - Users
  - Verify
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: >-

  https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html
overlays:
  - url: overlays/cognito-idp-openapi-search.yml
    type: APIs.io Search
  - url: overlays/cognito-idp-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-

      https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html
    type: Documentation
  - url: openapi/cognito-idp-openapi-original.yml
    type: OpenAPI
description: |-

  Amazon Cognito user pool, serves as a user directory for authenticating
  and authorizing users in web and mobile applications. When integrated into
  your app, the user pool functions as an OpenID Connect (OIDC) identity
  provider, offering enhanced security features, identity federation
  capabilities, seamless app integration, and customizable user experiences.

---