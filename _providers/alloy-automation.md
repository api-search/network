---
api_count: 3
apis:
- description: The Alloy Embedded API enables SaaS companies to embed native integration workflows directly in their products. Manage end users, retrieve available integrations, trigger events, monitor workflow exec
  name: Alloy Automation Embedded API
  slug: embedded-api
- description: The Alloy Connectivity API enables companies to build native integration UIs with a single API endpoint. Manage users, discover connector resources, configure credentials, and execute connector action
  name: Alloy Automation Connectivity API
  slug: connectivity-api
- description: The Alloy Unified API enables companies to accomplish access-based app integrations across commerce, CRM, ERP, and other categories through a single standardized interface.
  name: Alloy Automation Unified API
  slug: unified-api
capabilities:
- description: ''
  name: Integration Platform
  slug: integration-platform
common:
- title: ''
  type: Website
  url: https://runalloy.com/
- title: ''
  type: Documentation
  url: https://docs.runalloy.com/
- title: ''
  type: Blog
  url: https://runalloy.com/blog/
- title: ''
  type: Pricing
  url: https://runalloy.com/platform/pricing/
- title: ''
  type: StatusPage
  url: https://status.runalloy.com/
- title: ''
  type: About
  url: https://runalloy.com/about-us/
- title: ''
  type: GitHubOrganization
  url: https://github.com/alloy-automation
- title: Node.js SDK
  type: SDK
  url: https://github.com/alloy-automation/alloy-node
- title: Python SDK
  type: SDK
  url: https://github.com/alloy-automation/alloy-python
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alloy-automation
- title: ''
  type: SpectralRules
  url: rules/alloy-automation-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/alloy-automation-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/integration-platform.yaml
created: '2026-03-16'
description: Alloy Automation is the all-in-one integration infrastructure platform for SaaS and AI, offering embedded iPaaS, unified API, and connectivity API products that let companies launch native integrations, build workflows, and connect to 1000+ apps with a single endpoint.
features:
- description: Drag-and-drop orchestration platform for shipping native integrations directly in your SaaS product, handling auth, deployment, and observability.
  name: Embedded iPaaS
- description: Single endpoint to access 1000+ third-party app connectors with built-in credential management, resource discovery, and real-time action execution.
  name: Connectivity API
- description: Model Context Protocol server providing AI agents secure, remote-hosted access to 1000+ tools with built-in context, permissioning, and authentication.
  name: MCP Server
- description: Visual workflow builder with logic blocks (Branch, If-Else, Iterate, Error Handler) and data transformation for building complex automation flows.
  name: Workflow Builder
- description: Self-service integration marketplace experience enabling end users to discover, install, and configure integrations within your product.
  name: Installation Manager
- description: Build custom connectors for proprietary or internal APIs using Alloy's connector framework with custom OAuth and authentication handling.
  name: Custom Connectors
- description: Custom event triggers and webhook destinations for real-time integration workflows responding to external events.
  name: Webhook Support
- description: GDPR, CCPA, HIPAA, and SOC 2 compliance with user data purging, static IP addresses, encryption, and SSO/SAML support.
  name: Compliance Controls
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: E-commerce order management, product catalog, and customer data integration
  name: Shopify
- description: CRM contact, opportunity, and account sync integration
  name: Salesforce
- description: Accounting GL sync, invoice creation, and payment reconciliation
  name: QuickBooks
- description: CRM and marketing automation contact and deal sync
  name: HubSpot
- description: Anthropic Claude AI agent integration via Alloy MCP server
  name: Claude
- description: LangChain AI agent integration using Alloy MCP tools
  name: LangChain
- description: Vercel AI SDK integration for building AI-powered workflows
  name: Vercel AI SDK
jsonld:
- class_count: 0
  name: Alloy Automation Connectivity Context
  property_count: 22
  slug: alloy-automation-connectivity-context
- class_count: 0
  name: Alloy Automation Embedded Context
  property_count: 23
  slug: alloy-automation-embedded-context
layout: provider
modified: '2026-04-19'
name: Alloy Automation
rules:
- name: Alloy Automation API Rules
  rule_count: 16
  severity_counts:
    error: 4
    hint: 0
    info: 5
    warn: 7
  slug: alloy-automation-spectral-rules
skills: []
slug: alloy-automation
solutions: []
tags:
- Automation
- Embedded Integrations
- Integrations
- iPaaS
- Unified API
- Workflows
url: https://raw.githubusercontent.com/api-evangelist/alloy-automation/refs/heads/main/apis.yml
use_cases:
- description: Embed a branded integration marketplace in your SaaS product allowing customers to self-serve connections to Shopify, Salesforce, NetSuite, and 1000+ apps.
  name: Native Integration Marketplace
- description: Connect LLM-powered AI agents to third-party business applications using the Alloy MCP server with Claude, LangChain, and Vercel AI SDK.
  name: AI Agent Integration
- description: Automate order management, returns, 3PL fulfillment, and inventory sync across Shopify, BigCommerce, WooCommerce, and marketplace platforms.
  name: E-Commerce Automation
- description: Sync general ledger entries, invoices, and journal entries between your platform and QuickBooks, NetSuite, Xero, and SAP.
  name: Accounting Integration
---
