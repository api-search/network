---
api_count: 3
apis:
- description: RESTful API for interacting with DynamoDB tables and items.
  name: Amazon DynamoDB API
  slug: ''
- description: API for capturing and processing change data from DynamoDB tables in near real-time, providing time-ordered sequences of item-level modifications.
  name: Amazon DynamoDB Streams API
  slug: ''
- description: API for managing DynamoDB Accelerator (DAX) clusters, an in-memory caching service that delivers microsecond response times for DynamoDB read workloads.
  name: Amazon DynamoDB Accelerator (DAX) API
  slug: ''
asyncapis:
- description: Amazon DynamoDB Streams captures a time-ordered sequence of item-level modifications in any DynamoDB table and stores this information in a log for up to 24 hours. Applications can access this log and
  name: Amazon DynamoDB Streams
  slug: dynamodb-streams-asyncapi
capabilities:
- description: Unified workflow for managing DynamoDB tables, items, queries, batch operations, transactions, and backups. Used by backend developers and data engineers.
  name: Amazon DynamoDB Database Management
  slug: database-management
common:
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/database/category/database/amazon-dynamodb/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Resources
  url: https://aws.amazon.com/dynamodb/resources/
- title: ''
  type: SpectralRules
  url: rules/dynamodb-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/dynamodb-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/database-management.yaml
created: '2024'
description: A fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.
features:
- description: Consistent low-latency reads and writes at any scale with SSD-backed storage.
  name: Single-Digit Millisecond Performance
- description: Multi-region, multi-active replication for globally distributed applications.
  name: Global Tables
- description: Automatically scale throughput capacity based on workload without capacity planning.
  name: On-Demand Capacity
- description: Capture item-level changes for real-time processing, replication, and event-driven architectures.
  name: DynamoDB Streams
- description: Continuous backups with restore to any second within the last 35 days.
  name: Point-in-Time Recovery
- description: ACID transactions across multiple items and tables for complex business logic.
  name: Transactions
- description: Execute SQL-compatible queries against DynamoDB tables using PartiQL language.
  name: PartiQL Support
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Trigger Lambda functions from DynamoDB Streams for event-driven processing.
  name: AWS Lambda
- description: Export table data to S3 or import from S3 for analytics and data migration.
  name: Amazon S3
- description: Stream DynamoDB changes to Kinesis for real-time analytics pipelines.
  name: Amazon Kinesis
- description: Provision and manage DynamoDB tables as infrastructure as code.
  name: AWS CloudFormation
- description: Monitor table metrics, set alarms, and track performance with CloudWatch integration.
  name: Amazon CloudWatch
jsonld:
- class_count: 0
  name: Dynamodb Context
  property_count: 0
  slug: dynamodb-context
layout: provider
modified: '2026-04-18'
name: Amazon DynamoDB
rules:
- name: Amazon DynamoDB API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: dynamodb-spectral-rules
skills: []
slug: dynamodb
solutions: []
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
url: https://aws.amazon.com/dynamodb/
use_cases:
- description: Use as the data layer for serverless architectures with Lambda and API Gateway.
  name: Serverless Application Backend
- description: Store and query player data, session state, and leaderboards with consistent low latency.
  name: Gaming Leaderboards
- description: Ingest and query high-volume time-series data from IoT devices at scale.
  name: IoT Data Storage
- description: Store shopping cart and session data with high availability and automatic scaling.
  name: E-Commerce Shopping Cart
---
