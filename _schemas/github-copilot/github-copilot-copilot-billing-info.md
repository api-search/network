---
description: Copilot billing and subscription information for an organization, including seat breakdown and feature policy settings.
layout: schema
name: CopilotBillingInfo
properties_list:
- description: How Copilot seats are managed for the organization.
  name: seat_management_setting
  type: string
- description: Policy for Copilot Chat in IDEs.
  name: ide_chat
  type: string
- description: Policy for Copilot Chat on github.com.
  name: platform_chat
  type: string
- description: Policy for Copilot in the CLI.
  name: cli
  type: string
- description: Policy for suggestions matching public code.
  name: public_code_suggestions
  type: string
- description: The Copilot plan type for the organization.
  name: plan_type
  type: string
provider_name: GitHub Copilot
provider_slug: github-copilot
schema_file: json-schema/github-copilot-copilot-billing-info-schema.json
slug: github-copilot-copilot-billing-info
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
title: CopilotBillingInfo
---
