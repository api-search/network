---
api_count: 7
apis:
- description: Amazon Kinesis Data Streams is a massively scalable and durable real-time data streaming service. It can continuously capture gigabytes of data per second from hundreds of thousands of sources such as
  name: Amazon Kinesis Data Streams
  slug: ''
- description: Amazon Data Firehose (formerly Amazon Kinesis Data Firehose) is the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. It can capture, transform, and del
  name: Amazon Data Firehose
  slug: ''
- description: Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics) is a fully managed service for processing and analyzing streaming data in real time using Apache Flink. You can build a
  name: Amazon Managed Service for Apache Flink
  slug: ''
- description: Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning, playback, and other processing. It automatically provisions and elast
  name: Amazon Kinesis Video Streams
  slug: ''
- description: The Amazon Kinesis Video Streams Media API provides operations for reading and writing media data to and from a Kinesis video stream, enabling real-time media ingestion and consumption.
  name: Amazon Kinesis Video Streams Media
  slug: ''
- description: The Amazon Kinesis Video Streams Archived Media API provides operations for accessing archived video data from Kinesis video streams, including retrieving clips, HLS and DASH streaming session URLs, i
  name: Amazon Kinesis Video Streams Archived Media
  slug: ''
- description: The Amazon Kinesis Video Signaling Channels API facilitates peer-to-peer WebRTC communication by enabling applications to securely discover each other and exchange connection offers and answers throug
  name: Amazon Kinesis Video Signaling Channels
  slug: ''
asyncapis:
- description: Amazon Kinesis Data Streams is a massively scalable and durable real-time data streaming service. This AsyncAPI specification describes the event-driven consumer patterns for Kinesis Data Streams, inc
  name: Amazon Kinesis Data Streams
  slug: amazon-kinesis-streams-asyncapi
capabilities:
- description: Unified workflow capability for Amazon Kinesis combining resource management and operations.
  name: Amazon Kinesis Workflow
  slug: amazon-kinesis-workflow
common:
- title: ''
  type: FAQ
  url: https://aws.amazon.com/kinesis/data-streams/faqs/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis/
- title: ''
  type: Customers
  url: https://aws.amazon.com/kinesis/customers/
- title: ''
  type: Resources
  url: https://aws.amazon.com/kinesis/resources/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/kinesis/
- title: ''
  type: SDK & Tools
  url: https://aws.amazon.com/tools/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/kinesis/
- title: ''
  type: Firehose Blog
  url: https://aws.amazon.com/blogs/big-data/category/analytics/amazon-kinesis/kinesis-data-firehose/
- title: ''
  type: Video Streams FAQs
  url: https://aws.amazon.com/kinesis/video-streams/faqs/
- title: ''
  type: Firehose FAQs
  url: https://aws.amazon.com/firehose/faqs/
- title: ''
  type: Managed Flink FAQs
  url: https://aws.amazon.com/managed-service-apache-flink/faqs/
- title: ''
  type: Video Streams Resources
  url: https://aws.amazon.com/kinesis/video-streams/resources/
- title: ''
  type: Portal
  url: https://aws.amazon.com/kinesis/
- title: ''
  type: Pricing
  url: https://aws.amazon.com/kinesis/data-streams/pricing/
- title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-iam.html
- title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Stack Overflow
  url: https://stackoverflow.com/questions/tagged/amazon-kinesis
- title: ''
  type: SpectralRules
  url: rules/amazon-kinesis-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-kinesis-workflow.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-kinesis-vocabulary.yaml
created: 2024-01-01 00:00:00+00:00
description: Amazon Kinesis makes it easy to collect, process, and analyze real-time streaming data so you can get timely insights and react quickly to new information. Amazon Kinesis offers key capabilities to cost-effectively process streaming data at any scale, along with the flexibility to choose the tools that best suit the requirements of your application.
features: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Trigger Lambda functions to process records from Kinesis streams.
  name: AWS Lambda
- description: Use Kinesis streams as source for Firehose delivery.
  name: Amazon Kinesis Data Firehose
- description: Store processed streaming records in DynamoDB.
  name: Amazon DynamoDB
jsonld:
- class_count: 2
  name: Amazon Kinesis Context
  property_count: 7
  slug: amazon-kinesis-context
layout: provider
modified: '2026-04-19'
name: Amazon Kinesis
rules:
- name: Amazon Kinesis API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: amazon-kinesis-spectral-rules
skills: []
slug: amazon-kinesis
solutions: []
tags:
- Analytics
- Big Data
- Data Processing
- Real-Time
- Streaming
url: https://raw.githubusercontent.com/api-search/amazon-web-services/main/apis/kinesis.yml
use_cases:
- description: Analyze streaming data for operational metrics and business intelligence.
  name: Real-Time Analytics
- description: Build event-driven microservices that react to real-time data streams.
  name: Event-Driven Architectures
- description: Feed real-time data into ML models for online training and inference.
  name: Machine Learning
---
