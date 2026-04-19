---
description: A tool result content block, providing the output from a tool invocation.
layout: schema
name: ToolResultBlockParam
properties_list:
- description: ''
  name: type
  type: string
- description: The id of the tool use request this is a result for. Must match a tool_use block id.
  name: tool_use_id
  type: string
- description: The result of the tool call. Can be a string or array of content blocks.
  name: content
  type: string
- description: Set to true if the tool execution resulted in an error.
  name: is_error
  type: boolean
provider_name: Claude
provider_slug: claude
schema_file: json-schema/claude-messages-tool-result-block-param-schema.json
slug: claude-messages-tool-result-block-param
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
title: ToolResultBlockParam
---
