---
aid: global-system-for-mobile-communications:one-time-password-api
name: GSMA Camara Project One Time Password API
tags:
  - Anti Fraud
  - Subscribers
  - Identity
  - Passwords
humanURL: >-
  https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
properties:
  - url: https://github.com/camaraproject/OTPValidation/releases/tag/r1.2
    type: GitHubRepository
  - url: >-
      https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/OTPValidation/r1.2/code/API_definitions/one-time-password-sms.yaml&nocors
    type: Documentation
  - url: openapi/one-time-password-api-openapi.yml
    type: OpenAPI
  - url: bruno/GSMA Camara Project One Time Password SMS/bruno.json
    type: BrunoCollection
  - url: >-
      https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/lm2bnug/gsma-camara-project-one-time-password-sms
    type: PostmanCollection
description: >-
  One Time Password API delivers a short-lived one-time password to a mobile
  phone number via SMS. The API then validates the code as input by the end-user
  into the service, to verify proof of possession.

---