---
api_count: 1
apis:
- description: RESTful API for AWS X-Ray distributed tracing operations including trace retrieval, service map generation, sampling rule management, group management, and insights analysis for application performanc
  name: Amazon X-Ray REST API
  slug: amazon-xray-rest-api
capabilities:
- description: Unified workflow for developers and operations teams to analyze distributed traces, visualize service maps, manage sampling rules, and investigate application performance insights using Amazon X-Ray.
  name: Amazon X-Ray Distributed Tracing
  slug: distributed-tracing
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/xray/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/xray/
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
  url: https://aws.amazon.com/blogs/developer/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/xray/
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
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-xray
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-xray-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-xray-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/distributed-tracing.yaml
created: '2024-01-15'
description: AWS X-Ray is a distributed tracing service that helps developers analyze and debug production applications, providing end-to-end visibility into requests as they travel through the application. X-Ray provides service maps, trace analysis, sampling rules, group filtering, and AI-powered insights for identifying performance bottlenecks and errors across microservices and serverless architectures.
features:
- description: Trace requests as they travel across services, microservices, and serverless functions to identify bottlenecks and errors.
  name: End-to-End Distributed Tracing
- description: Automatically generate visual service maps showing all connected services and their health status and latency.
  name: Service Map Visualization
- description: Create groups with filter expressions to organize and analyze subsets of traces based on service names, URLs, or annotations.
  name: Trace Filtering and Groups
- description: Configurable sampling rules to control the percentage of requests traced, balancing coverage with cost.
  name: Adaptive Sampling
- description: AI-powered automatic detection of anomalies and performance issues with root cause analysis across the service map.
  name: X-Ray Insights
- description: Native tracing support across Lambda, EC2, ECS, EKS, API Gateway, SNS, SQS, and 200+ other AWS services.
  name: AWS Service Integration
- description: X-Ray SDKs for Java, Node.js, Python, Go, Ruby, and .NET for custom application instrumentation.
  name: SDK and Agent Support
- description: Deep integration with Amazon CloudWatch for correlating traces with metrics, logs, and alarms.
  name: CloudWatch Integration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Automatic tracing of Lambda function invocations and downstream calls.
  name: AWS Lambda
- description: Native tracing of API Gateway requests through backend services.
  name: Amazon API Gateway
- description: Correlation of traces with CloudWatch metrics, logs, and alarms.
  name: Amazon CloudWatch
- description: Service mesh integration for automatic tracing of Envoy-based microservices.
  name: AWS App Mesh
- description: X-Ray supports the OpenTelemetry standard via the AWS Distro for OpenTelemetry.
  name: OpenTelemetry
jsonld:
- class_count: 108
  name: Amazon Xray Context
  property_count: 164
  slug: amazon-xray-context
layout: provider
modified: '2026-04-19'
name: Amazon X-Ray
rules:
- name: Amazon X-Ray API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 5
  slug: amazon-xray-spectral-rules
skills: []
slug: amazon-xray
solutions: []
tags:
- Application Performance
- AWS
- Debugging
- Distributed Tracing
- Monitoring
- Observability
url: https://raw.githubusercontent.com/api-evangelist/amazon-xray/refs/heads/main/apis.yml
use_cases:
- description: Trace requests across microservices to identify which service is causing latency or errors in distributed applications.
  name: Microservices Debugging
- description: Monitor Lambda function execution chains and identify cold start impacts and downstream service bottlenecks.
  name: Serverless Application Monitoring
- description: Use trace data and service maps to identify and eliminate performance bottlenecks in production applications.
  name: Performance Optimization
- description: Drill into traces to understand the exact call chain that caused an error or latency spike.
  name: Root Cause Analysis
- description: Track end-to-end latency and error rates across services to ensure application SLAs are being met.
  name: SLA Compliance Monitoring
---
