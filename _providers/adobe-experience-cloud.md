---
api_count: 6
apis:
- description: 'The Adobe Analytics 2.0 API provides programmatic access to Adobe Analytics reporting, management, and configuration capabilities. It enables developers to retrieve report data, manage report suites, '
  name: Adobe Analytics 2.0 API
  slug: analytics-api
- description: The Adobe Experience Platform API provides RESTful access to core platform services including data ingestion, unified profile management, identity resolution, dataset management, schema registry, quer
  name: Adobe Experience Platform API
  slug: experience-platform-api
- description: The Adobe Target API provides programmatic access to Adobe Target for managing A/B tests, experience targeting, multivariate tests, automated personalization activities, audiences, offers, and real-ti
  name: Adobe Target API
  slug: target-api
- description: The Adobe Journey Optimizer API enables programmatic management of customer journeys, campaigns, messages, offers, placements, and content templates across email, push, SMS, and in-app channels for or
  name: Adobe Journey Optimizer API
  slug: journey-optimizer-api
- description: The Adobe Campaign API provides RESTful access to Adobe Campaign for managing subscriber profiles, subscription services, marketing workflows, email deliveries, and real-time transactional messaging a
  name: Adobe Campaign API
  slug: campaign-api
- description: Adobe I/O Events enables developers to receive near-real-time notifications from Adobe services via webhooks and journal polling. Events are emitted when significant changes occur across Adobe Experie
  name: Adobe I/O Events
  slug: io-events
asyncapis:
- description: Adobe I/O Events enables developers to receive near-real-time notifications from Adobe services via webhooks and journal polling. Events are emitted when significant changes occur across Adobe Experie
  name: Adobe I/O Events
  slug: adobe-io-events-asyncapi
capabilities:
- description: Unified workflow for managing real-time customer profiles, audience segmentation, and data ingestion using Adobe Experience Platform. Designed for data engineers and customer data platform administrat
  name: Adobe Experience Cloud Customer Data Platform
  slug: customer-data-platform
- description: 'Unified workflow capability combining Adobe Analytics, Adobe Target, and Adobe Journey Optimizer for data-driven marketing campaigns, A/B testing, and personalized journey orchestration. Designed for '
  name: Adobe Experience Cloud Digital Marketing
  slug: digital-marketing
common:
- title: ''
  type: Portal
  url: https://developer.adobe.com/
- title: ''
  type: Documentation
  url: https://developer.adobe.com/developer-console/docs/guides/
- title: ''
  type: Documentation
  url: https://developer.adobe.com/apis/
- title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- title: ''
  type: Support
  url: https://experienceleague.adobe.com/
- title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
- title: ''
  type: StatusPage
  url: https://status.adobe.com/
- title: ''
  type: Console
  url: https://developer.adobe.com/console/
- title: ''
  type: SignUp
  url: https://developer.adobe.com/
- title: ''
  type: GettingStarted
  url: https://developer.adobe.com/developer-console/docs/guides/getting-started/
- title: ''
  type: GitHubOrganization
  url: https://github.com/adobe
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AdobeDeveloperTV
- title: ''
  type: ChangeLog
  url: https://developer.adobe.com/events/docs/whats_new/
- title: ''
  type: SpectralRules
  url: rules/adobe-experience-cloud-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/customer-data-platform.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/digital-marketing.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/adobe-experience-cloud-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/adobe-experience-cloud-analytics-api-context.jsonld
- title: ''
  type: JSON-LD
  url: json-ld/adobe-experience-cloud-campaign-api-context.jsonld
- title: ''
  type: JSON-LD
  url: json-ld/adobe-experience-cloud-context.jsonld
- title: ''
  type: JSON-LD
  url: json-ld/adobe-experience-cloud-experience-platform-api-context.jsonld
- title: ''
  type: JSON-LD
  url: json-ld/adobe-experience-cloud-io-events-context.jsonld
- title: ''
  type: JSON-LD
  url: json-ld/adobe-experience-cloud-journey-optimizer-api-context.jsonld
- title: ''
  type: JSON-LD
  url: json-ld/adobe-experience-cloud-target-api-context.jsonld
created: '2025-01-01'
description: Adobe Experience Cloud is an integrated suite of applications and services for digital marketing, analytics, advertising, and commerce. It provides tools for content management, personalization, customer journey orchestration, audience segmentation, real-time customer data platforms, offer decisioning, and cross-channel campaign execution, enabling organizations to deliver personalized customer experiences at scale.
features:
- description: Build and query unified customer profiles from multiple data sources using the Experience Platform APIs.
  name: Real-Time Customer Profiles
- description: Retrieve dimensional reports, calculated metrics, and segment data from Adobe Analytics via REST API.
  name: Analytics Reporting
- description: Create, manage, and retrieve results for A/B tests and automated personalization activities via Adobe Target API.
  name: A/B and Multivariate Testing
- description: Orchestrate email, SMS, push, and in-app campaigns programmatically using Adobe Campaign and Journey Optimizer APIs.
  name: Multi-Channel Campaign Execution
- description: Subscribe to near-real-time events from all Adobe Experience Cloud products via Adobe I/O Events.
  name: Webhook Event Streaming
- description: Manage offers, placements, and decisioning rules for personalized content delivery using Journey Optimizer APIs.
  name: Offer Decisioning
- description: Ingest batch and streaming data and register schemas using Experience Platform APIs.
  name: Data Ingestion and Schema Registry
- description: Resolve customer identities across devices and channels using Experience Platform Identity Service API.
  name: Identity Resolution
- description: Create and evaluate audience segments using Experience Platform Segmentation Service API.
  name: Audience Segmentation
- description: Secure all APIs using OAuth 2.0 server-to-server credentials via Adobe Developer Console.
  name: OAuth 2.0 and JWT Authentication
image: /assets/icons/adobe-experience-cloud.png
integrations:
- description: Sync customer data and campaign results between Adobe Experience Cloud and Salesforce CRM.
  name: Salesforce
- description: Ingest data from Azure Data Lake and Blob Storage into Adobe Experience Platform.
  name: Microsoft Azure
- description: Connect Google BigQuery datasets to Adobe Experience Platform for data ingestion and activation.
  name: Google BigQuery
- description: Integrate Workfront project management with Adobe Experience Cloud for content workflow automation.
  name: Workfront
- description: Sync lead data and campaign activities between Marketo Engage and Adobe Experience Cloud.
  name: Marketo Engage
- description: Connect ServiceNow customer data with Adobe Experience Cloud for unified customer service experiences.
  name: ServiceNow
- description: Connect Snowflake data warehouse to Experience Platform for federated audience composition.
  name: Snowflake
jsonld:
- class_count: 18
  name: Adobe Experience Cloud Analytics Api Context
  property_count: 34
  slug: adobe-experience-cloud-analytics-api-context
- class_count: 14
  name: Adobe Experience Cloud Campaign Api Context
  property_count: 20
  slug: adobe-experience-cloud-campaign-api-context
- class_count: 7
  name: Adobe Experience Cloud Context
  property_count: 11
  slug: adobe-experience-cloud-context
- class_count: 20
  name: Adobe Experience Cloud Experience Platform Api Context
  property_count: 37
  slug: adobe-experience-cloud-experience-platform-api-context
- class_count: 10
  name: Adobe Experience Cloud Io Events Context
  property_count: 122
  slug: adobe-experience-cloud-io-events-context
- class_count: 27
  name: Adobe Experience Cloud Journey Optimizer Api Context
  property_count: 28
  slug: adobe-experience-cloud-journey-optimizer-api-context
- class_count: 15
  name: Adobe Experience Cloud Target Api Context
  property_count: 28
  slug: adobe-experience-cloud-target-api-context
layout: provider
modified: '2026-04-19'
name: Adobe Experience Cloud
rules:
- name: Adobe Experience Cloud API Rules
  rule_count: 31
  severity_counts:
    error: 16
    hint: 0
    info: 2
    warn: 13
  slug: adobe-experience-cloud-spectral-rules
skills: []
slug: adobe-experience-cloud
solutions: []
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
url: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/apis.yml
use_cases:
- description: Ingest data from multiple sources, resolve identities, and activate unified customer profiles for personalization.
  name: Customer Data Platform
- description: Automate campaign creation, scheduling, and execution across email, SMS, and push channels using Campaign and Journey Optimizer APIs.
  name: Marketing Automation
- description: Extract Adobe Analytics data into custom dashboards, BI tools, and data warehouses via the Analytics 2.0 API.
  name: Digital Analytics Reporting
- description: Deliver personalized content and offers in real time using Adobe Target and Journey Optimizer APIs.
  name: Real-Time Personalization
- description: Build reactive integrations that respond to Experience Cloud events such as profile updates, campaign completions, and audience changes.
  name: Event-Driven Workflows
- description: Create and activate audiences across paid media, email, and on-site channels using Experience Platform Segmentation API.
  name: Audience Activation
---
