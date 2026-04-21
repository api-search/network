---
consumed_apis:
- cloudflare-workers-ai
- cloudflare-ai-gateway
- cloudflare-vectorize
description: AI and machine learning capabilities combining Workers AI model inference, AI Gateway for observability and control, and Vectorize for vector search. Used by AI/ML engineers building intelligent applications at the edge.
layout: capability
name: Cloudflare AI and ML
operations:
- description: Create a chat completion.
  method: POST
  name: create-chat-completion
  path: /v1/chat-completions
- description: Generate text embeddings.
  method: POST
  name: create-embeddings
  path: /v1/embeddings
- description: List AI gateways.
  method: GET
  name: list-ai-gateways
  path: /v1/ai-gateways
- description: List Vectorize indexes.
  method: GET
  name: list-vectorize-indexes
  path: /v1/vectorize-indexes
personas: []
provider_name: Cloudflare
provider_slug: cloudflare
search_terms:
- insert vectors into an index.
- list vectorize indexes
- delete a vectorize index.
- create a vectorize index.
- cloudflare
- get ai gateway details.
- run an ai model.
- ai create chat completion
- list ai gateway logs.
- delete an ai gateway.
- platform
- create chat completion
- ai create embeddings
- vectorize create index
- api gateway
- web performance
- ai execute model
- ai create text completion
- create an ai response.
- gateway list gateways
- vector database
- cloud
- ddos protection
- serverless
- list ai gateways.
- machine learning
- list vectorize indexes.
- gateway list logs
- gateway create gateway
- chat completions.
- create a chat completion.
- edge computing
- ai gateway
- perform similarity query.
- object storage
- ai gateway management.
- text embeddings.
- vectorize insert vectors
- vectorize list indexes
- security
- dns
- edge
- vectorize delete index
- cdn
- ai create response
- list ai gateway instances.
- create an ai gateway.
- containers
- list ai gateways
- real-time communication
- artificial intelligence
- create embeddings
- generate text embeddings.
- vectorize query vectors
- vectorize index management.
- gateway get gateway
- create a text completion.
- gateway delete gateway
slug: ai-and-ml
tags:
- Cloudflare
- Artificial Intelligence
- Machine Learning
- Vector Database
tools:
- description: Run an AI model.
  hints:
    readOnly: true
  name: ai-execute-model
- description: Create a chat completion.
  hints:
    readOnly: true
  name: ai-create-chat-completion
- description: Generate text embeddings.
  hints:
    readOnly: true
  name: ai-create-embeddings
- description: Create a text completion.
  hints:
    readOnly: true
  name: ai-create-text-completion
- description: Create an AI response.
  hints:
    readOnly: true
  name: ai-create-response
- description: List AI Gateway instances.
  hints:
    openWorld: true
    readOnly: true
  name: gateway-list-gateways
- description: Create an AI Gateway.
  hints:
    readOnly: false
  name: gateway-create-gateway
- description: Get AI Gateway details.
  hints:
    readOnly: true
  name: gateway-get-gateway
- description: List AI Gateway logs.
  hints:
    readOnly: true
  name: gateway-list-logs
- description: Delete an AI Gateway.
  hints:
    destructive: true
    idempotent: true
  name: gateway-delete-gateway
- description: List Vectorize indexes.
  hints:
    openWorld: true
    readOnly: true
  name: vectorize-list-indexes
- description: Create a Vectorize index.
  hints:
    readOnly: false
  name: vectorize-create-index
- description: Perform similarity query.
  hints:
    readOnly: true
  name: vectorize-query-vectors
- description: Insert vectors into an index.
  hints:
    readOnly: false
  name: vectorize-insert-vectors
- description: Delete a Vectorize index.
  hints:
    destructive: true
    idempotent: true
  name: vectorize-delete-index
---
