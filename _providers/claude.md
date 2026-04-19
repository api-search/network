---
api_count: 7
apis:
- description: Primary API for sending messages to Claude and receiving responses.
  name: Claude Messages API
  slug: ''
- description: API for asynchronously processing large volumes of message requests at reduced cost with 50 percent discount.
  name: Claude Message Batches API
  slug: ''
- description: API for listing and retrieving metadata about available Claude models including capabilities and context windows.
  name: Claude Models API
  slug: ''
- description: API for uploading and managing files to reference in Claude API requests without re-uploading content each time.
  name: Claude Files API
  slug: ''
- description: API for programmatically managing organization resources including members workspaces API keys and invites.
  name: Claude Admin API
  slug: ''
- description: API for tracking token consumption and costs across your organization with breakdowns by model workspace and service tier.
  name: Claude Usage and Cost API
  slug: ''
- description: Legacy API for generating text completions - deprecated in favor of the Messages API.
  name: Claude Text Completions API
  slug: ''
capabilities:
- description: Unified workflow for AI-powered messaging, token counting, batch processing, and model discovery. Used by AI application developers and data scientists.
  name: Claude AI Messaging
  slug: ai-messaging
common:
- title: ''
  type: Portal
  url: https://console.anthropic.com
- title: ''
  type: Documentation
  url: https://docs.anthropic.com
- title: ''
  type: GettingStarted
  url: https://docs.anthropic.com/en/docs/get-started
- title: ''
  type: Pricing
  url: https://www.anthropic.com/pricing
- title: ''
  type: RateLimits
  url: https://docs.anthropic.com/en/api/rate-limits
- title: ''
  type: Authentication
  url: https://docs.anthropic.com/en/api/getting-started
- title: ''
  type: ChangeLog
  url: https://docs.anthropic.com/en/release-notes/api
- title: ''
  type: StatusPage
  url: https://status.anthropic.com
- title: ''
  type: Blog
  url: https://www.anthropic.com/news
- title: ''
  type: Support
  url: https://support.anthropic.com
- title: ''
  type: TermsOfService
  url: https://www.anthropic.com/legal/commercial-terms
- title: ''
  type: PrivacyPolicy
  url: https://www.anthropic.com/legal/privacy
- title: ''
  type: GitHubOrganization
  url: https://github.com/anthropics
- title: ''
  type: SpectralRules
  url: rules/claude-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/claude-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/ai-messaging.yaml
created: '2024'
description: Anthropic's Claude AI assistant API for natural language processing and conversation.
features:
- description: Maintain context across multiple message exchanges for natural dialogue interactions.
  name: Multi-Turn Conversations
- description: Enable Claude to call external tools and functions to perform actions and retrieve data.
  name: Tool Use
- description: Process and analyze images alongside text for multimodal understanding.
  name: Vision
- description: Allow Claude to reason step-by-step for complex tasks with visible thinking process.
  name: Extended Thinking
- description: Receive responses in real-time via server-sent events for responsive user experiences.
  name: Streaming Responses
- description: Process large volumes of requests asynchronously at 50 percent reduced cost.
  name: Message Batches
- description: Pre-calculate token usage for messages including tools, images, and documents.
  name: Token Counting
image: https://www.anthropic.com/images/icons/anthropic-icon.png
integrations:
- description: Access Claude models through AWS Bedrock for enterprise deployment with AWS infrastructure.
  name: Amazon Bedrock
- description: Use Claude on Google Cloud through Vertex AI integration.
  name: Google Cloud Vertex AI
- description: Integrate Claude into LangChain pipelines for advanced AI application development.
  name: LangChain
- description: Connect Claude to external data sources and tools via the Model Context Protocol.
  name: MCP Protocol
jsonld:
- class_count: 0
  name: Claude Context
  property_count: 20
  slug: claude-context
- class_count: 0
  name: Claude Messages Context
  property_count: 0
  slug: claude-messages-context
layout: provider
modified: '2026-04-18'
name: Claude
rules:
- name: Claude API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: claude-spectral-rules
skills: []
slug: claude
solutions: []
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
url: https://www.anthropic.com
use_cases:
- description: Build conversational interfaces with context-aware responses and tool integration.
  name: AI-Powered Chat Applications
- description: Generate, edit, and transform text content for marketing, documentation, and creative writing.
  name: Content Generation
- description: Use Claude for code generation, review, debugging, and technical documentation.
  name: Code Assistance
- description: Extract information, summarize, and answer questions about documents and images.
  name: Document Analysis
- description: Process large datasets of prompts efficiently using the Message Batches API.
  name: Batch Processing
---
