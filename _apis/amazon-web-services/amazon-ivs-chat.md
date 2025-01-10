---
aid: amazon-web-services:amazon-ivs-chat
name: Amazon IVS Chat
tags:
  - ARN
  - Chat
  - Configurations
  - Disconnect
  - Events
  - Logging
  - Messages
  - Resources
  - Rooms
  - Send
  - Tags
  - Tokens
  - Untag
  - Users
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://aws.amazon.com/ivs/features/chat/
overlays:
  - url: overlays/ivschat-openapi-search.yml
    type: APIs.io Search
  - url: overlays/ivschat-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://aws.amazon.com/ivs/features/chat/
    type: Documentation
  - url: openapi/ivschat-openapi-original.yml
    type: OpenAPI
description: |-

  The Amazon IVS Chat control-plane API allows you to create and manage
  resources for Amazon IVS Chat, and integrate with the Amazon IVS Chat
  Messaging API for real-time chat room interactions. This regional AWS
  service includes resources such as LoggingConfiguration and Room, which
  can be tagged for organization and access management.

---