---
aid: openai:openai-chat-api
name: OpenAI Chat API
tags:
  - Chat
  - Completions
  - Conversations
  - Creates
  - Given
  - Models
  - Responses
score: 149
baseURL: https://api.openai.com
humanURL: https://platform.openai.com/docs/api-reference/chat
overlays:
  - url: >-

      overlays/https://github.com/apis-json/artisanal/tree/main/apis/openai/chat-openapi-search.yml
    type: APIs.io Search
  - url: overlays/chat-openapi-search.yml
    type: APIs.io Search
  - url: overlays/chat-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://platform.openai.com/docs/api-reference/chat
    type: Documentation
  - url: openapi/chat-openapi-original.yml
    type: OpenAPI
description: |-

  Given a list of messages comprising a conversation, the model will return
  a response., providing an AI chat interface you can use to engage with
  users.

---