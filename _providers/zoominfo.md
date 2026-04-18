---
api_count: 1
apis:
- description: The ZoomInfo API is a set of HTTPS endpoints you can use to programmatically retrieve and integrate ZoomInfo data into your existing technology stack and ...
  name: ZoomInfo
  slug: zoominfo
capabilities:
- description: 'Unified capability for B2B data enrichment workflows combining contact, company, org chart, corporate hierarchy, location, technology, intent, and IP enrichment. Used by sales ops, marketing ops, and '
  name: ZoomInfo Data Enrichment
  slug: data-enrichment
- description: Unified capability for monitoring and compliance workflows combining webhook management, API usage tracking, and compliance operations. Used by platform admins and data governance teams to manage data
  name: ZoomInfo Monitoring And Compliance
  slug: monitoring-and-compliance
- description: Unified capability for B2B prospecting workflows combining contact search, company search, intent signals, news, and scoops. Used by sales development reps and account executives to identify and prior
  name: ZoomInfo Prospecting And Search
  slug: prospecting-and-search
- description: Workflow for sales teams to find, qualify, and enrich prospect data. Combines contact search, company search, intent signals, and enrichment for targeted outreach.
  name: ZoomInfo Sales Prospecting
  slug: sales-prospecting
common:
- title: ''
  type: Pricing
  url: https://www.zoominfo.com/pricing
- title: ''
  type: Blog
  url: https://pipeline.zoominfo.com/
- title: ''
  type: Customers
  url: https://www.zoominfo.com/about/case-studies
- title: ''
  type: Partners
  url: https://www.zoominfo.com/partner
- title: ''
  type: Support
  url: https://www.zoominfo.com/about/help-center
- title: ''
  type: FAQ
  url: https://www.zoominfo.com/faqs/business
- title: ''
  type: Glossary
  url: https://pipeline.zoominfo.com/glossary
- title: ''
  type: Authentication
  url: https://api-docs.zoominfo.com/#authentication
- title: ''
  type: GettingStarted
  url: https://api-docs.zoominfo.com/getting-started
- title: ''
  type: RateLimits
  url: https://api-docs.zoominfo.com/rate-limits
- title: ''
  type: TermsOfService
  url: https://www.zoominfo.com/about/terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://www.zoominfo.com/about/privacy-policy
- title: ''
  type: StatusPage
  url: https://status.zoominfo.com
- title: ''
  type: GitHubOrganization
  url: https://github.com/Zoominfo
- title: ''
  type: DeveloperPortal
  url: https://api-docs.zoominfo.com
- title: ''
  type: APIReference
  url: https://api-docs.zoominfo.com
- title: MCP Server
  type: Hub
  url: https://github.com/Zoominfo/zoominfo-mcp-plugin
- title: ''
  type: SpectralRules
  url: rules/zoominfo-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/zoominfo-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-enrichment.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/sales-prospecting.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/zoominfo-api.yaml
created: '2025-02-09'
description: ZoomInfo is a leading B2B contact database and sales intelligence platform that provides detailed company and contact information, helping sales and marketing teams identify and connect with potential customers.
features:
- description: Search for contacts by job title, company, location, industry, and other criteria
  name: Contact Search
- description: Search for companies by industry, revenue, employee count, location, and technology stack
  name: Company Search
- description: Enrich contact records with verified email addresses, phone numbers, and professional details
  name: Contact Enrichment
- description: Enrich company records with firmographic data including revenue, employee count, and technographics
  name: Company Enrichment
- description: Identify companies showing buying intent signals based on content consumption patterns
  name: Intent Data
- description: Access business intelligence scoops about company changes, hiring, and strategic initiatives
  name: Scoops
- description: Search and enrich news articles related to companies and contacts
  name: News Intelligence
- description: Identify technologies used by companies across their tech stack
  name: Technology Tracking
- description: Map organizational structures including parent companies, subsidiaries, and divisions
  name: Corporate Hierarchy
- description: Access organizational chart data showing reporting relationships within companies
  name: Org Chart
- description: Real-time notifications for data changes and updates via webhook subscriptions
  name: Webhooks
- description: Submit batch search and enrichment jobs for large-scale data processing
  name: Bulk Operations
- description: Identify website visitors by IP address and enrich with company information
  name: WebSights
- description: Access compliance data to support GDPR and privacy regulation requirements
  name: Compliance
image: https://www.zoominfo.com/assets/img/zoominfo-logo.png
integrations:
- description: Native integration to enrich and sync contact and company data with Salesforce CRM
  name: Salesforce
- description: Seamless integration to push enriched data into HubSpot CRM and marketing automation
  name: HubSpot
- description: Integration to enrich records and sync data with Microsoft Dynamics CRM
  name: Microsoft Dynamics 365
- description: Marketing automation integration for lead enrichment and scoring with Marketo
  name: Marketo
- description: Sales engagement platform integration for enriched prospect data in Outreach sequences
  name: Outreach
- description: Integration to power Salesloft cadences with verified contact information
  name: Salesloft
- description: Notifications and alerts for intent signals and data updates delivered to Slack channels
  name: Slack
- description: Data sharing integration to access ZoomInfo data directly in Snowflake data warehouse
  name: Snowflake
- description: Audience targeting integration to reach ideal prospects with Google advertising campaigns
  name: Google Ads
- description: Integration to match and enrich LinkedIn profile data with ZoomInfo intelligence
  name: LinkedIn
jsonld:
- class_count: 0
  name: Zoominfo Context
  property_count: 278
  slug: zoominfo-context
layout: provider
modified: '2026-04-18'
name: ZoomInfo
rules:
- name: ZoomInfo API Rules
  rule_count: 21
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 1
  slug: zoominfo-spectral-rules
skills: []
slug: zoominfo
solutions: []
tags:
- B2B
- B2B Data
- Company Data
- Contact Database
- Contacts
- Data
- Lead Generation
- Marketing Intelligence
- Sales Intelligence
url: https://raw.githubusercontent.com/api-evangelist/zoominfo/refs/heads/main/apis.yml
use_cases:
- description: Identify and prioritize ideal prospects using firmographic and intent data to build targeted sales pipelines
  name: Sales Prospecting
- description: Automatically enrich inbound leads with verified contact and company data for faster qualification
  name: Lead Enrichment
- description: Build targeted account lists and personalize outreach using detailed company intelligence
  name: Account-Based Marketing
- description: Cleanse and update CRM records with accurate contact information and company details
  name: CRM Data Hygiene
- description: Analyze market segments, technology adoption, and competitive landscapes using company data
  name: Market Research
- description: Monitor competitor activities, technology changes, and strategic moves through scoops and news
  name: Competitive Intelligence
- description: Identify accounts actively researching solutions in your category based on intent signals
  name: Buyer Intent Analysis
- description: Convert anonymous website traffic into identified company accounts using IP enrichment
  name: Website Visitor Identification
---
