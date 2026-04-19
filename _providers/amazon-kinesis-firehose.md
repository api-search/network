---
api_count: 1
apis:
- description: The Amazon Kinesis Data Firehose API provides the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. The API allows you to create and manage delivery str
  name: Amazon Kinesis Data Firehose API
  slug: ''
capabilities:
- description: Unified workflow capability for Amazon Kinesis Data Firehose combining resource management and operations.
  name: Amazon Kinesis Data Firehose Workflow
  slug: amazon-kinesis-firehose-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Portal
  url: https://aws.amazon.com/kinesis/data-firehose/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/firehose/
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
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/firehose/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-kinesis-firehose-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-kinesis-firehose-workflow.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-kinesis-firehose-vocabulary.yaml
created: '2024-01-15'
description: Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. It can capture, transform, and deliver streaming data to Amazon S3, Amazon Redshift, Amazon OpenSearch Service, Splunk, and any custom HTTP endpoint. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration.
features:
- description: Fully managed service that automatically scales to match data throughput with no ongoing administration.
  name: Zero Administration
- description: Transform streaming data using AWS Lambda before delivering to destinations.
  name: Data Transformation
- description: Deliver data to Amazon S3, Redshift, OpenSearch Service, Splunk, Datadog, and custom HTTP endpoints.
  name: Multiple Destinations
- description: Automatically convert data formats such as JSON to Apache Parquet or Apache ORC before storing in S3.
  name: Format Conversion
- description: Compress data using GZIP, ZIP, or Snappy before delivering to S3 to reduce storage costs.
  name: Data Compression
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Deliver streaming data to S3 buckets as the primary data lake destination.
  name: Amazon S3
- description: Load streaming data into Redshift data warehouse for SQL analytics.
  name: Amazon Redshift
- description: Index streaming data in OpenSearch for real-time search and visualization.
  name: Amazon OpenSearch Service
- description: Transform and enrich streaming data using Lambda functions before delivery.
  name: AWS Lambda
- description: Send streaming data to Splunk for security and operational analytics.
  name: Splunk
jsonld:
- class_count: 1
  name: Amazon Kinesis Firehose Context
  property_count: 7
  slug: amazon-kinesis-firehose-context
layout: provider
modified: '2026-04-19'
name: Amazon Kinesis Data Firehose
rules:
- name: Amazon Kinesis Data Firehose API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: amazon-kinesis-firehose-spectral-rules
skills: []
slug: amazon-kinesis-firehose
solutions: []
tags:
- Analytics
- AWS
- Data Delivery
- Streaming
url: https://aws.amazon.com/kinesis/data-firehose/
use_cases:
- description: Stream application and infrastructure logs to Amazon OpenSearch Service for real-time analysis.
  name: Log Analytics
- description: Capture website clickstream data and deliver to data lakes for behavioral analysis.
  name: Clickstream Analytics
- description: Ingest IoT device telemetry into S3 or Redshift for analytics and reporting.
  name: IoT Data Ingestion
- description: Stream security events and logs to SIEM systems like Splunk for threat detection.
  name: Security Analytics
---
