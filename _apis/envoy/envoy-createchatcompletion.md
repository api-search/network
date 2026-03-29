---
aid: envoy:envoy-createchatcompletion
name: Create a chat completion
tags:
- Chat
humanURL: 
properties: []
description: >-
  Creates a chat completion response for the provided messages using an AI model routed through the gateway. The request format is compatible with the OpenAI Chat Completions API. The gateway selects a backend based on the AIGatewayRoute rules, which may include header-based routing, model-based routing, and backend traffic policies for rate limiting and token quota management. Supports streaming via server-sent events when stream is set to true.

---
