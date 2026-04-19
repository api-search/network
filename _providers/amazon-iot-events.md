---
api_count: 1
apis:
- description: The AWS IoT Events API provides access to detector models, inputs, alarms, and event detection configurations for building IoT event-driven workflows.
  name: AWS IoT Events API
  slug: aws-iot-events-api
capabilities:
- description: Unified capability for IoT Developer, Solutions Architect to manage detect and respond to events from iot sensors and applications operations.
  name: Amazon IoT Events - Iot Event Management
  slug: iot-event-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/iot-events/
- title: ''
  type: Website
  url: https://aws.amazon.com/iot-events/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/iotevents/
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
  url: https://aws.amazon.com/blogs/iot/tag/aws-iot-events/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/iotevents/
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
  url: rules/amazon-iot-events-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/iot-events.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/iot-event-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-iot-events-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-iot-events-context.jsonld
created: '2026-03-16'
description: AWS IoT Events is a managed service that makes it easy to detect and respond to events from IoT sensors and applications. You can use it to build complex event detection logic, create state machines for IoT workflows, and trigger alerts or actions when specific conditions are met.
features:
- description: Create state machines to detect complex event patterns across IoT data streams.
  name: Detector Models
- description: Built-in alarm management for monitoring IoT sensor thresholds.
  name: Alarm Management
- description: Define structured event inputs and route IoT data to detector models.
  name: Event Inputs
- description: Trigger actions to SNS, SQS, Lambda, and other services when events are detected.
  name: Multi-Trigger Actions
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Receives message data from IoT Core for event detection.
  name: AWS IoT Core
- description: Sends alerts and notifications when events are detected.
  name: Amazon SNS
- description: Triggers Lambda functions to execute response workflows.
  name: AWS Lambda
jsonld:
- class_count: 101
  name: Amazon Iot Events Context
  property_count: 141
  slug: amazon-iot-events-context
layout: provider
modified: '2026-04-19'
name: Amazon IoT Events
rules:
- name: Amazon IoT Events API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: amazon-iot-events-spectral-rules
skills: []
slug: amazon-iot-events
solutions: []
tags:
- AWS
- Event Detection
- IoT
- State Machine
- Automation
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-events/refs/heads/main/apis.yml
use_cases:
- description: Detect equipment failures and trigger maintenance workflows automatically.
  name: Industrial Alarm Management
- description: Detect patterns across multiple sensor streams over time.
  name: Complex Event Processing
- description: Alert operations teams when device metrics indicate impending failure.
  name: Predictive Maintenance
---
