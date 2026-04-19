---
api_count: 1
apis:
- description: API for creating and managing event buses, rules, targets, and connections for routing events across applications, microservices, and SaaS integrations.
  name: Amazon EventBridge API
  slug: ''
asyncapis:
- description: Amazon EventBridge delivers events from event sources to targets based on rules you define. This AsyncAPI specification documents the event channels and message schemas for events delivered by EventBr
  name: Amazon EventBridge Event Delivery
  slug: amazon-eventbridge-asyncapi
capabilities:
- description: Unified capability for managing Amazon EventBridge resources. Combines Amazon EventBridge APIs for Integration Engineer workflows in Event-Driven Architecture.
  name: Amazon EventBridge Management
  slug: amazon-eventbridge-capability
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
  url: https://console.aws.amazon.com/events/
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
  url: rules/amazon-eventbridge-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-eventbridge-capability.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/api.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-eventbridge-vocabulary.yaml
created: '2024-01-15'
description: Amazon EventBridge is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your own applications, SaaS applications, and AWS services and routes that data to targets such as Lambda, SNS, SQS, and more.
features:
- description: Central event bus for routing events between AWS services and applications
  name: Event Bus
- description: Create rules to filter and route events to specific targets
  name: Event Rules
- description: Discover, create, and manage event schemas with code binding generation
  name: Schema Registry
- description: Receive events from SaaS partners like Zendesk, Datadog, and PagerDuty
  name: SaaS Integrations
- description: Send events to external HTTP endpoints via API Destinations
  name: API Destinations
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Invoke Lambda functions in response to events
  name: AWS Lambda
- description: Fan out events to multiple subscribers via SNS topics
  name: Amazon SNS
- description: Queue events for reliable processing with SQS
  name: Amazon SQS
- description: Start state machine executions in response to events
  name: AWS Step Functions
- description: Receive Zendesk support ticket and activity events
  name: Zendesk
jsonld:
- class_count: 5
  name: Amazon Eventbridge Context
  property_count: 9
  slug: amazon-eventbridge-context
layout: provider
modified: '2026-04-19'
name: Amazon EventBridge
rules:
- name: Amazon EventBridge API Rules
  rule_count: 20
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 9
  slug: amazon-eventbridge-spectral-rules
skills: []
slug: amazon-eventbridge
solutions: []
tags:
- Amazon Web Services
- AWS
- Event Bus
- Event-Driven
- Events
- Integration
- Serverless
url: https://aws.amazon.com/eventbridge/
use_cases:
- description: Decouple microservices by routing events through a central event bus
  name: Microservices Decoupling
- description: React to CloudWatch alarms and AWS service events in real time
  name: Application Monitoring
- description: Receive and process events from SaaS applications without polling
  name: SaaS Event Processing
- description: Route events across AWS accounts and regions for enterprise architectures
  name: Multi-Account Event Routing
---
