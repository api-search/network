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
- gateway list logs
- chat completions.
- ai create embeddings
- create an ai gateway.
- create a text completion.
- ai execute model
- create embeddings
- ai create text completion
- list ai gateway logs.
- edge computing
- serverless
- dns
- cloudflare
- security
- delete a vectorize index.
- generate text embeddings.
- ddos protection
- create an ai response.
- list ai gateway instances.
- list ai gateways
- vector database
- gateway delete gateway
- cdn
- vectorize delete index
- ai gateway management.
- create a chat completion.
- vectorize list indexes
- machine learning
- create chat completion
- create a vectorize index.
- perform similarity query.
- ai create chat completion
- object storage
- gateway get gateway
- cloud
- vectorize index management.
- run an ai model.
- containers
- gateway create gateway
- api gateway
- web performance
- vectorize query vectors
- delete an ai gateway.
- ai gateway
- list ai gateways.
- list vectorize indexes
- vectorize insert vectors
- text embeddings.
- artificial intelligence
- platform
- real-time communication
- insert vectors into an index.
- vectorize create index
- edge
- get ai gateway details.
- gateway list gateways
- ai create response
- list vectorize indexes.
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
