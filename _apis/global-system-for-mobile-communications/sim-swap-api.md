---
aid: global-system-for-mobile-communications:sim-swap-api
name: GSMA Camara Project SIM Swap API
tags:
  - Anti Fraud
  - Subscribers
  - SIM
  - Swaps
humanURL: >-
  https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
properties:
  - url: https://github.com/camaraproject/SimSwap/releases/tag/r1.3
    type: GitHubRepository
  - url: >-
      https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/SimSwap/r1.3/code/API_definitions/sim-swap.yaml&nocors
    type: Documentation
  - url: openapi/sim-swap-api-openapi.yml
    type: OpenAPI
  - url: bruno/GSMA Camara Project SIM Swap API/bruno.json
    type: BrunoCollection
  - url: >-
      https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/1ohhvf0/gsma-camara-project-sim-swap-api
    type: PostmanCollection
description: >-
  SIM Swap API checks the last date that the SIM card associated with a mobile
  phone number has changed. The response may be a timestamp or a yes/no for a
  defined period (e.g. last 24h).

---