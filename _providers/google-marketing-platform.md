---
api_count: 1
apis:
- description: The Marketing Platform Admin API enables programmatic management of organization-level settings including links to Google Analytics accounts, service level configuration, and organization administrati
  name: Google Marketing Platform Admin API
  slug: admin
capabilities:
- description: Unified workflow for managing Google Marketing Platform organizations and their Analytics account integrations including service level configuration. Used by marketing platform administrators and anal
  name: Google Marketing Platform Analytics Administration
  slug: marketing-analytics
common:
- title: ''
  type: Portal
  url: https://marketingplatform.google.com
- title: ''
  type: GettingStarted
  url: https://developers.google.com/marketing-platform/devguides/api/admin/v1/rest
- title: ''
  type: Documentation
  url: https://developers.google.com/marketing-platform
- title: ''
  type: Authentication
  url: https://developers.google.com/docs/api/how-tos/authorizing
- title: ''
  type: Pricing
  url: https://marketingplatform.google.com/about/
- title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- title: ''
  type: Support
  url: https://developers.google.com/marketing-platform/support
- title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
- title: Admin API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/admin-api.yaml
- title: Marketing Analytics Administration Workflow
  type: NaftikoCapability
  url: capabilities/marketing-analytics.yaml
created: '2026-03-13'
description: The Google Marketing Platform Admin API provides programmatic access to manage links between Google Marketing Platform organizations and Google Analytics accounts. It enables creating, updating, deleting, and listing organization links and managing service levels for integrated marketing analytics.
features:
- description: List and manage Google Marketing Platform organizations with programmatic access to organization settings.
  name: Organization Management
- description: Create, list, and delete links between Marketing Platform organizations and Google Analytics accounts.
  name: Analytics Account Linking
- description: Set and manage Analytics property service levels including standard and 360 tier assignments.
  name: Service Level Configuration
- description: Access and manage multiple Marketing Platform organizations from a single authenticated session.
  name: Multi-Organization Access
image: /assets/icons/google-marketing-platform.png
integrations:
- description: Direct linking and service level management for Google Analytics accounts within Marketing Platform organizations.
  name: Google Analytics
- description: Part of the Google Marketing Platform suite for tag management and measurement integration.
  name: Google Tag Manager
- description: Integrated advertising platform within Google Marketing Platform for programmatic media buying.
  name: Display and Video 360
- description: Search campaign management platform integrated with Marketing Platform for cross-channel analytics.
  name: Search Ads 360
jsonld:
- class_count: 0
  name: Openapi Context
  property_count: 0
  slug: openapi-context
layout: provider
modified: '2026-04-18'
name: Google Marketing Platform Admin
rules:
- name: Google Marketing Platform Admin API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: google-marketing-platform-spectral-rules
skills: []
slug: google-marketing-platform
solutions: []
tags:
- Analytics
- Google Marketing Platform
- Marketing
- Organization Management
- Platform Administration
url: https://raw.githubusercontent.com/api-evangelist/google-marketing-platform/refs/heads/main/apis.yml
use_cases:
- description: Programmatically link Google Analytics accounts to Marketing Platform organizations for enterprise-scale deployments.
  name: Enterprise Analytics Setup
- description: Automate the assignment of Analytics 360 service levels to properties across large organizations.
  name: Service Tier Management
- description: List and audit all Marketing Platform organizations and their linked Analytics accounts for governance.
  name: Organization Auditing
---
