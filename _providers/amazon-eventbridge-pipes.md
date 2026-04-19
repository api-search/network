---
api_count: 1
apis:
- description: API for creating and managing pipes that connect event sources to targets with optional filtering, enrichment, and transformation capabilities.
  name: Amazon EventBridge Pipes API
  slug: ''
capabilities:
- description: Unified capability for managing Amazon EventBridge Pipes resources. Combines Amazon EventBridge Pipes APIs for Integration Engineer workflows in Event Processing.
  name: Amazon EventBridge Pipes Management
  slug: amazon-eventbridge-pipes-capability
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
  url: rules/amazon-eventbridge-pipes-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-eventbridge-pipes-capability.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/api.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-eventbridge-pipes-vocabulary.yaml
created: '2024-01-15'
description: Amazon EventBridge Pipes helps you create point-to-point integrations between event producers and consumers with optional transform, filter, and enrich steps. It reduces the amount of integration code you need to write and maintain when building event-driven applications.
features:
- description: Connect event sources directly to targets with minimal code
  name: Point-to-Point Integration
- description: Filter events before processing to reduce costs and noise
  name: Event Filtering
- description: Enrich events with data from Lambda, Step Functions, or API destinations
  name: Event Enrichment
- description: Transform event payloads using input transformers
  name: Event Transformation
- description: Process events in batches for improved throughput
  name: Batching Support
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Use DynamoDB Streams as an event source
  name: Amazon DynamoDB Streams
- description: Connect SQS queues as event sources or targets
  name: Amazon SQS
- description: Process Kinesis data stream events
  name: Amazon Kinesis
- description: Use Lambda as enrichment or target for pipe events
  name: AWS Lambda
- description: Connect Apache Kafka and Amazon MSK as event sources
  name: Apache Kafka
jsonld:
- class_count: 83
  name: Amazon Eventbridge Pipes Context
  property_count: 130
  slug: amazon-eventbridge-pipes-context
layout: provider
modified: '2026-04-19'
name: Amazon EventBridge Pipes
rules:
- name: Amazon EventBridge Pipes API Rules
  rule_count: 20
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 9
  slug: amazon-eventbridge-pipes-spectral-rules
skills: []
slug: amazon-eventbridge-pipes
solutions: []
tags:
- Amazon Web Services
- AWS
- Event-Driven
- Integration
- Messaging
- Serverless
url: https://aws.amazon.com/eventbridge/pipes/
use_cases:
- description: Stream DynamoDB or Aurora changes to downstream systems
  name: Database Change Data Capture
- description: Connect SQS queues to Lambda or Step Functions for message processing
  name: Queue Processing
- description: Process Kinesis or Kafka streams with filtering and enrichment
  name: Stream Analytics
- description: Connect SaaS event sources to AWS targets without custom code
  name: SaaS Integration
---
