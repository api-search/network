---
description: ''
layout: schema
name: CreateResponseRequest
properties_list:
- description: Model ID used to generate the response, like gpt-4o or o3. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points.
  name: model
  type: string
- description: Text, image, or file inputs to the model, used to generate a response. Can be a string for simple text input, or an array of input items for multi-turn and multimodal inputs.
  name: input
  type: string
- description: A system (or developer) message inserted at the beginning of the model's context. Use this for top-level guidance on the model's behavior, tone, or constraints.
  name: instructions
  type: string
- description: The unique ID of the previous response to the model. Use this to create multi-turn conversations. The model will use the previous response as context.
  name: previous_response_id
  type: string
- description: An upper bound for the number of tokens that can be generated for a response, including visible output tokens and reasoning tokens.
  name: max_output_tokens
  type: integer
- description: What sampling temperature to use, between 0 and 2. Higher values like 0.8 make the output more random, while lower values like 0.2 make it more focused and deterministic.
  name: temperature
  type: number
- description: An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.
  name: top_p
  type: number
- description: An array of tools the model may use to generate a response. Supports built-in tools (web_search_preview, file_search, code_interpreter, computer_use_preview) and custom function tools.
  name: tools
  type: array
- description: How the model should select which tool to use. auto allows the model to decide, required forces the model to use a tool, none disables tool use.
  name: tool_choice
  type: string
- description: The truncation strategy to use for the model context. auto will use the model-defined default truncation strategy. disabled will error if the context exceeds the model's context window.
  name: truncation
  type: string
- description: Configuration for text response format.
  name: text
  type: object
- description: Configuration for reasoning models (o-series). Controls how much reasoning effort the model uses.
  name: reasoning
  type: object
- description: Whether to store the generated response for later retrieval via the GET /responses endpoint. Defaults to true.
  name: store
  type: boolean
- description: Set of 16 key-value pairs that can be attached to an object. Useful for storing additional information in a structured format.
  name: metadata
  type: object
- description: If set to true, the model response data will be streamed as server-sent events to the client.
  name: stream
  type: boolean
- description: Whether to allow the model to run tool calls in parallel.
  name: parallel_tool_calls
  type: boolean
- description: A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.
  name: user
  type: string
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-responses-create-response-request-schema.json
slug: chatgpt-responses-create-response-request
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
title: CreateResponseRequest
---
