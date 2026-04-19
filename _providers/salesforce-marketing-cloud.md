---
api_count: 15
apis:
- description: Core REST API for interacting with Marketing Cloud features including email, SMS, push notifications, and data extensions. REST API uses JSON request and response bodies and resource endpoints to supp
  name: Marketing Cloud REST API
  slug: ''
- description: Legacy SOAP-based API for Marketing Cloud operations, including email sends, subscriber management, and data extension operations.
  name: SOAP API
  slug: ''
- description: Specialized API for sending triggered, transactional messages including order confirmations, password resets, and real-time notifications.
  name: Transactional Messaging API
  slug: ''
- description: API for creating, managing, and automating customer journeys across multiple channels and touchpoints.
  name: Journey Builder API
  slug: ''
- description: API for managing data extensions, which are database tables used to store and segment customer data in Marketing Cloud.
  name: Data Extensions API
  slug: ''
- description: API for creating and managing email send definitions, which define the configuration for sending emails to subscribers.
  name: Email Send Definition API
  slug: ''
- description: API for sending push notifications to mobile devices, managing device registrations, and tracking push message engagement.
  name: Mobile Push API
  slug: ''
- description: API for sending SMS and MMS messages, managing mobile numbers, and handling keyword-based subscriptions.
  name: SMS/MMS API
  slug: ''
- description: API for managing marketing assets including images, documents, content blocks, and templates across Marketing Cloud.
  name: Asset API
  slug: ''
- description: API for leveraging AI-powered product and content recommendations to personalize customer experiences.
  name: Einstein Recommendations API
  slug: ''
- description: REST API for creating and manipulating marketing content in Content Builder, a single cross-channel repository for emails, images, text, content blocks, and other documents.
  name: Content Builder API
  slug: ''
- description: REST API for creating, reading, updating, and deleting contacts in Marketing Cloud.
  name: Contacts API
  slug: ''
- description: API for initiating and managing marketing automations, including file upload, download, decryption, compression, and decompression operations within Automation Studio.
  name: Automation Studio API
  slug: ''
- description: API for managing and performing marketing campaigns within Marketing Cloud.
  name: Campaign API
  slug: ''
- description: API for registering callbacks and subscriptions to receive real-time event notifications from Marketing Cloud.
  name: Event Notification Service API
  slug: ''
capabilities:
- description: Unified workflow for digital marketers to manage contacts, orchestrate customer journeys, and automate multi-channel campaigns across email, SMS, and push channels.
  name: Salesforce Marketing Cloud Automation
  slug: marketing-automation
common:
- title: ''
  type: DeveloperPortal
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/overview
- title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/apis-overview.html
- title: ''
  type: Authentication
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/authentication.html
- title: ''
  type: APIReference
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/references
- title: ''
  type: Support
  url: https://help.salesforce.com/s/
- title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- title: ''
  type: SDK
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/sdks.html
- title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/
- title: ''
  type: Pricing
  url: https://www.salesforce.com/products/marketing-cloud/pricing/
- title: ''
  type: ChangeLog
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/release-notes.html
- title: ''
  type: RateLimits
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting.html
- title: ''
  type: GitHubRepository
  url: https://github.com/salesforce-marketingcloud/SFDC-MC-REST-Style-Guide
- title: ''
  type: Training
  url: https://trailhead.salesforce.com/en/content/learn/trails/get-started-with-marketing-cloud
- title: ''
  type: NaftikoCapability
  url: capabilities/marketing-automation.yaml
created: '2024-01-15'
description: Salesforce Marketing Cloud is a comprehensive digital marketing platform that enables businesses to manage customer journeys, email marketing, mobile messaging, social media marketing, advertising, and data analytics.
features:
- description: Design, send, and track targeted email campaigns with dynamic content, personalization, and A/B testing capabilities.
  name: Email Marketing
- description: Create automated, multi-step customer journeys across email, SMS, push, and advertising channels with branching logic.
  name: Journey Builder
- description: Centralized contact database with attribute sets, segmentation, and cross-channel identity resolution.
  name: Contact Management
- description: Send real-time transactional messages like order confirmations and password resets with guaranteed delivery.
  name: Transactional Messaging
- description: Leverage AI-powered recommendations and predictive analytics to personalize content and optimize send times.
  name: Einstein AI Personalization
- description: Schedule and automate data imports, file transfers, SQL queries, and multi-step marketing workflows.
  name: Automation Studio
- description: Centralized content management system for creating, organizing, and reusing marketing assets across channels.
  name: Content Builder
- description: Subscribe to real-time webhook notifications for email tracking events, data changes, and audit activities.
  name: Event Notifications
image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
integrations:
- description: Bi-directional sync with Sales Cloud and Service Cloud for unified customer profiles and campaign attribution.
  name: Salesforce CRM
- description: Connect to unified customer data profiles for advanced segmentation and real-time personalization.
  name: Salesforce Data Cloud
- description: Track email campaign performance and website conversions with Google Analytics integration.
  name: Google Analytics
- description: Sync e-commerce customer data, purchase history, and cart events for targeted marketing automation.
  name: Shopify
- description: Integrate commerce data for personalized product recommendations and transactional messaging.
  name: Salesforce Commerce Cloud
jsonld:
- class_count: 0
  name: Salesforce Marketing Cloud Context
  property_count: 0
  slug: salesforce-marketing-cloud-context
layout: provider
modified: '2026-04-19'
name: Salesforce Marketing Cloud
rules:
- name: Salesforce Marketing Cloud API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: salesforce-marketing-cloud-spectral-rules
skills: []
slug: salesforce-marketing-cloud
solutions: []
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
url: https://www.salesforce.com/products/marketing-cloud/overview/
use_cases:
- description: Automate multi-step welcome sequences across email and SMS to guide new customers through product adoption.
  name: Customer Onboarding Journeys
- description: Trigger personalized follow-up emails and push notifications when customers abandon shopping carts.
  name: Abandoned Cart Recovery
- description: Coordinate marketing messages across email, SMS, push, and advertising for unified campaign execution.
  name: Cross-Channel Campaign Orchestration
- description: Manage subscriber preferences, segment audiences, and automate re-engagement campaigns for inactive contacts.
  name: Subscriber Lifecycle Management
- description: React to customer behaviors in real time with triggered messages based on website visits, purchases, or app activity.
  name: Real-Time Event-Driven Marketing
---
