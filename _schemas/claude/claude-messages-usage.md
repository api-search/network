---
description: Token usage information for the request.
layout: schema
name: Usage
properties_list:
- description: The number of input tokens consumed.
  name: input_tokens
  type: integer
- description: The number of output tokens generated.
  name: output_tokens
  type: integer
- description: The number of input tokens used to create a cache entry.
  name: cache_creation_input_tokens
  type: integer
- description: The number of input tokens read from cache.
  name: cache_read_input_tokens
  type: integer
provider_name: Claude
provider_slug: claude
schema_file: json-schema/claude-messages-usage-schema.json
slug: claude-messages-usage
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
title: Usage
---
