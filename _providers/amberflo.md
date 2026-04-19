---
api_count: 4
apis:
- description: The Amberflo Metering API provides meter definition management, high-throughput event ingestion, usage queries, raw event queries, and filtering rules. It supports real-time metering for API calls, to
  name: Amberflo Metering API
  slug: metering-api
- description: The Amberflo Billing API manages customers, pricing plans, invoices, prepaid orders, promotions, commitments, and billing analysis. It supports usage-based monetization workflows including revenue rec
  name: Amberflo Billing API
  slug: billing-api
- description: The Amberflo Cost Tracking API provides AI and cloud cost management capabilities including cloud provider integrations, business unit management, cost allocation rules, budget management, and cost qu
  name: Amberflo Cost Tracking API
  slug: cost-tracking-api
- description: The Amberflo AI Gateway provides a unified API for routing requests to 1,500+ LLM models with intelligent model routing, cost optimization, built-in fallbacks, and MCP server traffic monitoring. It tr
  name: Amberflo AI Gateway API
  slug: ai-gateway-api
capabilities:
- description: Unified workflow for API monetization teams combining metering and billing APIs. Enables end-to-end usage tracking, customer management, and billing automation for product and finance teams.
  name: Amberflo Usage-Based Monetization
  slug: usage-based-monetization
common:
- title: ''
  type: Website
  url: https://www.amberflo.io/
- title: ''
  type: Documentation
  url: https://docs.amberflo.io/
- title: ''
  type: DeveloperPortal
  url: https://docs.amberflo.io/
- title: ''
  type: GettingStarted
  url: https://docs.amberflo.io/docs/quick-start
- title: ''
  type: APIReference
  url: https://docs.amberflo.io/reference/
- title: ''
  type: SignUp
  url: https://ui.amberflo.io/cGxnLXNpZ251cA==
- title: ''
  type: Login
  url: https://ui.amberflo.io/login
- title: ''
  type: Pricing
  url: https://www.amberflo.io/pricing
- title: ''
  type: Blog
  url: https://www.amberflo.io/resources/blog
- title: ''
  type: TermsOfService
  url: https://www.amberflo.io/legal/terms-and-condition
- title: ''
  type: PrivacyPolicy
  url: https://www.amberflo.io/legal/privacy-policy
- title: ''
  type: Compliance
  url: https://trust.amberflo.io/
- title: ''
  type: TrustCenter
  url: https://trust.amberflo.io/
- title: ''
  type: GitHubOrganization
  url: https://github.com/amberflo
- title: Python SDK
  type: SDK
  url: https://pypi.org/project/amberflo-metering-python/
- title: TypeScript SDK
  type: SDK
  url: https://github.com/amberflo/metering-typescript
- title: Go SDK
  type: SDK
  url: https://github.com/amberflo/metering-go
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/rules/amberflo-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/capabilities/usage-based-monetization.yaml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/vocabulary/amberflo-vocabulary.yaml
created: '2026-03-27'
description: Amberflo is a cloud metering, usage-based billing, and AI cost management platform. It provides real-time event ingestion, customer billing automation, AI gateway capabilities, and FinOps visibility for API-driven and AI-powered businesses. The platform supports usage-based, token-based, seat-based, and outcome-based pricing models with automated invoicing and embeddable billing dashboards.
features:
- description: Ingest millions to billions of high-cardinality usage events in real time with idempotency, deduplication, and automatic aggregation.
  name: Real-Time Event Ingestion
- description: Unified LLM access and control across 1,500+ models with per-unit costs, rollups, budgets, Cost Guards, and margin analysis per customer.
  name: AI Cost Management
- description: Single API for multiple LLM providers with intelligent cost optimization, automatic retries, fallbacks, and MCP server traffic monitoring.
  name: AI Gateway and Model Routing
- description: Flexible billing models including usage-based, token-based, seat-based, fixed fee, and outcome-based pricing with multi-currency support and automated invoicing.
  name: Usage-Based Billing
- description: Customer-facing billing portals and dashboards via a React.js UI Kit with custom domain support and SSO integration.
  name: Embeddable Billing Dashboards
- description: Revenue recognition automation, RevRec ledger tracking, tax management, and integrations with Stripe and NetSuite.
  name: Revenue Operations
- description: Spending limits, threshold alerts, Cost Guards, and automated notifications for cloud and AI cost governance.
  name: Budget Management
- description: Chargeback rates, quotes, and invoices for internal cost allocation and showback reporting across business units.
  name: Chargeback and Showback
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Native integration with Stripe for payment processing and revenue operations workflows.
  name: Stripe
- description: Integration with NetSuite for revenue recognition and financial reporting.
  name: NetSuite
- description: Official Kong plugin for metering API requests handled by Kong instances and monetizing APIs.
  name: Kong
- description: Integration with AWS SaaS Builder Toolkit for SaaS billing and metering best practices on AWS.
  name: AWS SaaS Builder Toolkit
- description: Logging callback for LiteLLM to meter LLM usage and monitor AI costs.
  name: LiteLLM
- description: Examples and utilities for metering AWS Lambda function invocations.
  name: AWS Lambda
jsonld:
- class_count: 1
  name: Amberflo Billing Address Context
  property_count: 6
  slug: amberflo-billing-address-context
- class_count: 5
  name: Amberflo Billing Customer Context
  property_count: 10
  slug: amberflo-billing-customer-context
- class_count: 1
  name: Amberflo Billing Invoice Context
  property_count: 7
  slug: amberflo-billing-invoice-context
- class_count: 3
  name: Amberflo Billing Prepaid Context
  property_count: 5
  slug: amberflo-billing-prepaid-context
- class_count: 1
  name: Amberflo Billing Pricing Context
  property_count: 3
  slug: amberflo-billing-pricing-context
- class_count: 1
  name: Amberflo Metering Filtering Context
  property_count: 5
  slug: amberflo-metering-filtering-context
- class_count: 3
  name: Amberflo Metering Meter Context
  property_count: 10
  slug: amberflo-metering-meter-context
- class_count: 3
  name: Amberflo Metering Usage Context
  property_count: 11
  slug: amberflo-metering-usage-context
layout: provider
modified: '2026-04-19'
name: Amberflo
skills: []
slug: amberflo
solutions: []
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/apis.yml
use_cases:
- description: Meter API usage and automatically bill customers based on calls, tokens, or custom events with flexible pricing models.
  name: API Monetization
- description: Track and govern LLM spending across teams and customers with budgets, alerts, and per-customer cost attribution.
  name: AI Cost Governance
- description: Automate end-to-end billing for SaaS products with usage-based pricing plans, invoicing, and customer portals.
  name: SaaS Billing Automation
- description: Allocate and showback cloud costs to business units and customers using automated cost allocation rules and chargeback workflows.
  name: Cloud FinOps
- description: Provide customers with real-time visibility into their usage and costs via embedded dashboards and billing portals.
  name: Customer Cost Transparency
- description: Query and analyze usage data in real time with batch and sparse query modes, raw event queries, and revenue calculation analytics.
  name: Usage Analytics and Reporting
---
