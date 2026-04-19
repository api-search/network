---
description: LLM text completion request.
layout: schema
name: CompleteRequest
properties_list:
- description: The model name. See documentation for possible values.
  name: model
  type: string
- description: ''
  name: messages
  type: array
- description: Temperature controls the amount of randomness used in response generation. A higher temperature corresponds to more randomness.
  name: temperature
  type: number
- description: Threshold probability for nucleus sampling. A higher top-p value increases the diversity of tokens that the model considers, while a lower value results in more predictable output.
  name: top_p
  type: number
- description: The maximum number of output tokens to produce. The default value is model-dependent.
  name: max_tokens
  type: integer
- description: Deprecated in favor of "max_tokens", which has identical behavior.
  name: max_output_tokens
  type: integer
- description: An object describing response format config for structured-output mode.
  name: response_format
  type: object
- description: List of tools to be used during tool calling
  name: tools
  type: array
- description: The provisioned throughput ID to be used with the request.
  name: provisioned_throughput_id
  type: string
- description: Reserved
  name: sf-ml-xp-inflight-prompt-action
  type: string
- description: Reserved
  name: sf-ml-xp-inflight-prompt-client-id
  type: string
- description: Reserved
  name: sf-ml-xp-inflight-prompt-public-key
  type: string
- description: Reserved
  name: stream
  type: boolean
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/cortex-inference-complete-request-schema.json
slug: cortex-inference-complete-request
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: CompleteRequest
---
