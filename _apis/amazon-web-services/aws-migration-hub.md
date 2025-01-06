---
aid: amazon-web-services:aws-migration-hub
name: AWS Migration Hub
tags:
  - Attributes
  - Migrations
  - Resources
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/migration-hub/
overlays:
  - url: overlays/awsmigrationhub-openapi-search.yml
    type: APIs.io Search
  - url: overlays/awsmigrationhub-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/migration-hub/
    type: Documentation
  - url: openapi/awsmigrationhub-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/migration-hub/features/
    type: Features
  - url: https://aws.amazon.com/migration-hub/pricing/
    type: Pricing
  - url: https://aws.amazon.com/migration-hub/getting-started/
    type: Getting Started
  - url: https://aws.amazon.com/migration-hub/resources/
    type: Resources
  - url: https://aws.amazon.com/migration-hub/faqs/
    type: FAQ
  - url: https://aws.amazon.com/migration-hub/partners/
    type: Partners
description: |-

  The AWS Migration Hub API provides users with the ability to view server
  and application migration progress and easily incorporate
  resource-specific migration tools through a code-based interface. To
  ensure smooth operation, it is crucial to specify your AWS Migration Hub
  home region before using any API functions to prevent encountering a
  HomeRegionNotSetException error. Furthermore, all API requests should
  originate from within your assigned home region for proper functioning.

---