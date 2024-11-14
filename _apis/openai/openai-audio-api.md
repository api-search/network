---
aid: openai:openai-audio-api
name: OpenAI Audio API
tags:
  - Audio
  - English
  - Generates
  - Inputs
  - Languages
  - Speech
  - Text
  - Transcribes
  - Transcriptions
  - Translations
score: 128
baseURL: https://api.openai.com
humanURL: https://platform.openai.com/docs/guides/text-to-speech
overlays:
  - url: >-
      overlays/https://github.com/apis-json/artisanal/tree/main/apis/openai/audio-openapi-search.yml
    type: APIs.io Search
  - url: overlays/audio-openapi-search.yml
    type: APIs.io Search
  - url: overlays/audio-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://platform.openai.com/docs/guides/text-to-speech
    type: Documentation
  - url: properties/audio-openapi-original.yml
    type: OpenAPI
description: >-
  The Audio API provides two speech to text endpoints, transcriptions and
  translations, based on our state-of-the-art open source large-v2 Whisper
  model.

---