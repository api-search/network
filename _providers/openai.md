---
api_count: 22
apis:
- description: The Assistants API allows you to build AI assistants within your own applications. An Assistant has instructions and can leverage models, tools, and knowledge to respond to user queries. The Assistant
  name: OpenAI Assistants API
  slug: openai-assistants-api
- description: The Audio API provides two speech to text endpoints, transcriptions and translations, based on our state-of-the-art open source large-v2 Whisper model.
  name: OpenAI Audio API
  slug: openai-audio-api
- description: Given a list of messages comprising a conversation, the model will return a response., providing an AI chat interface you can use to engage with users.
  name: OpenAI Chat API
  slug: openai-chat-api
- description: Chat models take a list of messages as input and return a model-generated message as output. Although the chat format is designed to make multi-turn conversations easy, it's just as useful for single-
  name: OpenAI Chat Completions API
  slug: openai-chat-completions-api
- description: Learn how to turn text into numbers, unlocking use cases like search. OpenAI's text embeddings measure the relatedness of text strings.
  name: OpenAI Embeddings API
  slug: openai-embeddings-api
- description: Files are used to upload documents that can be used with features like Assistants and Fine-tuning. Upload a file that can be used across various endpoints. The size of all the files uploaded by one or
  name: OpenAI Files API
  slug: openai-files-api
- description: Manage fine-tuning jobs to tailor a model to your specific training data. Creates a fine-tuning job which begins the process of creating a new model from a given dataset.Response includes details of t
  name: OpenAI Fine Tuning API
  slug: openai-fine-tuning-api
- description: Learn how to generate or manipulate images with DALL_E in the API. The Images API provides three methods for interacting with images - creating images from scratch based on a text prompt, creating edi
  name: OpenAI Images API
  slug: openai-images-api
- description: List and describe the various models available in the API. You can refer to the Models documentation to understand what models are available and the differences between them.
  name: OpenAI Models API
  slug: openai-models-api
- description: Create threads that assistants can interact with.
  name: OpenAI Threads API
  slug: openai-threads-api
- description: The Responses API is OpenAI's most advanced interface for generating model responses. It combines the strengths of the Chat Completions and Assistants APIs into a single streamlined interface, support
  name: OpenAI Responses API
  slug: openai-responses-api
- description: The Moderations API can be used to check whether text or images are potentially harmful. It classifies content across several categories including harassment, hate speech, sexual content, self-harm, v
  name: OpenAI Moderations API
  slug: openai-moderations-api
- description: The Batch API enables asynchronous processing of requests with 50% cost discount, higher rate limits, and completion within 24 hours. It supports /v1/responses, /v1/chat/completions, /v1/embeddings, /
  name: OpenAI Batch API
  slug: openai-batch-api
- description: Vector stores are collections of processed files that power semantic search for the file_search tool in the Responses and Assistants APIs. When you add a file to a vector store it is automatically chu
  name: OpenAI Vector Stores API
  slug: openai-vector-stores-api
- description: The Uploads API creates an intermediate Upload object that you can add Parts to, enabling large file uploads. Currently an Upload can accept at most 8 GB in total and expires after an hour. Once you c
  name: OpenAI Uploads API
  slug: openai-uploads-api
- description: The Realtime API enables low-latency, bidirectional communication with models that natively support speech-to-speech interactions as well as multimodal inputs (audio, images, and text) and outputs (au
  name: OpenAI Realtime API
  slug: openai-realtime-api
- description: The Evals API allows you to programmatically configure and run evaluations to test model outputs against your expectations. Evaluations ensure model responses meet style and content criteria you speci
  name: OpenAI Evals API
  slug: openai-evals-api
- description: 'The legacy Completions API endpoint provides a freeform text completion interface using a text prompt. Unlike the Chat Completions endpoint which uses a list of messages, the Completions API input is '
  name: OpenAI Completions API
  slug: openai-completions-api
- description: The Videos API enables programmatic creation, extension, and remixing of videos using Sora models. It provides endpoints for creating a new render job from a text prompt, checking video status, downlo
  name: OpenAI Videos API
  slug: openai-videos-api
- description: The Conversations API allows you to create and manage stateful conversations for use with the Responses API. A conversation object contains an id, a created_at timestamp, and metadata. Because convers
  name: OpenAI Conversations API
  slug: openai-conversations-api
- description: 'The Containers API manages sandboxed containers used by Code Interpreter for running Python, data work, file transforms, and iterative debugging. Containers can be created explicitly or auto-managed, '
  name: OpenAI Containers API
  slug: openai-containers-api
- description: ChatKit is the best way to build agentic chat experiences. It provides session and thread management for building internal knowledge base assistants, research companions, support agents, and more. Cha
  name: OpenAI ChatKit API
  slug: openai-chatkit-api
capabilities:
- description: Unified content generation combining Chat, Images, Audio, and Embeddings APIs for developers to generate text, images, speech, and vector representations.
  name: OpenAI Content Generation
  slug: content-generation
common:
- title: ''
  type: Portal
  url: https://platform.openai.com/docs/overview
- title: ''
  type: GettingStarted
  url: https://platform.openai.com/docs/quickstart
- title: ''
  type: SDKs
  url: https://platform.openai.com/docs/libraries
- title: ''
  type: Forums
  url: https://community.openai.com/categories
- title: ''
  type: RateLimits
  url: https://platform.openai.com/docs/guides/rate-limits
- title: ''
  type: Deprecations
  url: https://platform.openai.com/docs/deprecations
- title: ''
  type: TermsOfService
  url: https://openai.com/policies/
- title: ''
  type: TermsOfService
  url: https://openai.com/policies/terms-of-use/
- title: ''
  type: PrivacyPolicy
  url: https://openai.com/policies/privacy-policy/
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/overview
- title: ''
  type: Support
  url: https://help.openai.com/en
- title: ''
  type: Status
  url: https://status.openai.com/
- title: ''
  type: Authentication
  url: https://platform.openai.com/docs/api-reference/authentication
- title: ''
  type: Webhooks
  url: https://platform.openai.com/docs/api-reference/webhook_events/response
- title: ''
  type: OpenAPI
  url: properties/openai-openapi
- title: ''
  type: JSONSchema
  url: json-schema/openai-chat-completion-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/openai-embedding-schema.json
- title: ''
  type: JSONLD
  url: json-ld/openai-context.jsonld
- title: ''
  type: GitHubOrganization
  url: https://github.com/openai
- title: ''
  type: Plans
  url: https://openai.com/api/pricing/
- title: ''
  type: Pricing
  url: https://openai.com/api/pricing/
- title: ''
  type: Tiers
  url: https://openai.com/api/pricing/
- title: ''
  type: RateLimits
  url: https://example.com/rate-limits
- title: ''
  type: StatusPage
  url: https://status.openai.com/
- title: ''
  type: API Keys
  url: https://platform.openai.com/api-keys
- title: ''
  type: Signup
  url: https://platform.openai.com/signup
- title: ''
  type: Login
  url: https://platform.openai.com/login
- title: ''
  type: ChangeLog
  url: https://developers.openai.com/changelog/
- title: ''
  type: Blog
  url: https://developers.openai.com/blog/
- title: ''
  type: Cookbook
  url: https://cookbook.openai.com/
- title: ''
  type: SafetyBestPractices
  url: https://platform.openai.com/docs/guides/safety-best-practices
- title: ''
  type: BestPractices
  url: https://platform.openai.com/docs/guides/production-best-practices
- title: ''
  type: Security
  url: https://openai.com/security-and-privacy/
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/administration
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/audit-logs
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/usage
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/guides/function-calling
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/guides/structured-outputs
- title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-openapi
- title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-python
- title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-node
- title: ''
  type: TermsOfService
  url: https://openai.com/policies/service-terms/
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/guides/webhooks
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/webhook-events
- title: ''
  type: Documentation
  url: https://developers.openai.com/api/docs/guides/deep-research/
- title: ''
  type: Documentation
  url: https://developers.openai.com/api/docs/guides/voice-agents/
- title: ''
  type: Documentation
  url: https://developers.openai.com/api/docs/guides/code-generation/
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/guides/images-vision
- title: ''
  type: Documentation
  url: https://developers.openai.com/api/docs/guides/conversation-state/
- title: ''
  type: Documentation
  url: https://developers.openai.com/api/docs/guides/migrate-to-responses/
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/containers
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/container-files
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/chatkit
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/videos
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/conversations/create
- title: ''
  type: Portal
  url: https://developers.openai.com/
- title: ''
  type: Documentation
  url: https://developers.openai.com/api/reference/
- title: ''
  type: Documentation
  url: https://developers.openai.com/codex
- title: ''
  type: GitHubRepository
  url: https://github.com/openai/chatkit-js
- title: ''
  type: SpectralRules
  url: rules/openai-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/openai-vocabulary.yaml
created: '2024-04-14'
description: APIs for accessing OpenAI's artificial intelligence models including GPT, DALL-E, Whisper, and Embeddings.
features:
- description: Generate conversational responses using GPT models with multi-turn message history, function calling, and structured outputs.
  name: Chat Completions
- description: Advanced model response interface combining Chat Completions and Assistants with built-in tools like web search and code interpreter.
  name: Responses API
- description: Build AI assistants with persistent threads, code interpreter, file search, and function calling capabilities.
  name: Assistants
- description: Low-latency bidirectional communication for speech-to-speech interactions via WebRTC, WebSocket, and SIP connections.
  name: Realtime API
- description: Create, edit, and generate variations of images using DALL-E models from text prompts.
  name: Image Generation
- description: Text-to-speech synthesis and speech-to-text transcription and translation using Whisper and TTS models.
  name: Audio and Speech
- description: Generate vector representations of text for semantic search, clustering, and recommendation use cases.
  name: Embeddings
- description: Customize models on your own training data to improve performance for specific tasks and domains.
  name: Fine-Tuning
- description: Asynchronous processing of up to 50,000 requests at 50% cost discount with 24-hour completion window.
  name: Batch Processing
- description: Programmatically configure and run evaluations to test model outputs against quality and content criteria.
  name: Evals
- description: Create, extend, and remix videos using Sora models from text prompts via the Videos API.
  name: Video Generation
- description: Managed document storage with automatic chunking, embedding, and semantic search for file_search tool.
  name: Vector Stores
image: https://openai.com/favicon.ico
integrations:
- description: Official Python client library for accessing all OpenAI API endpoints with async support and streaming.
  name: Python SDK
- description: Official TypeScript and JavaScript client library for server-side and edge runtime OpenAI API integration.
  name: Node.js SDK
- description: Run OpenAI models on Azure infrastructure with enterprise security, compliance, and regional data residency.
  name: Microsoft Azure OpenAI
- description: Framework integration for building LLM-powered applications with chains, agents, and retrieval-augmented generation.
  name: LangChain
- description: Integration with Vercel AI SDK for building streaming AI-powered web applications with React and Next.js.
  name: Vercel AI SDK
- description: No-code automation integration connecting OpenAI to thousands of apps for automated AI-powered workflows.
  name: Zapier
jsonld:
- class_count: 0
  name: Openai Audio Context
  property_count: 0
  slug: openai-audio-context
- class_count: 0
  name: Openai Chat Completions Context
  property_count: 0
  slug: openai-chat-completions-context
- class_count: 0
  name: Openai Context
  property_count: 15
  slug: openai-context
- class_count: 0
  name: Openai Embeddings Context
  property_count: 0
  slug: openai-embeddings-context
- class_count: 0
  name: Openai Images Context
  property_count: 0
  slug: openai-images-context
layout: provider
modified: '2026-04-18'
name: OpenAI
rules:
- name: OpenAI API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: openai-spectral-rules
skills: []
slug: openai
solutions: []
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/apis.yml
use_cases:
- description: Build chatbots, virtual assistants, and customer support agents using Chat Completions or Responses API.
  name: Conversational AI
- description: Generate marketing copy, articles, product descriptions, and creative writing with controllable tone and style.
  name: Content Generation
- description: Automate code writing, debugging, refactoring, and documentation generation across programming languages.
  name: Code Generation
- description: Extract, summarize, and answer questions from uploaded documents using Assistants with file search.
  name: Document Analysis
- description: Build real-time voice-based AI agents for customer service, sales, and interactive experiences.
  name: Voice Agents
- description: Implement intelligent search using embeddings and vector stores for knowledge bases and document retrieval.
  name: Semantic Search
- description: Automatically classify and filter harmful content across text and images using the Moderations API.
  name: Content Moderation
- description: Extract structured data from unstructured text using function calling and structured outputs.
  name: Data Extraction
---
