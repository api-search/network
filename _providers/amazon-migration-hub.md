---
api_count: 1
apis:
- description: AWS Migration Hub provides a single location to track the progress of application migrations across multiple AWS and partner solutions, giving visibility into migration progress and enabling the use o
  name: Amazon Migration Hub API
  slug: migration-hub-api
capabilities:
- description: Workflow capability for Amazon Migration Hub media processing operations for broadcast engineers and media developers.
  name: Amazon Migration Hub Workflow
  slug: amazon-migration-hub-media-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/migration-hub/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/migration-hub/
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
  url: https://console.aws.amazon.com/migration-hub/
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
  url: rules/amazon-migration-hub-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-migration-hub-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-migration-hub-media-workflow.yaml
created: '2026-03-16'
description: AWS Migration Hub provides a single location to track the progress of application migrations across multiple AWS and partner solutions, giving visibility into migration progress and enabling the use of other AWS migration tools.
features:
- description: Track migration progress across multiple applications and migration tools from a single console.
  name: Centralized Migration Tracking
- description: Integrate with AWS Database Migration Service, Server Migration Service, and partner tools.
  name: Multi-Tool Integration
- description: Discover on-premises servers and dependencies to plan migrations effectively.
  name: Application Discovery
- description: Receive real-time updates on task progress and resource migration status.
  name: Migration Status Notifications
- description: Associate discovered resources with migration tasks for tracking.
  name: Resource Association
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Track SMS migration job progress in Migration Hub.
  name: AWS Server Migration Service
- description: Monitor DMS database migration tasks from Migration Hub.
  name: AWS Database Migration Service
- description: Import discovery data to identify and plan server migrations.
  name: AWS Application Discovery Service
- description: Track CloudFormation stack deployments as migration tasks.
  name: AWS CloudFormation
jsonld:
- class_count: 80
  name: Amazon Migration Hub Migration Hub Api Context
  property_count: 30
  slug: amazon-migration-hub-migration-hub-api-context
layout: provider
modified: '2026-04-19'
name: Amazon Migration Hub
rules:
- name: Amazon Migration Hub API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 7
  slug: amazon-migration-hub-spectral-rules
skills: []
slug: amazon-migration-hub
solutions: []
tags:
- AWS
- Broadcasting
- Media Processing
- Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-migration-hub/refs/heads/main/apis.yml
use_cases:
- description: Manage complex migrations of hundreds or thousands of servers to AWS.
  name: Large-Scale Cloud Migration
- description: Track the status of all applications in a migration portfolio.
  name: Migration Portfolio Management
- description: Coordinate migrations using multiple AWS and partner migration tools simultaneously.
  name: Multi-Tool Orchestration
- description: Generate progress reports and status updates for stakeholders.
  name: Migration Reporting
---
