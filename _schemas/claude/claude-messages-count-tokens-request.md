---
description: ''
layout: schema
name: CountTokensRequest
properties_list:
- description: The model to use for token counting.
  name: model
  type: string
- description: Input messages to count tokens for.
  name: messages
  type: array
- description: System prompt to include in the token count.
  name: system
  type: string
- description: Tool definitions to include in the token count.
  name: tools
  type: array
provider_name: Claude
provider_slug: claude
schema_file: json-schema/claude-messages-count-tokens-request-schema.json
slug: claude-messages-count-tokens-request
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
title: CountTokensRequest
---
