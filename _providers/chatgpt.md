---
api_count: 13
apis:
- description: API for accessing OpenAI's ChatGPT language models for chat completions and conversations.
  name: ChatGPT API
  slug: ''
- description: The Responses API is OpenAI's recommended API primitive for new projects, an evolution of Chat Completions with built-in tools like web search, file search, code interpreter, and support for agentic w
  name: OpenAI Responses API
  slug: ''
- description: API for generating embedding vectors from input text using models like text-embedding-3-small and text-embedding-3-large, useful for search, clustering, and recommendations.
  name: OpenAI Embeddings API
  slug: ''
- description: API for generating and editing images from text prompts using DALL-E and GPT Image models, supporting image generations, edits, and variations.
  name: OpenAI Images API
  slug: ''
- description: API for audio capabilities including text-to-speech generation, speech transcription, and translation using Whisper and other audio models.
  name: OpenAI Audio API
  slug: ''
- description: API for classifying text and images to detect potentially harmful content across categories like hate, violence, and self-harm.
  name: OpenAI Moderations API
  slug: ''
- description: API for creating and managing fine-tuning jobs to customize OpenAI models on your own training data, supporting supervised fine-tuning and direct preference optimization.
  name: OpenAI Fine-Tuning API
  slug: ''
- description: API for uploading and managing files used across OpenAI features including fine-tuning, assistants, batch processing, and vision.
  name: OpenAI Files API
  slug: ''
- description: API for sending asynchronous groups of requests at lower cost with a separate pool of significantly higher rate limits, supporting chat completions, embeddings, and completions endpoints.
  name: OpenAI Batch API
  slug: ''
- description: API for uploading large files in multiple parts, supporting files up to 8 GB for use with fine-tuning, assistants, and batch processing.
  name: OpenAI Uploads API
  slug: ''
- description: API for creating and managing vector stores used by the file search tool, supporting collections of processed files for retrieval-augmented generation.
  name: OpenAI Vector Stores API
  slug: ''
- description: API for real-time multimodal communication with models over WebRTC, WebSocket, and SIP, supporting speech-to-speech, text, image, and audio inputs and outputs with ultra-low latency.
  name: OpenAI Realtime API
  slug: ''
- description: API for listing and retrieving information about available OpenAI models, including details on permissions and capabilities.
  name: OpenAI Models API
  slug: ''
common:
- title: ''
  type: Portal
  url: https://platform.openai.com
- title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference
- title: ''
  type: GettingStarted
  url: https://platform.openai.com/docs/quickstart
- title: ''
  type: Authentication
  url: https://platform.openai.com/docs/api-reference/authentication
- title: ''
  type: Pricing
  url: https://openai.com/pricing
- title: ''
  type: RateLimits
  url: https://platform.openai.com/docs/guides/rate-limits
- title: ''
  type: ChangeLog
  url: https://platform.openai.com/docs/changelog
- title: ''
  type: Blog
  url: https://openai.com/blog
- title: ''
  type: StatusPage
  url: https://status.openai.com
- title: ''
  type: Support
  url: https://help.openai.com
- title: ''
  type: GitHubOrganization
  url: https://github.com/openai
- title: ''
  type: SDK
  url: https://developers.openai.com/api/docs/libraries/
- title: ''
  type: CodeExamples
  url: https://cookbook.openai.com/
- title: ''
  type: OpenAPI
  url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
- title: ''
  type: TermsOfService
  url: https://openai.com/terms
- title: ''
  type: PrivacyPolicy
  url: https://openai.com/privacy
- title: ''
  type: Security
  url: https://openai.com/business-data/
- title: ''
  type: Models
  url: https://platform.openai.com/docs/models
- title: ''
  type: SignUp
  url: https://platform.openai.com/signup
- title: ''
  type: Login
  url: https://platform.openai.com/login
created: '2024'
description: OpenAI's ChatGPT API for conversational AI and language model interactions.
features:
- description: Generate conversational responses using GPT models with support for text, function calling, structured outputs, vision inputs, and streaming.
  name: Chat Completions
- description: Next-generation API with built-in tools for web search, file search, computer use, and code interpreter supporting agentic workflows.
  name: Responses API
- description: Generate vector representations of text for search, clustering, classification, and recommendation use cases.
  name: Embeddings
- description: Create and edit images from text prompts using DALL-E and GPT Image models.
  name: Image Generation
- description: Text-to-speech generation, speech transcription, and translation using Whisper and other audio models.
  name: Audio and Speech
- description: Classify text and images to detect potentially harmful content across safety categories.
  name: Content Moderation
- description: Customize OpenAI models on your own training data for domain-specific performance improvements.
  name: Fine-Tuning
- description: Send asynchronous groups of requests at lower cost with higher rate limits.
  name: Batch Processing
- description: Ultra-low latency multimodal communication over WebRTC, WebSocket, and SIP.
  name: Realtime Communication
- description: Manage collections of processed files for retrieval-augmented generation with the file search tool.
  name: Vector Stores
image: https://openai.com/content/images/2023/05/openai-avatar.png
integrations:
- description: Deploy OpenAI models on Azure infrastructure with enterprise security, compliance, and regional availability.
  name: Microsoft Azure OpenAI
- description: Build LLM-powered applications using the LangChain framework with OpenAI model providers.
  name: LangChain
- description: Connect ChatGPT to thousands of apps for automated workflows without code.
  name: Zapier
- description: Integrate ChatGPT into Slack workspaces for team collaboration and AI-assisted communication.
  name: Slack
jsonld:
- class_count: 0
  name: Chatgpt Chat Completions Context
  property_count: 0
  slug: chatgpt-chat-completions-context
- class_count: 0
  name: Chatgpt Context
  property_count: 16
  slug: chatgpt-context
- class_count: 0
  name: Chatgpt Responses Context
  property_count: 0
  slug: chatgpt-responses-context
layout: provider
modified: '2026-04-18'
name: ChatGPT
rules:
- name: ChatGPT API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: chatgpt-spectral-rules
skills: []
slug: chatgpt
solutions: []
tags:
- Agents
- AI
- ChatGPT
- Embeddings
- Fine-Tuning
- GPT-4
- GPT-5
- Language Model
- OpenAI
- Realtime
url: https://platform.openai.com/docs/api-reference
use_cases:
- description: Build AI-powered chatbots and support agents that handle customer inquiries, troubleshoot issues, and escalate complex cases.
  name: Customer Support Automation
- description: Generate marketing copy, blog posts, product descriptions, and creative content at scale.
  name: Content Generation
- description: Help developers write, review, debug, and explain code across multiple programming languages.
  name: Code Assistance
- description: Extract insights from unstructured text, summarize documents, and perform sentiment analysis.
  name: Data Analysis
- description: Build applications that process text, images, and audio inputs together for richer user experiences.
  name: Multimodal Applications
- description: Create autonomous AI agents that use tools, search the web, and execute multi-step tasks.
  name: Agentic Workflows
---
