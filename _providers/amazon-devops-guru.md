---
api_count: 1
apis:
- description: The Amazon DevOps Guru API provides programmatic access to manage resource collections, insights, anomalies, and recommendations for improving application operational performance and availability. Cov
  name: Amazon DevOps Guru API
  slug: ''
capabilities:
- description: Workflow capability for DevOps engineers and SREs to monitor application health, investigate anomalies, follow remediation recommendations, and configure operational intelligence coverage using Amazon
  name: Amazon DevOps Guru Operational Intelligence
  slug: operational-intelligence
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/devops-guru/
- title: ''
  type: Website
  url: https://aws.amazon.com/devops-guru/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/devops-guru/
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
  url: https://aws.amazon.com/blogs/devops/category/artificial-intelligence/amazon-devops-guru/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/devops-guru/
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
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-devops-guru-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-devops-guru-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/operational-intelligence.yaml
created: '2026-03-16'
description: Amazon DevOps Guru is a machine learning-powered service that makes it easy to improve an application's operational performance and availability. It detects behaviors that deviate from normal operating patterns so you can identify operational issues long before they impact your customers.
features:
- description: Uses machine learning to detect behavioral deviations across hundreds of AWS metrics without manual threshold configuration.
  name: ML-Powered Anomaly Detection
- description: Identifies anomalies before they become operational issues, allowing teams to remediate before customer impact.
  name: Proactive Insights
- description: Surfaces insights when active operational issues are detected to accelerate root cause analysis.
  name: Reactive Insights
- description: Provides specific remediation recommendations with links to relevant documentation and AWS console pages.
  name: Actionable Recommendations
- description: Analyzes CloudWatch Logs for log-based anomalies to include log patterns in operational insights.
  name: CloudWatch Logs Integration
- description: Automatically creates OpsCenter OpsItems for detected insights to streamline incident management.
  name: AWS OpsCenter Integration
- description: Define which applications to monitor by specifying CloudFormation stack names for precise application-scoped coverage.
  name: CloudFormation-Based Coverage
- description: Enable DevOps Guru across an entire AWS Organization to centrally monitor all accounts and regions.
  name: Organizations Integration
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Ingests CloudWatch metrics and logs for anomaly detection and event correlation.
  name: Amazon CloudWatch
- description: Uses CloudFormation stacks to define application boundaries for targeted monitoring coverage.
  name: AWS CloudFormation
- description: Automatically creates OpsCenter OpsItems for detected insights to enable incident management workflows.
  name: AWS OpsCenter
- description: Sends insight notifications to SNS topics for routing to teams via email, Slack, PagerDuty, or other channels.
  name: Amazon SNS
- description: Enables organization-wide monitoring by aggregating insights across multiple AWS accounts.
  name: AWS Organizations
- description: Emits DevOps Guru events to EventBridge for custom automation and routing workflows.
  name: Amazon EventBridge
jsonld:
- class_count: 23
  name: Amazon Devops Guru Context
  property_count: 54
  slug: amazon-devops-guru-context
layout: provider
modified: '2026-04-19'
name: Amazon DevOps Guru
rules:
- name: Amazon DevOps Guru API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 4
  slug: amazon-devops-guru-spectral-rules
skills: []
slug: amazon-devops-guru
solutions: []
tags:
- Anomaly Detection
- AWS
- DevOps
- Machine Learning
- Operational Intelligence
url: https://aws.amazon.com/devops-guru/
use_cases:
- description: Detect potential issues in application behavior before they impact end users using ML-powered proactive insights.
  name: Proactive Operational Monitoring
- description: Rapidly identify the root cause of operational incidents by correlating anomalies, events, and recommendations.
  name: Incident Root Cause Analysis
- description: Use continuous behavioral monitoring to identify performance bottlenecks and optimization opportunities.
  name: Application Performance Optimization
- description: Monitor operational health across all accounts in an AWS Organization from a single pane of glass.
  name: Multi-Account Operations
- description: Integrate DevOps Guru insights into CI/CD pipelines to gate deployments on operational health status.
  name: DevOps Pipeline Integration
---
