---
description: Request body for creating a text completion.
layout: schema
name: CreateCompletionRequest
properties_list:
- description: The prompt(s) to generate completions for.
  name: prompt
  type: string
- description: The maximum number of tokens that can be generated.
  name: max_tokens
  type: integer
- description: Sampling temperature to use.
  name: temperature
  type: number
- description: Nucleus sampling parameter.
  name: top_p
  type: number
- description: How many completions to generate for each prompt.
  name: n
  type: integer
- description: Whether to stream back partial progress.
  name: stream
  type: boolean
- description: Up to 4 sequences where the API will stop generating further tokens.
  name: stop
  type: string
- description: Penalizes new tokens based on whether they appear in the text so far.
  name: presence_penalty
  type: number
- description: Penalizes new tokens based on their existing frequency in the text.
  name: frequency_penalty
  type: number
- description: A unique identifier representing your end-user.
  name: user
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-openai-service-create-completion-request-schema.json
slug: azure-openai-service-create-completion-request
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: CreateCompletionRequest
---
