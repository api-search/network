---
description: Aggregated Copilot usage metrics for a single day, broken down by feature, editor, language, and model.
layout: schema
name: CopilotMetricsDay
properties_list:
- description: The date these metrics apply to (YYYY-MM-DD).
  name: date
  type: string
- description: Total users with any Copilot activity on this date.
  name: total_active_users
  type: integer
- description: Total users who actively engaged with Copilot features on this date.
  name: total_engaged_users
  type: integer
- description: ''
  name: copilot_ide_code_completions
  type: string
- description: ''
  name: copilot_ide_chat
  type: string
- description: ''
  name: copilot_dotcom_chat
  type: string
- description: ''
  name: copilot_dotcom_pull_requests
  type: string
provider_name: GitHub Copilot
provider_slug: github-copilot
schema_file: json-schema/github-copilot-copilot-metrics-day-schema.json
slug: github-copilot-copilot-metrics-day
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
title: CopilotMetricsDay
---
