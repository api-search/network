---
api_count: 2
apis:
- description: 'The primary REST API for ActiveCampaign, organized around resources such as contacts, deals, accounts, automations, campaigns, messages, lists, tags, webhooks, custom objects, and ecommerce entities. '
  name: ActiveCampaign API v3
  slug: activecampaign-v3
- description: API for managing SMS broadcasts, lists, metrics, and AI-powered content generation in ActiveCampaign. Supports creating, scheduling, and tracking SMS broadcast campaigns.
  name: ActiveCampaign SMS Broadcast API
  slug: activecampaign-sms
capabilities:
- description: Workflow capability for CRM and sales pipeline management including deals, accounts, tasks, and pipeline stages. Used by sales teams and revenue operations to track and advance deals.
  name: ActiveCampaign CRM and Sales
  slug: crm-sales
- description: 'Unified workflow capability for marketing automation, contact management, campaign execution, and list segmentation. Used by marketing teams and growth engineers to orchestrate multi-channel customer '
  name: ActiveCampaign Marketing Automation
  slug: marketing-automation
common:
- title: ''
  type: Portal
  url: https://developers.activecampaign.com/
- title: ''
  type: GettingStarted
  url: https://help.activecampaign.com/hc/en-us/articles/207317590-Getting-started-with-the-API
- title: ''
  type: Authentication
  url: https://developers.activecampaign.com/reference/authentication
- title: ''
  type: Pricing
  url: https://www.activecampaign.com/pricing
- title: ''
  type: Blog
  url: https://www.activecampaign.com/blog
- title: ''
  type: FAQ
  url: https://www.activecampaign.com/about/faq
- title: ''
  type: Forums
  url: https://community.activecampaign.com/latest
- title: ''
  type: StatusPage
  url: https://status.activecampaign.com/
- title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/acdevrel/activecampaign-developer-relations/overview
- title: ''
  type: GitHubOrganization
  url: https://github.com/ActiveCampaign
- title: PHP SDK
  type: SDK
  url: https://github.com/ActiveCampaign/activecampaign-api-php
- title: Node.js SDK
  type: SDK
  url: https://github.com/ActiveCampaign/activecampaign-api-nodejs
- title: ''
  type: SpectralRules
  url: rules/activecampaign-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/activecampaign-vocabulary.yaml
- title: ActiveCampaign API v3 Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/activecampaign-v3.yaml
- title: Marketing Automation Workflow
  type: NaftikoCapability
  url: capabilities/marketing-automation.yaml
- title: CRM and Sales Workflow
  type: NaftikoCapability
  url: capabilities/crm-sales.yaml
- title: SMS API Context
  type: JSON-LD
  url: json-ld/activecampaign-sms-context.jsonld
created: '2025-02-17'
description: ActiveCampaign is a leading marketing automation platform that helps businesses of all sizes seamlessly engage with their customers. With its user-friendly interface and powerful features, ActiveCampaign allows businesses to create personalized email campaigns, automate workflows, and track customer interactions in real-time. The platform offers a REST API (v3), SMS Broadcast API, webhooks, and custom object schemas for building deep integrations and automations.
features:
- description: Create and send conversion-focused email campaigns with personalization and segmentation.
  name: Email Marketing
- description: Build automated customer journeys and workflows triggered by contact behavior and events.
  name: Marketing Automation
- description: Built-in sales CRM for managing deals, pipelines, tasks, and customer relationships.
  name: CRM
- description: Reach contacts via SMS broadcast campaigns with AI-powered content generation.
  name: SMS Marketing
- description: Automate growth and customer engagement through WhatsApp communications.
  name: WhatsApp Messaging
- description: Automate transactional alerts, password resets, and notifications via Postmark integration.
  name: Transactional Email
- description: Create custom data schemas to activate complex data for segmentation and personalized automation.
  name: Custom Objects
- description: Track contact behaviors and activities across web properties and integrations.
  name: Contact Event Tracking
- description: Receive real-time event notifications for contact, campaign, automation, and custom object activities.
  name: Webhooks
- description: Deploy conversion-ready landing pages for lead capture and campaigns.
  name: Landing Pages
- description: AI-powered orchestration and autonomous marketing agents for campaign suggestions and personalization.
  name: Active Intelligence
- description: Connect AI applications to ActiveCampaign using the Model Context Protocol server.
  name: MCP Server
image: /assets/icons/activecampaign.png
integrations:
- description: Sync contact and deal data between ActiveCampaign and Salesforce CRM.
  name: Salesforce
- description: Connect ActiveCampaign to 1000+ apps via Zapier automation workflows.
  name: Zapier
- description: Send notifications and trigger automations from Slack using OAuth2 integration.
  name: Slack
- description: Sync scheduling data and trigger automations with custom objects via OAuth2.
  name: Calendly
- description: Integrate SMS workflows using Twilio with Basic Auth for outbound messaging.
  name: Twilio
- description: Sync ecommerce customers, orders, and products for automated campaigns.
  name: Shopify
- description: Embed forms and capture leads from WordPress sites.
  name: WordPress
- description: Connect Wix websites for lead capture and customer journey automation.
  name: Wix
jsonld:
- class_count: 18
  name: Activecampaign Sms Context
  property_count: 51
  slug: activecampaign-sms-context
layout: provider
modified: '2026-04-19'
name: ActiveCampaign
rules:
- name: ActiveCampaign API Rules
  rule_count: 26
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 12
  slug: activecampaign-spectral-rules
skills: []
slug: activecampaign
solutions:
- description: Entry-level plan with marketing automation, up to 5 automation actions, and 1 user.
  name: Starter
- description: Mid-tier plan with unlimited automation actions, landing pages, and standard segmentation.
  name: Plus
- description: Advanced plan with predictive content, advanced segmentation, and 3 users.
  name: Pro
- description: Full-featured plan with custom objects, dedicated account team, and premium segmentation.
  name: Enterprise
tags:
- Marketing Automation
- Email Marketing
- CRM
- Sales Automation
- Customer Experience
url: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/apis.yml
use_cases:
- description: Automate email sequences to nurture leads through the sales funnel based on behavior.
  name: Lead Nurturing
- description: Trigger post-purchase emails, abandoned cart recovery, and personalized product recommendations.
  name: E-Commerce Automation
- description: Automate onboarding sequences for SaaS products to improve activation and retention.
  name: Customer Onboarding
- description: Segment contacts using tags, custom fields, and custom objects for targeted campaigns.
  name: Contact Segmentation
- description: Manage deals, tasks, and pipeline stages with CRM and automation integration.
  name: Sales Pipeline Management
- description: Send targeted SMS campaigns to subscriber lists with engagement tracking.
  name: SMS Broadcast Campaigns
- description: Build real-time integrations using webhooks for contact and campaign activity events.
  name: Webhook-Driven Integrations
---
