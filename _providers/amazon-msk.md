---
api_count: 1
apis:
- description: Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that enables you to build and run applications that use Apache Kafka to process streaming data, with the infrastructur
  name: Amazon MSK API
  slug: msk-api
capabilities:
- description: Workflow capability for Amazon MSK media processing operations for broadcast engineers and media developers.
  name: Amazon MSK Workflow
  slug: amazon-msk-media-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/msk/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/msk/
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
  url: https://console.aws.amazon.com/msk/
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
  url: rules/amazon-msk-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-msk-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-msk-media-workflow.yaml
created: '2026-03-16'
description: Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that enables you to build and run applications that use Apache Kafka to process streaming data, with the infrastructure management handled by AWS.
features:
- description: Automatically provisions, configures, and maintains Apache Kafka clusters without operational overhead.
  name: Fully Managed Kafka
- description: Multi-AZ deployments with automatic replication and failover for data durability.
  name: High Durability
- description: Serverless cluster mode that automatically scales capacity to match streaming demand.
  name: MSK Serverless
- description: Fully managed Kafka Connect to stream data to and from databases and other services.
  name: MSK Connect
- description: Offload older data to low-cost Amazon S3 storage while keeping recent data on brokers.
  name: Tiered Storage
- description: Manage and enforce schemas for Kafka topics with AWS Glue Schema Registry integration.
  name: Schema Registry
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Process MSK streams with Kinesis Data Analytics for Apache Flink.
  name: Amazon Kinesis Data Analytics
- description: Trigger Lambda functions from MSK topics for serverless stream processing.
  name: AWS Lambda
- description: Use MSK Connect to sink data from Kafka topics to S3 buckets.
  name: Amazon S3
- description: Monitor cluster and broker metrics with CloudWatch dashboards and alarms.
  name: Amazon CloudWatch
- description: Authenticate Kafka clients using IAM roles for MSK cluster access control.
  name: AWS IAM
- description: Enforce data schemas for Kafka producers and consumers.
  name: AWS Glue Schema Registry
jsonld:
- class_count: 139
  name: Amazon Msk Msk Api Context
  property_count: 129
  slug: amazon-msk-msk-api-context
layout: provider
modified: '2026-04-19'
name: Amazon MSK
rules:
- name: Amazon MSK API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 7
  slug: amazon-msk-spectral-rules
skills: []
slug: amazon-msk
solutions: []
tags:
- AWS
- Broadcasting
- Media Processing
- Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-msk/refs/heads/main/apis.yml
use_cases:
- description: Build real-time data pipelines for clickstream analytics, log aggregation, and metrics.
  name: Real-Time Data Streaming
- description: Implement event sourcing patterns with durable, ordered Kafka topics.
  name: Event Sourcing
- description: Process streaming data with Apache Flink, Spark Streaming, or custom consumers.
  name: Stream Processing
- description: Stream database changes to downstream systems using Debezium and MSK Connect.
  name: Database Change Data Capture
---
