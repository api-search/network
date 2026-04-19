---
api_count: 1
apis:
- description: The Amazon Detective API provides programmatic access to manage security investigation workflows. It enables developers to create and manage behavior graphs, invite and manage member accounts, start a
  name: Amazon Detective API
  slug: ''
capabilities:
- description: Workflow capability for SOC analysts and security engineers to conduct end-to-end security investigations using Amazon Detective. Combines behavior graph management, member account administration, inv
  name: Amazon Detective Security Investigation
  slug: security-investigation
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/detective/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/detective/
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
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/detective/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/tag/amazon-detective/
- title: ''
  type: ReleaseNotes
  url: https://docs.aws.amazon.com/detective/latest/userguide/release-notes.html
- title: ''
  type: SpectralRules
  url: rules/amazon-detective-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-detective-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/security-investigation.yaml
created: '2024-01-15'
description: Amazon Detective is a security investigation service that makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. It automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build interactive visualizations that help you conduct faster and more efficient security investigations.
features:
- description: Automatically builds a behavior graph from log data using machine learning and graph theory to visualize security issues.
  name: Behavior Graph Analysis
- description: Start and manage structured investigations on IAM users and roles with scoped time ranges and severity scoring.
  name: Security Investigations
- description: Automatically identifies indicators including impossible travel, flagged IP addresses, new geolocations, new user agents, and TTP observations.
  name: Indicators of Compromise
- description: Aggregate security data from multiple AWS accounts using an administrator account and member account model.
  name: Multi-Account Support
- description: Automatically enable new organization accounts as member accounts in the organization behavior graph.
  name: AWS Organizations Integration
- description: Ingest security telemetry from CloudTrail, VPC Flow Logs, GuardDuty findings, EKS audit logs, and Active Directory audit logs.
  name: Data Source Packages
- description: Provides interactive graph visualizations in the AWS console to explore entity relationships and security events.
  name: Interactive Visualizations
- description: Assigns severity levels (Informational, Low, Medium, High, Critical) based on likelihood and impact of compromise indicators.
  name: Investigation Severity Scoring
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Automatically ingests GuardDuty findings into the behavior graph for deeper investigation context.
  name: Amazon GuardDuty
- description: Ingests CloudTrail API call logs to track user and service activity across your AWS environment.
  name: AWS CloudTrail
- description: Analyzes VPC flow logs to identify network communication patterns and anomalies.
  name: Amazon VPC Flow Logs
- description: Optionally ingests EKS audit logs to monitor Kubernetes API server activity.
  name: Amazon EKS
- description: Integrates with AWS Organizations to manage multi-account behavior graphs and auto-enable new accounts.
  name: AWS Organizations
- description: Surfaces Detective investigation context within Security Hub for consolidated security findings.
  name: AWS Security Hub
jsonld:
- class_count: 53
  name: Amazon Detective Context
  property_count: 55
  slug: amazon-detective-context
layout: provider
modified: '2026-04-19'
name: Amazon Detective
rules:
- name: Amazon Detective API Rules
  rule_count: 39
  severity_counts:
    error: 18
    hint: 0
    info: 9
    warn: 12
  slug: amazon-detective-spectral-rules
skills: []
slug: amazon-detective
solutions: []
tags:
- AWS
- Forensics
- Investigation
- Security
url: https://aws.amazon.com/detective/
use_cases:
- description: Rapidly investigate security incidents by analyzing entity behavior, network activity, and API call patterns across your AWS environment.
  name: Security Incident Investigation
- description: Proactively search for suspicious activity and potential threats using behavior analysis and machine learning across your AWS accounts.
  name: Threat Hunting
- description: Identify the root cause of security issues by exploring the relationships between resources, users, and events in a behavior graph.
  name: Root Cause Analysis
- description: Collect and preserve forensic evidence for compliance investigations using structured investigations with defined scope and time ranges.
  name: Compliance Forensics
- description: Centrally manage security investigations across an AWS Organization from a single administrator account.
  name: Multi-Account Security Operations
---
