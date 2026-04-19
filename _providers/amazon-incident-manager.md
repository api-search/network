---
api_count: 1
apis:
- description: The AWS Systems Manager Incident Manager API provides programmatic access to create and manage response plans, incidents, timelines, related items, and replication sets for automated incident response
  name: AWS Systems Manager Incident Manager API
  slug: aws-ssm-incidents-api
capabilities:
- description: Unified capability for operations teams to manage incident response plans, respond to active incidents, update timelines, and coordinate responders.
  name: Amazon Incident Manager - Incident Response
  slug: incident-response
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/systems-manager/features/#Incident_Manager
- title: ''
  type: Website
  url: https://aws.amazon.com/systems-manager/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/incident-manager/
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
  url: https://aws.amazon.com/blogs/mt/tag/aws-systems-manager-incident-manager/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/systems-manager/incidents/
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
  url: rules/amazon-incident-manager-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/ssm-incidents.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/incident-response.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-incident-manager-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-incident-manager-context.jsonld
created: '2026-03-16'
description: AWS Systems Manager Incident Manager is an incident management console designed to help users mitigate and recover from incidents affecting their AWS-hosted applications. It enables faster incident resolution by automating response plans and engaging responders across notification channels.
features:
- description: Create response plans that automatically engage responders and execute runbooks when incidents occur.
  name: Automated Response Plans
- description: Track incident status, severity, and timeline in real time from a centralized console.
  name: Incident Tracking
- description: Notify responders via SMS, email, voice, and PagerDuty through contact channels.
  name: Multi-Channel Notifications
- description: Automatically run Systems Manager Automation runbooks as part of incident response.
  name: Runbook Automation
- description: Generate analysis reports with timeline events to identify root causes and improve future response.
  name: Post-Incident Analysis
- description: Replicate incident data across multiple AWS regions for global incident management.
  name: Multi-Region Replication
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Trigger incident response plans automatically from CloudWatch alarms.
  name: Amazon CloudWatch
- description: Run automation runbooks as part of incident response workflows.
  name: AWS Systems Manager Automation
- description: Integrate with PagerDuty for on-call management and notification.
  name: PagerDuty
- description: Receive incident notifications and updates in Slack or Microsoft Teams.
  name: AWS Chatbot
jsonld:
- class_count: 100
  name: Amazon Incident Manager Context
  property_count: 108
  slug: amazon-incident-manager-context
layout: provider
modified: '2026-04-19'
name: Amazon Incident Manager
rules:
- name: Amazon Incident Manager API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: amazon-incident-manager-spectral-rules
skills: []
slug: amazon-incident-manager
solutions: []
tags:
- Automation
- AWS
- DevOps
- Incident Management
- Operations
url: https://raw.githubusercontent.com/api-evangelist/amazon-incident-manager/refs/heads/main/apis.yml
use_cases:
- description: Define escalation policies and on-call schedules to ensure the right responders are engaged.
  name: On-Call Management
- description: Integrate with CloudWatch alarms and EventBridge to automatically trigger response plans.
  name: Automated Incident Detection
- description: Coordinate incident response across multiple teams with shared incident channels.
  name: Cross-Team Coordination
- description: Maintain incident timelines and analysis reports for regulatory compliance and audits.
  name: Compliance and Audit
---
