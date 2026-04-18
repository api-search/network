---
api_count: 10
apis:
- description: Core CloudWatch API for metrics, alarms, and dashboards.
  name: Amazon CloudWatch API
  slug: ''
- description: API for ingesting, storing, and analyzing log data.
  name: Amazon CloudWatch Logs API
  slug: ''
- description: Event-driven architecture for responding to state changes in AWS resources.
  name: Amazon CloudWatch Events API
  slug: ''
- description: Automated monitoring for applications with anomaly detection.
  name: Amazon CloudWatch Application Insights API
  slug: ''
- description: API for creating and managing canaries that continuously monitor endpoints and APIs using synthetic traffic.
  name: Amazon CloudWatch Synthetics API
  slug: ''
- description: API for monitoring internet performance and availability between applications hosted on AWS and end users.
  name: Amazon CloudWatch Internet Monitor API
  slug: ''
- description: API for real user monitoring to collect client-side data about web and mobile application performance from actual user sessions.
  name: Amazon CloudWatch RUM API
  slug: ''
- description: API for creating and managing cross-account observability links between source accounts and monitoring accounts.
  name: Amazon CloudWatch Observability Access Manager API
  slug: ''
- description: API for automatic instrumentation and monitoring of application services with service level objectives.
  name: Amazon CloudWatch Application Signals API
  slug: ''
- description: API for active network monitoring to identify network issues within AWS or company networks using synthetic probes.
  name: Amazon CloudWatch Network Monitor API
  slug: ''
capabilities:
- description: Monitor AWS resources with metrics, alarms, dashboards, anomaly detection, and metric streams. Used by DevOps engineers and SRE teams.
  name: AWS CloudWatch Monitoring and Observability
  slug: monitoring-and-observability
common:
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/aws/category/management-tools/amazon-cloudwatch/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/cloudwatch/faqs/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: ChangeLog
  url: https://aws.amazon.com/releasenotes/
- title: ''
  type: Pricing
  url: https://aws.amazon.com/cloudwatch/pricing/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudwatch/
- title: ''
  type: SDK
  url: https://aws.amazon.com/tools/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloudwatch/
- title: ''
  type: OpenAPI
  url: openapi/cloudwatch-openapi.yml
- title: ''
  type: JSONSchema
  url: json-schema/cloudwatch-alarm-schema.json
- title: ''
  type: JSONLD
  url: json-ld/cloudwatch-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/cloudwatch-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/cloudwatch-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/monitoring-and-observability.yaml
created: '2024-01-15'
description: Amazon CloudWatch is a monitoring and observability service that provides data and actionable insights for AWS, hybrid, and on-premises applications and infrastructure resources.
features:
- Unified monitoring across AWS resources with automatic dashboards
- Metric collection and custom metrics publishing
- CloudWatch Alarms with composite alarm support and anomaly detection
- CloudWatch Logs Insights for interactive log analytics
- Synthetics canaries for endpoint and API monitoring
- Real User Monitoring (RUM) for client-side performance
- Internet Monitor for availability and latency tracking
- Application Signals for automatic service instrumentation and SLOs
- Cross-account observability with Observability Access Manager
- Network Monitor for hybrid connectivity health
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- Amazon SNS for alarm notifications
- AWS Lambda for automated remediation
- Amazon EventBridge for event-driven architectures
- AWS X-Ray for distributed tracing
- Amazon Managed Grafana for visualization
- AWS Systems Manager for operational automation
- PagerDuty and Slack via SNS topic subscriptions
- Terraform and CloudFormation for infrastructure as code
jsonld:
- class_count: 0
  name: Cloudwatch Context
  property_count: 0
  slug: cloudwatch-context
layout: provider
modified: '2026-04-18'
name: AWS CloudWatch
rules:
- name: AWS CloudWatch API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: cloudwatch-spectral-rules
skills: []
slug: cloudwatch
solutions: []
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
url: https://raw.githubusercontent.com/api-evangelist/cloudwatch/refs/heads/main/apis.yml
use_cases:
- Monitoring application health and setting automated alarms
- Centralized log aggregation and analysis across AWS services
- Tracking end-user experience with real user monitoring
- Proactively detecting API and endpoint issues with synthetic monitoring
- Managing SLOs across microservices architectures
- Monitoring network performance for Direct Connect and VPN
- Cross-account observability for multi-account AWS organizations
- Anomaly detection on metrics to identify unexpected behavior
---
