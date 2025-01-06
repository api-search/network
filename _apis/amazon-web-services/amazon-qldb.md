---
aid: amazon-web-services:amazon-qldb
name: Amazon QLDB
tags:
  - Command
  - Send
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/qldb/
overlays:
  - url: overlays/qldb-session-openapi-search.yml
    type: APIs.io Search
  - url: overlays/qldb-session-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/qldb/
    type: Documentation
  - url: openapi/qldb-session-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/qldb/features/
    type: Features
  - url: https://aws.amazon.com/qldb/pricing/
    type: Pricing
  - url: https://aws.amazon.com/qldb/resources/
    type: Resources
  - url: https://aws.amazon.com/qldb/faqs/
    type: FAQ
  - url: https://aws.amazon.com/qldb/customers/
    type: Customers
description: |-

  The recommended way to interact with the transactional data APIs for
  Amazon QLDB is to use the QLDB driver or the QLDB shell for executing data
  transactions on a ledger. When working with an AWS SDK, it is advised to
  use the QLDB driver, which abstracts the data plane and manages
  SendCommand API calls.

---