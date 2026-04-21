---
consumed_apis:
- claude-messages
description: Unified workflow for AI-powered messaging, token counting, batch processing, and model discovery. Used by AI application developers and data scientists.
layout: capability
name: Claude AI Messaging
operations:
- description: Create a message.
  method: POST
  name: create-message
  path: /v1/messages
- description: Count message tokens.
  method: POST
  name: count-tokens
  path: /v1/token-counts
- description: List message batches.
  method: GET
  name: list-batches
  path: /v1/batches
- description: Create a message batch.
  method: POST
  name: create-batch
  path: /v1/batches
- description: Get batch status.
  method: GET
  name: get-batch
  path: /v1/batches/{id}
- description: Delete a batch.
  method: DELETE
  name: delete-batch
  path: /v1/batches/{id}
- description: List available models.
  method: GET
  name: list-models
  path: /v1/models
- description: Get model metadata.
  method: GET
  name: get-model
  path: /v1/models/{id}
personas: []
provider_name: Claude
provider_slug: claude
search_terms:
- count tokens in a message.
- create a message batch.
- create a batch of message requests.
- large language models
- create a message.
- cancel message batch
- messaging
- list batches
- list all message batches.
- conversational ai
- list models
- cancel an in-progress batch.
- count message tokens.
- count message tokens
- individual batch management.
- batch management.
- machine learning
- claude
- get model
- ai
- generative ai
- create message
- send a message to claude and receive a response.
- retrieve message batch
- delete message batch
- create batch
- list message batches.
- list available models.
- anthropic
- delete batch
- model details.
- get completed batch results.
- get message batch status and details.
- retrieve message batch results
- model discovery.
- token counting.
- create message batch
- get model metadata.
- chatbot
- delete a batch.
- list available claude models.
- get batch
- artificial intelligence
- message operations.
- natural language processing
- count tokens
- list message batches
- get batch status.
- delete a completed batch.
slug: ai-messaging
tags:
- Anthropic
- Claude
- AI
- Messaging
tools:
- description: Send a message to Claude and receive a response.
  hints:
    readOnly: false
  name: create-message
- description: Count tokens in a message.
  hints:
    readOnly: true
  name: count-message-tokens
- description: Create a batch of message requests.
  hints:
    readOnly: false
  name: create-message-batch
- description: List all message batches.
  hints:
    openWorld: true
    readOnly: true
  name: list-message-batches
- description: Get message batch status and details.
  hints:
    readOnly: true
  name: retrieve-message-batch
- description: Get completed batch results.
  hints:
    readOnly: true
  name: retrieve-message-batch-results
- description: Cancel an in-progress batch.
  hints:
    readOnly: false
  name: cancel-message-batch
- description: Delete a completed batch.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-message-batch
- description: List available Claude models.
  hints:
    openWorld: true
    readOnly: true
  name: list-models
- description: Get model metadata.
  hints:
    readOnly: true
  name: get-model
---
