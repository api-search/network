---
api_count: 1
apis:
- description: API for publishing metrics, creating alarms, managing dashboards, querying logs, and configuring observability for AWS resources and applications.
  name: Amazon CloudWatch API
  slug: ''
capabilities:
- description: Workflow for observability and monitoring using Amazon CloudWatch for Operations Engineer personas.
  name: Amazon CloudWatch Observability and Monitoring
  slug: observability
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/cloudwatch/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/
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
  url: https://aws.amazon.com/blogs/mt/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudwatch/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-cloudwatch
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-cloudwatch-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudwatch-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/observability.yaml
created: '2024-01-15'
description: Amazon CloudWatch is an intelligent observability platform providing complete visibility into performance, availability, and security across your entire technology stack. Monitor applications, infrastructure, and workloads with unified metrics, logs, and traces plus AI-powered insights.
features:
- description: Monitor metrics, logs, and traces in one interface for complete system visibility.
  name: Unified Observability
- description: Detect anomalies and investigate issues using AI-powered CloudWatch Investigations.
  name: AI-Powered Insights
- description: Create custom dashboards with pre-built and customizable metric visualizations.
  name: Dashboards
- description: Set threshold-based alarms on any metric to trigger automated actions.
  name: Alarms
- description: Analyze log data with SQL and natural language queries using CloudWatch Logs Insights.
  name: Log Insights
- description: Ingest OpenTelemetry data alongside native AWS metrics and traces.
  name: OpenTelemetry Integration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Monitor EC2 instance performance metrics including CPU, network, and disk.
  name: Amazon EC2
- description: Monitor Lambda invocations, errors, and duration metrics automatically.
  name: AWS Lambda
- description: Ingest Prometheus metrics into CloudWatch for unified monitoring.
  name: Amazon Prometheus
- description: Connect CloudWatch data sources to Grafana dashboards.
  name: Grafana
- description: Correlate traces from X-Ray with CloudWatch metrics and logs.
  name: AWS X-Ray
jsonld:
- class_count: 10
  name: Amazon Cloudwatch Context
  property_count: 32
  slug: amazon-cloudwatch-context
layout: provider
modified: '2026-04-19'
name: Amazon CloudWatch
rules:
- name: Amazon CloudWatch API Rules
  rule_count: 19
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 6
  slug: amazon-cloudwatch-spectral-rules
skills: []
slug: amazon-cloudwatch
solutions: []
tags:
- AWS
- CloudWatch
- Monitoring
- Observability
- Metrics
- Logs
url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudwatch/refs/heads/main/apis.yml
use_cases:
- description: Monitor EC2, RDS, Lambda, and other AWS resources with built-in metrics.
  name: Infrastructure Monitoring
- description: Track application performance metrics and detect latency or error rate spikes.
  name: Application Performance
- description: Aggregate and query application logs for troubleshooting and analytics.
  name: Log Analysis
- description: Trigger auto-scaling, Lambda functions, or SNS alerts based on metric alarms.
  name: Automated Remediation
---
