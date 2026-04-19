---
api_count: 1
apis:
- description: The AWS IoT SiteWise API provides access to asset model management, asset data ingestion, time-series data queries, portals, and dashboards for industrial IoT monitoring.
  name: AWS IoT SiteWise API
  slug: aws-iot-sitewise-api
capabilities:
- description: Unified capability for OT Engineer, Data Analyst to manage collect, organize, and analyze industrial equipment data operations.
  name: Amazon IoT SiteWise - Industrial Asset Management
  slug: industrial-asset-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/iot-sitewise/
- title: ''
  type: Website
  url: https://aws.amazon.com/iot-sitewise/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/iot-sitewise/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/iot/tag/aws-iot-sitewise/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/iotsitewise/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-iot-sitewise-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/iot-sitewise.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/industrial-asset-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-iot-sitewise-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-iot-sitewise-context.jsonld
created: '2026-03-16'
description: AWS IoT SiteWise is a managed service that makes it easy to collect, store, organize, and monitor industrial data at scale. It provides tools to create asset models representing your industrial operations and analyze equipment performance across your facilities.
features:
- description: Create hierarchical asset models that represent your industrial equipment and processes.
  name: Asset Modeling
- description: Ingest and store industrial sensor data with automatic data quality classification.
  name: Time-Series Data Storage
- description: Build no-code dashboards for industrial operations visualization.
  name: SiteWise Monitor
- description: Process data locally at industrial sites using SiteWise Edge.
  name: Edge Processing
- description: Define metrics and transforms on asset data using built-in formula engine.
  name: Computed Properties
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Collects industrial data from OPC-UA, Modbus, and Ethernet/IP sources at the edge.
  name: AWS IoT Greengrass
- description: Streams asset property data for real-time analytics.
  name: Amazon Kinesis
- description: Visualizes SiteWise industrial data in business dashboards.
  name: Amazon QuickSight
jsonld:
- class_count: 102
  name: Amazon Iot Sitewise Context
  property_count: 196
  slug: amazon-iot-sitewise-context
layout: provider
modified: '2026-04-19'
name: Amazon IoT SiteWise
rules:
- name: Amazon IoT SiteWise API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: amazon-iot-sitewise-spectral-rules
skills: []
slug: amazon-iot-sitewise
solutions: []
tags:
- AWS
- Asset Management
- Industrial IoT
- IoT
- Time Series Data
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-sitewise/refs/heads/main/apis.yml
use_cases:
- description: Track OEE and equipment health across multiple manufacturing facilities.
  name: Equipment Performance Monitoring
- description: Monitor and optimize energy consumption across industrial sites.
  name: Energy Management
- description: Analyze production line data to identify bottlenecks and inefficiencies.
  name: Process Optimization
---
