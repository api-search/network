---
api_count: 1
apis:
- description: The AWS IoT FleetWise API provides access to vehicle data modeling, fleet management, signal catalogs, campaigns, and data collection for connected vehicle platforms.
  name: AWS IoT FleetWise API
  slug: aws-iot-fleetwise-api
capabilities:
- description: Unified capability for Automotive Engineer, IoT Developer to manage collect, transform, and transfer vehicle data to the cloud operations.
  name: Amazon IoT FleetWise - Vehicle Fleet Management
  slug: vehicle-fleet-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/iot-fleetwise/
- title: ''
  type: Website
  url: https://aws.amazon.com/iot-fleetwise/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/iot-fleetwise/
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
  url: https://aws.amazon.com/blogs/iot/tag/aws-iot-fleetwise/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/iotfleetwise/
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
  url: rules/amazon-iot-fleetwise-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/iot-fleetwise.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/vehicle-fleet-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-iot-fleetwise-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-iot-fleetwise-context.jsonld
created: '2026-03-16'
description: AWS IoT FleetWise is a managed service that makes it easy for automotive manufacturers to collect, transform, and transfer vehicle data to the cloud in near-real time. It provides tools for vehicle data modeling, intelligent data collection, and cloud-based analytics.
features:
- description: Model vehicle signals using VSS and OEM-specific data dictionaries.
  name: Vehicle Signal Catalog
- description: Collect vehicle data conditionally based on events, time windows, or triggers.
  name: Intelligent Data Collection
- description: Deploy data collection campaigns across thousands of vehicles simultaneously.
  name: Fleet-Wide Campaigns
- description: Analyze collected vehicle data using Amazon Timestream and QuickSight.
  name: Cloud Analytics
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Stores vehicle time-series telemetry data for analysis.
  name: Amazon Timestream
- description: Stores raw vehicle data files for batch analytics.
  name: Amazon S3
- description: Provides connectivity for vehicle data transmission.
  name: AWS IoT Core
jsonld:
- class_count: 102
  name: Amazon Iot Fleetwise Context
  property_count: 147
  slug: amazon-iot-fleetwise-context
layout: provider
modified: '2026-04-19'
name: Amazon IoT FleetWise
rules:
- name: Amazon IoT FleetWise API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: amazon-iot-fleetwise-spectral-rules
skills: []
slug: amazon-iot-fleetwise
solutions: []
tags:
- Automotive
- AWS
- Connected Vehicles
- IoT
- Telematics
- Vehicle Data
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-fleetwise/refs/heads/main/apis.yml
use_cases:
- description: Collect and analyze vehicle diagnostic data from CAN bus.
  name: OBD Data Collection
- description: Analyze driving patterns for safety scoring and insurance.
  name: Driver Behavior Analysis
- description: Monitor vehicle health and predict maintenance needs.
  name: Predictive Maintenance
---
