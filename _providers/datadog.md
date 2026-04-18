---
api_count: 85
apis:
- description: The Datadog API is an HTTP REST API. The API uses resource-oriented URLs to call the API, uses status codes to indicate the success or failure of requests, returns JSON from all requests, and uses sta
  name: Datadog API
  slug: datadog-api
- description: The Metrics API allows you to post metrics data to be graphed on Datadog dashboards, query metrics from any time period as timeseries or scalar values, and modify tag configurations for metrics. It al
  name: Datadog Metrics API
  slug: datadog-metrics-api
- description: The Logs API allows you to search and send log events to the Datadog platform over HTTP. It supports querying and aggregating log data from the Log Management product.
  name: Datadog Logs API
  slug: datadog-logs-api
- description: The Event Management API allows you to programmatically post events to the Events Explorer and fetch events from the Events Explorer. Events represent notable changes or activity within your monitored
  name: Datadog Events API
  slug: datadog-events-api
- description: The Monitors API allows you to create, update, delete, and mute monitors that watch a metric or check and notify your team when a defined threshold has been exceeded.
  name: Datadog Monitors API
  slug: datadog-monitors-api
- description: The Dashboards API allows you to create, update, delete, and retrieve dashboards and dashboard lists. It also supports organizing, finding, and sharing dashboards with your team and organization.
  name: Datadog Dashboards API
  slug: datadog-dashboards-api
- description: The Incidents API allows you to manage incident response, as well as associated attachments, metadata, and todos. It also supports creating, updating, deleting, and retrieving services associated with
  name: Datadog Incidents API
  slug: datadog-incidents-api
- description: The Synthetics API allows you to manage API tests and browser tests programmatically. Datadog Synthetics uses simulated user requests and browser rendering to help ensure uptime, identify regional iss
  name: Datadog Synthetics API
  slug: datadog-synthetics-api
- description: The Service Level Objectives API provides a framework for defining clear targets around application performance. SLOs help teams provide a consistent customer experience, balance feature development w
  name: Datadog Service Level Objectives API
  slug: datadog-service-level-objectives-api
- description: The Security Monitoring API allows you to create and manage security rules, signals, and filters. It provides programmatic access to Datadog Cloud SIEM capabilities for threat detection and security s
  name: Datadog Security Monitoring API
  slug: datadog-security-monitoring-api
- description: The Service Definition API allows you to create, update, retrieve, and delete service definitions in the Datadog Service Catalog. It supports the v2.2 schema and earlier; for v3.0 schema use the Softw
  name: Datadog Service Definition API
  slug: datadog-service-definition-api
- description: The Software Catalog API allows you to create, update, retrieve, and delete Software Catalog entities using the v3.0 schema. It provides a unified catalog for tracking ownership, reliability, and perf
  name: Datadog Software Catalog API
  slug: datadog-software-catalog-api
- description: The Users API allows you to create, edit, and disable users within your Datadog organization. It supports role assignment and user management for access control purposes.
  name: Datadog Users API
  slug: datadog-users-api
- description: The Roles API is used to create and manage Datadog roles, the global permissions they grant, and which users belong to them. Roles provide role-based access control for Datadog resources and features.
  name: Datadog Roles API
  slug: datadog-roles-api
- description: The Key Management API allows you to manage your Datadog API and application keys. It provides endpoints to create, list, update, and delete both API keys and application keys for your organization.
  name: Datadog Key Management API
  slug: datadog-key-management-api
- description: The Organizations API allows you to create, edit, and manage your Datadog organizations. It supports multi-org account configurations where a parent organization manages one or more child organization
  name: Datadog Organizations API
  slug: datadog-organizations-api
- description: 'The Downtimes API gives you greater control over monitor notifications by allowing you to globally exclude scopes from alerting. Downtime settings can be scheduled with start and end times to prevent '
  name: Datadog Downtimes API
  slug: datadog-downtimes-api
- description: The RUM API allows you to manage Real User Monitoring applications and search or aggregate RUM events over HTTP. It provides access to session data, user interactions, and frontend performance metrics
  name: Datadog RUM API
  slug: datadog-rum-api
- description: The APM Retention Filters API allows you to manage configuration of APM retention filters for your organization. Retention filters control which traces are indexed and retained for analysis and requir
  name: Datadog APM Retention Filters API
  slug: datadog-apm-retention-filters-api
- description: The Usage Metering API allows you to get hourly, daily, and monthly usage across multiple facets of Datadog. It is available to all Pro and Enterprise customers, with usage data delayed by up to 72 ho
  name: Datadog Usage Metering API
  slug: datadog-usage-metering-api
- description: The Spans API allows you to search and aggregate spans from your Datadog platform over HTTP. It supports querying distributed tracing data collected by Datadog APM.
  name: Datadog Spans API
  slug: datadog-spans-api
- description: The Processes API allows you to query processes data for your organization. It provides access to live process information collected from hosts running the Datadog Agent.
  name: Datadog Processes API
  slug: datadog-processes-api
- description: The Teams API allows you to view and manage teams within Datadog. Teams can be associated with incidents, dashboards, and other resources to organize ownership and collaboration within your organizati
  name: Datadog Teams API
  slug: datadog-teams-api
- description: The Workflow Automation API allows you to automate end-to-end processes by connecting Datadog with the rest of your tech stack. It supports over 1,000 out-of-the-box actions including integrations wit
  name: Datadog Workflow Automation API
  slug: datadog-workflow-automation-api
- description: The Case Management API allows you to view and manage cases and projects within Datadog Case Management. Cases can be created from monitors, security signals, and other alert sources to track investig
  name: Datadog Case Management API
  slug: datadog-case-management-api
- description: The Observability Pipelines API allows you to collect and process logs within your own infrastructure and route them to downstream integrations. It provides programmatic management of pipeline configu
  name: Datadog Observability Pipelines API
  slug: datadog-observability-pipelines-api
- description: The Sensitive Data Scanner API allows you to create, update, delete, and retrieve sensitive data scanner groups and rules. It enables automated detection and redaction of sensitive data within logs, A
  name: Datadog Sensitive Data Scanner API
  slug: datadog-sensitive-data-scanner-api
- description: The AWS Integration API allows you to configure your Datadog-AWS integration directly through the Datadog API. It supports managing AWS accounts, metrics collection, and log forwarding configuration.
  name: Datadog AWS Integration API
  slug: datadog-aws-integration-api
- description: The GCP Integration API allows you to configure your Datadog-Google Cloud Platform integration directly through the Datadog API. It supports managing GCP projects, service accounts, and metrics collec
  name: Datadog GCP Integration API
  slug: datadog-gcp-integration-api
- description: The CI Visibility Pipelines API allows you to search or aggregate CI Visibility pipeline events and send them to your Datadog site over HTTP. It provides insight into the performance and reliability o
  name: Datadog CI Visibility Pipelines API
  slug: datadog-ci-visibility-pipelines-api
- description: The Network Device Monitoring API allows you to fetch devices and interfaces and their attributes. It provides programmatic access to network topology and performance data collected from network devic
  name: Datadog Network Device Monitoring API
  slug: datadog-network-device-monitoring-api
- description: The On-Call API allows you to configure and manage Datadog On-Call schedules, escalation policies, and teams. It also supports triggering and managing on-call pages directly through the Datadog API.
  name: Datadog On-Call API
  slug: datadog-on-call-api
- description: The DORA Metrics API allows you to search and send events for DORA Metrics to measure and improve software delivery performance. It tracks deployment frequency, lead time for changes, change failure r
  name: Datadog DORA Metrics API
  slug: datadog-dora-metrics-api
- description: The Cloud Cost Management API allows you to set up, edit, and delete Cloud Cost Management accounts for AWS and Azure. Cost data can be queried using the Metrics endpoint with the cloud_cost data sour
  name: Datadog Cloud Cost Management API
  slug: datadog-cloud-cost-management-api
- description: The Hosts API allows you to search for hosts by name, alias, or tag and retrieve host totals. Hosts live within the past 3 hours are included by default, with a retention of 7 days.
  name: Datadog Hosts API
  slug: datadog-hosts-api
- description: The Tags API allows you to assign tags to hosts, returning a mapping of tags to hosts for your entire infrastructure. Tags can be used to filter and group resources across Datadog.
  name: Datadog Tags API
  slug: datadog-tags-api
- description: The Containers API allows you to get all containers for your organization. It provides programmatic access to container data collected from hosts running the Datadog Agent.
  name: Datadog Containers API
  slug: datadog-containers-api
- description: The Container Images API allows you to get all container images for your organization. It provides visibility into the container images running across your infrastructure.
  name: Datadog Container Images API
  slug: datadog-container-images-api
- description: The Notebooks API allows you to interact with Datadog Notebooks programmatically. Notebooks combine graphs and text in a linear, cell-based layout for exploring and sharing stories with your data.
  name: Datadog Notebooks API
  slug: datadog-notebooks-api
- description: The Dashboard Lists API allows you to interact with dashboard lists through the API to organize, find, and share all of your dashboards with your team and organization.
  name: Datadog Dashboard Lists API
  slug: datadog-dashboard-lists-api
- description: The Logs Pipelines API allows you to manage pipelines and processors that operate on incoming logs, parsing and transforming them into structured attributes for easier querying.
  name: Datadog Logs Pipelines API
  slug: datadog-logs-pipelines-api
- description: The Logs Indexes API allows you to manage configuration of log indexes for your organization. Log indexes define how logs are filtered, aggregated, and stored for retention and querying.
  name: Datadog Logs Indexes API
  slug: datadog-logs-indexes-api
- description: The Logs Metrics API allows you to manage configuration of log-based metrics for your organization. It provides the ability to generate metrics from log data for cost-effective long-term analysis.
  name: Datadog Logs Metrics API
  slug: datadog-logs-metrics-api
- description: The Logs Archives API allows you to manage logs archives that forward all ingested logs to cloud storage systems. It supports configuration of archive destinations and rehydration settings.
  name: Datadog Logs Archives API
  slug: datadog-logs-archives-api
- description: The Logs Custom Destinations API allows you to manage custom destinations that forward all ingested logs to external destinations such as Elasticsearch, Microsoft Sentinel, and HTTP endpoints.
  name: Datadog Logs Custom Destinations API
  slug: datadog-logs-custom-destinations-api
- description: The Logs Restriction Queries API allows you to manage restriction queries that control which logs the logs_read_data permission grants read access to, enabling fine-grained log access control by role.
  name: Datadog Logs Restriction Queries API
  slug: datadog-logs-restriction-queries-api
- description: The Spans Metrics API allows you to manage configuration of span-based metrics for your organization. It provides the ability to generate metrics from spans for cost-effective long-term analysis of AP
  name: Datadog Spans Metrics API
  slug: datadog-spans-metrics-api
- description: The Service Checks API allows you to submit a list of service checks to Datadog. Service checks can be submitted up to 10 minutes in the past and are used to monitor the status of services.
  name: Datadog Service Checks API
  slug: datadog-service-checks-api
- description: The Snapshots API allows you to take graph snapshots. Snapshots are PNG images generated by rendering a specified widget and capturing it once the data is available.
  name: Datadog Snapshots API
  slug: datadog-snapshots-api
- description: The IP Ranges API provides a list of IP prefixes belonging to Datadog. It returns available prefix information for Agent, API, and APM endpoints along with IPv4 and IPv6 prefixes.
  name: Datadog IP Ranges API
  slug: datadog-ip-ranges-api
- description: The IP Allowlist API is used to manage the IP addresses that can access the Datadog API and web UI. It allows you to configure IP address restrictions for your organization.
  name: Datadog IP Allowlist API
  slug: datadog-ip-allowlist-api
- description: The Audit API allows you to search your Audit Logs events over HTTP. It returns Audit Logs events that match an audit search query, providing visibility into actions taken within your organization.
  name: Datadog Audit API
  slug: datadog-audit-api
- description: The APM API provides endpoints for working with Application Performance Monitoring services and tracing data. It supports querying service-level metrics and trace data collected by Datadog APM.
  name: Datadog APM API
  slug: datadog-apm-api
- description: The Webhooks Integration API allows you to configure the Datadog-Webhooks integration directly through the Datadog API. It supports creating, updating, and deleting webhook endpoints and custom variab
  name: Datadog Webhooks Integration API
  slug: datadog-webhooks-integration-api
- description: The SLO Corrections API allows you to create, update, and delete corrections for Service Level Objectives. SLO corrections adjust SLO status calculations to account for planned maintenance or known is
  name: Datadog SLO Corrections API
  slug: datadog-slo-corrections-api
- description: The AWS Logs Integration API allows you to configure log collection from AWS services and manage your Datadog-AWS Logs integration. It supports listing and managing AWS log collection configurations.
  name: Datadog AWS Logs Integration API
  slug: datadog-aws-logs-integration-api
- description: The Azure Integration API allows you to configure your Datadog-Azure integration directly through the Datadog API. It supports managing Azure tenants, host filters, and metrics collection settings.
  name: Datadog Azure Integration API
  slug: datadog-azure-integration-api
- description: The Slack Integration API allows you to configure your Datadog-Slack integration directly through the Datadog API. It supports managing Slack channels for monitor notifications and alerts.
  name: Datadog Slack Integration API
  slug: datadog-slack-integration-api
- description: The PagerDuty Integration API allows you to configure your Datadog-PagerDuty integration directly through the Datadog API. It supports managing PagerDuty services and scheduling configurations.
  name: Datadog PagerDuty Integration API
  slug: datadog-pagerduty-integration-api
- description: The Opsgenie Integration API allows you to configure your Datadog-Opsgenie integration directly through the Datadog API. It supports managing Opsgenie services and alert routing.
  name: Datadog Opsgenie Integration API
  slug: datadog-opsgenie-integration-api
- description: The Cloudflare Integration API allows you to manage your Datadog-Cloudflare integration directly through the Datadog API. It supports listing and managing Cloudflare accounts and their associated reso
  name: Datadog Cloudflare Integration API
  slug: datadog-cloudflare-integration-api
- description: The Fastly Integration API allows you to manage your Datadog-Fastly integration accounts and services directly through the Datadog API. It supports listing and managing Fastly accounts.
  name: Datadog Fastly Integration API
  slug: datadog-fastly-integration-api
- description: The Confluent Cloud API allows you to manage your Datadog-Confluent Cloud integration accounts and account resources directly through the Datadog API. It supports monitoring Kafka clusters and related
  name: Datadog Confluent Cloud API
  slug: datadog-confluent-cloud-api
- description: The Okta Integration API allows you to configure your Datadog-Okta integration directly through the Datadog API. It supports listing and managing Okta accounts and their configurations.
  name: Datadog Okta Integration API
  slug: datadog-okta-integration-api
- description: The Microsoft Teams Integration API allows you to configure your Datadog-Microsoft Teams integration directly through the Datadog API. It supports managing Teams channels for notifications and alerts.
  name: Datadog Microsoft Teams Integration API
  slug: datadog-microsoft-teams-integration-api
- description: The Jira Integration API allows you to configure your Datadog-Jira integration directly through the Datadog API. It supports managing Jira issue templates and project configurations.
  name: Datadog Jira Integration API
  slug: datadog-jira-integration-api
- description: The Error Tracking API allows you to search issues within your organization programmatically. It returns a list of issues that match a given search query using event search syntax.
  name: Datadog Error Tracking API
  slug: datadog-error-tracking-api
- description: The Application Security API provides protection against application-level attacks that aim to exploit code-level vulnerabilities such as SSRF, SQL injection, Log4Shell, and XSS.
  name: Datadog Application Security API
  slug: datadog-application-security-api
- description: The CSM Threats API provides endpoints for managing Cloud Security Management Workload Protection agent rules. It monitors file, network, and process activity to detect real-time threats to your infra
  name: Datadog CSM Threats API
  slug: datadog-csm-threats-api
- description: The CSM Agents API allows you to get the list of all Cloud Security Management agents running on your hosts and containers. It provides visibility into agent coverage across your infrastructure.
  name: Datadog CSM Agents API
  slug: datadog-csm-agents-api
- description: The Service Scorecards API allows you to create and manage scorecard rules and outcomes. Scorecards help formalize your organization's best practices and track service compliance against defined crite
  name: Datadog Service Scorecards API
  slug: datadog-service-scorecards-api
- description: The Service Dependencies API allows you to get a list of services from APM and their dependencies. Services are filtered by environment and primary tag to map your service topology.
  name: Datadog Service Dependencies API
  slug: datadog-service-dependencies-api
- description: The Powerpack API allows you to create, update, delete, and retrieve Powerpacks. Powerpacks are templated groups of dashboard widgets that scale graphing expertise as reusable building blocks.
  name: Datadog Powerpack API
  slug: datadog-powerpack-api
- description: The Embeddable Graphs API allows you to create and manage embeddable graph snapshots that can be shared outside of Datadog. It supports creating, revoking, and listing embeddable graphs.
  name: Datadog Embeddable Graphs API
  slug: datadog-embeddable-graphs-api
- description: The RUM Metrics API allows you to manage configuration of RUM-based metrics for your organization. It provides the ability to generate metrics from Real User Monitoring data.
  name: Datadog RUM Metrics API
  slug: datadog-rum-metrics-api
- description: The Domain Allowlist API allows you to manage the email domain allowlist for your organization. It supports getting and updating the list of allowed email domains.
  name: Datadog Domain Allowlist API
  slug: datadog-domain-allowlist-api
- description: The Restriction Policies API allows you to manage restriction policies associated with Datadog resources including dashboards, notebooks, security rules, SLOs, workflows, and more.
  name: Datadog Restriction Policies API
  slug: datadog-restriction-policies-api
- description: The AuthN Mappings API is used to automatically map groups of users to roles in Datadog using attributes sent from Identity Providers. It enables federated authentication to role mapping.
  name: Datadog AuthN Mappings API
  slug: datadog-authn-mappings-api
- description: The Integrations API allows you to manage Datadog integrations programmatically. It provides endpoints for configuring and managing third-party service integrations within your organization.
  name: Datadog Integrations API
  slug: datadog-integrations-api
- description: The CI Visibility Tests API allows you to search or aggregate CI Visibility test events over HTTP. It provides insight into the performance and reliability of your test suites.
  name: Datadog CI Visibility Tests API
  slug: datadog-ci-visibility-tests-api
- description: The Agentless Scanning API provides visibility into risks and vulnerabilities within your hosts, running containers, and serverless functions without requiring teams to install Agents.
  name: Datadog Agentless Scanning API
  slug: datadog-agentless-scanning-api
- description: The Static Analysis API provides access to static analysis and dependency scanning results. It supports querying code analysis data for your organization.
  name: Datadog Static Analysis API
  slug: datadog-static-analysis-api
- description: The Entity Risk Scores API provides security risk assessments for entities like cloud resources, identities, or services based on detected signals, misconfigurations, and identity risks.
  name: Datadog Entity Risk Scores API
  slug: datadog-entity-risk-scores-api
- description: The API Management API allows you to create and manage APIs from OpenAPI specifications. It supports the Datadog API Catalog for tracking API performance, security, and ownership.
  name: Datadog API Management API
  slug: datadog-api-management-api
- description: The Cloud Workload Security API provides endpoints for managing workload protection rules and agent configurations. It monitors file, network, and process activity to detect real-time threats.
  name: Datadog Cloud Workload Security API
  slug: datadog-cloud-workload-security-api
capabilities:
- description: Unified workflow for incident management combining incidents, events, and monitors. Used by incident commanders and on-call engineers for creating incidents, correlating events, and managing monitor a
  name: Datadog Incident Management
  slug: incident-management
- description: Unified workflow for log analytics combining logs and events. Used by platform engineers and developers for submitting, searching, and aggregating logs alongside event correlation.
  name: Datadog Log Analytics
  slug: log-analytics
- description: Unified workflow for infrastructure monitoring and alerting combining monitors, metrics, hosts, and dashboards. Used by SREs and DevOps engineers for setting up alerts, querying metrics, tracking host
  name: Datadog Monitoring And Alerting
  slug: monitoring-and-alerting
- description: Unified workflow for synthetic testing combining synthetics concurrency management and monitors. Used by QA engineers and SREs for managing synthetic test execution capacity and monitoring test result
  name: Datadog Synthetic Testing
  slug: synthetic-testing
common:
- title: ''
  type: Website
  url: https://www.datadoghq.com/
- title: ''
  type: Portal
  url: https://docs.datadoghq.com/api/
- title: ''
  type: Documentation
  url: https://docs.datadoghq.com/
- title: ''
  type: Authentication
  url: https://docs.datadoghq.com/api/latest/authentication/
- title: ''
  type: GitHubOrganization
  url: https://github.com/DataDog
- title: ''
  type: Blog
  url: https://www.datadoghq.com/blog/
- title: ''
  type: Support
  url: https://www.datadoghq.com/support/
- title: ''
  type: StatusPage
  url: https://status.datadoghq.com/
- title: ''
  type: Pricing
  url: https://www.datadoghq.com/pricing/
- title: ''
  type: Login
  url: https://app.datadoghq.com/
- title: ''
  type: SignUp
  url: https://www.datadoghq.com/free-datadog-trial/
- title: ''
  type: JSON-LD
  url: json-ld/datadog-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/datadog-metric-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/datadog-monitor-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/datadog-log-event-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/datadog-event-schema.json
- title: ''
  type: Products
  url: https://www.datadoghq.com/product/
- title: ''
  type: Customers
  url: https://www.datadoghq.com/customers/
- title: ''
  type: Pricing
  url: https://www.datadoghq.com/pricing/
- title: ''
  type: About
  url: https://www.datadoghq.com/about/leadership/
- title: ''
  type: Blog
  url: https://www.datadoghq.com/blog/
- title: ''
  type: Login
  url: https://app.datadoghq.com/account/login
- title: ''
  type: Login
  url: https://app.datadoghq.com/account/login
- title: ''
  type: Login
  url: https://app.datadoghq.com/account/login
- title: ''
  type: SignUp
  url: https://us5.datadoghq.com/signup
- title: ''
  type: Support
  url: https://www.datadoghq.com/support/
- title: ''
  type: Certifications
  url: https://www.datadoghq.com/certification/overview/
- title: ''
  type: PrivacyPolicy
  url: https://www.datadoghq.com/privacy/
- title: ''
  type: Security
  url: https://www.datadoghq.com/security/
- title: ''
  type: Trust
  url: https://trust.datadoghq.com/
- title: ''
  type: Partners
  url: https://www.datadoghq.com/partner/network/
- title: ''
  type: Documentation
  url: https://docs.datadoghq.com/
- title: ''
  type: Portal
  url: https://docs.datadoghq.com/api/latest/
- title: ''
  type: GettingStarted
  url: https://docs.datadoghq.com/getting_started/
- title: ''
  type: Authentication
  url: https://docs.datadoghq.com/api/latest/authentication/
- title: ''
  type: StatusPage
  url: https://status.datadoghq.com/
- title: ''
  type: GitHub Organization
  url: https://github.com/DataDog
- title: ''
  type: RateLimits
  url: https://docs.datadoghq.com/api/latest/rate-limits/
- title: ''
  type: Developer Portal
  url: https://docs.datadoghq.com/developers/
- title: ''
  type: SDKs
  url: https://docs.datadoghq.com/developers/libraries/
- title: ''
  type: TermsOfService
  url: https://www.datadoghq.com/legal/terms/
- title: ''
  type: Agent
  url: https://docs.datadoghq.com/agent/
- title: ''
  type: Community
  url: https://community.datadoghq.com/
- title: ''
  type: Authorization Scopes
  url: https://docs.datadoghq.com/api/latest/scopes/
- title: ''
  type: Using the API
  url: https://docs.datadoghq.com/api/latest/using-the-api/
- title: ''
  type: Learning Center
  url: https://learn.datadoghq.com/
- title: ''
  type: Events
  url: https://www.datadoghq.com/events-webinars/
- title: ''
  type: Marketplace
  url: https://www.datadoghq.com/marketplacepartners/
- title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/datadog/datadog-s-public-workspace/overview
- title: ''
  type: GettingStarted
  url: https://docs.datadoghq.com/getting_started/api/
- title: ''
  type: Learning Resources
  url: https://www.datadoghq.com/learn/
created: 2024/04/14
description: Datadog is a monitoring and analytics platform that helps organizations gain insight into their infrastructure, applications, and services. It allows users to collect, visualize, and analyze real-time data from a variety of sources, including servers, databases, and cloud services. Datadog's platform enables companies to track performance metrics, troubleshoot issues, and optimize their systems for peak efficiency.
features:
- description: Monitor servers, containers, databases, and cloud services with real-time metrics and dashboards.
  name: Infrastructure Monitoring
- description: Trace requests across microservices with application performance monitoring.
  name: APM and Distributed Tracing
- description: Collect, process, and analyze logs from any source with full-text search and analytics.
  name: Log Management
- description: Monitor front-end application performance and user experience in real time.
  name: Real User Monitoring (RUM)
- description: Proactive monitoring with API tests, browser tests, and multi-step workflows.
  name: Synthetic Monitoring
- description: Detect threats and misconfigurations across infrastructure and applications.
  name: Security Monitoring
- description: Build custom dashboards with drag-and-drop widgets for metrics, logs, and traces.
  name: Dashboards
- description: Configure monitors and alerts with thresholds, anomaly detection, and notifications.
  name: Alerting
- description: Manage incident response workflows with timeline, notifications, and postmortems.
  name: Incidents
- description: Define and track SLOs with error budget monitoring and alerting.
  name: Service Level Objectives
- description: Monitor CI/CD pipeline performance, test results, and deployment tracking.
  name: CI/CD Visibility
- description: Track and optimize cloud infrastructure costs across providers.
  name: Cloud Cost Management
image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
integrations:
- description: Native integration with 80+ AWS services for metrics, logs, and traces.
  name: AWS
- description: Container orchestration monitoring with cluster, pod, and node visibility.
  name: Kubernetes
- description: Infrastructure-as-code management of Datadog monitors, dashboards, and alerts.
  name: Terraform
- description: Alert notifications and incident management within Slack channels.
  name: Slack
- description: Incident escalation and on-call management integration.
  name: PagerDuty
- description: Create Jira tickets from Datadog alerts and incidents.
  name: Jira
jsonld:
- class_count: 60
  name: Datadog Context
  property_count: 106
  slug: datadog-context
layout: provider
modified: '2026-04-17'
name: Datadog
rules:
- name: Datadog API Rules
  rule_count: 19
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 3
  slug: datadog-spectral-rules
skills: []
slug: datadog
solutions:
- description: Infrastructure monitoring with 800+ integrations for servers, containers, and cloud.
  name: Datadog Infrastructure
- description: Application performance monitoring with distributed tracing and profiling.
  name: Datadog APM
- description: Log management with indexing, archiving, and analytics.
  name: Datadog Logs
- description: Cloud security posture management and threat detection.
  name: Datadog Security
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/apis.yml
use_cases:
- description: Correlate metrics, traces, and logs across the entire application stack.
  name: Full-Stack Observability
- description: Monitor Kubernetes, Docker, and container orchestration platforms.
  name: Container Monitoring
- description: Monitor AWS, Azure, GCP, and hybrid cloud environments.
  name: Cloud Infrastructure Monitoring
- description: Identify and resolve application bottlenecks with distributed tracing.
  name: Application Performance Management
- description: Centralize and analyze logs for troubleshooting and compliance.
  name: Log Analytics
- description: Automate incident detection, response, and resolution workflows.
  name: Incident Management
- description: Integrate monitoring into CI/CD pipelines with API-driven workflows.
  name: DevOps Automation
- description: Monitor cloud security misconfigurations and compliance violations.
  name: Security Posture Management
---
