---
description: A tool use content block in a response, indicating the model wants to use a tool.
layout: schema
name: ToolUseBlock
properties_list:
- description: ''
  name: type
  type: string
- description: A unique identifier for this particular tool use block. Used to match tool results to tool use requests.
  name: id
  type: string
- description: The name of the tool being used.
  name: name
  type: string
- description: An object containing the input passed to the tool, conforming to the tool's input_schema.
  name: input
  type: object
provider_name: Claude
provider_slug: claude
schema_file: json-schema/claude-messages-tool-use-block-schema.json
slug: claude-messages-tool-use-block
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
title: ToolUseBlock
---
