---
consumed_apis:
- aimlapi
description: Unified workflow for accessing 400+ AI models via AIMLAPI gateway including chat completions, image generation, embeddings, and model discovery. Used by developers building AI-powered applications.
layout: capability
name: AIMLAPI AI Model Operations
operations:
- description: Create a chat completion
  method: POST
  name: create-chat-completion
  path: /v1/chat/completions
- description: Generate an image
  method: POST
  name: create-image
  path: /v1/images/generations
- description: Create embeddings
  method: POST
  name: create-embedding
  path: /v1/embeddings
- description: List all models
  method: GET
  name: list-models
  path: /v1/models
personas: []
provider_name: AIMLAPI
provider_slug: aimlapi
search_terms:
- generate vector embeddings for semantic search and rag applications
- discover all 400+ available ai models on aimlapi platform
- video generation
- image generation
- create chat completion
- api gateway
- AI Engineer
- list models
- generate an image from a text prompt using aimlapi image generation models
- machine learning
- api key management and model discovery
- embeddings
- list available models
- create embedding
- list all models
- Developer
- ai models
- developer integrating ai capabilities into applications via aimlapi
- ai engineer evaluating and comparing models for ml pipelines
- generate an image
- generate a chat response from any of 400+ ai language models via aimlapi
- create image
- generate embeddings
- ai model inference across modalities
- create a chat completion
- developer tools
- access 400+ ai models for chat, image generation, embeddings, and model discovery
- speech
- chat completions via 400+ llms
- artificial intelligence
- llm
- create embeddings
- generate image
slug: ai-model-operations
tags:
- Artificial Intelligence
- LLM
- Image Generation
- Embeddings
- Developer Tools
- API Gateway
tools:
- description: Generate a chat response from any of 400+ AI language models via AIMLAPI
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-chat-completion
- description: Generate an image from a text prompt using AIMLAPI image generation models
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: generate-image
- description: Generate vector embeddings for semantic search and RAG applications
  hints:
    openWorld: true
    readOnly: true
  name: create-embedding
- description: Discover all 400+ available AI models on AIMLAPI platform
  hints:
    openWorld: true
    readOnly: true
  name: list-models
---
