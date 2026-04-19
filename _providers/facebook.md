---
api_count: 6
apis:
- description: The primary way to read and write data to the Facebook social graph, providing access to user profiles, posts, pages, photos, videos, comments, and social interactions. Supports nodes, edges, and fiel
  name: Facebook Graph API
  slug: facebook-graph-api
- description: Programmatically manage Facebook ad campaigns, ad sets, ad creatives, Custom Audiences, and advertising reports. Access performance insights and automate campaign optimization at scale.
  name: Facebook Marketing API
  slug: facebook-marketing-api
- description: Manage Instagram Business and Creator account content including publishing media, retrieving posts, managing comments, discovering mentions, and accessing account insights for analytics.
  name: Instagram API
  slug: instagram-api
- description: Build messaging experiences on Facebook Messenger and Instagram Direct. Send and receive messages, create bot interactions, use templates and webviews, manage conversation routing, and integrate NLP c
  name: Messenger Platform API
  slug: messenger-platform-api
- description: Publish and manage content on Threads, Meta's text-based social platform. Create posts and carousels, retrieve and moderate replies, access insights, and manage creator profiles at scale.
  name: Threads API
  slug: threads-api
- description: Send and receive messages through WhatsApp Business Platform. Support text, media, templates, interactive messages, and manage business profiles for customer communication at scale.
  name: WhatsApp Business API
  slug: whatsapp-business-api
capabilities:
- description: Workflow capability for managing advertising campaigns across Facebook and Instagram. Combines Marketing API for campaign management with Graph API for content insights and Instagram API for visual ad
  name: Facebook Advertising and Marketing
  slug: advertising-and-marketing
- description: Workflow capability for customer messaging across Messenger and WhatsApp. Combines Messenger Platform API for Facebook/Instagram messaging with WhatsApp Business API for business communication. Used b
  name: Facebook Messaging and Communication
  slug: messaging-and-communication
- description: Workflow capability for managing content across Facebook, Instagram, and Threads. Combines Graph API for Facebook posts, Instagram API for visual content, and Threads API for text-based publishing. Us
  name: Facebook Social Media Management
  slug: social-media-management
common:
- title: ''
  type: Portal
  url: https://developers.facebook.com
- title: ''
  type: GettingStarted
  url: https://developers.facebook.com/docs/development/create-an-app
- title: ''
  type: ChangeLog
  url: https://developers.facebook.com/docs/graph-api/changelog
- title: ''
  type: StatusPage
  url: https://developers.facebook.com/status
- title: ''
  type: TermsOfService
  url: https://developers.facebook.com/terms
- title: ''
  type: PrivacyPolicy
  url: https://developers.facebook.com/policy
- title: ''
  type: RateLimits
  url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting
- title: ''
  type: GitHubOrganization
  url: https://github.com/facebook
- title: ''
  type: Blog
  url: https://developers.facebook.com/blog
- title: ''
  type: Support
  url: https://developers.facebook.com/support
- title: ''
  type: FAQ
  url: https://developers.facebook.com/docs/development/faq
- title: ''
  type: Errors
  url: https://developers.facebook.com/docs/graph-api/guides/error-handling
- title: ''
  type: SpectralRules
  url: rules/facebook-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/facebook-vocabulary.yaml
- title: Social Media Management
  type: NaftikoCapability
  url: capabilities/social-media-management.yaml
- title: Advertising and Marketing
  type: NaftikoCapability
  url: capabilities/advertising-and-marketing.yaml
- title: Messaging and Communication
  type: NaftikoCapability
  url: capabilities/messaging-and-communication.yaml
created: '2024-01-15'
description: Facebook is Meta's social networking platform providing APIs for developers to integrate with Facebook's ecosystem. The Facebook Graph API is the primary way to read and write data to the Facebook social graph. Meta also provides APIs for marketing and advertising, Instagram content management, Messenger bots, Threads publishing, and WhatsApp business messaging.
features:
- description: HTTP-based API for reading and writing to the Facebook social graph with nodes, edges, and fields.
  name: Graph API
- description: Real-time notifications when changes occur to data your app has access to.
  name: Webhooks
- description: Send multiple API calls in a single HTTP request for improved performance.
  name: Batch Requests
- description: OAuth 2.0 access tokens for user, page, app, and client authentication flows.
  name: Access Tokens
- description: Authentication system allowing users to log into apps with their Facebook credentials.
  name: Facebook Login
- description: Analytics tool for measuring ad effectiveness and tracking website visitor actions.
  name: Meta Pixel
- description: Server-side event tracking for ad measurement without browser dependencies.
  name: Conversions API
image: /assets/icons/facebook.png
integrations:
- description: Connect Shopify stores with Facebook and Instagram shops for social commerce.
  name: Shopify
- description: Facebook social plugins and login integration for WordPress sites.
  name: WordPress
- description: Sync Facebook lead ads and audiences with Salesforce CRM.
  name: Salesforce
- description: Connect Facebook advertising and messaging with HubSpot marketing automation.
  name: HubSpot
- description: Automate workflows between Facebook and thousands of other apps.
  name: Zapier
jsonld:
- class_count: 5
  name: Facebook Graph Api Context
  property_count: 14
  slug: facebook-graph-api-context
- class_count: 3
  name: Facebook Instagram Api Context
  property_count: 11
  slug: facebook-instagram-api-context
- class_count: 6
  name: Facebook Marketing Api Context
  property_count: 14
  slug: facebook-marketing-api-context
layout: provider
modified: '2026-04-18'
name: Facebook
rules:
- name: Facebook API Rules
  rule_count: 30
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 12
  slug: facebook-spectral-rules
skills: []
slug: facebook
solutions: []
tags:
- Advertising
- Content Publishing
- Messaging
- Social Media
- Social Networking
url: https://developers.facebook.com
use_cases:
- description: Manage pages, publish content, and engage with audiences across Facebook and Instagram.
  name: Social Media Management
- description: Automate ad campaign creation, optimization, and reporting at scale.
  name: Advertising Automation
- description: Build conversational experiences on Messenger and WhatsApp for customer support and engagement.
  name: Customer Messaging
- description: Publish and schedule content across Facebook, Instagram, and Threads platforms.
  name: Content Publishing
- description: Access performance data and audience insights across Meta platforms.
  name: Analytics and Insights
- description: Integrate product catalogs and shopping experiences with Facebook and Instagram shops.
  name: E-Commerce Integration
---
