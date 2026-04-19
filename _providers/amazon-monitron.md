---
api_count: 1
apis:
- description: Amazon Monitron is an end-to-end system that uses machine learning to detect abnormal behavior in industrial machinery. It includes sensors, a gateway, and the Monitron mobile app to enable predictive
  name: Amazon Monitron API
  slug: monitron-api
capabilities:
- description: Workflow capability for Amazon Monitron media processing operations for broadcast engineers and media developers.
  name: Amazon Monitron Workflow
  slug: amazon-monitron-media-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/monitron/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/monitron/
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
  url: https://aws.amazon.com/blogs/media/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/monitron/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-monitron-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-monitron-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-monitron-media-workflow.yaml
created: '2026-03-16'
description: Amazon Monitron is an end-to-end system that uses machine learning to detect abnormal behavior in industrial machinery. It includes sensors, a gateway, and the Monitron mobile app to enable predictive maintenance and reduce unplanned downtime.
features:
- description: Machine learning models trained on industrial machinery data to detect abnormal behavior automatically.
  name: ML-Based Anomaly Detection
- description: Organize machine monitoring deployments into projects with access control.
  name: Project Management
- description: Integrated hardware sensors, gateway, cloud processing, and mobile app in one solution.
  name: End-to-End System
- description: Identify potential equipment failures before they occur to schedule proactive maintenance.
  name: Predictive Maintenance
- description: Manage project administrators and user associations with fine-grained permissions.
  name: User Access Control
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Monitron gateway connects to the cloud via AWS IoT Core.
  name: AWS IoT Core
- description: Stream Monitron measurement data to Kinesis for real-time analytics.
  name: Amazon Kinesis
- description: Export historical sensor data to S3 for long-term analysis.
  name: Amazon S3
- description: Control API access and project permissions with IAM policies.
  name: AWS IAM
jsonld:
- class_count: 6
  name: Amazon Monitron Monitron Api Context
  property_count: 10
  slug: amazon-monitron-monitron-api-context
layout: provider
modified: '2026-04-19'
name: Amazon Monitron
rules:
- name: Amazon Monitron API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 7
  slug: amazon-monitron-spectral-rules
skills: []
slug: amazon-monitron
solutions: []
tags:
- AWS
- Broadcasting
- Media Processing
- Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-monitron/refs/heads/main/apis.yml
use_cases:
- description: Monitor motors, pumps, fans, and compressors for early signs of failure.
  name: Industrial Equipment Monitoring
- description: Build data-driven maintenance schedules based on actual equipment health.
  name: Predictive Maintenance Programs
- description: Reduce unplanned production downtime by catching issues before equipment fails.
  name: Downtime Reduction
- description: Deploy sensors across entire manufacturing facilities for comprehensive asset health.
  name: Plant-Wide Monitoring
---
