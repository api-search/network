---
api_count: 1
apis:
- description: The AWS IoT Device Defender API provides programmatic access to security profiles, audit configurations, anomaly detection, and violation management for IoT fleet security.
  name: AWS IoT Device Defender API
  slug: aws-iot-defender-api
capabilities:
- description: Unified capability for Security Engineer, IoT Developer to manage security service for iot fleet auditing and anomaly detection operations.
  name: Amazon IoT Device Defender - Iot Security Monitoring
  slug: iot-security-monitoring
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/iot-device-defender/
- title: ''
  type: Website
  url: https://aws.amazon.com/iot-device-defender/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html
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
  url: https://aws.amazon.com/blogs/iot/tag/aws-iot-device-defender/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/iot/home#/devicedefender
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
  url: rules/amazon-iot-device-defender-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/iot-device-defender.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/iot-security-monitoring.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-iot-device-defender-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-iot-device-defender-context.jsonld
created: '2026-03-16'
description: AWS IoT Device Defender is a security service that lets you continuously audit your IoT configurations to detect deviations from security best practices. It also lets you detect abnormal device behavior through ML-based anomaly detection and take actions to mitigate security risks.
features:
- description: Continuously audit IoT configurations against security best practices.
  name: Configuration Audit
- description: Detect abnormal device behavior using machine learning models.
  name: ML Anomaly Detection
- description: Define expected behaviors for device metrics and receive alerts on violations.
  name: Security Profiles
- description: Automatically take actions to mitigate security violations.
  name: Automated Mitigation
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Monitors all IoT Core device connections and policies.
  name: AWS IoT Core
- description: Sends security metrics and alerts to CloudWatch.
  name: Amazon CloudWatch
- description: Publishes IoT security findings to Security Hub.
  name: AWS Security Hub
jsonld:
- class_count: 102
  name: Amazon Iot Device Defender Context
  property_count: 266
  slug: amazon-iot-device-defender-context
layout: provider
modified: '2026-04-19'
name: Amazon IoT Device Defender
rules:
- name: Amazon IoT Device Defender API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: amazon-iot-device-defender-spectral-rules
skills: []
slug: amazon-iot-device-defender
solutions: []
tags:
- AWS
- Compliance
- IoT
- Security
- Vulnerability Management
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-device-defender/refs/heads/main/apis.yml
use_cases:
- description: Ensure IoT deployments meet security compliance requirements.
  name: IoT Compliance
- description: Detect compromised devices exhibiting abnormal communication patterns.
  name: Threat Detection
- description: Audit IoT policies and certificates against security best practices.
  name: Security Auditing
---
