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
- create jira integration
- palo alto networks
- manage onboarded sspm applications.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- ai security engineer
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- investigates security incidents, triages alerts, and coordinates response actions.
- manage dlp incidents.
- cybersecurity
- retrieve log forwarding configuration settings.
- soar
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- data protection
- retrieve details for a specific saas asset.
- update saas incident
- manages service accounts, roles, and access policies for platform api access.
- designs and implements network security architectures and policies.
- get dlp report summary
- soc analyst
- list all sspm jira integrations.
- conducts automated adversarial testing against ai systems and llm applications.
- sase
- create a new jira integration.
- sd wan operator
- manage sspm jira integrations.
- update a dlp incident status or assignee.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- get or update a specific saas security incident.
- remove app
- vulnerability manager
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- manage email incident verdicts.
- list all jira integrations.
- retrieve a specific dlp data pattern by id.
- list all onboarded saas applications in sspm.
- get a dlp summary report for a given time range.
- researches threat actors, malware campaigns, and vulnerability trends.
- get user activity log.
- update dlp incident
- list email dlp incidents with optional filters.
- list saas users
- mssp operator
- malware researcher
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- list saas incidents
- incident responder
- get data snippets for a specific dlp incident.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- browser security admin
- sase admin
- update a dlp incident.
- get recipients for a specific email dlp incident.
- manages multi-tenant security operations at scale for managed service providers.
- platform engineer
- get dlp incident
- list available applications in the catalog.
- list dlp incidents with optional filters for severity and status.
- update posture check status.
- get email attachments
- list posture checks with optional filters.
- cloud security engineer
- list email dlp incidents.
- retrieve a list of users across saas applications.
- retrieve a specific data pattern by id.
- retrieve a list of monitored saas assets.
- firewall
- retrieve a specific dlp incident by id.
- network security engineer
- get a specific data pattern.
- list data patterns
- remove an onboarded sspm application.
- get a specific posture check by id.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- remove an onboarded saas application from sspm.
- get a specific sspm posture check by id.
- list sspm posture checks with optional filters.
- list saas assets
- list email incidents
- update the verdict for an email dlp incident.
- update email verdict
- monitors and remediates cloud security misconfigurations and compliance violations.
- identity security posture
- retrieve activity log for a specific user.
- get saas incident
- list app catalog
- manages enterprise browser policies and secure browsing configurations.
- update a specific saas security incident.
- list users across saas applications.
- list available applications in the sspm catalog.
- list all onboarded saas applications.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- onboard a new saas application.
- compliance team
- get a specific email dlp incident.
- update posture check status
- browse the sspm application catalog.
- list available dlp data patterns.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- designs sase and sd-wan network architectures for secure remote access.
- cloud security
- get dlp snippets
- cloud security posture management, compliance monitoring, and workload protection.
- list available data patterns.
- threat hunter
- data loss prevention, saas security monitoring, and identity security posture.
- iam admin
- retrieve a list of connected saas applications.
- sre
- get a specific posture check.
- get a specific saas asset.
- get email recipients
- access dlp report summaries.
- create a new jira integration for sspm.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- saas security admin
- list connected saas applications.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- retrieve details for a specific saas security incident.
- manages logging infrastructure, integrations, and platform automation.
- secures ai applications with runtime scanning and vulnerability assessment.
- sspm
- list posture checks
- get or update a specific dlp incident.
- manage enterprise browser policies, user sessions, and deployments.
- proactively searches for threats and iocs across telemetry data.
- data protection analyst
- manages multi-tenant hierarchies and service group configurations for mssps.
- firewall policy management, network objects, and cloud-native firewall configuration.
- get attachments for a specific email dlp incident.
- retrieve a specific email dlp incident by id.
- update the status of a posture check.
- list dlp incidents with optional filters.
- get log forwarding settings
- threat intel analyst
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- ai runtime security scanning and automated red teaming for ai applications.
- get email incident
- executes containment, eradication, and recovery actions during security incidents.
- remove an onboarded saas application.
- access email incident recipients.
- compliance officer
- manage sspm posture checks.
- red team operator
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- analyzes suspicious files and samples for malware characteristics.
- access dlp incident data snippets.
- threat intelligence
- get user activities
- get saas asset
- list dlp data patterns.
- list dlp incidents
- onboard app
- get log forwarding configuration settings.
- list onboarded apps
- list saas security incidents with optional filters.
- monitors network health, performance, and digital experience metrics.
- subscription manager
- digital experience monitoring, log management, and best practice assessment.
- update the status of an sspm posture check.
- network architect
- enterprise it
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- get data pattern
- list jira integrations
- network security
- list saas applications
- identity and access management, tenant hierarchies, and subscription management.
- saas security
- access email incident attachments.
- manage saas security incidents.
- retrieve a list of saas security incidents.
- firewall admin
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- xdr
- network operations
- get posture check
- investigates dlp incidents and manages sensitive data protection policies.
- tenant operator
- enterprise browser policy management and secure browsing.
- list monitored saas assets.
- onboard a new saas application in sspm.
- dlp
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
