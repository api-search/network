---
description: ''
layout: schema
name: CreateChatCompletionRequest
properties_list:
- description: ID of the model to use. See the model endpoint compatibility table for which models work with the Chat API.
  name: model
  type: string
- description: A list of messages comprising the conversation so far. Each message has a role (system, user, assistant, or tool) and content.
  name: messages
  type: array
- description: Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
  name: frequency_penalty
  type: number
- description: Modify the likelihood of specified tokens appearing in the completion. Maps token IDs to bias values from -100 to 100.
  name: logit_bias
  type: object
- description: Whether to return log probabilities of the output tokens.
  name: logprobs
  type: boolean
- description: An integer specifying the number of most likely tokens to return at each token position, each with an associated log probability. logprobs must be set to true if this parameter is used.
  name: top_logprobs
  type: integer
- description: The maximum number of tokens that can be generated in the chat completion. The total length of input tokens and generated tokens is limited by the model's context length.
  name: max_tokens
  type: integer
- description: An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and reasoning tokens.
  name: max_completion_tokens
  type: integer
- description: How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices.
  name: n
  type: integer
- description: Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
  name: presence_penalty
  type: number
- description: An object specifying the format that the model must output. Setting to json_object enables JSON mode. Setting to json_schema enables Structured Outputs with a supplied JSON schema.
  name: response_format
  type: object
- description: If specified, the system will make a best effort to sample deterministically so that repeated requests with the same seed and parameters should return the same result.
  name: seed
  type: integer
- description: Up to 4 sequences where the API will stop generating further tokens.
  name: stop
  type: string
- description: 'If set, partial message deltas will be sent as server-sent events. The stream is terminated by a data: [DONE] message.'
  name: stream
  type: boolean
- description: Options for streaming responses.
  name: stream_options
  type: object
- description: What sampling temperature to use, between 0 and 2. Higher values make the output more random, lower values more focused and deterministic.
  name: temperature
  type: number
- description: An alternative to sampling with temperature, called nucleus sampling. The model considers the results of the tokens with top_p probability mass.
  name: top_p
  type: number
- description: A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for.
  name: tools
  type: array
- description: Controls which (if any) tool is called by the model. none means the model will not call any tool. auto means the model can pick between generating a message or calling one or more tools. required mean
  name: tool_choice
  type: string
- description: Whether to enable parallel function calling during tool use.
  name: parallel_tool_calls
  type: boolean
- description: A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.
  name: user
  type: string
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-chat-completions-create-chat-completion-request-schema.json
slug: openai-chat-completions-create-chat-completion-request
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: CreateChatCompletionRequest
---
