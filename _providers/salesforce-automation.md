---
api_count: 15
apis:
- description: Core REST API for accessing Salesforce data and metadata programmatically.
  name: Salesforce REST API
  slug: ''
- description: Enterprise-grade SOAP API for complex integrations and bulk operations.
  name: Salesforce SOAP API
  slug: ''
- description: Asynchronous API optimized for loading and querying large data sets.
  name: Salesforce Bulk API 2.0
  slug: ''
- description: API for managing customizations and building tools for application lifecycle management.
  name: Salesforce Metadata API
  slug: ''
- description: Real-time event monitoring and push notifications using Bayeux protocol.
  name: Salesforce Streaming API
  slug: ''
- description: Event-driven architecture for publishing and subscribing to custom events.
  name: Salesforce Platform Events API
  slug: ''
- description: API for accessing and manipulating Analytics dashboards and datasets.
  name: Salesforce Analytics API
  slug: ''
- description: API for building custom development tools for Salesforce applications.
  name: Salesforce Tooling API
  slug: ''
- description: REST API for integrating mobile apps, intranet sites, and third-party web applications with Salesforce, including Chatter feeds, groups, and users.
  name: Salesforce Connect REST API
  slug: ''
- description: gRPC-based API for publishing and subscribing to platform events, change data capture events, and custom channels in real time.
  name: Salesforce Pub/Sub API
  slug: ''
- description: GraphQL API for querying Salesforce data with a single endpoint, reducing round trips and improving application performance.
  name: Salesforce GraphQL API
  slug: ''
- description: API for receiving near-real-time notifications of changes to Salesforce records to synchronize corresponding records in external data stores.
  name: Salesforce Change Data Capture API
  slug: ''
- description: REST API for invoking standard and custom actions programmatically, including flow actions and process automation triggers.
  name: Salesforce Invocable Actions API
  slug: ''
- description: REST API for executing multiple API requests in a single call, with the ability to use the output of one request as input to another.
  name: Salesforce Composite API
  slug: ''
- description: Framework for exposing Apex classes and methods as RESTful web services, enabling custom API endpoints on the Salesforce platform.
  name: Salesforce Apex REST API
  slug: ''
capabilities:
- description: Unified workflow combining the Salesforce REST API and Bulk API for comprehensive data operations including CRUD, queries, search, and bulk data loading. Used by Salesforce admins and integration deve
  name: Salesforce Data Operations
  slug: data-operations
common:
- title: ''
  type: Portal
  url: https://developer.salesforce.com
- title: ''
  type: Website
  url: https://www.salesforce.com
- title: ''
  type: Developer Portal
  url: https://developer.salesforce.com
- title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs
- title: ''
  type: API Library
  url: https://developer.salesforce.com/docs/apis
- title: ''
  type: Trailhead Learning
  url: https://trailhead.salesforce.com
- title: ''
  type: API Status
  url: https://status.salesforce.com
- title: ''
  type: Community
  url: https://developer.salesforce.com/forums
- title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs
- title: ''
  type: Pricing
  url: https://www.salesforce.com/editions-pricing/overview/
- title: ''
  type: Terms of Service
  url: https://www.salesforce.com/company/legal/agreements/
- title: ''
  type: Privacy Policy
  url: https://www.salesforce.com/company/privacy/
- title: ''
  type: Sign Up
  url: https://developer.salesforce.com/signup
- title: ''
  type: Login
  url: https://login.salesforce.com
- title: ''
  type: GitHub
  url: https://github.com/salesforce
- title: ''
  type: GitHub Organization
  url: https://github.com/developerforce
- title: ''
  type: Stack Exchange
  url: https://salesforce.stackexchange.com
- title: ''
  type: X (Twitter)
  url: https://twitter.com/salesforcedevs
- title: ''
  type: Support
  url: https://developer.salesforce.com/support
- title: ''
  type: Contact
  url: https://www.salesforce.com/company/contact-us/
- title: ''
  type: Rate Limits
  url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm
- title: ''
  type: API Versioning
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_versions.htm
- title: ''
  type: Postman Collection
  url: https://www.postman.com/salesforce-developers/workspace/salesforce-developers/overview
- title: ''
  type: Postman GitHub
  url: https://github.com/forcedotcom/postman-salesforce-apis
- title: ''
  type: SDKs
  url: https://jsforce.github.io/
- title: ''
  type: Release Notes
  url: https://help.salesforce.com/s/articleView?id=release-notes.rn_api_nc.htm&language=en_US&release=248&type=5
- title: ''
  type: API End-of-Life Policy
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/api_rest_eol.htm
- title: ''
  type: SpectralRules
  url: rules/salesforce-automation-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/salesforce-automation-vocabulary.yaml
- title: Data Operations Workflow
  type: NaftikoCapability
  url: capabilities/data-operations.yaml
- title: ''
  type: JSONStructure
  url: json-structure/salesforce-automation-flow-structure.json
- title: Flow Example
  type: Example
  url: examples/salesforce-automation-flow-example.json
- title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce
created: '2024-01-01'
description: A collection of Salesforce APIs for automating business processes, sales operations, and customer relationship management.
features:
- description: Supports multiple OAuth flows including authorization code, JWT bearer, and client credentials.
  name: OAuth 2.0 Authentication
- description: Salesforce Object Query Language for structured data queries across objects.
  name: SOQL Queries
- description: Full-text search across multiple objects using Salesforce Object Search Language.
  name: SOSL Search
- description: Asynchronous bulk API for loading, deleting, and querying millions of records.
  name: Bulk Data Operations
- description: Platform events, Change Data Capture, and streaming API for real-time notifications.
  name: Real-Time Events
- description: Declarative automation with Flow Builder for record-triggered, scheduled, and screen flows.
  name: Flow Automation
- description: Execute multiple API requests in a single call with request chaining.
  name: Composite API
- description: Single-endpoint GraphQL API for efficient data queries.
  name: GraphQL Support
- description: Programmatic invocation of standard and custom automation actions.
  name: Invocable Actions
- description: Multi-step approval workflows with programmatic submission and management.
  name: Approval Processes
image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
integrations:
- description: Native integration platform for connecting Salesforce with enterprise systems.
  name: MuleSoft
- description: Salesforce-owned collaboration platform with deep CRM integration.
  name: Slack
- description: Analytics and visualization platform integrated with Salesforce data.
  name: Tableau
- description: Cloud application platform for extending Salesforce with custom apps.
  name: Heroku
- description: Official Postman workspace with pre-built API collections for testing.
  name: Postman
jsonld:
- class_count: 0
  name: Salesforce Automation Context
  property_count: 16
  slug: salesforce-automation-context
layout: provider
modified: '2026-04-18'
name: Salesforce Automation
rules:
- name: Salesforce Automation API Rules
  rule_count: 37
  severity_counts:
    error: 18
    hint: 0
    info: 7
    warn: 12
  slug: salesforce-automation-spectral-rules
skills: []
slug: salesforce-automation
solutions: []
tags:
- Automation
- Cloud
- CRM
- Enterprise
- Sales
url: https://developer.salesforce.com
use_cases:
- description: Automate lead assignment, opportunity stage progression, and deal closure workflows.
  name: Sales Pipeline Automation
- description: Bulk import and export of large datasets between Salesforce and external systems.
  name: Data Migration
- description: Keep external systems in sync with Salesforce using Change Data Capture events.
  name: Real-Time Data Sync
- description: Build custom REST endpoints using Apex REST for bespoke integration scenarios.
  name: Custom Integrations
- description: Programmatic access to Einstein Analytics dashboards and datasets.
  name: Analytics and Reporting
- description: Trigger flows, approval processes, and invocable actions based on data changes.
  name: Process Automation
---
