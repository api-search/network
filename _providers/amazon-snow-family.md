---
api_count: 1
apis:
- description: The AWS Snow Device Management API provides programmatic access to manage Snow device jobs, tasks, device resources, and network configurations for edge computing and data transfer operations.
  name: AWS Snow Device Management API
  slug: aws-snow-device-management-api
capabilities: []
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/snowball/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/snowball/latest/developer-guide/api-reference.html
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
  url: https://aws.amazon.com/blogs/storage/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/snowball/
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
  url: rules/amazon-snow-family-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-snow-family-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/amazon-snow-family.yaml
created: '2026-03-16'
description: AWS Snow Family is a collection of physical devices and capacity points that help customers with data transfers in and out of AWS when network capacity is limited or unavailable. It includes Snowcone, Snowball, and Snowmobile devices for edge computing and offline data migration.
features:
- description: Transfer large datasets to AWS using physical devices.
  name: Petabyte-scale Data Transfer
- description: Run compute workloads at the edge with Snowball Edge and Snowcone.
  name: Edge Computing
- description: Use multiple Snow Family devices as a cluster for more storage and compute.
  name: Cluster Mode
- description: All data is automatically encrypted with 256-bit encryption.
  name: Encryption
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Transfer data directly to S3 buckets using Snow devices.
  name: Amazon S3
- description: Run IoT Greengrass on Snowball Edge for edge IoT workloads.
  name: AWS IoT Greengrass
- description: Run EC2 compute instances on Snowball Edge devices.
  name: Amazon EC2
- description: Use DataSync with Snow Family for accelerated data transfer.
  name: AWS DataSync
jsonld:
- class_count: 77
  name: Amazon Snow Family Context
  property_count: 122
  slug: amazon-snow-family-context
layout: provider
modified: '2026-04-19'
name: Amazon Snow Family
rules:
- name: Amazon Snow Family API Rules
  rule_count: 19
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 7
  slug: amazon-snow-family-spectral-rules
skills: []
slug: amazon-snow-family
solutions: []
tags:
- AWS
- Data Migration
- Edge Computing
- Offline Transfer
- Physical Appliance
url: https://raw.githubusercontent.com/api-evangelist/amazon-snow-family/refs/heads/main/apis.yml
use_cases:
- description: Migrate terabytes to petabytes of data to AWS.
  name: Large Data Migration
- description: Run AWS compute in environments with no internet connectivity.
  name: Disconnected Edge Computing
- description: Collect and transfer disaster recovery data to AWS.
  name: Disaster Recovery
---
