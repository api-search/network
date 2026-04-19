---
description: Schema for the AGENT.md vendor-neutral AI coding agent configuration format.
layout: schema
name: AGENT.md Configuration Schema
properties_list:
- description: Name of the project.
  name: project
  type: string
- description: High-level description of the project and its purpose.
  name: description
  type: string
- description: General instructions for the AI agent when working on this project.
  name: instructions
  type: array
- description: Technology stack information.
  name: stack
  type: object
- description: Code style and convention guidelines.
  name: conventions
  type: object
- description: List of development tools used in the project.
  name: tools
  type: array
- description: Patterns, libraries, or approaches the agent should avoid.
  name: avoid
  type: array
- description: Areas or files the agent should focus on.
  name: focus
  type: array
- description: Additional project context for the agent.
  name: context
  type: string
provider_name: AGENT.md
provider_slug: agent-md
schema_file: json-schema/agent-md-schema.json
slug: agent-md
tags:
- AI Agents
- AI Copilot
- Coding Standards
- Developer Workflow
- Configuration
- Standards
title: AGENT.md Configuration Schema
---
