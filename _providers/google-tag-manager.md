---
api_count: 2
apis:
- description: The Tag Manager API allows clients to access and modify container and tag configuration.
  name: Google Tag Manager API
  slug: ''
- description: The Server-side Tagging API provides APIs for building custom tags, clients, and variables that run in a server-side container, enabling server-to-server data collection and processing.
  name: Google Tag Manager Server-side Tagging API
  slug: ''
capabilities:
- description: Workflow for managing tag deployment lifecycle including accounts, containers, workspaces, tags, triggers, variables, and version publishing. Used by marketing technologists and web analytics engineer
  name: Google Tag Manager Tag Deployment Management
  slug: tag-deployment-management
common:
- title: ''
  type: Portal
  url: https://developers.google.com/tag-platform
- title: ''
  type: GettingStarted
  url: https://developers.google.com/tag-platform/tag-manager/api/v2/devguide
- title: ''
  type: Authentication
  url: https://developers.google.com/tag-platform/tag-manager/api/v2/authorization
- title: ''
  type: Documentation
  url: https://developers.google.com/tag-platform/tag-manager
- title: ''
  type: Blog
  url: https://blog.google/products/marketingplatform/
- title: ''
  type: SDK
  url: https://developers.google.com/tag-platform/tag-manager/api/v2/libraries
- title: ''
  type: Support
  url: https://support.google.com/tagmanager
- title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- title: ''
  type: SignUp
  url: https://tagmanager.google.com/
- title: ''
  type: Login
  url: https://tagmanager.google.com/
- title: ''
  type: RateLimits
  url: https://developers.google.com/tag-platform/tag-manager/api/v2/limits-quotas
- title: ''
  type: ChangeLog
  url: https://support.google.com/tagmanager/answer/4620708
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-tag-manager
- title: ''
  type: YouTube
  url: https://www.youtube.com/googlemarketingplatform
- title: ''
  type: SpectralRules
  url: rules/google-tag-manager-spectral-rules.yml
- title: Tag Manager API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/tag-manager.yaml
- title: Tag Deployment Management Workflow
  type: NaftikoCapability
  url: capabilities/tag-deployment-management.yaml
created: '2024-01-01'
description: Google Tag Manager is a tag management system that allows you to quickly and easily update measurement codes and related code fragments collectively known as tags on your website or mobile app.
features:
- description: List and manage Google Tag Manager accounts with full access control.
  name: Account Management
- description: Create, update, delete, and configure containers for web, mobile, and server-side tagging.
  name: Container Management
- description: Create and manage workspaces for collaborative tag development with conflict resolution.
  name: Workspace Management
- description: Create, update, delete, and revert tags with full parameter and firing trigger configuration.
  name: Tag Configuration
- description: Define triggers that control when and how tags fire based on events and conditions.
  name: Trigger Configuration
- description: Create and manage variables that provide dynamic values to tags and triggers.
  name: Variable Management
- description: Create, publish, and manage container versions with rollback capabilities.
  name: Version Control
- description: Manage user access and permissions at the account and container level.
  name: User Permissions
- description: Build custom server-side tags, clients, and variables for server-to-server data collection.
  name: Server-Side Tagging
- description: Structured data layer for passing information between your website and Tag Manager.
  name: Data Layer
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_tag_manager.svg
integrations:
- description: Native integration with Google Analytics 4 for event tracking and measurement.
  name: Google Analytics
- description: Deploy Google Ads conversion tracking and remarketing tags with built-in templates.
  name: Google Ads
- description: Integrate with Campaign Manager, Display & Video 360, and Search Ads 360.
  name: Google Marketing Platform
- description: Deploy and manage Facebook Pixel tracking with community template support.
  name: Facebook Pixel
- description: Integrate with consent management platforms for privacy-compliant tag firing.
  name: Consent Management Platforms
jsonld:
- class_count: 8
  name: Google Tag Manager Context
  property_count: 8
  slug: google-tag-manager-context
- class_count: 0
  name: Google Tag Manager V2 Context
  property_count: 0
  slug: google-tag-manager-v2-context
layout: provider
modified: '2026-04-18'
name: Google Tag Manager
rules:
- name: Google Tag Manager API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: google-tag-manager-spectral-rules
skills: []
slug: google-tag-manager
solutions: []
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
url: https://tagmanager.google.com/
use_cases:
- description: Deploy and manage marketing and analytics tags without modifying website code.
  name: Marketing Tag Deployment
- description: Track conversions across multiple advertising platforms with centralized tag management.
  name: Conversion Tracking
- description: Implement consent-based tag firing and data collection policies for GDPR and CCPA compliance.
  name: Privacy Compliance
- description: Deploy and manage A/B testing tags and experiment configurations across web properties.
  name: A/B Testing
- description: Process data server-side for improved performance, accuracy, and privacy compliance.
  name: Server-Side Data Collection
---
