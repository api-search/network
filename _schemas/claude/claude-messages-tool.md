---
description: Definition of a tool that the model can use.
layout: schema
name: Tool
properties_list:
- description: The name of the tool. Must match the regex ^[a-zA-Z0-9_-]{1,64}$.
  name: name
  type: string
- description: A detailed description of what the tool does, when it should be used, and what each parameter means.
  name: description
  type: string
- description: JSON Schema object defining the expected parameters for the tool.
  name: input_schema
  type: object
- description: The type of tool. Omit for custom tools. Use specific type strings for server tools like web_search_20260209, code_execution_20260120, text_editor_20250728, etc.
  name: type
  type: string
provider_name: Claude
provider_slug: claude
schema_file: json-schema/claude-messages-tool-schema.json
slug: claude-messages-tool
tags:
- Artificial Intelligence
- Chatbot
- Conversational AI
- Generative AI
- Large Language Models
- Machine Learning
- Natural Language Processing
title: Tool
---
