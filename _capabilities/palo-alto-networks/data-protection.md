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
- enterprise it
- access dlp incident data snippets.
- onboard a new saas application in sspm.
- compliance officer
- get posture check
- data protection analyst
- remove an onboarded saas application from sspm.
- designs sase and sd-wan network architectures for secure remote access.
- retrieve activity log for a specific user.
- access dlp report summaries.
- list all onboarded saas applications.
- list app catalog
- malware researcher
- get or update a specific dlp incident.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- get saas incident
- ai runtime security scanning and automated red teaming for ai applications.
- list available applications in the catalog.
- get email attachments
- list users across saas applications.
- get user activities
- researches threat actors, malware campaigns, and vulnerability trends.
- manages enterprise browser policies and secure browsing configurations.
- cloud security posture management, compliance monitoring, and workload protection.
- update posture check status.
- manage saas security incidents.
- get log forwarding configuration settings.
- get dlp incident
- create a new jira integration for sspm.
- list dlp incidents
- access email incident attachments.
- list monitored saas assets.
- network security
- access email incident recipients.
- list all jira integrations.
- retrieve a list of monitored saas assets.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- proactively searches for threats and iocs across telemetry data.
- get a specific data pattern.
- list data patterns
- platform engineer
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- list dlp incidents with optional filters for severity and status.
- get log forwarding settings
- analyzes suspicious files and samples for malware characteristics.
- get data snippets for a specific dlp incident.
- remove app
- firewall policy management, network objects, and cloud-native firewall configuration.
- manage sspm posture checks.
- monitors network health, performance, and digital experience metrics.
- update the verdict for an email dlp incident.
- dlp
- retrieve a list of connected saas applications.
- vulnerability manager
- manages multi-tenant security operations at scale for managed service providers.
- conducts automated adversarial testing against ai systems and llm applications.
- get email recipients
- manages logging infrastructure, integrations, and platform automation.
- remove an onboarded sspm application.
- get recipients for a specific email dlp incident.
- compliance team
- list saas incidents
- create jira integration
- list saas assets
- retrieve a specific data pattern by id.
- manage dlp incidents.
- get saas asset
- designs and implements network security architectures and policies.
- manages multi-tenant hierarchies and service group configurations for mssps.
- get a specific posture check.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- update posture check status
- update a dlp incident status or assignee.
- saas security admin
- tenant operator
- incident responder
- list email dlp incidents with optional filters.
- update the status of a posture check.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- manage sspm jira integrations.
- get user activity log.
- cloud security engineer
- retrieve details for a specific saas asset.
- data protection
- list email dlp incidents.
- get a specific posture check by id.
- list available dlp data patterns.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- list dlp incidents with optional filters.
- firewall
- get or update a specific saas security incident.
- retrieve a list of saas security incidents.
- remove an onboarded saas application.
- list posture checks with optional filters.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- list available data patterns.
- list saas applications
- sase
- update a specific saas security incident.
- threat intel analyst
- sd wan operator
- manage enterprise browser policies, user sessions, and deployments.
- retrieve a specific dlp data pattern by id.
- update a dlp incident.
- network operations
- list sspm posture checks with optional filters.
- manages service accounts, roles, and access policies for platform api access.
- browse the sspm application catalog.
- retrieve a specific dlp incident by id.
- threat hunter
- get dlp snippets
- cybersecurity
- onboard a new saas application.
- get a specific sspm posture check by id.
- firewall admin
- soc analyst
- mssp operator
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- identity security posture
- identity and access management, tenant hierarchies, and subscription management.
- monitors and remediates cloud security misconfigurations and compliance violations.
- list available applications in the sspm catalog.
- browser security admin
- sase admin
- list posture checks
- threat intelligence
- palo alto networks
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- get a specific email dlp incident.
- get email incident
- list all sspm jira integrations.
- soar
- list all onboarded saas applications in sspm.
- manage email incident verdicts.
- investigates security incidents, triages alerts, and coordinates response actions.
- get data pattern
- saas security
- cloud security
- network architect
- get a specific saas asset.
- list connected saas applications.
- create a new jira integration.
- get a dlp summary report for a given time range.
- get attachments for a specific email dlp incident.
- retrieve a specific email dlp incident by id.
- list email incidents
- executes containment, eradication, and recovery actions during security incidents.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- ai security engineer
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- xdr
- onboard app
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- sre
- network security engineer
- iam admin
- list jira integrations
- data loss prevention, saas security monitoring, and identity security posture.
- list saas users
- digital experience monitoring, log management, and best practice assessment.
- secures ai applications with runtime scanning and vulnerability assessment.
- red team operator
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- update email verdict
- update dlp incident
- enterprise browser policy management and secure browsing.
- list saas security incidents with optional filters.
- retrieve a list of users across saas applications.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- update saas incident
- list dlp data patterns.
- update the status of an sspm posture check.
- manage onboarded sspm applications.
- sspm
- list onboarded apps
- retrieve log forwarding configuration settings.
- investigates dlp incidents and manages sensitive data protection policies.
- retrieve details for a specific saas security incident.
- subscription manager
- get dlp report summary
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
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
