---
aid: openai:openai-files-api
name: OpenAI Files API
tags:
  - Files
  - Artificial Intelligence
  - AI
score: 894
baseURL: https://api.openai.com
humanURL: https://platform.openai.com/docs/api-reference/files
overlays:
  - url: overlays/files-openapi-search.yml
    type: APIs.io Search
  - url: overlays/files-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://platform.openai.com/docs/api-reference/files
    type: Documentation
  - url: properties/files-openapi-original.yml
    type: OpenAPI
description: >-
  Files are used to upload documents that can be used with features like
  Assistants and Fine-tuning. Upload a file that can be used across various
  endpoints. The size of all the files uploaded by one organization can be up to
  100 GB.

---