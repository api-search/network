---
api_count: 1
apis:
- description: The Activepieces API provides programmatic access to the automation platform, enabling management of flows, connections, projects, users, folders, pieces, templates, and execution monitoring. Uses Bea
  name: Activepieces API
  slug: activepieces-api
capabilities:
- description: Unified workflow capability for building, managing, monitoring, and debugging automation flows. Used by developers and no-code builders to orchestrate integrations across 400+ app connections.
  name: Activepieces Workflow Automation
  slug: workflow-automation
common:
- title: ''
  type: Portal
  url: https://www.activepieces.com/
- title: ''
  type: Documentation
  url: https://www.activepieces.com/docs/
- title: ''
  type: GettingStarted
  url: https://www.activepieces.com/docs/getting-started/introduction
- title: ''
  type: Authentication
  url: https://www.activepieces.com/docs/endpoints/overview
- title: ''
  type: Pricing
  url: https://www.activepieces.com/pricing
- title: ''
  type: GitHubOrganization
  url: https://github.com/activepieces
- title: ''
  type: GitHubRepository
  url: https://github.com/activepieces/activepieces
- title: ''
  type: StatusPage
  url: https://status.activepieces.com/
- title: ''
  type: SpectralRules
  url: rules/activepieces-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/activepieces-vocabulary.yaml
- title: Activepieces API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/activepieces.yaml
- title: Workflow Automation Capability
  type: NaftikoCapability
  url: capabilities/workflow-automation.yaml
- title: Activepieces Context
  type: JSON-LD
  url: json-ld/activepieces-context.jsonld
created: '2026-03-16'
description: Activepieces is an open-source, no-code automation platform that enables users to streamline workflows by connecting various applications and automating tasks. It supports over 400 MCP servers and integrations, allowing developers to build custom TypeScript-based pieces. The platform offers AI agents, MCPs, and workflow automation capabilities with both cloud and self-hosted deployment options.
features:
- description: No-code drag-and-drop interface for building automation workflows with triggers and actions.
  name: Visual Flow Builder
- description: Over 400 pre-built integrations (pieces) written in TypeScript, available as MCP servers for AI agents.
  name: 400+ Integration Pieces
- description: Native AI agent creation and orchestration within automation workflows.
  name: AI Agents
- description: Every piece automatically becomes an MCP server for use with AI agents and LLMs like Claude.
  name: MCP Servers
- description: Build custom TypeScript-based integration pieces and publish them to npm.
  name: Custom Pieces
- description: Version control for flows with publish/draft states and rollback capabilities.
  name: Flow Versioning
- description: Add approval steps, delays, and human decision points in automation workflows.
  name: Human-in-the-Loop
- description: Deploy on Docker, Kubernetes, AWS, GCP, or any cloud provider with full data control.
  name: Self-Hosting
- description: Synchronize flows with Git repositories for version control and CI/CD integration.
  name: Git Sync
- description: Trigger flows via webhooks from any external system or service.
  name: Webhook Triggers
- description: Full programmatic access to manage flows, connections, projects, and execution history.
  name: REST API
- description: Share and reuse flow templates across projects and teams.
  name: Flow Templates
image: /assets/icons/activepieces.png
integrations:
- description: Trigger workflows on GitHub events and automate repository operations.
  name: GitHub
- description: Send emails, parse inbound mail, and automate email workflows.
  name: Gmail
- description: Send notifications, create channels, and respond to Slack events.
  name: Slack
- description: Integrate GPT models for AI-powered automation and content generation.
  name: OpenAI
- description: Read and write data to Google Sheets for data synchronization workflows.
  name: Google Sheets
- description: Sync records and trigger workflows from Airtable database changes.
  name: Airtable
- description: Create and update Salesforce records from automation workflows.
  name: Salesforce
- description: Trigger flows on payment events and automate billing operations.
  name: Stripe
jsonld:
- class_count: 25
  name: Activepieces Context
  property_count: 35
  slug: activepieces-context
layout: provider
modified: '2026-04-19'
name: Activepieces
rules:
- name: Activepieces API Rules
  rule_count: 25
  severity_counts:
    error: 10
    hint: 0
    info: 4
    warn: 11
  slug: activepieces-spectral-rules
skills: []
slug: activepieces
solutions:
- description: Free, open-source self-hosted deployment with unlimited flows and no task limits.
  name: Community Edition
- description: Cloud plan at $25/mo with 10 active flows, AI agents, and 500 AI credits.
  name: Plus
- description: Cloud plan at $150/mo with 50 active flows, team collaboration, and 1,000 AI credits.
  name: Business
- description: Custom pricing with unlimited flows, SSO, audit logs, and custom AI model support.
  name: Enterprise
tags:
- Automation
- No-Code
- Open Source
- Workflow
- AI Agents
- MCP
url: https://raw.githubusercontent.com/api-evangelist/activepieces/refs/heads/main/apis.yml
use_cases:
- description: Automate lead capture, email sequences, and CRM updates from marketing platforms.
  name: Marketing Automation
- description: Sync contacts, deals, and activities between CRM, email, and communication tools.
  name: Sales Operations
- description: Keep data in sync across databases, spreadsheets, and SaaS applications.
  name: Data Synchronization
- description: Use Activepieces as an MCP server to give AI agents access to 400+ integrations.
  name: AI Agent Orchestration
- description: Automate user provisioning, notifications, and system integrations.
  name: IT Automation
- description: Automate order processing, inventory updates, and customer notifications.
  name: E-Commerce Operations
- description: Embed Activepieces as a white-label automation platform in SaaS products.
  name: Developer Integration Platform
---
