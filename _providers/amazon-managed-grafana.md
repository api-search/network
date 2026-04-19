---
api_count: 1
apis:
- description: The Amazon Managed Grafana API provides programmatic access to create and manage Grafana workspaces, users, SAML configurations, and workspace API keys for managed Grafana deployments. Covers workspac
  name: Amazon Managed Grafana API
  slug: amazon-managed-grafana-api
capabilities:
- description: Workflow capability for platform and operations teams to create and manage Grafana workspaces, dashboards, and access controls for observability on Amazon Managed Grafana.
  name: Amazon Managed Grafana - Observability Dashboard Workflow
  slug: observability-dashboard-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/grafana/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/grafana/
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
  url: https://aws.amazon.com/blogs/mt/tag/amazon-managed-grafana/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/grafana/
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
  url: rules/amazon-managed-grafana-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-managed-grafana-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/observability-dashboard-workflow.yaml
created: '2026-03-16'
description: Amazon Managed Grafana is a fully managed service for open source Grafana developed in collaboration with Grafana Labs. It enables interactive data visualizations and dashboards for operational metrics, logs, and traces from multiple sources including AWS services, third-party ISVs, and on-premises data. The service handles provisioning, setup, scaling, and maintenance of Grafana, allowing teams to focus on creating dashboards and analyzing data.
features:
- description: Provision and manage Grafana workspaces without infrastructure setup, patching, or scaling.
  name: Fully Managed Grafana
- description: Configure SAML-based single sign-on for workspace authentication and user management.
  name: SSO and SAML Integration
- description: Connect to AWS services, third-party ISVs, and on-premises data sources in a single dashboard.
  name: Multi-Source Data Visualization
- description: Create and manage API keys for programmatic access to Grafana workspace resources.
  name: Workspace API Keys
- description: Associate and manage Grafana Enterprise licenses for advanced features.
  name: License Management
- description: Deploy workspaces within a VPC for secure private access to data sources.
  name: VPC Integration
- description: Manage user and group permissions within Grafana workspaces using role assignments.
  name: Role-Based Access Control
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Visualize CloudWatch metrics and logs natively in Grafana dashboards.
  name: Amazon CloudWatch
- description: Query Prometheus metrics from AMP workspaces as a Grafana data source.
  name: Amazon Managed Service for Prometheus
- description: Trace application requests and visualize distributed tracing data in Grafana.
  name: AWS X-Ray
- description: Query OpenSearch indices for log analytics and visualization.
  name: Amazon OpenSearch Service
- description: Visualize time-series data stored in Amazon Timestream.
  name: Amazon Timestream
- description: Integrate with IAM Identity Center for centralized user authentication.
  name: AWS IAM Identity Center
jsonld:
- class_count: 55
  name: Amazon Managed Grafana Context
  property_count: 77
  slug: amazon-managed-grafana-context
layout: provider
modified: '2026-04-19'
name: Amazon Managed Grafana
rules:
- name: Amazon Managed Grafana API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 7
  slug: amazon-managed-grafana-spectral-rules
skills: []
slug: amazon-managed-grafana
solutions: []
tags:
- AWS
- Dashboards
- Monitoring
- Observability
- Visualization
url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-grafana/refs/heads/main/apis.yml
use_cases:
- description: Visualize AWS infrastructure metrics from CloudWatch, EC2, RDS, and other services in unified dashboards.
  name: Infrastructure Monitoring
- description: Monitor Kubernetes and ECS workloads using Prometheus and CloudWatch Container Insights data sources.
  name: Container Observability
- description: Track application latency, error rates, and throughput with custom dashboards and alerting.
  name: Application Performance Monitoring
- description: Build executive dashboards combining operational and business metrics from multiple data sources.
  name: Business Metrics Dashboards
- description: Visualize security findings and compliance metrics from AWS Security Hub and GuardDuty.
  name: Security and Compliance Monitoring
---
