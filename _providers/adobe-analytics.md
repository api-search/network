---
api_count: 6
apis:
- description: The Adobe Analytics 2.0 APIs provide programmatic access to data, reports, and administration features within Adobe Analytics. They allow you to perform almost any action available in the Analytics us
  name: Adobe Analytics API
  slug: ''
- description: The Bulk Data Insertion API (BDIA) lets you upload server-side call data in batches of compressed CSV files instead of using client-side libraries such as AppMeasurement. It is the recommended success
  name: Adobe Analytics Bulk Data Insertion API
  slug: ''
- description: The Livestream API is a reporting feature in Adobe Analytics that allows clients to receive traffic data processed by Adobe Analytics in real time. Hits are streamed to the client on a hit-by-hit basi
  name: Adobe Analytics Livestream API
  slug: ''
- description: The Data Repair API allows you to permanently delete or transform data that has already been ingested in Adobe Analytics. It provides endpoints for estimating repair scope, creating repair jobs, and m
  name: Adobe Analytics Data Repair API
  slug: ''
- description: The Data Insertion API allows server-side data submission to Adobe Analytics one event at a time using HTTP GET or POST requests. Unlike the Bulk Data Insertion API which processes compressed CSV file
  name: Adobe Analytics Data Insertion API
  slug: ''
- description: The Adobe Analytics 1.4 APIs provide programmatic access to reporting, classifications, data sources, and report suite configuration. This version is deprecated and scheduled for end-of-life on August
  name: Adobe Analytics 1.4 API
  slug: ''
asyncapis:
- description: The Adobe Analytics Livestream API delivers real-time analytics hit data to a connected client as each hit is processed by Adobe Analytics servers. Data is streamed in line-delimited JSON format compr
  name: Adobe Analytics Livestream API
  slug: adobe-analytics-livestream-asyncapi
capabilities:
- description: Unified workflow for server-side data collection and ingestion combining Bulk Data Insertion for high-volume event uploads with the Analytics API for report suite discovery and validation. Used by dat
  name: Adobe Analytics Data Collection
  slug: data-collection
- description: 'Unified workflow for analytics reporting, component management, and data governance combining the Analytics 2.0 API for reports, segments, calculated metrics, and the Data Repair API for data quality '
  name: Adobe Analytics Reporting And Analysis
  slug: reporting-and-analysis
common:
- title: ''
  type: Portal
  url: https://developer.adobe.com/analytics-apis/docs/2.0/
- title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/docs/analytics.html
- title: ''
  type: GettingStarted
  url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/
- title: ''
  type: Console
  url: https://developer.adobe.com/console/
- title: ''
  type: Authentication
  url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/authentication/
- title: ''
  type: Support
  url: https://developer.adobe.com/analytics-apis/docs/2.0/support/
- title: ''
  type: Support
  url: https://experienceleaguecommunities.adobe.com/t5/adobe-analytics/ct-p/adobe-analytics-community
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/adobe-analytics
- title: ''
  type: GitHubOrganization
  url: https://github.com/AdobeDocs
- title: ''
  type: ChangeLog
  url: https://experienceleague.adobe.com/en/docs/analytics/release-notes/latest
- title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy/policy.html
- title: ''
  type: StatusPage
  url: https://status.adobe.com/
- title: ''
  type: Blog
  url: https://blog.adobe.com/en/topics/analytics
- title: ''
  type: GitHubRepository
  url: https://github.com/AdobeDocs/analytics-2.0-apis
- title: ''
  type: JSONSchema
  url: json-schema/adobe-analytics-report-request-schema.json
- title: ''
  type: JSONLD
  url: json-ld/adobe-analytics-context.jsonld
- title: Analytics MCP Servers Documentation
  type: GitHubRepository
  url: https://github.com/AdobeDocs/analytics-mcp
- title: Analytics 1.4 APIs Documentation
  type: GitHubRepository
  url: https://github.com/AdobeDocs/analytics-1.4-apis
- title: ''
  type: Training
  url: https://experienceleague.adobe.com/docs/analytics-learn/tutorials/overview.html
- title: ''
  type: JSONLD
  url: json-ld/adobe-analytics-bulk-data-insertion-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/adobe-analytics-data-repair-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/adobe-analytics-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/adobe-analytics-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/reporting-and-analysis.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-collection.yaml
created: 2024-01-01 00:00:00+00:00
description: Adobe Analytics provides real-time analytics and detailed segmentation capabilities across all marketing channels, enabling organizations to discover high-value audiences and power customer intelligence.
features:
- description: Access and analyze data in real time as visitors interact with digital properties.
  name: Real-Time Analytics
- description: Build custom segments to isolate and analyze specific visitor groups and behaviors.
  name: Custom Segmentation
- description: Create derived metrics combining existing metrics with mathematical formulas.
  name: Calculated Metrics
- description: Organize and partition data collection across multiple sites and business units.
  name: Report Suites
- description: Mark specific dates or ranges in reports with notes for contextual analysis.
  name: Annotations
- description: Upload server-side event data in compressed CSV batches for high-volume collection.
  name: Bulk Data Insertion
- description: Permanently delete or transform previously ingested data for privacy compliance.
  name: Data Repair
- description: Receive real-time streaming hit data as each event is processed by Adobe servers.
  name: Livestream
- description: Programmatically discover all available dimensions and metrics in report suites.
  name: Dimension And Metric Exploration
- description: Apply tags to segments, metrics, and other components for organization and discovery.
  name: Component Tagging
image: /assets/icons/adobe-analytics.png
integrations:
- description: Send Analytics data to Experience Platform for unified customer profiles and journey orchestration.
  name: Adobe Experience Platform
- description: Use Analytics segments to power personalization and A/B testing in Adobe Target.
  name: Adobe Target
- description: Share audience segments between Analytics and Audience Manager for cross-channel activation.
  name: Adobe Audience Manager
- description: Integrate campaign data with Analytics for end-to-end campaign performance measurement.
  name: Adobe Campaign
- description: Extend Analytics data into CJA for cross-channel analysis with Experience Platform data.
  name: Adobe Customer Journey Analytics
- description: Deploy and manage Analytics tags via Adobe Experience Platform Launch tag management.
  name: Adobe Launch
- description: Import Google Ads cost and click data for integrated paid search analytics.
  name: Google Ads
- description: Connect Analytics data to Power BI dashboards for enterprise reporting and visualization.
  name: Microsoft Power BI
jsonld:
- class_count: 0
  name: Adobe Analytics Bulk Data Insertion Context
  property_count: 4
  slug: adobe-analytics-bulk-data-insertion-context
- class_count: 0
  name: Adobe Analytics Context
  property_count: 23
  slug: adobe-analytics-context
- class_count: 0
  name: Adobe Analytics Data Repair Context
  property_count: 6
  slug: adobe-analytics-data-repair-context
layout: provider
modified: '2026-04-18'
name: Adobe Analytics
rules:
- name: Adobe Analytics API Rules
  rule_count: 21
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 1
  slug: adobe-analytics-spectral-rules
skills: []
slug: adobe-analytics
solutions: []
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
url: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/apis.yml
use_cases:
- description: Measure effectiveness of marketing campaigns across channels with attribution and conversion tracking.
  name: Marketing Campaign Analysis
- description: Analyze multi-touch customer journeys to identify drop-off points and optimize conversion paths.
  name: Customer Journey Optimization
- description: Evaluate which content resonates most with audiences and drives engagement.
  name: Content Performance Tracking
- description: Discover high-value audience segments for personalized marketing and advertising.
  name: Audience Discovery And Targeting
- description: Delete or repair PII and sensitive data to comply with GDPR, CCPA, and other regulations.
  name: Privacy Compliance Data Management
- description: Monitor live traffic and KPIs with streaming data for immediate anomaly detection.
  name: Real-Time Monitoring And Alerting
- description: Collect analytics data from backend systems, IoT devices, and server-side applications.
  name: Server-Side Data Collection
- description: Combine web, mobile, and offline data for unified cross-channel analytics reporting.
  name: Cross-Channel Reporting
---
