---
api_count: 1
apis:
- description: API for creating, updating, and managing scheduled tasks using cron expressions, rate expressions, and one-time schedules at scale.
  name: Amazon EventBridge Scheduler API
  slug: ''
capabilities:
- description: Unified capability for managing Amazon EventBridge Scheduler resources. Combines Amazon EventBridge Scheduler APIs for DevOps Engineer workflows in Task Scheduling.
  name: Amazon EventBridge Scheduler Management
  slug: amazon-eventbridge-scheduler-capability
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/eventbridge/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/eventbridge/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/scheduler/
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
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/eventbridge/faqs/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/eventbridge
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-eventbridge-scheduler-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-eventbridge-scheduler-capability.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/api.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-eventbridge-scheduler-vocabulary.yaml
created: '2024-01-15'
description: Amazon EventBridge Scheduler is a fully managed, serverless scheduler that enables you to create, run, and manage tasks from one central, managed service. With EventBridge Scheduler, you can create millions of schedules using cron and rate expressions.
features:
- description: Schedule tasks using flexible cron expressions or simple rate expressions
  name: Cron and Rate Scheduling
- description: Create one-time schedules for future tasks with precise timing
  name: One-Time Schedules
- description: Organize schedules into groups for bulk management and operations
  name: Schedule Groups
- description: Allow schedules to run within flexible time windows for load distribution
  name: Flexible Time Windows
- description: Specify schedules in any timezone for global deployments
  name: Timezone Support
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Invoke Lambda functions on a schedule
  name: AWS Lambda
- description: Send messages to SQS queues at scheduled intervals
  name: Amazon SQS
- description: Start Step Functions state machine executions on a schedule
  name: AWS Step Functions
- description: Run ECS tasks on a scheduled basis
  name: Amazon ECS
- description: Send events to EventBridge event buses on a schedule
  name: Amazon EventBridge
jsonld:
- class_count: 44
  name: Amazon Eventbridge Scheduler Context
  property_count: 54
  slug: amazon-eventbridge-scheduler-context
layout: provider
modified: '2026-04-19'
name: Amazon EventBridge Scheduler
rules:
- name: Amazon EventBridge Scheduler API Rules
  rule_count: 20
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 9
  slug: amazon-eventbridge-scheduler-spectral-rules
skills: []
slug: amazon-eventbridge-scheduler
solutions: []
tags:
- Amazon Web Services
- AWS
- Cron
- Event-Driven
- Scheduling
- Serverless
url: https://aws.amazon.com/eventbridge/scheduler/
use_cases:
- description: Schedule periodic data processing and ETL batch jobs
  name: Batch Job Scheduling
- description: Automatically generate and deliver reports on a schedule
  name: Report Generation
- description: Schedule automatic cleanup of temporary resources and old data
  name: Resource Cleanup
- description: Send scheduled notifications and reminders to users
  name: Reminder Notifications
---
