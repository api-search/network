---
aid: hubspot:hubspot-domains-api
name: HubSpot Domains API
tags:
  - Domains
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developers.hubspot.com/docs/api/overview
overlays:
  - url: >-

      overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/domains-openapi-search.yml
    type: APIs.io Search
properties:
  - url: https://developers.hubspot.com/docs/api/cms/domains
    type: Documentation
  - url: properties/hubspot-domains-api-openapi.yml
    type: OpenAPI
description: |-

  These endpoints allow you to return information about the domains
  connected to a particular HubSpot CMS site. You can return data for a list
  of domains or specify a domain by ID.

---