---
api_count: 1
apis:
- description: RESTful API for Amazon Simple Notification Service providing topic management, subscription lifecycle, message publishing, platform application management for mobile push, and SMS messaging operations
  name: Amazon SNS API
  slug: ''
asyncapis:
- description: 'Amazon Simple Notification Service (SNS) delivers notifications to subscribed endpoints when messages are published to topics. This AsyncAPI specification describes the notification messages that SNS '
  name: Amazon SNS Notifications
  slug: amazon-sns-notifications-asyncapi
capabilities:
- description: Pub/sub messaging workflow combining topic management, subscription lifecycle, message publishing, mobile push, and SMS operations. Used by developers and platform engineers for event-driven architect
  name: Amazon SNS Pub/Sub Messaging
  slug: pub-sub-messaging
common:
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/messaging-and-targeting/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Console
  url: https://console.aws.amazon.com/sns/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/services-in-scope/
- title: ''
  type: Support
  url: https://console.aws.amazon.com/support/home
- title: ''
  type: KnowledgeCenter
  url: https://aws.amazon.com/premiumsupport/knowledge-center/#Amazon_Simple_Notification_Service
- title: ''
  type: Partners
  url: https://aws.amazon.com/sns/partners/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: GitHubRepository
  url: https://github.com/awsdocs/amazon-sns-developer-guide
created: '2024-01-01'
description: Amazon Simple Notification Service (SNS) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication. It enables pub/sub, SMS, email, and mobile push notifications.
features:
- description: Fan-out messages to multiple subscribers through topics supporting HTTP/S, email, SQS, Lambda, and SMS protocols.
  name: Pub/Sub Messaging
- description: Strict message ordering and exactly-once delivery for use cases requiring sequence-preserving fan-out.
  name: FIFO Topics
- description: Subscription filter policies enabling subscribers to receive only the messages relevant to them.
  name: Message Filtering
- description: Cross-platform mobile push via APNs, FCM, and other push services through platform applications.
  name: Mobile Push Notifications
- description: Direct SMS text messaging to phone numbers worldwide with support for transactional and promotional messages.
  name: SMS Messaging
- description: Capture undeliverable messages for analysis and reprocessing to ensure no messages are lost.
  name: Dead-Letter Queues
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Fan out SNS messages to SQS queues for reliable asynchronous processing across multiple consumers.
  name: Amazon SQS
- description: Invoke Lambda functions directly from SNS notifications for serverless event processing.
  name: AWS Lambda
- description: Route SNS events through EventBridge for complex event-driven routing and filtering.
  name: Amazon EventBridge
- description: Define and manage SNS topics and subscriptions as infrastructure-as-code resources.
  name: AWS CloudFormation
- description: Deliver SNS messages to data lakes and analytics services through Kinesis Data Firehose.
  name: Amazon Kinesis Data Firehose
jsonld:
- class_count: 0
  name: Amazon Sns Context
  property_count: 0
  slug: amazon-sns-context
layout: provider
modified: '2026-04-18'
name: Amazon SNS
rules:
- name: Amazon SNS API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: amazon-sns-spectral-rules
skills: []
slug: amazon-sns
solutions: []
tags:
- AWS
- Email
- Messaging
- Notifications
- Pub/Sub
- Push Notifications
- SMS
url: https://raw.githubusercontent.com/api-evangelist/amazon-sns/refs/heads/main/apis.yml
use_cases:
- description: Broadcast application events to multiple microservices simultaneously using pub/sub topic subscriptions.
  name: Application Event Fan-Out
- description: Send targeted push notifications to mobile applications across iOS and Android platforms.
  name: Mobile Push Campaigns
- description: Deliver operational alerts via SMS, email, and HTTP endpoints for infrastructure monitoring.
  name: Alert and Monitoring Systems
- description: Send transactional notifications for order confirmations, shipping updates, and account activity.
  name: Order Confirmation Notifications
- description: Share events across AWS accounts using SNS topic policies for multi-account architectures.
  name: Cross-Account Event Distribution
---
