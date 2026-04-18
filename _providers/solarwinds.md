---
api_count: 13
apis:
- description: 'RESTful API for managing and monitoring network devices, servers, and applications through the Orion Platform. Provides access to the SolarWinds Information Service (SWIS) using SWQL queries via REST '
  name: SolarWinds Orion API
  slug: solarwinds-orion-api
- description: API for IT service management, ticketing, and help desk operations. Provides CRUD access to incidents, service requests, changes, problems, releases, and asset management resources.
  name: SolarWinds Service Desk API
  slug: solarwinds-service-desk-api
- description: Cloud-native observability API for logs, metrics, and distributed tracing.
  name: SolarWinds Observability API
  slug: solarwinds-observability-api
- description: API for database monitoring and performance analysis.
  name: SolarWinds Database Performance Analyzer API
  slug: solarwinds-dpa-api
- description: Network Performance Monitor REST API for network device monitoring.
  name: SolarWinds NPM REST API
  slug: solarwinds-npm-rest-api
- description: REST API for creating, reading, updating, and deleting data in Web Help Desk including tickets, clients, assets, and locations.
  name: SolarWinds Web Help Desk API
  slug: solarwinds-whd-api
- description: API for website uptime monitoring, performance monitoring, and transaction checks enabling automated management of checks, contacts, and reporting. Uses Bearer Token authentication for secure API acce
  name: SolarWinds Pingdom API
  slug: solarwinds-pingdom-api
- description: RESTful API for cloud-based log management including event submission, event retrieval, search, and account management. Supports sending events over HTTP/S and retrieving log data via paginating event
  name: SolarWinds Loggly API
  slug: solarwinds-loggly-api
- description: HTTP API for cloud-based log management including searching logs, managing systems, groups, saved searches, and user accounts. Provides endpoints for log search, settings management, and system config
  name: SolarWinds Papertrail API
  slug: solarwinds-papertrail-api
- description: API for IP address management providing CRUD operations for subnets, IP addresses, and DNS entries through the SolarWinds Information Service.
  name: SolarWinds IPAM API
  slug: solarwinds-ipam-api
- description: API for network configuration management providing automation of configuration backups, change management, and compliance through the SolarWinds Information Service.
  name: SolarWinds NCM API
  slug: solarwinds-ncm-api
- description: Server and Application Monitor API for monitoring application health and performance using the API Poller feature and SolarWinds Information Service.
  name: SolarWinds SAM API
  slug: solarwinds-sam-api
- description: REST API for application performance monitoring providing CRUD access to metrics, dashboards, alerts, and traces. Supports custom metrics submission and distributed tracing for cloud-native applicatio
  name: SolarWinds AppOptics API
  slug: solarwinds-appoptics-api
capabilities:
- description: Workflow for monitoring network infrastructure and website uptime combining Orion Platform SWQL queries with Pingdom synthetic monitoring for network and IT operations teams.
  name: SolarWinds Infrastructure Monitoring
  slug: infrastructure-monitoring
- description: Workflow for IT service management combining Service Desk incident/change management with Orion infrastructure data for IT support and service delivery teams.
  name: SolarWinds IT Service Management
  slug: it-service-management
- description: Workflow for centralized log management combining Loggly cloud log aggregation with Papertrail log search and system management for DevOps and operations teams.
  name: SolarWinds Log Management
  slug: log-management
common:
- title: ''
  type: Portal
  url: https://www.solarwinds.com
- title: ''
  type: Documentation
  url: https://documentation.solarwinds.com
- title: ''
  type: Support
  url: https://support.solarwinds.com
- title: ''
  type: Blog
  url: https://www.solarwinds.com/blog
- title: ''
  type: GitHubOrganization
  url: https://github.com/solarwinds
- title: ''
  type: StatusPage
  url: https://status.solarwinds.com
- title: ''
  type: PrivacyPolicy
  url: https://www.solarwinds.com/legal/privacy
- title: ''
  type: TermsOfService
  url: https://www.solarwinds.com/legal/terms
- title: ''
  type: Login
  url: https://customerportal.solarwinds.com
- title: ''
  type: Security
  url: https://www.solarwinds.com/information-security
- title: ''
  type: X
  url: https://twitter.com/solarwinds
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/solarwinds
- title: ''
  type: SDK
  url: https://github.com/solarwinds/OrionSDK
- title: ''
  type: CLI
  url: https://github.com/solarwinds/OrionSDK/tree/master/Samples/PowerShell
- title: ''
  type: JSONLD
  url: json-ld/solarwinds-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/solarwinds-node-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/solarwinds-alert-schema.json
created: '2024-01-15'
description: A collection of APIs provided by SolarWinds for IT infrastructure management, monitoring, and observability.
features:
- Network Device Monitoring via SWIS/SWQL
- IT Service Management and Ticketing
- Cloud-Native Observability (Logs, Metrics, Traces)
- Website Uptime and Synthetic Monitoring
- Cloud-Based Log Aggregation and Search
- Database Performance Analysis
- IP Address Management
- Network Configuration Compliance
image: https://www.solarwinds.com/sites/all/themes/solarwinds_theme/logo.png
integrations:
- Slack
- PagerDuty
- Microsoft Teams
- ServiceNow
- Jira
- AWS CloudWatch
- Azure Monitor
- Splunk
jsonld:
- class_count: 0
  name: Solarwinds Context
  property_count: 5
  slug: solarwinds-context
- class_count: 0
  name: Solarwinds Loggly Context
  property_count: 0
  slug: solarwinds-loggly-context
- class_count: 0
  name: Solarwinds Orion Context
  property_count: 0
  slug: solarwinds-orion-context
- class_count: 0
  name: Solarwinds Papertrail Context
  property_count: 0
  slug: solarwinds-papertrail-context
- class_count: 0
  name: Solarwinds Pingdom Context
  property_count: 0
  slug: solarwinds-pingdom-context
- class_count: 0
  name: Solarwinds Service Desk Context
  property_count: 0
  slug: solarwinds-service-desk-context
layout: provider
modified: '2026-04-18'
name: SolarWinds
rules:
- name: SolarWinds API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: solarwinds-spectral-rules
skills: []
slug: solarwinds
solutions: []
tags:
- Application Monitoring
- Database Monitoring
- Infrastructure
- IP Address Management
- IT Management
- ITSM
- Log Management
- Network Monitoring
- Observability
url: https://www.solarwinds.com/apis.json
use_cases:
- Network Infrastructure Monitoring and Alerting
- IT Incident Management and Ticketing Workflows
- Cloud Application Performance Monitoring
- Centralized Log Management and Search
- Website and API Uptime Monitoring
- Database Query Performance Tuning
---
