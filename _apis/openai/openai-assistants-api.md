---
aid: openai:openai-assistants-api
name: OpenAI Assistants API
tags:
  - Assistants
  - Attaching
  - File
  - Files
  - Instructions
  - Models
  - Modifies
  - Returns
score: 1329
baseURL: https://api.openai.com
humanURL: https://platform.openai.com/docs/assistants/overview
overlays:
  - url: >-
      overlays/https://github.com/apis-json/artisanal/tree/main/apis/openai/assistants-openapi-search.yml
    type: APIs.io Search
  - url: overlays/assistants-openapi-search.yml
    type: APIs.io Search
  - url: overlays/assistants-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://platform.openai.com/docs/assistants/overview
    type: Documentation
  - url: properties/assistants-openapi-original.yml
    type: OpenAPI
description: >-
  The Assistants API allows you to build AI assistants within your own
  applications. An Assistant has instructions and can leverage models, tools,
  and knowledge to respond to user queries. The Assistants API currently
  supports three types of tools - Code Interpreter, Retrieval, and Function
  calling. In the future, we plan to release more OpenAI-built tools, and allow
  you to provide your own tools on our platform.

---