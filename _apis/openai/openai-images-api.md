---
aid: openai:openai-images-api
name: OpenAI Images API
tags:
  - Creates
  - Edited
  - Edits
  - Extended
  - Generations
  - Given
  - Images
  - Original
  - Prompts
  - Variations
score: 120
baseURL: https://api.openai.com
humanURL: https://platform.openai.com/docs/guides/images
overlays:
  - url: overlays/images-openapi-search.yml
    type: APIs.io Search
  - url: overlays/images-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: https://platform.openai.com/docs/guides/images
    type: Documentation
  - url: properties/images-openapi-original.yml
    type: OpenAPI
description: >-
  Learn how to generate or manipulate images with DALL_E in the API. The Images
  API provides three methods for interacting with images - creating images from
  scratch based on a text prompt, creating edited versions of images by having
  the model replace some areas of a pre-existing image, based on a new text
  prompt, Creating variations of an existing image.

---