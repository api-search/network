---
description: Represents a chat completion response returned by model.
layout: schema
name: CreateChatCompletionResponse
properties_list:
- description: A unique identifier for the chat completion.
  name: id
  type: string
- description: The object type.
  name: object
  type: string
- description: The Unix timestamp of when the chat completion was created.
  name: created
  type: integer
- description: The model used for the chat completion.
  name: model
  type: string
- description: A list of chat completion choices.
  name: choices
  type: array
- description: The system fingerprint representing the backend configuration.
  name: system_fingerprint
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-openai-service-create-chat-completion-response-schema.json
slug: azure-openai-service-create-chat-completion-response
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: CreateChatCompletionResponse
---
