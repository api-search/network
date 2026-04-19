---
api_count: 6
apis:
- description: The Looker API provides programmatic access to Looker functionality including running queries, managing users, creating dashboards, and administering the platform.
  name: Looker API
  slug: api
- description: API for programmatically managing LookML projects, models, and views.
  name: LookML API
  slug: lookml
- description: The Looker Action API enables developers to define custom actions, or destinations, to which Looker can send query results, dashboard results, or user interactions via a webhook-like API.
  name: Looker Action API
  slug: action
- description: The Looker Embed SDK is a JavaScript library for embedding Looker content such as dashboards, Looks, Explores, reports, and extensions into web applications, with support for signed SSO and cookieless
  name: Looker Embed SDK
  slug: embed-sdk
- description: The Looker Extension Framework provides APIs and SDKs for building custom extensions that run inside the Looker UI, with access to the Looker API, Looker components library, and the Embed SDK.
  name: Looker Extension Framework API
  slug: extension-framework
- description: The Looker (Google Cloud core) REST API provides management capabilities for Looker instances running on Google Cloud, including instance lifecycle management, backups, and operations.
  name: Looker (Google Cloud core) API
  slug: google-cloud-core
capabilities:
- description: Unified workflow for business intelligence analytics including dashboards, looks, queries, and user management. Used by data analysts and BI administrators.
  name: Looker Analytics and Reporting
  slug: analytics-and-reporting
common:
- title: ''
  type: DeveloperPortal
  url: https://developers.looker.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/looker-open-source
- title: ''
  type: Support
  url: https://cloud.google.com/looker/docs/support
- title: ''
  type: StatusPage
  url: https://status.looker.com/
- title: ''
  type: PrivacyPolicy
  url: https://looker.com/privacy
- title: ''
  type: TermsOfService
  url: https://looker.com/terms
- title: ''
  type: SDK
  url: https://docs.cloud.google.com/looker/docs/api-sdk
- title: ''
  type: ChangeLog
  url: https://github.com/looker-open-source/sdk-codegen/blob/main/CHANGELOG.md
- title: ''
  type: ReleaseNotes
  url: https://docs.cloud.google.com/looker/docs/release-notes
- title: ''
  type: Pricing
  url: https://cloud.google.com/looker/pricing
- title: ''
  type: GettingStarted
  url: https://docs.cloud.google.com/looker/docs/api-getting-started
- title: ''
  type: Authentication
  url: https://docs.cloud.google.com/looker/docs/api-auth
- title: ''
  type: Tutorials
  url: https://developers.looker.com/api/tutorials/interactive-api-docs-whats-next/
- title: ''
  type: JSONSchema
  url: json-schema/looker-dashboard-schema.json
- title: ''
  type: JSONLD
  url: json-ld/looker-context.jsonld
- title: Looker API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/looker-api.yaml
- title: Analytics and Reporting Workflow
  type: NaftikoCapability
  url: capabilities/analytics-and-reporting.yaml
created: '2024-01-01'
description: Looker is a business intelligence and data analytics platform that enables organizations to explore, analyze, and share real-time business analytics.
features:
- description: Enable business users to explore data, build visualizations, and create dashboards without SQL knowledge using LookML models.
  name: Self-Service Analytics
- description: Define reusable data models in LookML that provide a semantic layer between databases and end-user analytics.
  name: Data Modeling with LookML
- description: Embed interactive dashboards, reports, and data explorations directly into web applications using SSO and cookieless authentication.
  name: Embedded Analytics
- description: Schedule and deliver reports and dashboards via email, Slack, S3, or custom action destinations.
  name: Scheduled Reports
- description: Build webhook-based actions to send query results to any external destination or trigger workflows.
  name: Custom Actions
- description: Programmatically manage users, roles, dashboards, queries, and platform settings through the Looker API.
  name: API-Driven Administration
image: https://looker.com/assets/img/images/logos/looker-logo.png
integrations:
- description: Native optimized connector for querying and analyzing data in Google BigQuery data warehouse.
  name: Google BigQuery
- description: High-performance connector for Snowflake cloud data warehouse with push-down query optimization.
  name: Snowflake
- description: Native connector for querying and visualizing data in Amazon Redshift data warehouse.
  name: Amazon Redshift
- description: Deliver scheduled reports and dashboard snapshots to Slack channels with interactive query capabilities.
  name: Slack
- description: Export query results and dashboard data directly to Google Sheets for collaborative analysis.
  name: Google Sheets
- description: Connect to Salesforce data for CRM analytics and combine with other data sources for unified views.
  name: Salesforce
jsonld:
- class_count: 0
  name: Looker Context
  property_count: 0
  slug: looker-context
layout: provider
modified: '2026-04-18'
name: Looker
rules:
- name: Looker API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: looker-spectral-rules
skills: []
slug: looker
solutions: []
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
url: https://raw.githubusercontent.com/api-evangelist/looker/refs/heads/main/apis.yml
use_cases:
- description: Build real-time executive dashboards aggregating KPIs from multiple data sources for leadership visibility.
  name: Executive Dashboards
- description: Embed analytics into SaaS products to provide customers with self-service reporting and data exploration.
  name: Customer-Facing Analytics
- description: Monitor data quality, usage patterns, and access controls across the organization through audit reports.
  name: Data Governance Reporting
- description: Analyze campaign performance, attribution, and ROI across marketing channels with unified data models.
  name: Marketing Performance Analytics
- description: Track operational metrics and KPIs in real time with automated alerting and scheduled report delivery.
  name: Operational Monitoring
---
