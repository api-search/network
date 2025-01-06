---
aid: amazon-web-services:amazon-lex
name: Amazon Lex
tags:
  - Alias
  - Bots
  - Content
  - Conversational
  - Names
  - Posts
  - Sessions
  - Text
  - Users
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/lex/
overlays:
  - url: overlays/runtimelex-openapi-search.yml
    type: APIs.io Search
  - url: overlays/runtimelex-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/lex/
    type: Documentation
  - url: openapi/runtimelex-openapi-original.yml
    type: OpenAPI
  - url: https://aws.amazon.com/lex/features/
    type: Features
  - url: https://aws.amazon.com/lex/pricing/
    type: Pricing
  - url: https://aws.amazon.com/lex/faqs/
    type: FAQ
  - url: https://aws.amazon.com/lex/getting-started/
    type: Getting Started
  - url: https://aws.amazon.com/lex/resources/
    type: Resources
  - url: https://aws.amazon.com/lex/customers/
    type: Customers
description: |-

  Amazon Lex offers build and runtime endpoints, each with a specific set of
  operations. Your conversational bot utilizes the runtime API to interpret
  user input text or voice. For instance, if a user says "I want pizza," the
  bot sends this input to Amazon Lex via the runtime API. 

---