---
description: IDE Chat metrics for a specific AI model.
layout: schema
name: IdeChatModel
properties_list:
- description: ''
  name: name
  type: string
- description: ''
  name: is_custom_model
  type: boolean
- description: ''
  name: custom_model_training_date
  type: '[''string'', ''null'']'
- description: ''
  name: total_engaged_users
  type: integer
- description: Total number of chat conversations.
  name: total_chats
  type: integer
- description: Number of times chat suggestions were inserted into code.
  name: total_chat_insertion_events
  type: integer
- description: Number of times chat responses were copied.
  name: total_chat_copy_events
  type: integer
provider_name: GitHub Copilot
provider_slug: github-copilot
schema_file: json-schema/github-copilot-ide-chat-model-schema.json
slug: github-copilot-ide-chat-model
tags:
- Agents
- AI
- Artificial Intelligence
- Code Generation
- Code Review
- Coding Agent
- Custom Instructions
- Developer Tools
- Extensions
- IDE
- Machine Learning
- MCP
- Metrics
- Model Context Protocol
- Productivity
title: IdeChatModel
---
