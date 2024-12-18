---
aid: global-system-for-mobile-communications:device-location-verification-api
name: GSMA Camara Project Device Location Verification API
tags:
  - Mobile
  - Connectivity
  - Location
  - Devices
humanURL: >-
  https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
properties:
  - url: https://github.com/camaraproject/DeviceLocation
    type: GitHubRepository
  - url: >-
      https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/DeviceLocation/r1.2/code/API_definitions/location-verification.yaml&nocors
    type: Documentation
  - url: properties/device-location-verification-api-openapi.yml
    type: OpenAPI
  - url: bruno/GSMA Camara Project Device Location Verification API/bruno.json
    type: BrunoCollection
  - url: >-
      https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/35240-23a17d7b-07a0-405e-896b-6c4f3f4cc8c6
    type: PostmanCollection
description: >-
  Device Location Verification API checks if a mobile device is in proximity of
  a given location. The API request contains the location to be checked and an
  accuracy range in km (between 2km and 200km). The API response indicates
  whether the location is within the accuracy range of the last known location
  of the MSISDN.

---