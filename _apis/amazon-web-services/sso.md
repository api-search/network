---
aid: amazon-web-services:sso
name: AWS IAM Identity Center
tags:
  - Credentials
  - Federation
  - Roles
  - Accounts
  - Assignment
  - Logout
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/iam/identity-center/
overlays:
  - url: overlays/sso-openapi-search.yml
    type: APIs.io Search
  - url: overlays/sso-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/iam/identity-center/
    type: Documentation
  - url: properties/sso-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/iam/identity-center/features/
    type: Features
  - url: https://aws.amazon.com/iam/identity-center/faqs/
    type: FAQ
  - url: https://aws.amazon.com/iam/identity-center/resources/
    type: Resources
description: >-
  The AWS IAM Identity Center Portal is a web service that simplifies the
  assignment of user access to IAM Identity Center resources, such as the AWS
  access portal. Users can have AWS account applications and roles assigned to
  them and be federated into the application. 

---