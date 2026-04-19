---
api_count: 1
apis:
- description: The Amazon SWF API provides programmatic access to manage workflows, activity tasks, decision tasks, and workflow execution history. It enables developers to coordinate distributed application compone
  name: Amazon Simple Workflow Service API
  slug: amazon-swf-api
capabilities:
- description: ''
  name: Amazon Swf Workflow Management
  slug: amazon-swf-workflow-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/swf/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/swf/
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
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/rules/amazon-swf-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/vocabulary/amazon-swf-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/capabilities/amazon-swf-workflow-management.yaml
created: '2026-03-16'
description: Amazon Simple Workflow Service (Amazon SWF) helps developers build, run, and scale background jobs that have parallel or sequential steps. It is a fully managed state tracker and task coordinator in the cloud that manages intertask dependencies, scheduling, and concurrency for application workflows.
features:
- description: Manages inter-task dependencies, scheduling, and concurrency for distributed workflows.
  name: Task Coordination
- description: Durably maintains application execution state throughout workflow lifecycle.
  name: State Tracking
- description: Supports workflows that run for up to 1 year with activity timeouts and retries.
  name: Long-Running Workflows
- description: Separates orchestration logic (deciders) from execution logic (activity workers).
  name: Decider and Activity Workers
- description: Supports multiple versions of workflow and activity types for safe deployments.
  name: Workflow Versioning
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations: []
jsonld:
- class_count: 13
  name: Amazon Swf Context
  property_count: 0
  slug: amazon-swf-context
layout: provider
modified: '2026-04-19'
name: Amazon Simple Workflow Service
rules:
- name: Amazon Simple Workflow Service API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: amazon-swf-spectral-rules
skills: []
slug: amazon-swf
solutions: []
tags:
- Automation
- AWS
- Task Coordination
- Workflow
url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/apis.yml
use_cases:
- description: Coordinate multi-step media encoding, transcoding, and publishing workflows.
  name: Media Processing Pipelines
- description: Orchestrate e-commerce order fulfillment with parallel and sequential steps.
  name: Order Processing
- description: Manage ETL pipelines and data processing jobs across distributed systems.
  name: Data Analytics Workflows
- description: Coordinate workflows that require human review or approval steps.
  name: Human Task Orchestration
---
