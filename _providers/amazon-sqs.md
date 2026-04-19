---
api_count: 1
apis:
- description: RESTful API for Amazon Simple Queue Service operations including queue management, message sending and receiving, batch operations, dead-letter queues, and access control.
  name: Amazon SQS API
  slug: ''
asyncapis:
- description: AsyncAPI specification for Amazon SQS event-driven messaging patterns. Amazon SQS provides reliable, highly-scalable hosted queues for storing messages as they travel between applications or microserv
  name: Amazon Simple Queue Service (SQS) Event Source Mapping
  slug: amazon-sqs-asyncapi
capabilities:
- description: Message queuing workflow for managing SQS queues, sending and receiving messages, batch operations, dead-letter queue management, and access control. Used by developers and DevOps engineers for micros
  name: Amazon SQS Message Queuing
  slug: message-queuing
common:
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/sqs/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://console.aws.amazon.com/support/home
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: CodeExamples
  url: https://docs.aws.amazon.com/code-library/latest/ug/sqs_code_examples.html
- title: ''
  type: GitHubRepository
  url: https://github.com/awsdocs/aws-doc-sdk-examples
created: '2024-01-01'
description: Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.
features:
- description: Maximum throughput, best-effort ordering, and at-least-once delivery for high-volume messaging workloads.
  name: Standard Queues
- description: Exactly-once processing and strict ordering guarantees for applications requiring message sequence preservation.
  name: FIFO Queues
- description: Automatic routing of failed messages to dead-letter queues for debugging and reprocessing.
  name: Dead-Letter Queues
- description: Bulk movement of messages between queues for reprocessing dead-letter queue contents.
  name: Message Move Tasks
- description: Automatic encryption of messages at rest using AWS KMS keys for data protection.
  name: Server-Side Encryption
- description: Reduced API costs and latency by allowing consumers to wait for messages to arrive before responding.
  name: Long Polling
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Automatically invoke Lambda functions when messages arrive in SQS queues for serverless processing.
  name: AWS Lambda
- description: Fan out SNS notifications to multiple SQS queues for parallel processing of published messages.
  name: Amazon SNS
- description: Route events from EventBridge to SQS queues for reliable event-driven architectures.
  name: Amazon EventBridge
- description: Provision and manage SQS queues as infrastructure-as-code using CloudFormation templates.
  name: AWS CloudFormation
- description: Create and manage SQS resources using HashiCorp Terraform infrastructure-as-code provider.
  name: Terraform
jsonld:
- class_count: 0
  name: Amazon Sqs Context
  property_count: 0
  slug: amazon-sqs-context
layout: provider
modified: '2026-04-18'
name: Amazon SQS
rules:
- name: Amazon SQS API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: amazon-sqs-spectral-rules
skills: []
slug: amazon-sqs
solutions: []
tags:
- AWS
- Cloud
- Distributed Systems
- Messaging
- Microservices
- Queue
url: https://raw.githubusercontent.com/api-evangelist/amazon-sqs/refs/heads/main/apis.yml
use_cases:
- description: Decouple microservices by using SQS queues as asynchronous communication buffers between services.
  name: Microservices Decoupling
- description: Trigger AWS Lambda functions from SQS messages for event-driven serverless architectures.
  name: Serverless Event Processing
- description: Use FIFO queues to ensure ordered processing of e-commerce orders and financial transactions.
  name: Order Processing Pipelines
- description: Distribute compute-intensive tasks across multiple workers using standard queues for parallel processing.
  name: Work Queue Distribution
- description: Queue batch processing jobs and manage their execution across distributed compute resources.
  name: Batch Job Orchestration
---
