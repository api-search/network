---
api_count: 1
apis:
- description: The AGENTS.md specification defines a standard Markdown file format for providing project context, build instructions, coding standards, and testing procedures to AI coding agents. The file is version
  name: AGENTS.md Specification
  slug: agents-md-specification
common:
- title: ''
  type: Portal
  url: https://agents.md/
- title: ''
  type: Documentation
  url: https://agents.md/
- title: ''
  type: GitHubOrganization
  url: https://github.com/agentic-ai-foundation
created: '2025-01-01'
description: AGENTS.md is an open standard file format that provides context and instructions to AI coding agents working on software projects. Like a README for agents, an AGENTS.md file lives in the project repository and tells AI agents how to build, test, and contribute code — including coding standards, build commands, testing procedures, and development conventions. Supported by over 60,000 open-source projects and major platforms including OpenAI Codex, Google Jules, Cursor, Devin, Windsurf, GitHub Copilot, and goose. Stewarded by the Agentic AI Foundation under the Linux Foundation.
features:
- description: Provides AI agents with structured information about the project including its purpose, architecture, and key concepts.
  name: Project Context for AI Agents
- description: Documents the exact commands needed to build, test, lint, and deploy the project so AI agents can execute them correctly.
  name: Build and Test Instructions
- description: Specifies coding conventions, style guides, naming patterns, and best practices that AI agents should follow when generating code.
  name: Coding Standards
- description: Supports nested AGENTS.md files in monorepo subdirectories, allowing different projects to have tailored agent instructions with closest-file-wins precedence.
  name: Monorepo Support
- description: The format uses standard Markdown with no mandatory fields, giving teams flexibility to include only the context their agents need.
  name: Open Standard with No Required Fields
- description: Supported by 60+ AI coding tools and editors including OpenAI Codex, Google Jules, Cursor, Devin, GitHub Copilot, Windsurf, and goose.
  name: Broad Tool Support
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Native AGENTS.md support for AI coding tasks via OpenAI's coding agent.
  name: OpenAI Codex
- description: AGENTS.md context ingestion in Google's AI coding agent for autonomous development tasks.
  name: Google Jules
- description: AGENTS.md file discovery and context loading in Cursor's AI-assisted editor.
  name: Cursor
- description: AGENTS.md support in Cognition's autonomous coding agent Devin.
  name: Devin (Cognition)
- description: AGENTS.md integration in GitHub Copilot for project-aware AI code suggestions.
  name: GitHub Copilot
- description: AGENTS.md context loading in Block's open-source goose AI agent, now under the Agentic AI Foundation.
  name: goose (AAIF)
- description: AGENTS.md support in Windsurf's AI-powered development environment.
  name: Windsurf
- description: AGENTS.md discovery in JetBrains' AI coding assistant Junie.
  name: JetBrains Junie
jsonld:
- class_count: 1
  name: Agents Md Context
  property_count: 13
  slug: agents-md-context
layout: provider
modified: '2026-04-19'
name: AGENTS.md
skills: []
slug: agents-md
solutions: []
tags:
- AI Agents
- AI Copilot
- Coding Standards
- Developer Workflow
- Open Standard
- Documentation
url: https://raw.githubusercontent.com/api-evangelist/agents-md/refs/heads/main/apis.yml
use_cases:
- description: Provide AI coding agents with project conventions and standards so their generated code passes review without needing manual style corrections.
  name: AI-Assisted Code Review
- description: Enable AI agents to independently implement features by giving them the context needed to set up the development environment, run tests, and validate their work.
  name: Autonomous Feature Development
- description: Accelerate AI agent productivity on legacy codebases by documenting the context that would normally come from exploring the project.
  name: Onboarding AI Agents to Existing Projects
- description: Ensure all AI agents working on a project operate from the same context, reducing inconsistencies when multiple agents collaborate.
  name: Consistent Multi-Agent Workflows
- description: Document security considerations and sensitive file locations so AI agents avoid introducing vulnerabilities or accidentally exposing credentials.
  name: Security-Aware AI Development
---
