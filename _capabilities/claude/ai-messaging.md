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
- token counting.
- count tokens
- get message batch status and details.
- list models
- list batches
- conversational ai
- artificial intelligence
- message operations.
- get batch status.
- create batch
- retrieve message batch results
- list available claude models.
- get batch
- natural language processing
- individual batch management.
- model details.
- get model metadata.
- delete batch
- delete a completed batch.
- list all message batches.
- create a message.
- batch management.
- delete a batch.
- generative ai
- messaging
- delete message batch
- get completed batch results.
- claude
- large language models
- create message batch
- create a message batch.
- list available models.
- list message batches
- send a message to claude and receive a response.
- create message
- anthropic
- cancel an in-progress batch.
- count message tokens
- ai
- list message batches.
- count message tokens.
- create a batch of message requests.
- retrieve message batch
- get model
- cancel message batch
- count tokens in a message.
- chatbot
- model discovery.
- machine learning
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
