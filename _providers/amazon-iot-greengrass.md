---
api_count: 1
apis:
- description: The AWS IoT Greengrass V2 API provides access to component management, core device management, and deployment orchestration for edge computing workloads.
  name: AWS IoT Greengrass API
  slug: aws-iot-greengrass-api
capabilities:
- description: Unified capability for IoT Developer, Edge Computing Engineer to manage extend aws compute and services to edge devices operations.
  name: Amazon IoT Greengrass - Edge Device Management
  slug: edge-device-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/greengrass/
- title: ''
  type: Website
  url: https://aws.amazon.com/greengrass/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/greengrass/v2/developerguide/
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
  url: https://aws.amazon.com/blogs/iot/tag/aws-iot-greengrass/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/greengrass/
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
  url: rules/amazon-iot-greengrass-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/iot-greengrass.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/edge-device-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-iot-greengrass-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-iot-greengrass-context.jsonld
created: '2026-03-16'
description: AWS IoT Greengrass extends AWS compute, messaging, data management, sync, and ML inference capabilities to edge devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage.
features:
- description: Run Lambda functions and containers on edge devices with local compute.
  name: Edge Computing
- description: Deploy reusable software components to edge devices from a component catalog.
  name: Component System
- description: Run machine learning inference locally with SageMaker model deployment.
  name: Local ML Inference
- description: Deploy and update software components to thousands of edge devices.
  name: Deployment Management
- description: Enable MQTT messaging between local IoT devices without cloud round-trips.
  name: Local Messaging
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Run Lambda functions on edge devices for local processing.
  name: AWS Lambda
- description: Deploy trained ML models to edge devices for local inference.
  name: Amazon SageMaker
- description: Syncs device state and routes messages between edge and cloud.
  name: AWS IoT Core
jsonld:
- class_count: 102
  name: Amazon Iot Greengrass Context
  property_count: 133
  slug: amazon-iot-greengrass-context
layout: provider
modified: '2026-04-19'
name: Amazon IoT Greengrass
rules:
- name: Amazon IoT Greengrass API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: amazon-iot-greengrass-spectral-rules
skills: []
slug: amazon-iot-greengrass
solutions: []
tags:
- AWS
- Edge Computing
- IoT
- Lambda
- Machine Learning
- Real-Time Processing
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-greengrass/refs/heads/main/apis.yml
use_cases:
- description: Process sensor data locally to reduce latency and bandwidth.
  name: Industrial Edge Processing
- description: Run computer vision and anomaly detection models at the edge.
  name: Edge ML Inference
- description: Continue processing and storing data when disconnected from the cloud.
  name: Offline Operation
---
