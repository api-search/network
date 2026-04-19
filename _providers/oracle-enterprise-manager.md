---
api_count: 17
apis:
- description: 'REST API for Oracle Enterprise Manager Cloud Control providing access to monitoring, configuration, and administration capabilities including targets, metrics, incidents, blackouts, credentials, user '
  name: Oracle Enterprise Manager Cloud Control REST API
  slug: ''
- description: 'Command-line interface providing scriptable access to Enterprise Manager functionality including target management, job operations, patching, provisioning, and administration tasks through verbs that '
  name: Enterprise Manager Command Line Interface (EM CLI)
  slug: ''
- description: API for creating, managing, and monitoring Enterprise Manager jobs and tasks including scheduling, execution tracking, and deployment procedures.
  name: Enterprise Manager Job System API
  slug: ''
- description: API for accessing performance metrics, monitoring data, and alerting information including numeric metric data points over time, latest metric values, and metric group metadata.
  name: Enterprise Manager Metric and Monitoring API
  slug: ''
- description: API for managing monitored targets including discovery, configuration, lifecycle operations, bulk property updates, and target type metadata.
  name: Enterprise Manager Target Management API
  slug: ''
- description: REST API for searching, viewing, and managing incidents and events in Enterprise Manager, including clearing, suppressing, unsuppressing incidents, viewing member events, and managing annotations.
  name: Enterprise Manager Incidents and Events API
  slug: ''
- description: REST API for managing blackouts (maintenance windows) in Enterprise Manager, including creating, editing, deleting, listing, and stopping blackouts, managing blackout reasons, and retrieving targets i
  name: Enterprise Manager Blackout Management API
  slug: ''
- description: REST API for managing named credentials, monitoring credentials, and preferred credentials in Enterprise Manager, including creating, listing, deleting, updating, testing, and searching credential typ
  name: Enterprise Manager Credentials Management API
  slug: ''
- description: 'REST API for managing Enterprise Manager users and roles, including creating, modifying, and deleting users and roles, managing privilege grants and role assignments, and listing secure resources and '
  name: Enterprise Manager User Management API
  slug: ''
- description: REST API for database maintenance operations including updates, upgrades, and patching, with support for creating and managing Gold Images, patch recommendations, compliance reporting, and Fleet Patch
  name: Enterprise Manager Database Patching and Maintenance API
  slug: ''
- description: REST API for managing deployment procedures including creating, submitting, and deleting procedures, managing procedure instances with resume, suspend, stop, and retry operations, and tracking executi
  name: Enterprise Manager Deployment Procedure API
  slug: ''
- description: REST API for configuring and managing database backup settings, fleet-level backup configuration, and scheduling backup operations in Enterprise Manager.
  name: Enterprise Manager Database Backup Management API
  slug: ''
- description: REST API for managing Oracle Zero Data Loss Recovery Appliance (ZDLRA) including adding and removing protected databases, creating and managing protection policies, creating archival backups, and retr
  name: Enterprise Manager ZDLRA Management API
  slug: ''
- description: REST API for executing SQL queries against database targets monitored by Enterprise Manager and against the Enterprise Manager repository, enabling custom data extraction for dashboards and KPI report
  name: Enterprise Manager SQL Execution REST API
  slug: ''
- description: REST API for managing Oracle Data Guard configurations in Enterprise Manager, enabling high availability operations including switchover, failover, and standby database management.
  name: Enterprise Manager Data Guard Administration REST API
  slug: ''
- description: REST APIs for Database as a Service (DBaaS) operations enabling self-service database provisioning, request management, and quota administration through Enterprise Manager Cloud Control.
  name: Enterprise Manager Cloud APIs (DBaaS)
  slug: ''
- description: Extensibility Development Kit providing tools, utilities, and APIs for developing Enterprise Manager plug-ins to extend platform capabilities for custom target monitoring and management.
  name: Enterprise Manager Extensibility Development Kit (EDK) API
  slug: ''
capabilities:
- description: 'Unified workflow for monitoring, incident response, and maintenance management across Oracle infrastructure using Enterprise Manager Cloud Control APIs. Designed for infrastructure administrators and '
  name: Oracle Enterprise Manager Infrastructure Management
  slug: infrastructure-management
common:
- title: ''
  type: Portal
  url: https://www.oracle.com/enterprise-manager/
- title: ''
  type: Documentation
  url: https://docs.oracle.com/en/enterprise-manager/
- title: ''
  type: Support
  url: https://www.oracle.com/support/
- title: ''
  type: Pricing
  url: https://www.oracle.com/enterprise-manager/pricing.html
- title: ''
  type: Blog
  url: https://blogs.oracle.com/oem/
- title: ''
  type: Training
  url: https://education.oracle.com/enterprise-manager
- title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/index.html
- title: ''
  type: ReleaseNotes
  url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrel/cloud-control-release-notes-emrel.html
- title: ''
  type: ChangeLog
  url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emcon/new-features-release-update.html
- title: ''
  type: Security
  url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emsec/index.html
- title: ''
  type: Resources
  url: https://www.oracle.com/enterprise-manager/technologies/
created: '2024-01-01'
description: Oracle Enterprise Manager (OEM) provides a comprehensive management platform for managing Oracle IT infrastructure and applications. The APIs enable programmatic access to monitoring, administration, and automation capabilities.
features:
- description: Monitor Oracle databases, hosts, middleware, and custom applications with configurable metrics, thresholds, and alerting.
  name: Target Monitoring
- description: Correlate events into actionable incidents with severity, priority, escalation, and automated notification workflows.
  name: Incident Management
- description: Schedule maintenance windows to suppress monitoring alerts during planned downtime without losing data collection.
  name: Blackout Management
- description: Automate database patching, upgrades, and fleet maintenance with Gold Images and compliance reporting.
  name: Database Lifecycle Management
- description: Create and manage multi-step deployment workflows for provisioning, patching, and configuration changes.
  name: Deployment Procedures
- description: Enable Database as a Service with self-service provisioning, quota management, and request workflows.
  name: Cloud Self-Service
image: /assets/icons/oracle-enterprise-manager.png
integrations:
- description: Visualize Enterprise Manager metrics in Grafana dashboards using the OEM data source plugin.
  name: Grafana
- description: Extend monitoring to OCI resources and hybrid cloud environments through unified management.
  name: Oracle Cloud Infrastructure
- description: Forward incidents to ServiceNow for ITSM integration and automated ticket creation.
  name: ServiceNow
jsonld:
- class_count: 0
  name: Oracle Enterprise Manager Cloud Control Context
  property_count: 0
  slug: oracle-enterprise-manager-cloud-control-context
- class_count: 9
  name: Oracle Enterprise Manager Context
  property_count: 13
  slug: oracle-enterprise-manager-context
layout: provider
modified: '2026-04-18'
name: Oracle Enterprise Manager
rules:
- name: Oracle Enterprise Manager API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: oracle-enterprise-manager-spectral-rules
skills: []
slug: oracle-enterprise-manager
solutions: []
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
url: https://raw.githubusercontent.com/api-evangelist/oracle-enterprise-manager/refs/heads/main/apis.yml
use_cases:
- description: Centralized monitoring of Oracle databases, hosts, middleware, and applications with real-time metrics and alerting.
  name: Infrastructure Monitoring
- description: Fleet-level database patching using Gold Images with compliance validation and rollback capabilities.
  name: Automated Patching
- description: Detect, triage, and resolve infrastructure issues using correlated incidents with annotations and escalation.
  name: Incident Response
- description: Analyze metric trends over time to forecast resource needs and optimize infrastructure utilization.
  name: Capacity Planning
---
