---
api_count: 1
apis:
- description: AgentGateway provides AI-native gateway capabilities for routing LLM traffic, federating MCP tools, enabling agent-to-agent communication, and applying security and observability controls across AI ag
  name: AgentGateway
  slug: agentgateway
common:
- title: ''
  type: GitHubOrganization
  url: https://github.com/agentgateway
- title: LLM Backend Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-schema/agentgateway-llm-backend-schema.json
- title: MCP Target Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-schema/agentgateway-mcp-target-schema.json
- title: Route Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-schema/agentgateway-route-schema.json
- title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-ld/agentgateway-context.jsonld
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/vocabulary/agentgateway-vocabulary.yaml
- title: ''
  type: Portal
  url: https://agentgateway.dev/
- title: ''
  type: Documentation
  url: https://agentgateway.dev/docs/
- title: ''
  type: GettingStarted
  url: https://agentgateway.dev/docs/quickstart/
- title: ''
  type: Support
  url: https://discord.gg/y9efgEmppm
created: '2026-03-27'
description: AgentGateway is an open-source, AI-native proxy and gateway for routing, observing, and governing traffic to and from AI agents, LLM providers, and MCP servers. Built on the A2A and MCP protocols, it provides a unified gateway for LLM consumption, MCP tool federation, agent-to-agent communication, security, and observability. AgentGateway supports multi-provider LLM routing across OpenAI, Anthropic, Google Gemini, AWS Bedrock, and Azure OpenAI with built-in RBAC, JWT authentication, rate limiting, and OpenTelemetry integration.
features:
- description: Routes traffic to OpenAI, Anthropic, Google Gemini, AWS Bedrock, and Azure OpenAI through a unified API with model aliasing, failover, and load balancing.
  name: LLM Gateway
- description: Connects LLMs to tools via Model Context Protocol with static and dynamic routing, tool federation, and stateful MCP sessions.
  name: MCP Gateway
- description: Enables secure, governed communication between AI agents using the A2A protocol for multi-agent orchestration.
  name: Agent-to-Agent (A2A) Gateway
- description: Intelligently routes requests to self-hosted models based on GPU utilization and request priority.
  name: Inference Routing
- description: Provides JWT, OAuth2, API key management, CORS, CSRF protection, MCP authentication, and external authorization support.
  name: Security and Authentication
- description: Supports request routing and matching, header manipulation, rate limiting, retries, gRPC routing, traffic splitting, and direct responses.
  name: Traffic Management
- description: Integrates with OpenTelemetry for metrics, traces, and access logging with a built-in Admin UI and debugging tools.
  name: Observability
- description: Applies prompt guards, content filtering, regex filters, moderation policies, and custom webhooks for AI safety.
  name: Guardrails
- description: Tracks budget and spend limits per user, team, or application with RBAC-based controls on LLM consumption.
  name: Cost Controls
- description: Supports prompt templates and enrichment for standardizing and augmenting requests before routing to LLM providers.
  name: Prompt Enrichment
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Route to OpenAI GPT models through the AgentGateway LLM backend with model aliasing and budget controls.
  name: OpenAI
- description: Connect to Anthropic Claude models via the unified LLM gateway with failover and load balancing.
  name: Anthropic
- description: Route traffic to Google Gemini models through the AgentGateway multi-provider backend.
  name: Google Gemini
- description: Integrate with AWS Bedrock for managed LLM access via the AgentGateway routing layer.
  name: AWS Bedrock
- description: Route requests to Azure-hosted OpenAI models through the unified gateway API.
  name: Azure OpenAI
- description: Connect to locally hosted Ollama models for self-hosted inference routing.
  name: Ollama
- description: Route to vLLM inference servers with GPU utilization-aware routing for optimal performance.
  name: vLLM
- description: Export metrics, traces, and logs to any OpenTelemetry-compatible observability backend.
  name: OpenTelemetry
- description: Deploy and configure AgentGateway on Kubernetes using the standard Gateway API for dynamic configuration.
  name: Kubernetes Gateway API
jsonld:
- class_count: 5
  name: Agentgateway Context
  property_count: 21
  slug: agentgateway-context
layout: provider
modified: '2026-04-19'
name: AgentGateway
skills: []
slug: agentgateway
solutions: []
tags:
- AI Gateway
- API Gateway
- MCP
- LLM
- Agent-to-Agent
- Open Source
- CNCF
- Observability
- Security
url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/apis.yml
use_cases:
- description: Route requests across multiple LLM providers with a single API, enabling failover, load balancing, and cost optimization without changing client code.
  name: Unified LLM Routing
- description: Aggregate tools from multiple MCP servers behind a single gateway endpoint, enabling agents to discover and invoke tools from any connected MCP server.
  name: MCP Tool Federation
- description: Apply organization-wide security policies, rate limits, budget controls, and content filters to all AI agent traffic through a centralized gateway.
  name: Enterprise AI Governance
- description: Convert existing REST APIs into MCP-native tool endpoints that AI agents can discover and invoke through the Model Context Protocol.
  name: REST API to MCP Conversion
- description: Enable secure agent-to-agent communication using the A2A protocol, allowing specialized agents to delegate tasks to each other through the gateway.
  name: Multi-Agent Orchestration
- description: Collect unified telemetry across all AI agent and LLM interactions to monitor cost, latency, and behavior at scale.
  name: Observability and Debugging
---
