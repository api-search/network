---
api_count: 1
apis:
- description: The Amazon WorkSpaces API provides programmatic access to manage cloud-based virtual desktops. It enables developers to create, modify, and terminate WorkSpaces, manage workspace bundles and directori
  name: Amazon WorkSpaces API
  slug: amazon-workspaces-api
capabilities:
- description: Unified workflow for IT administrators and end user computing teams to provision, manage, and maintain Amazon WorkSpaces virtual desktops at scale, including workspace lifecycle, bundle management, di
  name: Amazon WorkSpaces Virtual Desktop Management
  slug: virtual-desktop-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/workspaces/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/workspaces/
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
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/workspaces/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-workspaces-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-workspaces-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/virtual-desktop-management.yaml
created: '2024-01-15'
description: Amazon WorkSpaces is a managed, secure Desktop-as-a-Service (DaaS) solution that enables you to provision cloud-based virtual desktops for your users. It eliminates the need to procure and deploy hardware or install complex software, providing persistent desktops accessible from various devices with built-in security and management capabilities. The API provides 65 operations for workspace lifecycle management, bundle and directory management, image management, and IP access control groups.
features:
- description: Cloud-based Windows or Linux desktops with persistent storage that users can access from any device or location.
  name: Persistent Virtual Desktops
- description: Configurable compute bundles ranging from Value to Graphics.g4dn to match workload requirements and cost targets.
  name: Desktop Bundle Catalog
- description: Integration with AWS Managed Microsoft AD and AD Connector for user authentication and policy management.
  name: Active Directory Integration
- description: Deploy and manage applications across WorkSpaces using application assignment and streaming capabilities.
  name: Application Management
- description: Restrict workspace access by IP address ranges to enforce network-based access controls.
  name: IP Access Control Groups
- description: AlwaysOn mode for power users and AutoStop mode for cost optimization of occasional-use desktops.
  name: Running Mode Flexibility
- description: Thin client, web browser, iOS, Android, Linux, macOS, and Windows client access for bring-your-own-device scenarios.
  name: BYOD Support
- description: Automated snapshots enable restoring workspaces to previous states for disaster recovery and user error correction.
  name: Workspace Snapshots and Restore
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Managed Microsoft AD and AD Connector for user authentication and group policy management.
  name: AWS Directory Service
- description: IAM-based access control for WorkSpaces API operations and resource-level permissions.
  name: AWS IAM
- description: User storage and workspace image storage backed by Amazon S3.
  name: Amazon S3
- description: Audit logging of all WorkSpaces API calls for compliance and security monitoring.
  name: AWS CloudTrail
- description: Metrics and monitoring for workspace performance, connectivity, and health status.
  name: Amazon CloudWatch
jsonld:
- class_count: 175
  name: Amazon Workspaces Context
  property_count: 173
  slug: amazon-workspaces-context
layout: provider
modified: '2026-04-19'
name: Amazon WorkSpaces
rules:
- name: Amazon WorkSpaces API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 6
  slug: amazon-workspaces-spectral-rules
skills: []
slug: amazon-workspaces
solutions: []
tags:
- AWS
- Desktop
- End User Computing
- Virtual Desktop
- Desktop as a Service
url: https://raw.githubusercontent.com/api-evangelist/amazon-workspaces/refs/heads/main/apis.yml
use_cases:
- description: Provide secure cloud desktops to remote and distributed employees without managing physical hardware.
  name: Remote Work Enablement
- description: Quickly provision and terminate secure desktops for contractors with time-limited access needs.
  name: Contractor and Temporary Worker Access
- description: Replace aging desktop hardware with cloud-based virtual desktops to reduce capital expenditure.
  name: Desktop Refresh and Modernization
- description: Enable personal device usage while keeping corporate data and applications in the secure cloud environment.
  name: BYOD Security
- description: Maintain data residency and security compliance in regulated industries like healthcare and finance.
  name: Regulated Industry Compliance
---
