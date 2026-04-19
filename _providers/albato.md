---
api_count: 2
apis:
- description: REST API for managing multi-step automation workflows in Albato. Supports creating, enabling, disabling, and monitoring automation executions across 1,000+ connected apps.
  name: Albato Automations API
  slug: automations-api
- description: REST API for Albato Embedded iPaaS enabling SaaS companies to manage customer teams, app connectors, and automation templates for white-label integration delivery.
  name: Albato Embedded API
  slug: embedded-api
capabilities:
- description: Workflow capability for managing no-code automation and embedded iPaaS functionality in Albato. Combines automation workflow management and embedded team management to support operations teams and Saa
  name: Albato iPaaS Automation
  slug: ipaas-automation
common:
- title: ''
  type: Website
  url: https://albato.com
- title: ''
  type: Documentation
  url: https://wiki.albato.com/en
- title: Albato Embedded iPaaS
  type: GettingStarted
  url: https://albato.com/embedded
- title: ''
  type: Pricing
  url: https://albato.com/pricing
- title: Albato Embedded Pricing
  type: Pricing
  url: https://albato.com/embedded/pricing
- title: ''
  type: Blog
  url: https://albato.com/blog/all
- title: ''
  type: CaseStudies
  url: https://albato.com/blog/case-studies
- title: ''
  type: FAQ
  url: https://wiki.albato.com/en/collections/8343168-faq
- title: ''
  type: Licensing
  url: https://albato.com/license
- title: ''
  type: PrivacyPolicy
  url: https://albato.com/privacy
- title: ''
  type: FacebookGroup
  url: https://www.facebook.com/groups/albatocommunity
- title: ''
  type: Roadmap
  url: https://roadmap.albato.com/public
- title: ''
  type: SpectralRules
  url: rules/albato-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/albato-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/albato-albato-context.jsonld
- title: Albato Automations Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/automations-api.yaml
- title: Albato Embedded Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/embedded-api.yaml
- title: iPaaS Automation Workflow
  type: NaftikoCapability
  url: capabilities/ipaas-automation.yaml
created: '2025-06-06'
description: Albato is a no-code automation platform and embedded iPaaS that enables businesses to automate workflows by connecting 1,000+ apps without writing code. Supports multi-step automations with triggers, actions, conditions, and delays. Albato Embedded allows SaaS companies to offer white-label native integrations to their customers.
features:
- description: Visual automation builder for creating multi-step workflows connecting 1,000+ apps without writing code, with conditions, delays, and data transformations.
  name: No-Code Automation Builder
- description: Pre-built connectors for CRM, marketing, e-commerce, communication, and productivity apps including HubSpot, Salesforce, Google Workspace, Slack, Shopify, and more.
  name: 1,000+ App Integrations
- description: White-label integration platform for SaaS companies to embed Albato's automation capabilities natively in their products with full branding control.
  name: Albato Embedded iPaaS
- description: Support for complex automations with sequential and conditional steps, delays, loops, and data transformations without coding.
  name: Multi-Step Workflows
- description: Webhook-based real-time triggers for instant event processing and scheduled polling triggers for API-based app integrations.
  name: Real-Time and Scheduled Triggers
- description: Build custom API connectors from any REST API using the App Integrator without development handoff, supporting all major auth methods.
  name: Custom App Integrator
- description: Detailed execution history with step-level logging, success/error rates, real-time notifications, and dashboard insights.
  name: Execution Monitoring
- description: Built-in data mapping, field transformation, and JavaScript code steps for processing data between connected apps.
  name: Data Transformation
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: CRM and marketing automation for contact and deal management.
  name: HubSpot
- description: Enterprise CRM for sales pipeline and opportunity workflows.
  name: Salesforce
- description: Google Sheets, Gmail, Drive, Calendar, and Forms integrations.
  name: Google Workspace
- description: Team messaging integration for workflow notifications and alerts.
  name: Slack
- description: E-commerce integration for order, product, and customer automation.
  name: Shopify
- description: Payment processing integration for subscription and payment workflows.
  name: Stripe
- description: Workspace integration for task and project data synchronization.
  name: Notion
- description: Database integration for spreadsheet and grid data workflows.
  name: Airtable
jsonld:
- class_count: 0
  name: Albato Albato Context
  property_count: 36
  slug: albato-albato-context
layout: provider
modified: '2026-04-19'
name: Albato
rules:
- name: Albato API Rules
  rule_count: 24
  severity_counts:
    error: 15
    hint: 0
    info: 0
    warn: 9
  slug: albato-spectral-rules
skills: []
slug: albato
solutions: []
tags:
- No-Code Automation
- Workflow Automation
- Embedded iPaaS
- App Integration
- Integrations
- Webhooks
- White-Label
url: https://raw.githubusercontent.com/api-evangelist/albato/refs/heads/main/apis.yml
use_cases:
- description: Sync leads between CRM and marketing tools, automate email campaigns, and route prospects based on behavioral conditions.
  name: CRM and Marketing Automation
- description: Automate order notifications, inventory updates, fulfillment triggers, and customer communication across e-commerce platforms.
  name: E-Commerce Order Processing
- description: Use Albato Embedded to offer customers white-labeled integrations in your SaaS product without in-house iPaaS development.
  name: SaaS Native Integration Delivery
- description: Route tickets, trigger alerts, and sync customer data between helpdesk, CRM, and communication platforms automatically.
  name: Customer Support Automation
- description: Keep data consistent across business systems with bidirectional syncs, scheduled automations, and event-driven updates.
  name: Data Synchronization
---
