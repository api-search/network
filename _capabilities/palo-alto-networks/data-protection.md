---
consumed_apis:
- dlp
- email-dlp
- saas-security
- sspm
- identity-security-posture
description: Unified data protection capability for managing DLP incidents, email DLP events, SaaS security incidents and assets, and SaaS security posture checks across Enterprise DLP, Email DLP, SaaS Security, and SSPM APIs.
layout: capability
name: Palo Alto Networks Data Protection
operations:
- description: List DLP incidents with optional filters.
  method: GET
  name: list-dlp-incidents
  path: /v1/dlp-incidents
- description: Retrieve a specific DLP incident by ID.
  method: GET
  name: get-dlp-incident
  path: /v1/dlp-incidents/{incident_id}
- description: Update a DLP incident.
  method: PUT
  name: update-dlp-incident
  path: /v1/dlp-incidents/{incident_id}
- description: Get data snippets for a specific DLP incident.
  method: GET
  name: get-dlp-snippets
  path: /v1/dlp-incidents/{incident_id}/snippets
- description: List available data patterns.
  method: GET
  name: list-data-patterns
  path: /v1/data-patterns
- description: Retrieve a specific data pattern by ID.
  method: GET
  name: get-data-pattern
  path: /v1/data-patterns/{pattern_id}
- description: Get a DLP summary report for a given time range.
  method: GET
  name: get-dlp-report-summary
  path: /v1/dlp-reports/summary
- description: List email DLP incidents with optional filters.
  method: GET
  name: list-email-incidents
  path: /v1/email-incidents
- description: Retrieve a specific email DLP incident by ID.
  method: GET
  name: get-email-incident
  path: /v1/email-incidents/{incident_id}
- description: Update the verdict for an email DLP incident.
  method: PUT
  name: update-email-verdict
  path: /v1/email-incidents/{incident_id}/verdict
- description: Get attachments for a specific email DLP incident.
  method: GET
  name: get-email-attachments
  path: /v1/email-incidents/{incident_id}/attachments
- description: Get recipients for a specific email DLP incident.
  method: GET
  name: get-email-recipients
  path: /v1/email-incidents/{incident_id}/recipients
- description: List SaaS security incidents with optional filters.
  method: GET
  name: list-saas-incidents
  path: /v1/saas-incidents
- description: Retrieve details for a specific SaaS security incident.
  method: GET
  name: get-saas-incident
  path: /v1/saas-incidents/{incident_id}
- description: Update a specific SaaS security incident.
  method: PUT
  name: update-saas-incident
  path: /v1/saas-incidents/{incident_id}
- description: Retrieve a list of monitored SaaS assets.
  method: GET
  name: list-saas-assets
  path: /v1/saas-assets
- description: Retrieve details for a specific SaaS asset.
  method: GET
  name: get-saas-asset
  path: /v1/saas-assets/{asset_id}
- description: Retrieve a list of connected SaaS applications.
  method: GET
  name: list-saas-applications
  path: /v1/saas-applications
- description: Retrieve a list of users across SaaS applications.
  method: GET
  name: list-saas-users
  path: /v1/saas-users
- description: Retrieve activity log for a specific user.
  method: GET
  name: get-user-activities
  path: /v1/saas-users/{user_id}/activities
- description: Retrieve log forwarding configuration settings.
  method: GET
  name: get-log-forwarding-settings
  path: /v1/log-forwarding-settings
- description: List all onboarded SaaS applications.
  method: GET
  name: list-onboarded-apps
  path: /v1/sspm-apps
- description: Onboard a new SaaS application.
  method: POST
  name: onboard-app
  path: /v1/sspm-apps
- description: Remove an onboarded SaaS application.
  method: DELETE
  name: remove-app
  path: /v1/sspm-apps/{app_id}
- description: List posture checks with optional filters.
  method: GET
  name: list-posture-checks
  path: /v1/posture-checks
- description: Get a specific posture check by ID.
  method: GET
  name: get-posture-check
  path: /v1/posture-checks/{check_id}
- description: Update the status of a posture check.
  method: PUT
  name: update-posture-check-status
  path: /v1/posture-checks/{check_id}/status
- description: List available applications in the catalog.
  method: GET
  name: list-app-catalog
  path: /v1/sspm-app-catalog
- description: List all Jira integrations.
  method: GET
  name: list-jira-integrations
  path: /v1/jira-integrations
- description: Create a new Jira integration.
  method: POST
  name: create-jira-integration
  path: /v1/jira-integrations
personas:
- description: Investigates DLP incidents and manages sensitive data protection policies.
  id: data-protection-analyst
  name: Data Protection Analyst
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
search_terms:
- retrieve details for a specific saas security incident.
- secures ai applications with runtime scanning and vulnerability assessment.
- list app catalog
- retrieve log forwarding configuration settings.
- xdr
- vulnerability manager
- get saas incident
- soar
- get user activities
- network security engineer
- get email recipients
- get recipients for a specific email dlp incident.
- get log forwarding settings
- list available applications in the catalog.
- list connected saas applications.
- remove an onboarded sspm application.
- remove an onboarded saas application.
- get a specific posture check by id.
- list sspm posture checks with optional filters.
- manages service accounts, roles, and access policies for platform api access.
- update email verdict
- update a dlp incident status or assignee.
- list users across saas applications.
- list onboarded apps
- threat hunter
- browser security admin
- list email dlp incidents.
- sspm
- manage sspm posture checks.
- get a dlp summary report for a given time range.
- soc analyst
- platform engineer
- update the verdict for an email dlp incident.
- manages logging infrastructure, integrations, and platform automation.
- network architect
- digital experience monitoring, log management, and best practice assessment.
- saas security admin
- tenant operator
- access dlp report summaries.
- list dlp incidents with optional filters.
- identity and access management, tenant hierarchies, and subscription management.
- manage sspm jira integrations.
- ai security engineer
- iam admin
- onboard a new saas application in sspm.
- subscription manager
- get user activity log.
- network operations
- monitors network health, performance, and digital experience metrics.
- manages multi-tenant security operations at scale for managed service providers.
- update a dlp incident.
- update posture check status
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- get or update a specific saas security incident.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- retrieve a specific email dlp incident by id.
- retrieve a list of connected saas applications.
- list all jira integrations.
- sase
- access email incident attachments.
- sase admin
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- get email attachments
- get a specific saas asset.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- firewall
- network security
- designs sase and sd-wan network architectures for secure remote access.
- update a specific saas security incident.
- list monitored saas assets.
- identity security posture
- list dlp incidents
- researches threat actors, malware campaigns, and vulnerability trends.
- remove an onboarded saas application from sspm.
- enterprise it
- get a specific posture check.
- onboard app
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- get posture check
- retrieve a specific dlp data pattern by id.
- incident responder
- data protection
- manage saas security incidents.
- cloud security posture management, compliance monitoring, and workload protection.
- list available data patterns.
- designs and implements network security architectures and policies.
- conducts automated adversarial testing against ai systems and llm applications.
- retrieve details for a specific saas asset.
- update dlp incident
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- list data patterns
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- cybersecurity
- threat intel analyst
- create a new jira integration.
- update the status of an sspm posture check.
- get log forwarding configuration settings.
- manage dlp incidents.
- list saas security incidents with optional filters.
- list saas users
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- manages enterprise browser policies and secure browsing configurations.
- list dlp data patterns.
- browse the sspm application catalog.
- cloud security
- dlp
- get data pattern
- proactively searches for threats and iocs across telemetry data.
- update saas incident
- retrieve activity log for a specific user.
- firewall admin
- get dlp snippets
- list jira integrations
- get saas asset
- get dlp report summary
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- list email dlp incidents with optional filters.
- retrieve a list of monitored saas assets.
- manage onboarded sspm applications.
- retrieve a specific dlp incident by id.
- retrieve a list of users across saas applications.
- list dlp incidents with optional filters for severity and status.
- data protection analyst
- list saas incidents
- red team operator
- firewall policy management, network objects, and cloud-native firewall configuration.
- list posture checks with optional filters.
- retrieve a list of saas security incidents.
- list all sspm jira integrations.
- sd wan operator
- create a new jira integration for sspm.
- investigates security incidents, triages alerts, and coordinates response actions.
- get dlp incident
- list saas assets
- saas security
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- update posture check status.
- executes containment, eradication, and recovery actions during security incidents.
- manages multi-tenant hierarchies and service group configurations for mssps.
- list saas applications
- get a specific data pattern.
- manage enterprise browser policies, user sessions, and deployments.
- analyzes suspicious files and samples for malware characteristics.
- get or update a specific dlp incident.
- mssp operator
- sre
- retrieve a specific data pattern by id.
- access email incident recipients.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- list email incidents
- ai runtime security scanning and automated red teaming for ai applications.
- get attachments for a specific email dlp incident.
- list posture checks
- malware researcher
- compliance team
- get data snippets for a specific dlp incident.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- data loss prevention, saas security monitoring, and identity security posture.
- threat intelligence
- palo alto networks
- access dlp incident data snippets.
- list all onboarded saas applications in sspm.
- onboard a new saas application.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- list available applications in the sspm catalog.
- list all onboarded saas applications.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- remove app
- create jira integration
- update the status of a posture check.
- cloud security engineer
- get a specific sspm posture check by id.
- get email incident
- list available dlp data patterns.
- get a specific email dlp incident.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- manage email incident verdicts.
- compliance officer
- monitors and remediates cloud security misconfigurations and compliance violations.
- investigates dlp incidents and manages sensitive data protection policies.
- enterprise browser policy management and secure browsing.
slug: data-protection
tags:
- Palo Alto Networks
- Data Protection
- DLP
- SaaS Security
- SSPM
- Identity Security Posture
tools:
- description: List DLP incidents with optional filters for severity and status.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-dlp-incidents
- description: Retrieve a specific DLP incident by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-dlp-incident
- description: Update a DLP incident status or assignee.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-dlp-incident
- description: Get data snippets for a specific DLP incident.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-dlp-snippets
- description: List available DLP data patterns.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-data-patterns
- description: Retrieve a specific DLP data pattern by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-data-pattern
- description: Get a DLP summary report for a given time range.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-dlp-report-summary
- description: List email DLP incidents with optional filters.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-email-incidents
- description: Retrieve a specific email DLP incident by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-email-incident
- description: Update the verdict for an email DLP incident.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-email-verdict
- description: Get attachments for a specific email DLP incident.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-email-attachments
- description: Get recipients for a specific email DLP incident.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-email-recipients
- description: Retrieve a list of SaaS security incidents.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-saas-incidents
- description: Retrieve details for a specific SaaS security incident.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-saas-incident
- description: Update a specific SaaS security incident.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-saas-incident
- description: Retrieve a list of monitored SaaS assets.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-saas-assets
- description: Retrieve details for a specific SaaS asset.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-saas-asset
- description: Retrieve a list of connected SaaS applications.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-saas-applications
- description: Retrieve a list of users across SaaS applications.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-saas-users
- description: Retrieve activity log for a specific user.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-user-activities
- description: Retrieve log forwarding configuration settings.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-log-forwarding-settings
- description: List all onboarded SaaS applications in SSPM.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-onboarded-apps
- description: Onboard a new SaaS application in SSPM.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: onboard-app
- description: Remove an onboarded SaaS application from SSPM.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: remove-app
- description: List SSPM posture checks with optional filters.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-posture-checks
- description: Get a specific SSPM posture check by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-posture-check
- description: Update the status of an SSPM posture check.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-posture-check-status
- description: List available applications in the SSPM catalog.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-app-catalog
- description: List all SSPM Jira integrations.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-jira-integrations
- description: Create a new Jira integration for SSPM.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-jira-integration
---
