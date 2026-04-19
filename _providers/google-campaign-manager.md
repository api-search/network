---
api_count: 2
apis:
- description: Manage your DoubleClick Campaign Manager ad campaigns and reports programmatically. Create, retrieve, update, and delete campaigns, creatives, placements, and generate comprehensive reporting data.
  name: Campaign Manager 360 API
  slug: ''
- description: Data Transfer v2.0 provides raw, event-level reporting data from Campaign Manager 360 beyond what is available through standard reporting. Data is delivered to Google Cloud Storage as CSV files for ad
  name: Campaign Manager 360 Data Transfer v2.0
  slug: ''
capabilities:
- description: Unified workflow for managing digital advertising campaigns, ads, placements, and performance reports. Used by ad operations specialists and digital marketers.
  name: Google Campaign Manager Campaign Management
  slug: campaign-management
common:
- title: ''
  type: Portal
  url: https://developers.google.com/
- title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- title: ''
  type: Blog
  url: https://blog.google/products/marketingplatform/
- title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- title: ''
  type: GitHubRepository
  url: https://github.com/googleads/googleads-dfa-reporting-samples
- title: ''
  type: JSONLD
  url: json-ld/google-campaign-manager-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/google-campaign-manager-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/google-campaign-manager-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/campaign-management.yaml
created: '2024'
description: The Campaign Manager 360 API allows developers to programmatically manage campaigns, creatives, reports, and other advertising operations in Google's Campaign Manager 360 platform.
features:
- description: Create, update, and manage advertising campaigns from inception through completion with full programmatic control.
  name: Campaign Lifecycle Management
- description: Automate the placement and scheduling of ads across publisher sites with targeting and delivery rules.
  name: Ad Trafficking
- description: Generate standard, reach, path-to-conversion, cross-dimension, floodlight, and cross-media reach reports.
  name: Multi-Format Reporting
- description: Automatically generate ad tags for publishers to install on their pages.
  name: Placement Tag Generation
- description: Configure geo-targeting, technology targeting, day-part targeting, and audience segment rules.
  name: Audience Targeting
- description: Track and attribute conversions using Floodlight tags for cross-channel measurement.
  name: Floodlight Conversion Tracking
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
integrations:
- description: Combine Campaign Manager 360 data with Google Analytics for unified web analytics and attribution.
  name: Google Analytics
- description: Coordinate campaign management between Campaign Manager 360 and Google Ads platforms.
  name: Google Ads
- description: Integrate with DV360 for programmatic buying and campaign execution.
  name: Display & Video 360
- description: Export raw event-level data via Data Transfer for advanced analysis in BigQuery or other tools.
  name: Google Cloud Storage
- description: Automate Campaign Manager operations using Google Apps Script advanced service.
  name: Google Apps Script
jsonld:
- class_count: 0
  name: Google Campaign Manager Context
  property_count: 0
  slug: google-campaign-manager-context
layout: provider
modified: '2026-04-18'
name: Google Campaign Manager
rules:
- name: Google Campaign Manager API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: google-campaign-manager-spectral-rules
skills: []
slug: google-campaign-manager
solutions: []
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
url: https://developers.google.com/doubleclick-advertisers
use_cases:
- description: Automate the creation and configuration of advertising campaigns, ads, and placements across publisher inventory.
  name: Programmatic Campaign Setup
- description: Generate and schedule reports to analyze campaign performance, reach, and conversion data.
  name: Performance Reporting
- description: Use path-to-conversion and cross-media reach reports to understand multi-channel advertising impact.
  name: Cross-Channel Attribution
- description: Streamline trafficking workflows including placement creation, tag generation, and creative assignment.
  name: Ad Operations Automation
---
