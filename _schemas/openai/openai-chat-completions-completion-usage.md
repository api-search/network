---
description: ''
layout: schema
name: CompletionUsage
properties_list:
- description: Number of tokens in the prompt.
  name: prompt_tokens
  type: integer
- description: Number of tokens in the generated completion.
  name: completion_tokens
  type: integer
- description: Total number of tokens used in the request (prompt + completion).
  name: total_tokens
  type: integer
- description: Breakdown of completion tokens.
  name: completion_tokens_details
  type: object
- description: Breakdown of prompt tokens.
  name: prompt_tokens_details
  type: object
provider_name: OpenAI
provider_slug: openai
schema_file: json-schema/openai-chat-completions-completion-usage-schema.json
slug: openai-chat-completions-completion-usage
tags:
- AI
- Artificial Intelligence
- Large Language Models
- T1
title: CompletionUsage
---
