---
description: ''
layout: schema
name: ResponseTool
properties_list:
- description: The type of the tool.
  name: type
  type: string
- description: The name of the function. Required for function type tools.
  name: name
  type: string
- description: A description of what the function does.
  name: description
  type: string
- description: The parameters the function accepts, described as a JSON Schema object. Required for function type tools.
  name: parameters
  type: object
- description: Whether strict schema adherence is enabled for function tools.
  name: strict
  type: boolean
- description: The IDs of the vector stores to search. Required for file_search type tools.
  name: vector_store_ids
  type: array
- description: The maximum number of results to return from file search.
  name: max_num_results
  type: integer
- description: Ranking options for file search results.
  name: ranking_options
  type: object
- description: The container for the code interpreter tool. Specifies the sandbox environment.
  name: container
  type: object
- description: The width of the computer display in pixels. Required for computer_use_preview type.
  name: display_width
  type: integer
- description: The height of the computer display in pixels. Required for computer_use_preview type.
  name: display_height
  type: integer
- description: The environment of the computer. Required for computer_use_preview type.
  name: environment
  type: string
- description: A label for the MCP server. Required for mcp type tools.
  name: server_label
  type: string
- description: The URL of the MCP server. Required for mcp type tools.
  name: server_url
  type: string
- description: The list of allowed tool names from the MCP server.
  name: allowed_tools
  type: array
- description: Headers to pass to the MCP server for authentication.
  name: headers
  type: object
provider_name: ChatGPT
provider_slug: chatgpt
schema_file: json-schema/chatgpt-responses-response-tool-schema.json
slug: chatgpt-responses-response-tool
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
title: ResponseTool
---
