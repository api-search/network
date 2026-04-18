---
api_count: 31
apis:
- description: The Dynatrace Environment API provides access to monitoring data and configuration settings for a specific Dynatrace environment. It includes endpoints for metrics, problems, events, logs, entities, s
  name: Dynatrace Environment API
  slug: dynatrace-environment-api
- description: The Dynatrace Metrics API v2 allows you to query, ingest, and manage time-series metric data within a Dynatrace environment. It supports retrieving metric descriptors, querying data points with flexib
  name: Dynatrace Metrics API v2
  slug: dynatrace-metrics-api-v2
- description: 'The Dynatrace Log Monitoring API v2 enables ingestion, search, and export of log records within a Dynatrace environment. It allows you to stream log data to the Grail data lakehouse and retrieve logs '
  name: Dynatrace Log Monitoring API v2
  slug: dynatrace-log-monitoring-api-v2
- description: The Dynatrace Synthetic API v2 provides programmatic access to synthetic monitoring resources including browser monitors, HTTP monitors, and clickpaths. It allows you to create, update, delete, and re
  name: Dynatrace Synthetic API v2
  slug: dynatrace-synthetic-api-v2
- description: The Dynatrace Configuration API provides access to environment-level configuration settings including alerting profiles, anomaly detection rules, application detection rules, and data privacy settings
  name: Dynatrace Configuration API
  slug: dynatrace-configuration-api
- description: The Dynatrace Account Management API allows you to manage your Dynatrace account including users, groups, permissions, environments, and service users. It uses OAuth 2.0 authentication and enables pro
  name: Dynatrace Account Management API
  slug: dynatrace-account-management-api
- description: The Dynatrace OpenPipeline API enables configuration of data ingestion pipelines that handle observability, security, and business data from any source or format. It provides endpoints for managing pi
  name: Dynatrace OpenPipeline API
  slug: dynatrace-openpipeline-api
- description: The Dynatrace Automation API provides access to the Workflows automation engine, allowing you to create, manage, and execute automated workflows within Dynatrace. It supports orchestrating remediation
  name: Dynatrace Automation API
  slug: dynatrace-automation-api
- description: The Dynatrace Events API v2 enables you to push custom events into Dynatrace and retrieve event data from your monitored environment. It supports creating deployment events, custom annotations, and in
  name: Dynatrace Events API v2
  slug: dynatrace-events-api-v2
- description: The Dynatrace Problems API v2 allows you to query and manage detected problems within a Dynatrace environment. It provides endpoints for listing open and closed problems, retrieving problem details in
  name: Dynatrace Problems API v2
  slug: dynatrace-problems-api-v2
- description: 'The Dynatrace Entities API v2 enables querying of monitored entities such as services, hosts, processes, and applications within a Dynatrace environment. It supports filtering entities by type, tags, '
  name: Dynatrace Entities API v2
  slug: dynatrace-entities-api-v2
- description: The Dynatrace Settings API 2.0 is the modern, schema-driven configuration API for managing Dynatrace environment settings objects. It replaces portions of the Configuration API v1 and provides a unifi
  name: Dynatrace Settings API 2.0
  slug: dynatrace-settings-api-v2
- description: The Dynatrace Extensions API 2.0 provides endpoints for managing monitoring extensions including uploading, activating, configuring, and removing extensions within a Dynatrace environment. It supports
  name: Dynatrace Extensions API 2.0
  slug: dynatrace-extensions-api-v2
- description: The Dynatrace DQL/Grail Query API enables execution of DQL (Dynatrace Query Language) queries against the Grail data lakehouse via REST. Queries execute asynchronously using a POST to initiate and GET
  name: Dynatrace DQL/Grail Query API
  slug: dynatrace-grail-dql-api
- description: 'The Dynatrace Access Tokens API v2 allows you to create, list, update, and delete API access tokens and ActiveGate tokens within a Dynatrace environment. It provides fine-grained scope management for '
  name: Dynatrace Access Tokens API v2
  slug: dynatrace-access-tokens-api-v2
- description: The Dynatrace Service-Level Objectives API is a management API for creating, editing, listing, deleting, and evaluating SLOs and SLO templates within a Dynatrace environment. It enables programmatic d
  name: Dynatrace Service-Level Objectives API
  slug: dynatrace-slo-api
- description: The Dynatrace Releases API provides an overview of releases deployed in your monitored environment. It allows you to retrieve information about software releases, deployment versions, and release stag
  name: Dynatrace Releases API
  slug: dynatrace-releases-api
- description: The Dynatrace Network Zones API enables you to manage network zones within a Dynatrace environment. It provides endpoints for listing all network zones, retrieving zone details including OneAgent coun
  name: Dynatrace Network Zones API
  slug: dynatrace-network-zones-api
- description: The Dynatrace Deployment API provides endpoints for downloading OneAgent and ActiveGate installers, listing available installer versions, and retrieving ActiveGate endpoint information. It enables aut
  name: Dynatrace Deployment API
  slug: dynatrace-deployment-api
- description: The Dynatrace Audit Logs API provides access to audit-related events within a Dynatrace environment including logins, logouts, configuration changes, and API token modifications. Audit logs are retain
  name: Dynatrace Audit Logs API
  slug: dynatrace-audit-logs-api
- description: The Dynatrace Business Events API v2 enables ingestion of business event data in JSON format into Dynatrace via the bizevents/ingest endpoint. It supports business-grade reporting and analytics throug
  name: Dynatrace Business Events API v2
  slug: dynatrace-business-events-api-v2
- description: The Dynatrace Application Security API provides endpoints for querying vulnerabilities, vulnerability details, remediation items, vulnerable functions, and security attacks within a Dynatrace environm
  name: Dynatrace Application Security API
  slug: dynatrace-application-security-api
- description: 'The Dynatrace Custom Tags API allows you to manage custom tags on monitored entities within a Dynatrace environment. It provides endpoints for reading, adding, and removing tags from entities such as '
  name: Dynatrace Custom Tags API
  slug: dynatrace-custom-tags-api
- description: The Dynatrace ActiveGate API enables you to view and manage ActiveGate configurations within a Dynatrace environment. It provides endpoints for listing ActiveGates, retrieving ActiveGate details, mana
  name: Dynatrace ActiveGate API
  slug: dynatrace-activegate-api
- description: 'The Dynatrace Credential Vault API enables management of credentials used for synthetic browser and HTTP monitors within a Dynatrace environment. It supports creating, listing, updating, and deleting '
  name: Dynatrace Credential Vault API
  slug: dynatrace-credential-vault-api
- description: The Dynatrace Document API provides a platform service for creating, managing, and sharing documents such as dashboards, notebooks, and launchpads within Dynatrace. It persists content-agnostic docume
  name: Dynatrace Document API
  slug: dynatrace-document-api
- description: The Dynatrace Grail Bucket Management API provides a public API for managing storage buckets within the Grail data lakehouse. It supports creating, updating, deleting, and truncating buckets for organ
  name: Dynatrace Grail Bucket Management API
  slug: dynatrace-grail-bucket-management-api
- description: 'The Dynatrace Davis AI API provides access to the Davis predictive and causal AI platform service for customized AI/ML analysis. It delivers time series forecasting, anomaly detection model training, '
  name: Dynatrace Davis AI API
  slug: dynatrace-davis-ai-api
- description: 'The Dynatrace Hub API provides programmatic access to the Dynatrace Hub catalog content including apps, extensions, and technologies in the context of the current environment. It supports listing and '
  name: Dynatrace Hub API
  slug: dynatrace-hub-api
- description: The Dynatrace OneAgent on a Host API enables you to check the configuration and status of OneAgent instances deployed on your hosts. It provides endpoints for listing hosts with OneAgent details, retr
  name: Dynatrace OneAgent on a Host API
  slug: dynatrace-oneagent-on-host-api
- description: 'The Dynatrace Platform Management API provides basic read-only information about the currently logged-in environment including environment settings, license information, and permissions. It is a core '
  name: Dynatrace Platform Management API
  slug: dynatrace-platform-management-api
asyncapis:
- description: Dynatrace delivers problem lifecycle notifications to client-provided webhook endpoints via HTTP POST. When a problem is opened, updated, merged, or resolved, Dynatrace sends a notification payload to
  name: Dynatrace Problem Notifications API
  slug: dynatrace-problems-asyncapi
capabilities:
- description: Entity discovery and topology mapping workflow combining entities, metrics, and events for developers understanding service dependencies and infrastructure layout.
  name: Dynatrace Entity And Topology
  slug: entity-and-topology
- description: Identity and access management workflow for platform admins managing Dynatrace users, groups, permissions, and environments across the account.
  name: Dynatrace Identity And Access
  slug: identity-and-access
- description: Unified incident response workflow combining problems, events, and entity data for SREs investigating service degradations detected by Davis AI.
  name: Dynatrace Incident Response
  slug: incident-response
- description: Unified monitoring and observability workflow combining metrics, logs, events, and entity data for ops engineers managing infrastructure health and performance.
  name: Dynatrace Monitoring And Observability
  slug: monitoring-and-observability
common:
- title: ''
  type: Portal
  url: https://www.dynatrace.com/support/help/dynatrace-api
- title: ''
  type: Documentation
  url: https://docs.dynatrace.com/docs/dynatrace-api
- title: ''
  type: Authentication
  url: https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication
- title: ''
  type: GettingStarted
  url: https://www.dynatrace.com/support/help/dynatrace-api/basics
- title: ''
  type: APIReference
  url: https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-response-codes
- title: ''
  type: ChangeLog
  url: https://docs.dynatrace.com/docs/whats-new/dynatrace-api
- title: ''
  type: TermsOfService
  url: https://www.dynatrace.com/company/trust-center/terms/
- title: ''
  type: PrivacyPolicy
  url: https://www.dynatrace.com/company/trust-center/privacy/
- title: ''
  type: Support
  url: https://www.dynatrace.com/support/
- title: ''
  type: Pricing
  url: https://www.dynatrace.com/pricing/
- title: ''
  type: SignUp
  url: https://www.dynatrace.com/signup/
- title: ''
  type: Support
  url: https://community.dynatrace.com/
- title: ''
  type: Blog
  url: https://community.dynatrace.com/t5/Developer-Blog/bg-p/dev_blog
- title: ''
  type: StatusPage
  url: https://dynatrace.status.io/
- title: ''
  type: GitHubOrganization
  url: https://github.com/Dynatrace
- title: ''
  type: DeveloperPortal
  url: https://developer.dynatrace.com/
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/dynatrace
- title: ''
  type: YouTube
  url: https://www.youtube.com/c/dynatrace
- title: ''
  type: JSONSchema
  url: json-schema/dynatrace-metric-series-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/dynatrace-problem-schema.json
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-context.jsonld
- title: ''
  type: SDK
  url: https://developer.dynatrace.com/develop/sdks/
- title: ''
  type: Authentication
  url: https://developer.dynatrace.com/develop/access-platform-apis-from-outside/
- title: ''
  type: Security
  url: https://docs.dynatrace.com/docs/manage/identity-access-management
- title: ''
  type: GitHubRepository
  url: https://github.com/Dynatrace/dynatrace-api
- title: ''
  type: Marketplace
  url: https://www.dynatrace.com/hub/
- title: ''
  type: ReleaseNotes
  url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/basics/deprecation-migration-guides
- title: ''
  type: Documentation
  url: https://developer.dynatrace.com/plan/platform-services/
- title: Configuration as Code CLI
  type: CLI
  url: https://github.com/Dynatrace/dynatrace-configuration-as-code
- title: Java OneAgent SDK
  type: SDK
  url: https://github.com/Dynatrace/OneAgent-SDK-for-Java
- title: Python OneAgent SDK
  type: SDK
  url: https://github.com/Dynatrace/OneAgent-SDK-for-Python
- title: Node.js OneAgent SDK
  type: SDK
  url: https://github.com/Dynatrace/OneAgent-SDK-for-NodeJs
- title: .NET OneAgent SDK
  type: SDK
  url: https://github.com/Dynatrace/OneAgent-SDK-for-dotnet
- title: C OneAgent SDK
  type: SDK
  url: https://github.com/Dynatrace/OneAgent-SDK-for-C
- title: Swift Mobile SDK
  type: SDK
  url: https://github.com/Dynatrace/swift-mobile-sdk
- title: Workflow Samples
  type: CodeExamples
  url: https://github.com/Dynatrace/Dynatrace-workflow-samples
- title: Code Snippets
  type: CodeExamples
  url: https://github.com/Dynatrace/snippets
- title: Community Examples
  type: CodeExamples
  url: https://github.com/Dynatrace/community-examples
- title: Tutorials
  type: Tutorials
  url: https://github.com/Dynatrace/Dynatrace-Tutorial
- title: ''
  type: SpectralRules
  url: rules/dynatrace-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/dynatrace-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/identity-and-access.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/log-analytics.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/observability-monitoring.yaml
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-account-management-api-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-dynatrace-metric-series-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-dynatrace-problem-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-entities-api-v2-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-events-api-v2-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-log-monitoring-api-v2-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-metrics-api-v2-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-api-v2-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-entity-ref-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-impacted-entity-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-problem-details-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-problem-notification-payload-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-webhook-header-context.jsonld
- title: ''
  type: JSONLD
  url: json-ld/dynatrace-problems-webhook-notification-config-context.jsonld
created: '2025-01-08'
description: Dynatrace is a software intelligence platform that provides application performance monitoring, artificial intelligence for operations, cloud infrastructure monitoring, and digital experience management.
features:
- description: End-to-end monitoring of applications, infrastructure, and digital experiences with automatic discovery and AI-powered root cause analysis.
  name: Full-Stack Observability
- description: Deterministic AI engine that automatically detects anomalies, identifies root causes, and provides precise answers about performance issues without manual configuration.
  name: Davis AI Engine
- description: Unified data store that combines logs, metrics, traces, events, and business data in a single analytics platform with unlimited retention and DQL query language.
  name: Grail Data Lakehouse
- description: Real-time topology mapping and dependency analysis across distributed systems with automatic baselining and smart alerting.
  name: Software Intelligence
- description: Automated workflows, remediation, and orchestration capabilities that integrate with CI/CD pipelines and IT service management tools.
  name: Cloud Automation
- description: Runtime application security with vulnerability detection, attack protection, and security analytics built into the observability platform.
  name: Application Security
- description: Real user monitoring, session replay, and synthetic monitoring for web and mobile applications to optimize user experience.
  name: Digital Experience Monitoring
- description: Flexible data ingestion framework supporting any data source and format with configurable routing, processing, and enrichment pipelines.
  name: OpenPipeline Data Ingestion
- description: Extensible monitoring platform with 600+ out-of-the-box integrations and a framework for building custom data collection extensions.
  name: Extensions Framework
- description: Automated SLO tracking and evaluation with burn rate alerting and reliability scoring based on real monitoring data.
  name: Service Level Objectives
image: https://www.dynatrace.com/logo.png
integrations:
- description: Native integration with AWS services for monitoring EC2, Lambda, RDS, and other AWS resources with automatic tagging and topology mapping.
  name: AWS CloudWatch
- description: Deep integration with Microsoft Azure for monitoring Azure App Services, AKS, Functions, and other Azure platform services.
  name: Azure Monitor
- description: Integration with GCP services including GKE, Cloud Run, Cloud Functions, and BigQuery for comprehensive cloud monitoring.
  name: Google Cloud Platform
- description: Full-stack Kubernetes monitoring with automatic pod, node, and cluster discovery, resource utilization tracking, and workload health analysis.
  name: Kubernetes
- description: Bidirectional integration with ServiceNow for automated incident creation, enrichment, and resolution based on Dynatrace problem detection.
  name: ServiceNow
- description: Integration with PagerDuty for intelligent alert routing, incident management, and on-call notification based on Dynatrace AI-detected problems.
  name: PagerDuty
- description: Notification integration with Slack channels for real-time alerts on performance issues, deployments, and problem resolution updates.
  name: Slack
- description: Integration with Atlassian Jira for automated issue creation and tracking based on detected performance problems and vulnerabilities.
  name: Jira
- description: Terraform provider for infrastructure-as-code management of Dynatrace monitoring configuration, dashboards, and alerting profiles.
  name: Terraform
- description: Ansible collection for automated deployment and configuration of Dynatrace OneAgent and environment settings across infrastructure.
  name: Ansible
jsonld:
- class_count: 10
  name: Dynatrace Account Management Api Context
  property_count: 23
  slug: dynatrace-account-management-api-context
- class_count: 0
  name: Dynatrace Account Management Context
  property_count: 12
  slug: dynatrace-account-management-context
- class_count: 7
  name: Dynatrace Context
  property_count: 28
  slug: dynatrace-context
- class_count: 1
  name: Dynatrace Dynatrace Metric Series Context
  property_count: 2
  slug: dynatrace-dynatrace-metric-series-context
- class_count: 1
  name: Dynatrace Dynatrace Problem Context
  property_count: 14
  slug: dynatrace-dynatrace-problem-context
- class_count: 10
  name: Dynatrace Entities Api V2 Context
  property_count: 27
  slug: dynatrace-entities-api-v2-context
- class_count: 0
  name: Dynatrace Entities V2 Context
  property_count: 12
  slug: dynatrace-entities-v2-context
- class_count: 7
  name: Dynatrace Events Api V2 Context
  property_count: 22
  slug: dynatrace-events-api-v2-context
- class_count: 0
  name: Dynatrace Events V2 Context
  property_count: 9
  slug: dynatrace-events-v2-context
- class_count: 7
  name: Dynatrace Log Monitoring Api V2 Context
  property_count: 14
  slug: dynatrace-log-monitoring-api-v2-context
- class_count: 0
  name: Dynatrace Log Monitoring V2 Context
  property_count: 9
  slug: dynatrace-log-monitoring-v2-context
- class_count: 8
  name: Dynatrace Metrics Api V2 Context
  property_count: 30
  slug: dynatrace-metrics-api-v2-context
- class_count: 0
  name: Dynatrace Metrics V2 Context
  property_count: 10
  slug: dynatrace-metrics-v2-context
- class_count: 11
  name: Dynatrace Problems Api V2 Context
  property_count: 30
  slug: dynatrace-problems-api-v2-context
- class_count: 1
  name: Dynatrace Problems Entity Ref Context
  property_count: 3
  slug: dynatrace-problems-entity-ref-context
- class_count: 1
  name: Dynatrace Problems Impacted Entity Context
  property_count: 2
  slug: dynatrace-problems-impacted-entity-context
- class_count: 1
  name: Dynatrace Problems Problem Details Context
  property_count: 7
  slug: dynatrace-problems-problem-details-context
- class_count: 1
  name: Dynatrace Problems Problem Notification Payload Context
  property_count: 10
  slug: dynatrace-problems-problem-notification-payload-context
- class_count: 0
  name: Dynatrace Problems V2 Context
  property_count: 13
  slug: dynatrace-problems-v2-context
- class_count: 1
  name: Dynatrace Problems Webhook Header Context
  property_count: 2
  slug: dynatrace-problems-webhook-header-context
- class_count: 1
  name: Dynatrace Problems Webhook Notification Config Context
  property_count: 8
  slug: dynatrace-problems-webhook-notification-config-context
layout: provider
modified: '2026-04-18'
name: Dynatrace
rules:
- name: Dynatrace API Rules
  rule_count: 21
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 1
  slug: dynatrace-spectral-rules
skills: []
slug: dynatrace
solutions: []
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
url: https://raw.githubusercontent.com/api-evangelist/dynatrace/refs/heads/main/apis.yml
use_cases:
- description: Monitor hosts, containers, and cloud infrastructure with automatic discovery, health metrics, and capacity planning across hybrid and multi-cloud environments.
  name: Infrastructure Monitoring
- description: Trace distributed transactions end-to-end, identify bottlenecks, and optimize application performance with code-level visibility and AI-powered insights.
  name: Application Performance Management
- description: Ingest, search, and analyze log data at scale using the Grail data lakehouse with DQL queries for troubleshooting and compliance.
  name: Log Analytics and Management
- description: Track application health and performance during cloud migration with automatic dependency mapping and impact analysis.
  name: Cloud Migration Monitoring
- description: Integrate observability into CI/CD pipelines with automated quality gates, deployment validation, and incident response workflows.
  name: DevOps and SRE Automation
- description: Correlate business events with technical performance data to measure revenue impact and optimize digital business outcomes.
  name: Business Analytics
- description: Detect runtime vulnerabilities, monitor attack attempts, and assess application security posture with integrated security analytics.
  name: Security Posture Management
- description: Proactively monitor application availability and performance with browser-based and HTTP synthetic tests from global locations.
  name: Synthetic Testing
---
