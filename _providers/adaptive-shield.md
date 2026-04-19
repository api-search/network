---
api_count: 1
apis:
- description: 'The Adaptive Shield REST API v1 provides programmatic access to SaaS security posture data including alerts, user and device inventory, integration configurations, security check results, violations, '
  name: Adaptive Shield REST API
  slug: adaptive-shield-api
common:
- title: ''
  type: Website
  url: https://www.crowdstrike.com/platform/falcon-shield/
- title: ''
  type: Portal
  url: https://www.crowdstrike.com/platform/falcon-shield/
- title: ''
  type: Blog
  url: https://www.adaptive-shield.com/blog/
- title: ''
  type: Resources
  url: https://www.adaptive-shield.com/resources
- title: ''
  type: Support
  url: https://www.adaptive-shield.com/support
created: '2026-03-27'
description: Adaptive Shield (now CrowdStrike Falcon Shield) is a SaaS Security Posture Management (SSPM) platform that continuously monitors, remediates, and governs SaaS application security configurations and identity risks. Acquired by CrowdStrike, the platform covers 200+ SaaS integrations with over 3,500 built-in security checks, helping organizations detect misconfigurations, manage human and non-human identities, discover shadow applications, and maintain compliance across their entire SaaS stack. The REST API (v1) enables programmatic access to alerts, user inventory, device inventory, integrations, security checks, and compliance data.
features:
- description: Continuously monitors 200+ SaaS applications with 3,500+ built-in security checks to detect and remediate misconfigurations that expose organizations to security risks.
  name: SaaS Misconfiguration Detection
- description: Manages both human and non-human identities (NHI) across SaaS platforms, detecting over-privileged accounts and suspicious access patterns.
  name: Identity And Access Governance
- description: Discovers unsanctioned and shadow SaaS applications connected to the organization's environment, providing visibility into unauthorized integrations.
  name: Shadow App Discovery
- description: Provides visibility into and governance over AI agents operating within enterprise SaaS platforms including Microsoft 365, Salesforce, and OpenAI.
  name: AI Agent Visibility And Control
- description: Tracks compliance posture across SaaS applications against frameworks such as SOC 2, ISO 27001, GDPR, and HIPAA using automated security check mappings.
  name: Compliance Monitoring
- description: Public REST API v1 with API key authentication enables programmatic access to alerts, user/device inventory, integration data, security check results, violations, and compliance controls. US and EU regional endpoints available.
  name: REST API Access
- description: Integrates with SIEM platforms (Splunk, Datadog), security platforms (CrowdStrike Falcon), and vulnerability management platforms via API and native connectors.
  name: SIEM And Platform Integrations
image: /assets/icons/adaptive-shield.png
integrations:
- description: SaaS security monitoring for Microsoft 365 suite including Exchange, Teams, SharePoint, and OneDrive.
  name: Microsoft 365
- description: Security posture monitoring and misconfiguration detection for Salesforce CRM.
  name: Salesforce
- description: Configuration monitoring and security checks for Slack workspace settings.
  name: Slack
- description: Security configuration monitoring for Zoom video conferencing accounts.
  name: Zoom
- description: Identity provider integration for user access and authentication configuration monitoring.
  name: Okta
- description: Sends SaaS posture alerts as Datadog Events via OAuth integration.
  name: Datadog
- description: Splunk add-on for ingesting Adaptive Shield security events and alerts.
  name: Splunk
- description: Native integration with CrowdStrike Falcon platform following acquisition.
  name: CrowdStrike Falcon
layout: provider
modified: '2026-04-19'
name: Adaptive Shield
skills: []
slug: adaptive-shield
solutions: []
tags:
- SaaS Security
- SSPM
- Security Posture Management
- Cybersecurity
- Cloud Security
- Identity Management
- Compliance
url: https://raw.githubusercontent.com/api-evangelist/adaptive-shield/refs/heads/main/apis.yml
use_cases:
- description: Security teams can continuously monitor and remediate misconfigurations across the organization's entire SaaS stack from a single dashboard.
  name: SaaS Security Posture Management
- description: Detect and remediate over-privileged users, dormant accounts, and suspicious login behavior across all connected SaaS applications.
  name: Identity Risk Detection
- description: Automate compliance evidence collection and posture monitoring for SOC 2, ISO 27001, GDPR, and other frameworks across SaaS applications.
  name: Compliance Audit Automation
- description: Identify and assess risk from third-party OAuth apps and browser extensions connected to critical SaaS platforms.
  name: Third-Party App Risk Management
- description: Pull SaaS security alerts and posture data into SIEM and SOAR platforms via the REST API for unified security operations workflows.
  name: Security Operations Integration
---
