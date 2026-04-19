---
api_count: 2
apis:
- description: The Model Context Protocol (MCP) is an open-source standard for connecting AI applications to external systems including data sources, tools, and workflows. Originally developed by Anthropic and donat
  name: Model Context Protocol (MCP)
  slug: model-context-protocol
- description: Goose is a general-purpose, open-source AI agent that runs locally on your machine. Originally from Block and now under AAIF governance, goose supports 15+ LLM providers, 70+ MCP extensions, and provi
  name: Goose AI Agent
  slug: goose
common:
- title: ''
  type: GitHubOrganization
  url: https://github.com/agentic-ai-foundation
- title: ''
  type: Portal
  url: https://lfaidata.foundation/
- title: ''
  type: Documentation
  url: https://modelcontextprotocol.io/introduction
created: '2026-03-16'
description: The Agentic AI Foundation (AAIF) is a Linux Foundation project formed in December 2025 that brings together critical open standards and projects for AI agents under neutral governance. It hosts Anthropic's Model Context Protocol (MCP), Block's goose AI agent, and OpenAI's AGENTS.md to enable interoperable, open AI agent ecosystems. The foundation drives standardization of agent communication protocols, tool interfaces, and cross-platform agent portability.
features:
- description: All AAIF projects operate under Linux Foundation neutral governance, ensuring no single vendor controls the direction of AI agent standards.
  name: Neutral Open Governance
- description: MCP is a universal adapter standard enabling AI agents to connect to any external tool, data source, or workflow through a consistent protocol.
  name: Model Context Protocol (MCP)
- description: AAIF standards enable AI agents to run consistently across different platforms, environments, and LLM providers without vendor lock-in.
  name: Cross-Platform Agent Portability
- description: The MCP standard enables a rich ecosystem of 70+ tools and extensions that any compliant agent can discover and invoke.
  name: Tool and Extension Ecosystem
- description: AAIF projects support 15+ LLM providers including Anthropic, OpenAI, Google, Azure, and Ollama through standardized provider interfaces.
  name: Multi-LLM Provider Support
- description: The Agent Communication Protocol (ACP) enables agents to authenticate and communicate with each other and LLM providers through open standards.
  name: Open Agent Communication
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Native MCP support via the Anthropic Messages API, the originating implementation of the MCP standard.
  name: Claude (Anthropic)
- description: MCP tool integration via the OpenAI Responses API, enabling ChatGPT to invoke MCP-compatible tools.
  name: ChatGPT (OpenAI)
- description: GitHub Copilot in VS Code supports MCP servers for AI-assisted development through the AAIF MCP standard.
  name: VS Code
- description: Cursor IDE integrates MCP tool support for AI-assisted coding agents.
  name: Cursor
- description: AAIF operates under Linux Foundation governance alongside related projects in the LF AI & Data portfolio.
  name: Linux Foundation
jsonld:
- class_count: 5
  name: Agentic Ai Foundation Context
  property_count: 7
  slug: agentic-ai-foundation-context
layout: provider
modified: '2026-04-19'
name: Agentic AI Foundation
skills: []
slug: agentic-ai-foundation
solutions: []
tags:
- AI Agents
- Linux Foundation
- Open Source
- Standards
- MCP
- Agentic AI
- Interoperability
url: https://raw.githubusercontent.com/api-evangelist/agentic-ai-foundation/refs/heads/main/apis.yml
use_cases:
- description: Build MCP-compatible tools once and make them available to any AI agent or client that supports the MCP standard, eliminating integration silos.
  name: Interoperable AI Tool Development
- description: Organizations adopt AAIF standards to ensure their AI agent infrastructure is portable, auditable, and not locked to a single AI vendor.
  name: Enterprise Agent Standardization
- description: Use AAIF protocols to connect specialized AI agents that collaborate on complex tasks, each contributing domain-specific capabilities.
  name: Multi-Agent Workflow Orchestration
- description: Developers build and extend open-source AI agents like goose using the AAIF ecosystem of standards and extensions.
  name: Open-Source Agent Development
---
