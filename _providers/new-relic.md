---
api_count: 17
apis:
- description: The New Relic REST API v2 is the original HTTP REST interface for querying application performance data, configuring alerts, and managing account settings. New Relic recommends NerdGraph (GraphQL) for
  name: New Relic REST API v2
  slug: new-relic-rest-api-v2
- description: NerdGraph is New Relic's primary GraphQL API for querying observability data, managing account configuration, and accessing the full breadth of New Relic platform capabilities. It is the recommended A
  name: New Relic NerdGraph API
  slug: new-relic-nerdgraph-api
- description: The New Relic Metric API is an HTTP endpoint for ingesting dimensional metric data directly into the New Relic platform. It accepts JSON payloads via POST requests and is the underlying API used by Te
  name: New Relic Metric API
  slug: new-relic-metric-api
- description: The New Relic Event API allows you to send custom event data to the New Relic platform via HTTP POST. Custom events submitted through this API can be queried and visualized using NRQL, making it suita
  name: New Relic Event API
  slug: new-relic-event-api
- description: The New Relic Log API enables log data to be sent directly to the New Relic platform via HTTP POST requests. It accepts compressed JSON payloads and provides an alternative to log forwarding agents wh
  name: New Relic Log API
  slug: new-relic-log-api
- description: The New Relic Trace API allows distributed tracing data to be sent directly to New Relic in either New Relic format or Zipkin JSON v2 format. It is used by Telemetry SDKs, open source integrations, an
  name: New Relic Trace API
  slug: new-relic-trace-api
- description: The New Relic Alerts REST API provides endpoints for programmatically managing alert policies, conditions, notification channels, and muting rules. New Relic recommends using NerdGraph for new alert m
  name: New Relic Alerts API
  slug: new-relic-alerts-api
- description: The New Relic Synthetics API, available through NerdGraph, allows you to programmatically create, update, delete, and query synthetic monitors including ping monitors, scripted API monitors, browser m
  name: New Relic Synthetics API
  slug: new-relic-synthetics-api
- description: 'The New Relic Infrastructure Alerts REST API provides endpoints for creating and managing infrastructure-specific alert conditions such as host, process, and integration alert conditions. It uses the '
  name: New Relic Infrastructure Alerts API
  slug: new-relic-infrastructure-alerts-api
- description: The New Relic Browser API provides JavaScript methods for extending and customizing browser monitoring data collection within the New Relic browser agent. Developers can use it to add custom attribute
  name: New Relic Browser API
  slug: new-relic-browser-api
- description: The New Relic Partnership API is a web service API for New Relic partners that enables them to create, edit, upgrade, downgrade, and cancel New Relic accounts on behalf of their customers. It is avail
  name: New Relic Partnership API
  slug: new-relic-partnership-api
- description: The New Relic Telemetry SDKs are open source client libraries for sending metrics, events, logs, and traces (MELT) to New Relic using the ingest APIs. SDKs are available for Java, Python, Node.js, Go,
  name: New Relic Telemetry SDKs
  slug: new-relic-telemetry-sdk
- description: New Relic provides a native OTLP (OpenTelemetry Protocol) endpoint that accepts metrics, traces, and logs from any OpenTelemetry-instrumented application or OTLP exporter. It supports both gRPC and HT
  name: New Relic OpenTelemetry OTLP Endpoint
  slug: new-relic-opentelemetry-otlp
- description: New Relic Control is an observability control plane that unifies Fleet Control, Agent Control, and Pipeline Control into a single management layer. It enables DevOps and platform teams to remotely dep
  name: New Relic Control
  slug: new-relic-control
- description: 'The New Relic NRQL Lookups API is a REST API for managing lookup tables that can be used to enrich NRQL query results. It supports creating, updating, downloading, listing, and deleting lookup tables '
  name: New Relic NRQL Lookups API
  slug: new-relic-nrql-lookups-api
- description: 'The New Relic Security Data API allows vulnerability and security finding data to be sent directly to New Relic via HTTP POST. It accepts JSON payloads describing detected vulnerabilities or security '
  name: New Relic Security Data API
  slug: new-relic-security-data-api
- description: The New Relic Mobile SDK provides iOS and Android APIs for extending mobile monitoring data collection beyond what the agent captures automatically. Developers can add custom attributes, record custom
  name: New Relic Mobile SDK
  slug: new-relic-mobile-sdk
capabilities:
- description: Application performance monitoring workflow combining application metrics, deployments, hosts, and custom events for developers tracking application health and release impact.
  name: New Relic Application Monitoring
  slug: application-monitoring
- description: Alert policy and condition management workflow for platform admins configuring and maintaining New Relic alerting rules, notification channels, and policy structures.
  name: New Relic Alerting Configuration
  slug: full-stack-observability
- description: Incident response workflow combining alerts, incidents, violations, and events for SREs investigating and resolving production issues detected by New Relic.
  name: New Relic Incident Response
  slug: incident-response
- description: Telemetry data ingestion workflow combining event, log, metric, and trace APIs for ops engineers sending observability data to New Relic from external sources.
  name: New Relic Telemetry Ingestion
  slug: telemetry-ingestion
common:
- title: ''
  type: Portal
  url: https://newrelic.com/
- title: ''
  type: Pricing
  url: https://newrelic.com/pricing
- title: ''
  type: Documentation
  url: https://docs.newrelic.com/
- title: ''
  type: TermsOfService
  url: https://newrelic.com/termsandconditions/terms
- title: ''
  type: PrivacyPolicy
  url: https://newrelic.com/termsandconditions/privacy
- title: ''
  type: Blog
  url: https://newrelic.com/blog
- title: ''
  type: Partners
  url: https://newrelic.com/solutions/partners
- title: ''
  type: TrustCenter
  url: https://trust.newrelic.com/
- title: ''
  type: Login
  url: https://login.newrelic.com/login
- title: ''
  type: SignUp
  url: https://newrelic.com/signup
- title: ''
  type: Console
  url: https://one.newrelic.com/
- title: ''
  type: Portal
  url: https://developer.newrelic.com/
- title: ''
  type: Authentication
  url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
- title: ''
  type: Support
  url: https://support.newrelic.com/
- title: ''
  type: StatusPage
  url: https://status.newrelic.com/
- title: ''
  type: GitHubOrganization
  url: https://github.com/newrelic
- title: ''
  type: Support
  url: https://discuss.newrelic.com/
- title: ''
  type: GettingStarted
  url: https://docs.newrelic.com/docs/new-relic-solutions/get-started/intro-new-relic/
- title: ''
  type: ChangeLog
  url: https://docs.newrelic.com/whats-new/
- title: ''
  type: ChangeLog
  url: https://docs.newrelic.com/docs/release-notes/
- title: ''
  type: RateLimits
  url: https://docs.newrelic.com/docs/data-apis/manage-data/view-system-limits/
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/new-relic
- title: ''
  type: GitHubOrganization
  url: https://opensource.newrelic.com/
- title: ''
  type: YouTube
  url: https://www.youtube.com/@NewRelicInc
- title: ''
  type: JSON-LD
  url: json-ld/new-relic-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/new-relic-metric-payload-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/new-relic-event-payload-schema.json
- title: ''
  type: X
  url: https://twitter.com/newrelic
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/new-relic-inc-
- title: ''
  type: Security
  url: https://newrelic.com/security
- title: ''
  type: Security
  url: https://newrelic.com/security/compliance-certifications
- title: ''
  type: CLI
  url: https://github.com/newrelic/newrelic-cli
- title: ''
  type: CLI
  url: https://docs.newrelic.com/docs/new-relic-solutions/build-nr-ui/newrelic-cli/
- title: ''
  type: GitHubRepository
  url: https://registry.terraform.io/providers/newrelic/newrelic/latest/docs
- title: ''
  type: GitHubRepository
  url: https://github.com/newrelic/terraform-provider-newrelic
- title: ''
  type: Resources
  url: https://www.postman.com/new-relic/
- title: ''
  type: Documentation
  url: https://docs.newrelic.com/docs/apis/intro-apis/introduction-new-relic-apis/
- title: ''
  type: Documentation
  url: https://docs.newrelic.com/docs/nrql/get-started/introduction-nrql-new-relics-query-language/
- title: Java Agent
  type: SDK
  url: https://github.com/newrelic/newrelic-java-agent
- title: Python Agent
  type: SDK
  url: https://github.com/newrelic/newrelic-python-agent
- title: Node.js Agent
  type: SDK
  url: https://github.com/newrelic/node-newrelic
- title: Go Agent
  type: SDK
  url: https://github.com/newrelic/go-agent
- title: .NET Agent
  type: SDK
  url: https://github.com/newrelic/newrelic-dotnet-agent
- title: Ruby Agent
  type: SDK
  url: https://github.com/newrelic/newrelic-ruby-agent
- title: PHP Agent
  type: SDK
  url: https://github.com/newrelic/newrelic-php-agent
- title: ''
  type: SDK
  url: https://github.com/newrelic/infrastructure-agent
- title: ''
  type: GitHubRepository
  url: https://github.com/newrelic/helm-charts
- title: ''
  type: CodeExamples
  url: https://github.com/newrelic/newrelic-opentelemetry-examples
- title: ''
  type: SpectralRules
  url: rules/new-relic-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/new-relic-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/application-monitoring.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/full-stack-observability.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/telemetry-ingestion.yaml
created: '2025-01-13'
description: New Relic provides observability platform APIs for monitoring, analyzing, and optimizing your entire software stack with real-time insights into applications, infrastructure, and customer experience.
features:
- description: Monitor application performance with real-time metrics, error tracking, and transaction tracing across distributed systems.
  name: Application Performance Monitoring
- description: Monitor hosts, containers, cloud services, and on-premise infrastructure with automatic discovery and configuration.
  name: Infrastructure Monitoring
- description: Collect, search, and analyze log data at scale with structured logging, pattern detection, and correlation to traces and metrics.
  name: Log Management
- description: Trace requests across microservices and distributed systems to identify bottlenecks and optimize performance.
  name: Distributed Tracing
- description: Proactively monitor application availability and performance with scripted browser tests, API checks, and ping monitors.
  name: Synthetic Monitoring
- description: Capture real user experience data including page load times, JavaScript errors, and AJAX performance for web applications.
  name: Browser Monitoring
- description: Monitor mobile application performance, crashes, HTTP requests, and user interactions for iOS and Android apps.
  name: Mobile Monitoring
- description: Monitor network performance with flow data analysis, SNMP polling, and cloud network telemetry.
  name: Network Monitoring
- description: Monitor Kubernetes clusters, pods, containers, and workloads with automatic instrumentation and Pixie integration.
  name: Kubernetes Monitoring
- description: Monitor AWS Lambda, Azure Functions, and other serverless compute with invocation tracking and cold start analysis.
  name: Serverless Monitoring
- description: Use machine learning to detect anomalies, correlate incidents, and reduce alert noise with intelligent alerting.
  name: AIOps and Applied Intelligence
- description: Build custom dashboards with NRQL-powered charts, widgets, and real-time data visualization.
  name: Dashboards and Visualization
- description: Query all telemetry data with NRQL, a SQL-like query language for metrics, events, logs, and traces.
  name: NRQL Query Language
- description: Track, triage, and resolve application errors across the full stack with error grouping and assignment workflows.
  name: Errors Inbox
- description: Identify and prioritize security vulnerabilities in application dependencies and runtime environments.
  name: Vulnerability Management
- description: Define, track, and report on service level objectives and indicators to measure reliability.
  name: Service Level Management
- description: Track deployments and configuration changes to correlate performance shifts with code and infrastructure changes.
  name: Change Tracking
image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
integrations:
- description: Monitor AWS services including EC2, Lambda, RDS, S3, ECS, EKS, and CloudWatch with native integration.
  name: Amazon Web Services
- description: Monitor Azure services including VMs, App Service, Functions, AKS, and Azure Monitor with native integration.
  name: Microsoft Azure
- description: Monitor GCP services including Compute Engine, Cloud Functions, GKE, BigQuery, and Cloud Monitoring.
  name: Google Cloud Platform
- description: Monitor Kubernetes clusters with automatic discovery, Pixie integration, and OpenTelemetry support.
  name: Kubernetes
- description: Ingest Prometheus metrics using remote write or the Prometheus OpenMetrics integration.
  name: Prometheus
- description: Native OTLP endpoint support for ingesting metrics, traces, and logs from OpenTelemetry-instrumented applications.
  name: OpenTelemetry
- description: Provision and manage New Relic resources as code using the official Terraform provider.
  name: Terraform
- description: Query New Relic data from Grafana dashboards using the Grafana data source plugin.
  name: Grafana
- description: Send alert notifications to PagerDuty for incident management and on-call escalation.
  name: PagerDuty
- description: Receive alert notifications and share observability insights directly in Slack channels.
  name: Slack
- description: Create Jira issues from New Relic errors and alerts for issue tracking and resolution workflows.
  name: Jira
- description: Integrate with ServiceNow for ITSM workflows, incident creation, and change management.
  name: ServiceNow
- description: Connect repositories for code-level visibility, error linking, and deployment tracking via CodeStream.
  name: GitHub
- description: Monitor Docker containers with automatic instrumentation and container-level metrics.
  name: Docker
- description: Monitor Kafka clusters, topics, consumer groups, and message throughput.
  name: Apache Kafka
- description: Monitor MySQL database performance with query analysis, connection tracking, and replication metrics.
  name: MySQL
- description: Monitor PostgreSQL database performance with query analysis, index usage, and connection metrics.
  name: PostgreSQL
- description: Monitor MongoDB instances with query performance, replication status, and cluster metrics.
  name: MongoDB
- description: Monitor Redis instances with memory usage, command statistics, and key metrics.
  name: Redis
- description: Monitor Nginx web server performance with request rates, error rates, and upstream metrics.
  name: Nginx
jsonld:
- class_count: 0
  name: New Relic Context
  property_count: 88
  slug: new-relic-context
- class_count: 2
  name: New Relic Event Api Context
  property_count: 4
  slug: new-relic-event-api-context
- class_count: 0
  name: New Relic Event Context
  property_count: 3
  slug: new-relic-event-context
- class_count: 4
  name: New Relic Log Api Context
  property_count: 8
  slug: new-relic-log-api-context
- class_count: 0
  name: New Relic Log Context
  property_count: 5
  slug: new-relic-log-context
- class_count: 6
  name: New Relic Metric Api Context
  property_count: 12
  slug: new-relic-metric-api-context
- class_count: 0
  name: New Relic Metric Context
  property_count: 6
  slug: new-relic-metric-context
- class_count: 90
  name: New Relic Openapi Context
  property_count: 122
  slug: new-relic-openapi-context
- class_count: 6
  name: New Relic Trace Api Context
  property_count: 15
  slug: new-relic-trace-api-context
- class_count: 0
  name: New Relic Trace Context
  property_count: 6
  slug: new-relic-trace-context
layout: provider
modified: '2026-04-18'
name: New Relic
rules:
- name: New Relic API Rules
  rule_count: 21
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 1
  slug: new-relic-spectral-rules
skills: []
slug: new-relic
solutions: []
tags:
- Analysis
- Analytics
- APM
- DevOps
- Infrastructure
- Monitoring
- Observability
- Performance
- Platform
url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/apis.yml
use_cases:
- description: Gain unified visibility across applications, infrastructure, and digital experiences to quickly identify and resolve issues.
  name: Full-Stack Observability
- description: Monitor and validate cloud migration progress with baseline comparisons and performance tracking across hybrid environments.
  name: Cloud Migration Monitoring
- description: Integrate observability into development workflows with deployment markers, error tracking, and automated testing.
  name: DevOps and CI/CD Integration
- description: Define and track SLOs, manage error budgets, and implement reliability practices with data-driven insights.
  name: Site Reliability Engineering
- description: Detect, diagnose, and resolve incidents faster with correlated telemetry, anomaly detection, and automated workflows.
  name: Incident Response and Management
- description: Measure and optimize end-user experience across web, mobile, and synthetic channels.
  name: Digital Experience Monitoring
- description: Analyze resource utilization trends and forecast capacity needs to optimize infrastructure spending.
  name: Capacity Planning
- description: Maintain audit trails, security compliance, and data governance across observability data.
  name: Compliance and Audit
---
