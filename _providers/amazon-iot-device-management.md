---
api_count: 1
apis:
- description: The AWS IoT Device Management API provides access to thing groups, jobs, bulk registration, fleet indexing, and remote device management capabilities.
  name: AWS IoT Device Management API
  slug: aws-iot-management-api
capabilities:
- description: Unified capability for IoT Engineer, Operations Engineer to manage onboard, organize, and manage iot devices at scale operations.
  name: Amazon IoT Device Management - Iot Fleet Management
  slug: iot-fleet-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/iot-device-management/
- title: ''
  type: Website
  url: https://aws.amazon.com/iot-device-management/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html
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
  url: https://aws.amazon.com/blogs/iot/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/iot/
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
  url: rules/amazon-iot-device-management-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/iot-device-management.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/iot-fleet-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-iot-device-management-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-iot-device-management-context.jsonld
created: '2026-03-16'
description: AWS IoT Device Management makes it easy to securely onboard, organize, monitor, and remotely manage your IoT devices at scale. You can register your connected devices individually or in bulk, and easily manage permissions so your devices remain secure throughout their lifecycle.
features:
- description: Register thousands of devices simultaneously using bulk registration templates.
  name: Bulk Device Registration
- description: Search and query your entire device fleet based on attributes and shadow state.
  name: Fleet Indexing
- description: Deploy firmware updates, configuration changes, and software remotely at scale.
  name: Remote Jobs
- description: Organize devices into hierarchical groups for policies and bulk operations.
  name: Thing Groups
- description: Create secure bidirectional tunnels to devices behind firewalls for remote troubleshooting.
  name: Tunnel Secure
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: All device management operations integrate with IoT Core connectivity.
  name: AWS IoT Core
- description: Trigger automation workflows based on job status changes.
  name: AWS Lambda
- description: Store firmware and configuration files for remote deployment.
  name: Amazon S3
jsonld:
- class_count: 102
  name: Amazon Iot Device Management Context
  property_count: 266
  slug: amazon-iot-device-management-context
layout: provider
modified: '2026-04-19'
name: Amazon IoT Device Management
rules:
- name: Amazon IoT Device Management API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: amazon-iot-device-management-spectral-rules
skills: []
slug: amazon-iot-device-management
solutions: []
tags:
- AWS
- Device Management
- Fleet Management
- IoT
- OTA Updates
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-device-management/refs/heads/main/apis.yml
use_cases:
- description: Deploy firmware updates to thousands of devices simultaneously with rollback.
  name: OTA Firmware Updates
- description: Automate device provisioning and certificate management at manufacturing.
  name: Device Onboarding
- description: Monitor device connectivity, metadata, and shadow state across the entire fleet.
  name: Fleet Monitoring
---
