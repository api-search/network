---
description: ''
layout: schema
name: CreateChatCompletionRequest
properties_list:
- description: ID of the model to use. See the model endpoint compatibility table for details on which models work with the Chat Completions API.
  name: model
  type: string
- description: A list of messages comprising the conversation so far. Depending on the model, different message types (modalities) are supported, like text, images, and audio.
  name: messages
  type: array
- description: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
  name: frequency_penalty
  type: number
- description: Modify the likelihood of specified tokens appearing in the completion. Maps token IDs to bias values from -100 to 100.
  name: logit_bias
  type: object
- description: Whether to return log probabilities of the output tokens.
  name: logprobs
  type: boolean
- description: Number of most likely tokens to return at each position, each with an associated log probability. logprobs must be set to true if this parameter is used.
  name: top_logprobs
  type: integer
- description: An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens. Replaces the deprecated max_tokens parameter.
  name: max_completion_tokens
  type: integer
- description: How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all choices.
  name: n
  type: integer
- description: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
  name: presence_penalty
  type: number
- description: If specified, the system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result.
  name: seed
  type: integer
- description: Up to 4 sequences where the API will stop generating further tokens.
  name: stop
  type: string
- description: 'If set, partial message deltas will be sent as server-sent events as they become available. The stream is terminated by a data: [DONE] message.'
  name: stream
  type: boolean
- description: Options for streaming responses.
  name: stream_options
  type: object
- description: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
  name: temperature
  type: number
- description: An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.
  name: top_p
  type: number
- description: A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for.
  name: tools
  type: array
- description: Controls which (if any) tool is called by the model. "none" means the model will not call any tool. "auto" means the model can pick between generating a message or calling one or more tools. "required
  name: tool_choice
  type: string
- description: Whether to enable parallel function calling during tool use.
  name: parallel_tool_calls
  type: boolean
- description: A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.
  name: user
  type: string
- description: Whether or not to store the output of this chat completion request for use in the model distillation or evals products.
  name: store
  type: boolean
- description: Set of 16 key-value pairs that can be attached to an object. Useful for storing additional information in a structured format.
  name: metadata
  type: object
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-chat-completions-create-chat-completion-request-schema.json
slug: chatgpt-chat-completions-create-chat-completion-request
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
title: CreateChatCompletionRequest
---
