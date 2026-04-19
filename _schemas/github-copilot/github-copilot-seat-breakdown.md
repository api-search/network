---
description: Breakdown of Copilot seat counts by status.
layout: schema
name: SeatBreakdown
properties_list:
- description: Total number of Copilot seats.
  name: total
  type: integer
- description: Seats added in the current billing cycle.
  name: added_this_cycle
  type: integer
- description: Seats with pending invitations.
  name: pending_invitation
  type: integer
- description: Seats pending cancellation at end of cycle.
  name: pending_cancellation
  type: integer
- description: Seats active in the current billing cycle.
  name: active_this_cycle
  type: integer
- description: Seats inactive in the current billing cycle.
  name: inactive_this_cycle
  type: integer
provider_name: GitHub Copilot
provider_slug: github-copilot
schema_file: json-schema/github-copilot-seat-breakdown-schema.json
slug: github-copilot-seat-breakdown
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
title: SeatBreakdown
---
