---
aid: openai:openai-chat-completions-api
name: OpenAI Chat Completions API
tags:
  - Chat
  - Completions
  - Conversations
  - Creates
  - Given
  - Models
  - Parameters
  - Prompts
  - Provided
  - Responses
score: 281
baseURL: https://api.openai.com
humanURL: https://platform.openai.com/docs/api-reference/chat
overlays:
  - url: >-

      overlays/https://github.com/apis-json/artisanal/tree/main/apis/openai/completions-openapi-search.yml
    type: APIs.io Search
  - url: overlays/completions-openapi-search.yml
    type: APIs.io Search
  - url: overlays/completions-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://platform.openai.com/docs/api-reference/chat
    type: Documentation
  - url: openapi/completions-openapi-original.yml
    type: OpenAPI
description: |-

  Chat models take a list of messages as input and return a model-generated
  message as output. Although the chat format is designed to make multi-turn
  conversations easy, it's just as useful for single-turn tasks without any
  conversation.

---