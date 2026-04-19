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
- list monitored saas assets.
- get user activity log.
- manage email incident verdicts.
- retrieve a list of monitored saas assets.
- update the status of a posture check.
- get or update a specific dlp incident.
- manage enterprise browser policies, user sessions, and deployments.
- data protection analyst
- iam admin
- compliance team
- network operations
- retrieve a specific dlp incident by id.
- access dlp incident data snippets.
- cloud security
- onboard a new saas application in sspm.
- manage sspm jira integrations.
- malware researcher
- manage onboarded sspm applications.
- palo alto networks
- list all jira integrations.
- update a dlp incident status or assignee.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- identity security posture
- get or update a specific saas security incident.
- get a specific saas asset.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- retrieve activity log for a specific user.
- list posture checks
- get a dlp summary report for a given time range.
- update a specific saas security incident.
- remove an onboarded saas application.
- list saas incidents
- incident responder
- xdr
- update email verdict
- create a new jira integration for sspm.
- analyzes suspicious files and samples for malware characteristics.
- platform engineer
- executes containment, eradication, and recovery actions during security incidents.
- sd wan operator
- get a specific email dlp incident.
- get a specific posture check.
- create jira integration
- data protection
- vulnerability manager
- list email dlp incidents with optional filters.
- onboard a new saas application.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- retrieve a specific dlp data pattern by id.
- browser security admin
- list email incidents
- list available applications in the sspm catalog.
- get a specific posture check by id.
- ai runtime security scanning and automated red teaming for ai applications.
- get data pattern
- remove an onboarded saas application from sspm.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- threat intel analyst
- red team operator
- tenant operator
- manages logging infrastructure, integrations, and platform automation.
- retrieve a list of users across saas applications.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- monitors and remediates cloud security misconfigurations and compliance violations.
- retrieve details for a specific saas security incident.
- cybersecurity
- list dlp incidents
- firewall admin
- get user activities
- secures ai applications with runtime scanning and vulnerability assessment.
- retrieve details for a specific saas asset.
- update saas incident
- list app catalog
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- manage saas security incidents.
- firewall policy management, network objects, and cloud-native firewall configuration.
- get dlp incident
- secure access service edge with remote networking, sd-wan, and zero trust access.
- enterprise browser policy management and secure browsing.
- manage dlp incidents.
- list dlp incidents with optional filters for severity and status.
- compliance officer
- get a specific sspm posture check by id.
- list available applications in the catalog.
- list data patterns
- list available data patterns.
- investigates dlp incidents and manages sensitive data protection policies.
- access email incident recipients.
- sase admin
- retrieve a specific email dlp incident by id.
- manage sspm posture checks.
- list connected saas applications.
- get log forwarding settings
- cloud security posture management, compliance monitoring, and workload protection.
- list saas applications
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- dlp
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- list sspm posture checks with optional filters.
- network architect
- update dlp incident
- mssp operator
- create a new jira integration.
- update the status of an sspm posture check.
- list users across saas applications.
- network security engineer
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- get a specific data pattern.
- get recipients for a specific email dlp incident.
- get saas asset
- remove an onboarded sspm application.
- update posture check status.
- browse the sspm application catalog.
- list available dlp data patterns.
- retrieve a list of saas security incidents.
- data loss prevention, saas security monitoring, and identity security posture.
- researches threat actors, malware campaigns, and vulnerability trends.
- retrieve log forwarding configuration settings.
- manages service accounts, roles, and access policies for platform api access.
- get email attachments
- update a dlp incident.
- saas security admin
- list saas security incidents with optional filters.
- get attachments for a specific email dlp incident.
- get email recipients
- remove app
- list all sspm jira integrations.
- sre
- manages multi-tenant security operations at scale for managed service providers.
- list posture checks with optional filters.
- digital experience monitoring, log management, and best practice assessment.
- manages multi-tenant hierarchies and service group configurations for mssps.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- threat hunter
- soc analyst
- list jira integrations
- manages enterprise browser policies and secure browsing configurations.
- soar
- get email incident
- get saas incident
- list saas users
- subscription manager
- cloud security engineer
- list onboarded apps
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- sspm
- sase
- get dlp report summary
- designs and implements network security architectures and policies.
- threat intelligence
- retrieve a list of connected saas applications.
- conducts automated adversarial testing against ai systems and llm applications.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- designs sase and sd-wan network architectures for secure remote access.
- list dlp data patterns.
- get posture check
- update posture check status
- firewall
- access dlp report summaries.
- access email incident attachments.
- get log forwarding configuration settings.
- list all onboarded saas applications.
- list all onboarded saas applications in sspm.
- retrieve a specific data pattern by id.
- proactively searches for threats and iocs across telemetry data.
- list saas assets
- network security
- enterprise it
- onboard app
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- get data snippets for a specific dlp incident.
- list dlp incidents with optional filters.
- ai security engineer
- investigates security incidents, triages alerts, and coordinates response actions.
- saas security
- update the verdict for an email dlp incident.
- list email dlp incidents.
- monitors network health, performance, and digital experience metrics.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- get dlp snippets
- identity and access management, tenant hierarchies, and subscription management.
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
