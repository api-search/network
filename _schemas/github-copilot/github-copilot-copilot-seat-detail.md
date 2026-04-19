---
description: Details of a Copilot seat assignment for a user, including activity information and plan type.
layout: schema
name: CopilotSeatDetail
properties_list:
- description: Timestamp when the seat was created.
  name: created_at
  type: string
- description: Timestamp when the seat was last updated.
  name: updated_at
  type: string
- description: Date when seat cancellation takes effect. Null if not pending cancellation.
  name: pending_cancellation_date
  type: '[''string'', ''null'']'
- description: Timestamp of the user's last Copilot activity. Null if no activity recorded.
  name: last_activity_at
  type: '[''string'', ''null'']'
- description: The IDE or editor used during the user's last Copilot activity. Null if no activity recorded.
  name: last_activity_editor
  type: '[''string'', ''null'']'
- description: Timestamp of the user's last authentication with Copilot. Null if never authenticated.
  name: last_authenticated_at
  type: '[''string'', ''null'']'
- description: The Copilot plan type for this seat.
  name: plan_type
  type: string
- description: The GitHub user assigned to this seat.
  name: assignee
  type: string
- description: The team through which this seat was assigned, if applicable.
  name: assigning_team
  type: string
provider_name: GitHub Copilot
provider_slug: github-copilot
schema_file: json-schema/github-copilot-copilot-seat-detail-schema.json
slug: github-copilot-copilot-seat-detail
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
title: CopilotSeatDetail
---
