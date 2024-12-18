---
aid: amazon-web-services:servicediscovery
name: AWS Cloud Map
tags:
  - Services
  - Clouds
  - Maps
  - DNS
  - Namespaces
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/cloud-map/
overlays:
  - url: overlays/servicediscovery-openapi-search.yml
    type: APIs.io Search
  - url: overlays/servicediscovery-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/cloud-map/
    type: Documentation
  - url: properties/servicediscovery-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/cloud-map/features/
    type: Features
  - url: https://aws.amazon.com/cloud-map/pricing/
    type: Pricing
  - url: https://aws.amazon.com/cloud-map/faqs/
    type: FAQ
description: >-
  Our Cloud Map API allows you to easily set up and manage public DNS, private
  DNS, or HTTP namespaces for your microservice applications. By registering
  instances with Cloud Map via the API, you can ensure seamless integration and
  availability. Cloud Map automatically creates DNS records and optional health
  checks for public or private DNS namespaces, providing clients with up to
  eight healthy records in response to queries or requests.

---