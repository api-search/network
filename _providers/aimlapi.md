---
api_count: 1
apis:
- description: Access 400+ AI models from 40+ providers via a single OpenAI-compatible REST API. Supports chat completions, image generation, video generation, speech models, embeddings, music generation, and vision
  name: AIMLAPI
  slug: aimlapi
capabilities:
- description: Unified workflow for accessing 400+ AI models via AIMLAPI gateway including chat completions, image generation, embeddings, and model discovery. Used by developers building AI-powered applications.
  name: AIMLAPI AI Model Operations
  slug: ai-model-operations
common:
- title: ''
  type: GitHubOrganization
  url: https://github.com/aimlapi
- title: ''
  type: Blog
  url: https://aimlapi.com/blog
- title: ''
  type: Pricing
  url: https://aimlapi.com/ai-ml-api-pricing
- title: ''
  type: Documentation
  url: https://docs.aimlapi.com/
- title: ''
  type: FAQ
  url: https://docs.aimlapi.com/faq/can-i-use-api-in-python
- title: ''
  type: ChangeLog
  url: https://aimlapi.com/changelog
- title: ''
  type: SignUp
  url: https://aimlapi.com/app/sign-up/
- title: ''
  type: Affiliate
  url: https://aimlapi.com/affiliate
- title: ''
  type: PrivacyPolicy
  url: https://aimlapi.com/privacy-policy
- title: ''
  type: TermsOfService
  url: https://aimlapi.com/terms-and-conditions
- title: ''
  type: SpectralRules
  url: rules/aimlapi-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/ai-model-operations.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/aimlapi-vocabulary.yaml
created: '2025-01-07'
description: AIMLAPI is a unified AI model API gateway providing access to 400+ state-of-the-art AI models from OpenAI, Anthropic, Google, Meta, DeepSeek, Mistral, Stability AI, and 40+ other providers through a single OpenAI-compatible API. Supported modalities include text/chat LLMs, image generation, video generation, music generation, speech-to-text, text-to-speech, vision/OCR, embeddings, and 3D generation.
features:
- description: Access to 400+ models from OpenAI, Anthropic, Google, Meta, DeepSeek, Mistral, Stability AI, and 40+ providers.
  name: 400+ AI Models
- description: Drop-in replacement for OpenAI API — use existing OpenAI client libraries with AIMLAPI endpoint.
  name: OpenAI-Compatible API
- description: Chat completions, completion, function calling, streaming, reasoning, and code generation.
  name: Text and Chat Completions
- description: Generate images via DALL-E, Flux, Stable Diffusion, and other image generation models.
  name: Image Generation
- description: Generate video via Sora 2, Runway, and other video generation models.
  name: Video Generation
- description: Text-to-speech and speech-to-text transcription via Whisper and other speech models.
  name: Speech Models
- description: AI music generation via dedicated music models.
  name: Music Generation
- description: Image understanding, visual question answering, and OCR via vision-capable LLMs.
  name: Vision and OCR
- description: Generate vector embeddings for semantic search and RAG applications.
  name: Embeddings
- description: Online playground for experimenting with all available models without writing code.
  name: Playground
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Use the official OpenAI Python and Node.js SDKs with AIMLAPI base URL.
  name: OpenAI SDK
- description: Integrate AIMLAPI models with LangChain for agentic AI workflows.
  name: LangChain
- description: Use AIMLAPI with LlamaIndex for RAG and document intelligence pipelines.
  name: LlamaIndex
- description: Build AI-powered web apps using Vercel AI SDK with AIMLAPI as backend.
  name: Vercel AI SDK
- description: Native Python integration via requests library or OpenAI client.
  name: Python
- description: Node.js integration via OpenAI npm package pointed at AIMLAPI endpoint.
  name: Node.js
jsonld:
- class_count: 5
  name: Aimlapi Context
  property_count: 10
  slug: aimlapi-context
layout: provider
modified: '2026-04-19'
name: AIMLAPI
rules:
- name: AIMLAPI API Rules
  rule_count: 15
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 8
  slug: aimlapi-spectral-rules
skills: []
slug: aimlapi
solutions: []
tags:
- Artificial Intelligence
- Machine Learning
- AI Models
- LLM
- Image Generation
- Video Generation
- Speech
- Embeddings
- API Gateway
- Developer Tools
url: https://raw.githubusercontent.com/api-evangelist/aimlapi/refs/heads/main/apis.yml
use_cases:
- description: Build conversational AI chatbots and virtual assistants using leading LLMs.
  name: AI Chatbot Development
- description: Automate text, image, video, and music content generation for media and marketing.
  name: Content Generation
- description: Build retrieval-augmented generation applications using embeddings and LLMs.
  name: RAG Applications
- description: Integrate AI code generation and review capabilities into developer tools.
  name: Code Generation
- description: Extract information and summarize documents using vision and LLM models.
  name: Document Processing
- description: Add speech-to-text transcription and text-to-speech synthesis to applications.
  name: Voice Applications
---
