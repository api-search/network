---
api_count: 19
apis:
- description: The Amplitude HTTP V2 API enables developers to send event data directly from servers or clients to Amplitude's analytics platform. It supports uploading individual or batched events along with user p
  name: Amplitude HTTP V2 API
  slug: http-v2-api
- description: The Amplitude Batch Event Upload API is optimized for high-volume server-side event ingestion. It accepts batches of events up to 20MB per request and is designed for use cases where data volume may e
  name: Amplitude Batch Event Upload API
  slug: batch-event-upload-api
- description: The Amplitude Identify API allows developers to update user properties for a specific user without needing to send an accompanying event. This is useful for setting or modifying user attributes such a
  name: Amplitude Identify API
  slug: identify-api
- description: The Amplitude Group Identify API allows developers to set or update properties on groups within Amplitude. Groups are entities such as companies, teams, or accounts that users belong to. This API enab
  name: Amplitude Group Identify API
  slug: group-identify-api
- description: 'The Amplitude Dashboard REST API provides programmatic access to the same data displayed in Amplitude''s dashboard charts and graphs. It returns results in JSON format and supports queries filtered by '
  name: Amplitude Dashboard REST API
  slug: dashboard-rest-api
- description: The Amplitude Export API enables bulk export of raw event data for a given project within a specified date range. Results are returned as zipped archives of JSON files containing complete event record
  name: Amplitude Export API
  slug: export-api
- description: The Amplitude Behavioral Cohorts API allows developers to list, export, and upload cohorts in Amplitude. Cohorts are groups of users defined by shared behavioral patterns or properties. This API suppo
  name: Amplitude Behavioral Cohorts API
  slug: behavioral-cohorts-api
- description: 'The Amplitude Taxonomy API provides programmatic management of your analytics tracking plan. It supports creating, reading, updating, and deleting event categories, event types, event properties, and '
  name: Amplitude Taxonomy API
  slug: taxonomy-api
- description: The Amplitude Attribution API allows developers to send attribution campaign events to Amplitude from ad networks, attribution providers, or custom marketing tools. It associates users with the campai
  name: Amplitude Attribution API
  slug: attribution-api
- description: The Amplitude Chart Annotations API enables developers to programmatically create, retrieve, update, and delete annotations on Amplitude charts. Annotations mark significant events such as product rel
  name: Amplitude Chart Annotations API
  slug: chart-annotations-api
- description: The Amplitude Releases API allows developers to programmatically track software releases and deployments in Amplitude. By recording release events, teams can correlate product changes with analytics m
  name: Amplitude Releases API
  slug: releases-api
- description: 'The Amplitude Session Replay API enables developers to upload and manage session replay data for playback within Amplitude. Session replays provide qualitative insights by recording user interactions '
  name: Amplitude Session Replay API
  slug: session-replay-api
- description: The Amplitude User Profile API serves user profiles that include user properties, computed user properties, a list of cohort IDs the user belongs to, and personalized recommendations. It enables real-
  name: Amplitude User Profile API
  slug: user-profile-api
- description: 'The Amplitude User Mapping (Aliasing) API allows developers to merge users with different user IDs together in Amplitude. This is useful when a user initially interacts with a product anonymously and '
  name: Amplitude User Mapping API
  slug: user-mapping-api
- description: The Amplitude User Privacy API provides endpoints for managing user data in compliance with privacy regulations such as GDPR and CCPA. It supports requesting the deletion or suppression of user data b
  name: Amplitude User Privacy API
  slug: user-privacy-api
- description: The Amplitude SCIM API implements the System for Cross-domain Identity Management (SCIM) 2.0 standard for automated user provisioning and deprovisioning. It allows identity providers such as Okta, Azu
  name: Amplitude SCIM API
  slug: scim-api
- description: The Amplitude Data Subject Access Request (DSAR) API enables organizations to programmatically handle privacy requests in compliance with GDPR, CCPA, and other data protection regulations. It supports
  name: Amplitude Data Subject Access Request API
  slug: dsar-api
- description: The Amplitude Experiment Evaluation API retrieves variant assignment data for users through remote evaluation. When called, it evaluates targeting rules and returns the assigned variant for each activ
  name: Amplitude Experiment Evaluation API
  slug: experiment-evaluation-api
- description: The Amplitude Experiment Management API provides programmatic control over feature flags and experiments. It supports creating, updating, activating, and archiving experiments and flags, as well as ma
  name: Amplitude Experiment Management API
  slug: experiment-management-api
capabilities:
- description: Unified workflow for sending events and identifying users. For data engineers.
  name: Amplitude Analytics Ingestion
  slug: amplitude-analytics-ingestion
- description: Export raw event data and manage behavioral cohorts. For data analysts.
  name: Amplitude Data Export and Cohorts
  slug: amplitude-data-export-and-cohorts
- description: Manage and evaluate A/B experiments and feature flags. For product managers.
  name: Amplitude Experimentation
  slug: amplitude-experimentation
- description: Manage event schemas and chart annotations. For data governance teams.
  name: Amplitude Governance and Taxonomy
  slug: amplitude-governance-and-taxonomy
- description: SCIM provisioning and privacy compliance. For IT admins and compliance teams.
  name: Amplitude Identity and Privacy
  slug: amplitude-identity-and-privacy
common:
- title: ''
  type: Portal
  url: https://amplitude.com
- title: ''
  type: Documentation
  url: https://amplitude.com/docs
- title: ''
  type: GettingStarted
  url: https://amplitude.com/docs/get-started
- title: ''
  type: Authentication
  url: https://amplitude.com/docs/apis/authentication
- title: ''
  type: SDK
  url: https://amplitude.com/docs/sdks
- title: ''
  type: GitHubOrganization
  url: https://github.com/amplitude
- title: ''
  type: Blog
  url: https://amplitude.com/blog
- title: ''
  type: Academy
  url: https://academy.amplitude.com
- title: ''
  type: Support
  url: https://help.amplitude.com
- title: ''
  type: Pricing
  url: https://amplitude.com/pricing
- title: ''
  type: StatusPage
  url: https://status.amplitude.com
- title: ''
  type: TermsOfService
  url: https://amplitude.com/terms
- title: ''
  type: PrivacyPolicy
  url: https://amplitude.com/privacy
- title: ''
  type: JSONLD
  url: json-ld/amplitude-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/amplitude-event-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/amplitude-cohort-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/amplitude-experiment-schema.json
- title: ''
  type: SpectralRules
  url: rules/amplitude-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amplitude-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amplitude-analytics-ingestion.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amplitude-data-export-and-cohorts.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amplitude-experimentation.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amplitude-governance-and-taxonomy.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amplitude-identity-and-privacy.yaml
- title: ''
  type: JSONStructure
  url: json-structure/behavioral-cohorts-api-cohort-request-response-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/dashboard-rest-api-user-search-result-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/scim-api-scim-group-request-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/http-v2-api-event-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/experiment-evaluation-api-flag-configuration-structure.json
created: ''
description: Amplitude is a digital analytics platform that helps product teams understand user behavior, run experiments, and drive growth. It provides a suite of APIs for event ingestion, user management, cohort syncing, taxonomy governance, A/B testing, and data export. Amplitude is widely used by product, data, and engineering teams to build better digital experiences through data-driven insights.
features:
- description: High-throughput server-side and client-side event ingestion via HTTP V2 and Batch APIs.
  name: Event Ingestion
- description: Track user properties, behaviors, and cohorts for deep segmentation and reporting.
  name: User Analytics
- description: Run feature flag experiments and measure variant impact on key metrics.
  name: A/B Experimentation
- description: Define and sync audience segments based on user behavioral patterns.
  name: Behavioral Cohorts
- description: Programmatically manage event schemas, properties, and data governance rules.
  name: Taxonomy Management
- description: Export raw event data in bulk for warehousing and offline analysis.
  name: Data Export
- description: Capture and replay user sessions for qualitative UX research.
  name: Session Replay
- description: SCIM-based provisioning, user aliasing, and identity merging across systems.
  name: Identity Management
- description: GDPR and CCPA compliant data deletion and suppression APIs.
  name: Privacy Compliance
- description: Associate users with acquisition campaigns from ad networks and marketing tools.
  name: Attribution Tracking
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Route events from Segment's customer data platform to Amplitude.
  name: Segment
- description: Export raw event data directly into Snowflake for warehouse-native analytics.
  name: Snowflake
- description: Sync Amplitude data with Google BigQuery for custom SQL analysis.
  name: BigQuery
- description: Enrich Salesforce CRM records with Amplitude behavioral cohort data.
  name: Salesforce
- description: Sync audience cohorts from Amplitude to HubSpot for marketing automation.
  name: HubSpot
- description: Power personalized messaging campaigns using Amplitude behavioral cohorts.
  name: Braze
- description: Automate user provisioning in Amplitude via Okta using the SCIM API.
  name: Okta
- description: Receive automated alerts and chart embeds from Amplitude in Slack channels.
  name: Slack
jsonld:
- class_count: 3
  name: Amplitude Amplitude Cohort Context
  property_count: 7
  slug: amplitude-amplitude-cohort-context
- class_count: 1
  name: Amplitude Amplitude Event Context
  property_count: 36
  slug: amplitude-amplitude-event-context
- class_count: 3
  name: Amplitude Amplitude Experiment Context
  property_count: 15
  slug: amplitude-amplitude-experiment-context
- class_count: 3
  name: Amplitude Attribution Api Context
  property_count: 25
  slug: amplitude-attribution-api-context
- class_count: 8
  name: Amplitude Behavioral Cohorts Api Context
  property_count: 12
  slug: amplitude-behavioral-cohorts-api-context
- class_count: 6
  name: Amplitude Chart Annotations Api Context
  property_count: 8
  slug: amplitude-chart-annotations-api-context
- class_count: 0
  name: Amplitude Context
  property_count: 7
  slug: amplitude-context
- class_count: 7
  name: Amplitude Dashboard Rest Api Context
  property_count: 10
  slug: amplitude-dashboard-rest-api-context
- class_count: 6
  name: Amplitude Dsar Api Context
  property_count: 8
  slug: amplitude-dsar-api-context
- class_count: 4
  name: Amplitude Experiment Evaluation Api Context
  property_count: 19
  slug: amplitude-experiment-evaluation-api-context
- class_count: 16
  name: Amplitude Experiment Management Api Context
  property_count: 32
  slug: amplitude-experiment-management-api-context
- class_count: 4
  name: Amplitude Http V2 Api Context
  property_count: 44
  slug: amplitude-http-v2-api-context
- class_count: 5
  name: Amplitude Identify Api Context
  property_count: 15
  slug: amplitude-identify-api-context
- class_count: 8
  name: Amplitude Scim Api Context
  property_count: 25
  slug: amplitude-scim-api-context
- class_count: 11
  name: Amplitude Taxonomy Api Context
  property_count: 9
  slug: amplitude-taxonomy-api-context
- class_count: 4
  name: Amplitude User Mapping Api Context
  property_count: 6
  slug: amplitude-user-mapping-api-context
- class_count: 3
  name: Amplitude User Profile Api Context
  property_count: 12
  slug: amplitude-user-profile-api-context
layout: provider
modified: '2026-04-19'
name: Amplitude
rules:
- name: Amplitude API Rules
  rule_count: 23
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 9
  slug: amplitude-spectral-rules
skills: []
slug: amplitude
solutions: []
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/apis.yml
use_cases:
- description: Understand how users interact with your product to prioritize features and reduce churn.
  name: Product Analytics
- description: Run controlled A/B tests to measure the causal impact of product changes.
  name: Growth Experimentation
- description: Track campaign performance and ROI by connecting acquisition events to user behavior.
  name: Marketing Attribution
- description: Export raw event data to Snowflake, BigQuery, or Redshift for custom analysis.
  name: Data Warehouse Integration
- description: Sync behavioral cohorts to ad platforms and CRMs for targeted marketing.
  name: Audience Syndication
- description: Automate GDPR and CCPA data deletion workflows for privacy compliance.
  name: Compliance Automation
- description: Automate user provisioning and deprovisioning via SCIM integration with IdPs.
  name: Enterprise Identity Management
---
