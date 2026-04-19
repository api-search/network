---
api_count: 1
apis:
- description: 'The Amazon Managed Service for Prometheus API provides programmatic access to create and manage workspaces, alert manager definitions, rule groups namespaces, logging configurations, and scrapers for '
  name: Amazon Managed Service for Prometheus API
  slug: amazon-managed-prometheus-api
capabilities:
- description: Workflow capability for DevOps and SRE teams to manage Prometheus workspaces, configure alerting, and define recording rules for container metrics monitoring.
  name: Amazon Managed Service for Prometheus - Metrics Monitoring Workflow
  slug: metrics-monitoring-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/prometheus/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/prometheus/
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
  url: https://aws.amazon.com/blogs/mt/tag/amazon-managed-service-for-prometheus/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/prometheus/
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
  url: rules/amazon-managed-prometheus-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-managed-prometheus-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/metrics-monitoring-workflow.yaml
created: '2026-03-16'
description: Amazon Managed Service for Prometheus is a serverless, Prometheus-compatible monitoring service for container metrics. It automatically scales as your monitoring needs increase, works with open-source tools, and integrates with Amazon EKS and other container environments. The service provides fully managed workspaces, alert manager definitions, and rule group namespaces for Prometheus-compatible monitoring at scale.
features:
- description: Run Prometheus-compatible monitoring without managing servers, scaling, or high availability.
  name: Serverless Prometheus
- description: Configure Prometheus AlertManager rules for routing, grouping, and suppressing alerts.
  name: Alert Manager Definitions
- description: Define and manage Prometheus recording and alerting rules organized in namespaces.
  name: Rule Groups Namespaces
- description: Create managed scrapers to automatically collect metrics from Amazon EKS clusters.
  name: Managed Scrapers
- description: Configure logging for Prometheus workspaces to capture operational events.
  name: Logging Configuration
- description: Use standard Prometheus remote write and query APIs with existing tooling and clients.
  name: Prometheus-Compatible APIs
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Collect metrics from EKS clusters using managed scrapers and Prometheus remote write.
  name: Amazon EKS
- description: Visualize Prometheus metrics in Grafana dashboards using AMP as a data source.
  name: Amazon Managed Grafana
- description: Use ADOT collectors to send metrics to AMP workspaces via remote write.
  name: AWS Distro for OpenTelemetry
- description: Forward Prometheus alerts and metrics to CloudWatch for cross-service monitoring.
  name: Amazon CloudWatch
- description: Use native Prometheus Alertmanager configuration for alert routing and notification.
  name: Prometheus Alertmanager
jsonld:
- class_count: 48
  name: Amazon Managed Prometheus Context
  property_count: 21
  slug: amazon-managed-prometheus-context
layout: provider
modified: '2026-04-19'
name: Amazon Managed Service for Prometheus
rules:
- name: Amazon Managed Service for Prometheus API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 7
  slug: amazon-managed-prometheus-spectral-rules
skills: []
slug: amazon-managed-prometheus
solutions: []
tags:
- AWS
- Containers
- Monitoring
- Observability
- Prometheus
url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-prometheus/refs/heads/main/apis.yml
use_cases:
- description: Monitor EKS clusters and Kubernetes workloads with Prometheus metrics at any scale.
  name: Kubernetes Cluster Monitoring
- description: Collect and analyze container CPU, memory, and network metrics for performance optimization.
  name: Container Performance Metrics
- description: Monitor distributed microservices with Prometheus metrics and custom alert rules.
  name: Microservices Observability
- description: Track resource utilization trends over time for infrastructure capacity planning.
  name: Infrastructure Capacity Planning
- description: Define SLO-based alerting rules to monitor service level agreements in real time.
  name: SLA Monitoring
---
