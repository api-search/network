---
description: Code completion metrics for a specific AI model.
layout: schema
name: CodeCompletionsModel
properties_list:
- description: Name of the model or "default".
  name: name
  type: string
- description: Whether this is a custom fine-tuned model.
  name: is_custom_model
  type: boolean
- description: Training date of the custom model, if applicable.
  name: custom_model_training_date
  type: '[''string'', ''null'']'
- description: ''
  name: total_engaged_users
  type: integer
- description: ''
  name: languages
  type: array
provider_name: GitHub Copilot
provider_slug: github-copilot
schema_file: json-schema/github-copilot-code-completions-model-schema.json
slug: github-copilot-code-completions-model
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
title: CodeCompletionsModel
---
