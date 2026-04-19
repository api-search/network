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
- api gateway
- video generation
- artificial intelligence
- ai model inference across modalities
- chat completions via 400+ llms
- machine learning
- generate image
- create a chat completion
- list all models
- create image
- speech
- AI Engineer
- embeddings
- ai engineer evaluating and comparing models for ml pipelines
- discover all 400+ available ai models on aimlapi platform
- generate an image
- generate an image from a text prompt using aimlapi image generation models
- create embeddings
- generate embeddings
- llm
- create embedding
- generate a chat response from any of 400+ ai language models via aimlapi
- access 400+ ai models for chat, image generation, embeddings, and model discovery
- developer tools
- image generation
- developer integrating ai capabilities into applications via aimlapi
- list available models
- ai models
- Developer
- generate vector embeddings for semantic search and rag applications
- api key management and model discovery
- list models
- create chat completion
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
