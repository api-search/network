---
consumed_apis:
- cortex-xdr
- cortex-xsiam
- cortex-xsoar
- cortex-xpanse
description: Unified incident response capability for SOC analysts — investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface exposure across Cortex XDR, XSIAM, XSOAR, and Xpanse.
layout: capability
name: Palo Alto Networks Incident Response
operations:
- description: List XDR incidents.
  method: GET
  name: list-incidents
  path: /v1/incidents
- description: Create an incident in XSOAR.
  method: POST
  name: create-incident
  path: /v1/incidents
- description: Search XDR incidents with filters.
  method: POST
  name: search-incidents
  path: /v1/incidents/search
- description: Get incident details from XDR.
  method: GET
  name: get-incident-details
  path: /v1/incidents/{incident_id}
- description: Update an XDR incident.
  method: PUT
  name: update-incident
  path: /v1/incidents/{incident_id}
- description: Search XSIAM incidents with filters.
  method: POST
  name: search-xsiam-incidents
  path: /v1/xsiam-incidents/search
- description: Search XDR alerts with filters.
  method: POST
  name: search-xdr-alerts
  path: /v1/alerts/search
- description: Search XSIAM alerts with filters.
  method: POST
  name: search-xsiam-alerts
  path: /v1/xsiam-alerts/search
- description: List XDR endpoints with filters.
  method: POST
  name: search-endpoints
  path: /v1/endpoints/search
- description: Isolate endpoints.
  method: POST
  name: isolate-endpoints
  path: /v1/endpoints/isolate
- description: Unisolate endpoints.
  method: POST
  name: unisolate-endpoints
  path: /v1/endpoints/unisolate
- description: Initiate a scan on endpoints.
  method: POST
  name: scan-endpoints
  path: /v1/endpoints/scan
- description: List XSIAM endpoints with filters.
  method: POST
  name: search-xsiam-endpoints
  path: /v1/xsiam-endpoints/search
- description: Run a script on endpoints.
  method: POST
  name: run-script
  path: /v1/scripts/run
- description: Get script execution results.
  method: POST
  name: get-script-results
  path: /v1/scripts/results
- description: Start an XQL query on XDR.
  method: POST
  name: start-xql-query
  path: /v1/queries
- description: Get XQL query results from XDR.
  method: POST
  name: get-xql-query-results
  path: /v1/queries/results
- description: Start an XQL query on XSIAM.
  method: POST
  name: start-xsiam-xql-query
  path: /v1/xsiam-queries
- description: Get XQL query results from XSIAM.
  method: POST
  name: get-xsiam-xql-query-results
  path: /v1/xsiam-queries/results
- description: Get internet-exposed assets from Xpanse.
  method: POST
  name: search-exposed-assets
  path: /v1/attack-surface/assets/search
- description: Get internet exposure details for specific assets from Xpanse.
  method: POST
  name: get-asset-details
  path: /v1/attack-surface/assets/{asset_id}
- description: Search Xpanse incidents with filters.
  method: POST
  name: search-xpanse-incidents
  path: /v1/attack-surface/incidents/search
- description: Update an Xpanse incident.
  method: PUT
  name: update-xpanse-incident
  path: /v1/attack-surface/incidents/{incident_id}
- description: Get attack surface rules from Xpanse.
  method: POST
  name: search-attack-surface-rules
  path: /v1/attack-surface/rules/search
- description: Update an attack surface rule in Xpanse.
  method: PUT
  name: update-attack-surface-rule
  path: /v1/attack-surface/rules/{rule_id}
- description: Get exposed services from Xpanse.
  method: POST
  name: search-services
  path: /v1/attack-surface/services/search
- description: Get owned IP ranges from Xpanse.
  method: POST
  name: search-ip-ranges
  path: /v1/attack-surface/ip-ranges/search
- description: Create a new investigation in XSOAR.
  method: POST
  name: create-investigation
  path: /v1/investigations
- description: Retrieve a specific investigation by ID from XSOAR.
  method: GET
  name: get-investigation
  path: /v1/investigations/{investigation_id}
- description: Add an entry to an investigation in XSOAR.
  method: POST
  name: add-entry
  path: /v1/investigations/entries
- description: List available playbooks in XSOAR.
  method: GET
  name: list-playbooks
  path: /v1/playbooks
- description: Run a playbook on an investigation in XSOAR.
  method: POST
  name: run-playbook
  path: /v1/playbooks/run
- description: Search for available integrations in XSOAR.
  method: GET
  name: search-integrations
  path: /v1/integrations
- description: Search for integration instances in XSOAR.
  method: POST
  name: search-integration-instances
  path: /v1/integrations/instances/search
- description: List XSIAM assets with filters.
  method: POST
  name: search-xsiam-assets
  path: /v1/xsiam-assets/search
- description: Configure a datasource for XSIAM ingestion.
  method: POST
  name: configure-datasource
  path: /v1/xsiam-datasources
- description: Get audit management logs from XDR.
  method: POST
  name: get-xdr-audit-logs
  path: /v1/audit-logs/xdr
- description: Get audit management logs from Xpanse.
  method: POST
  name: get-xpanse-audit-logs
  path: /v1/audit-logs/xpanse
- description: Get management logs from XSIAM.
  method: POST
  name: get-xsiam-management-logs
  path: /v1/audit-logs/xsiam
personas:
- description: Investigates security incidents, triages alerts, and coordinates response actions.
  id: soc-analyst
  name: SOC Analyst
- description: Executes containment, eradication, and recovery actions during security incidents.
  id: incident-responder
  name: Incident Responder
- description: Proactively searches for threats and IOCs across telemetry data.
  id: threat-hunter
  name: Threat Hunter
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
search_terms:
- get script results
- initiate a scan on endpoints.
- get xdr audit logs.
- search xdr incidents with filters.
- xsiam list endpoints
- identity and access management, tenant hierarchies, and subscription management.
- get xpanse audit logs
- xsiam list incidents
- xdr unisolate endpoints
- search xdr alerts with filters.
- firewall policy management, network objects, and cloud-native firewall configuration.
- xpanse list ip ranges
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- list xsiam incidents with optional filters and pagination.
- xsoar get investigation
- create a new incident in cortex xsoar.
- list playbooks
- search for available integrations in xsoar.
- xpanse get audit logs
- xdr
- get exposed services from xpanse.
- list xdr endpoints with optional filters, pagination, and sorting.
- search xsiam incidents
- search xdr alerts.
- get xql query results
- run xsoar playbooks.
- list xsiam alerts with optional filters and pagination.
- run a script on endpoints.
- sase
- create xsoar investigations.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- sase admin
- get management logs from xsiam.
- configure xsiam datasources.
- search for available integrations in cortex xsoar.
- cloud security engineer
- run script
- sd wan operator
- secure access service edge with remote networking, sd-wan, and zero trust access.
- isolate endpoints.
- search for integration instances in cortex xsoar.
- data loss prevention, saas security monitoring, and identity security posture.
- search xdr alerts
- xsiam get xql results
- search services
- get extra data for a specific xdr incident.
- xdr get incident details
- get details for a specific exposed asset.
- search incidents with filters in cortex xsoar.
- add an entry to an investigation in cortex xsoar.
- update an attack surface rule in xpanse.
- unisolate endpoints.
- create investigation
- compliance team
- analyzes suspicious files and samples for malware characteristics.
- detection and response
- get incident details
- initiate a scan on endpoints via xdr.
- sre
- ai runtime security scanning and automated red teaming for ai applications.
- cybersecurity
- search ip ranges
- get xsiam management logs.
- xdr list endpoints
- xpanse update attack surface rule
- xdr scan endpoints
- secures ai applications with runtime scanning and vulnerability assessment.
- xsoar get incident
- search xsiam assets
- xsoar search integrations
- compliance officer
- unisolate endpoints
- manages logging infrastructure, integrations, and platform automation.
- start an xql query on xsiam.
- get a specific investigation.
- search xsiam endpoints.
- get xsiam management logs
- run playbook
- xsoar search integration instances
- update an attack surface rule.
- threat hunter
- run a playbook on an investigation in cortex xsoar.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- soar
- investigates dlp incidents and manages sensitive data protection policies.
- search endpoints
- search xsiam incidents with filters.
- data protection analyst
- get asset details
- xsiam configure datasource
- manages multi-tenant hierarchies and service group configurations for mssps.
- ai security engineer
- get xql query results from xsiam.
- list xdr incidents with optional filters, pagination, and sorting.
- search exposed assets
- run scripts on endpoints.
- list xsiam assets with filters.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- xdr run script
- saas security admin
- search incidents with filters.
- update xpanse incident
- list available playbooks in xsoar.
- list xdr alerts with optional filters, pagination, and sorting.
- run a script on endpoints via xdr.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- incident management — list, search, create, and update incidents.
- create an incident in xsoar.
- scan endpoints.
- researches threat actors, malware campaigns, and vulnerability trends.
- search xdr endpoints.
- add an entry to an investigation in xsoar.
- xsiam list assets
- xdr isolate endpoints
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- xsoar run playbook
- list incidents
- search for integration instances in xsoar.
- threat intel analyst
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- start xql queries on xdr.
- firewall
- network architect
- start xql queries on xsiam.
- proactively searches for threats and iocs across telemetry data.
- get xql query results from xdr.
- list xsiam assets with optional filters.
- search integrations
- browser security admin
- xsoar list playbooks
- list xsiam endpoints with optional filters.
- get incident details from xdr.
- list and manage xsoar playbooks.
- search xsoar integration instances.
- configure a datasource for xsiam ingestion.
- monitors and remediates cloud security misconfigurations and compliance violations.
- unisolate endpoints and restore network connectivity.
- search xpanse incidents.
- xpanse update incident
- cloud security
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- xsiam list alerts
- get internet-exposed assets from xpanse.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- xpanse list services
- list xdr incidents.
- get xpanse audit logs.
- designs and implements network security architectures and policies.
- xdr start xql query
- unisolate endpoints and restore network connectivity via xdr.
- xsiam start xql query
- search incidents
- search xsoar integrations.
- xsoar update incident
- get script execution results.
- xdr get xql results
- threat intelligence
- get or update a specific incident.
- firewall admin
- manages multi-tenant security operations at scale for managed service providers.
- isolate endpoints from the network via xdr.
- update an xdr incident.
- xdr update incident
- executes containment, eradication, and recovery actions during security incidents.
- palo alto networks
- get attack surface rules from xpanse.
- update an xpanse incident.
- search attack surface rules
- digital experience monitoring, log management, and best practice assessment.
- soc
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- incident responder
- incident response
- start xql query
- create a new investigation in xsoar.
- start xsiam xql query
- xdr get audit logs
- investigates security incidents, triages alerts, and coordinates response actions.
- retrieve a specific incident by id from cortex xsoar.
- get xpanse incidents.
- search integration instances
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- retrieve a specific investigation by id from cortex xsoar.
- xdr list incidents
- get audit management logs from xdr.
- xsoar create incident
- xsoar create investigation
- search exposed services.
- monitors network health, performance, and digital experience metrics.
- network operations
- conducts automated adversarial testing against ai systems and llm applications.
- xpanse get asset details
- list available playbooks in cortex xsoar.
- enterprise browser policy management and secure browsing.
- cloud security posture management, compliance monitoring, and workload protection.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- search owned ip ranges.
- get script execution results from xdr.
- search attack surface rules.
- create a new investigation in cortex xsoar.
- red team operator
- search xpanse incidents with filters.
- designs sase and sd-wan network architectures for secure remote access.
- list xdr endpoints with filters.
- get xdr audit logs
- get internet exposure details for specific assets from xpanse.
- enterprise it
- search xsiam assets.
- soc analyst
- subscription manager
- platform engineer
- search xsiam alerts
- search xsiam alerts.
- update incident
- security operations
- xpanse list exposed assets
- network security
- xsoar search incidents
- start an xql query on xdr.
- get investigation
- search xsiam alerts with filters.
- mssp operator
- get owned ip ranges from xpanse.
- list xsiam endpoints with filters.
- tenant operator
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- search xsiam incidents.
- search xsiam endpoints
- configure datasource
- manages enterprise browser policies and secure browsing configurations.
- xdr list alerts
- xdr get script results
- xpanse list attack surface rules
- get xsiam xql query results
- xsiam get management logs
- search internet-exposed assets.
- isolate endpoints from the network.
- xpanse list incidents
- malware researcher
- manages service accounts, roles, and access policies for platform api access.
- search xpanse incidents
- scan endpoints
- add entries to investigations.
- manage enterprise browser policies, user sessions, and deployments.
- retrieve a specific investigation by id from xsoar.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- network security engineer
- create incident
- vulnerability manager
- update an existing incident in cortex xsoar.
- xsoar add entry
- iam admin
- get audit management logs from xpanse.
- isolate endpoints
- add entry
- update attack surface rule
- run a playbook on an investigation in xsoar.
slug: incident-response
tags:
- Palo Alto Networks
- Incident Response
- SOC
- Security Operations
- Detection And Response
tools:
- description: List XDR incidents with optional filters, pagination, and sorting.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xdr-list-incidents
- description: Get extra data for a specific XDR incident.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xdr-get-incident-details
- description: Update an XDR incident.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: xdr-update-incident
- description: List XSIAM incidents with optional filters and pagination.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsiam-list-incidents
- description: Create a new incident in Cortex XSOAR.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xsoar-create-incident
- description: Search incidents with filters in Cortex XSOAR.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsoar-search-incidents
- description: Retrieve a specific incident by ID from Cortex XSOAR.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsoar-get-incident
- description: Update an existing incident in Cortex XSOAR.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xsoar-update-incident
- description: List XDR alerts with optional filters, pagination, and sorting.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xdr-list-alerts
- description: List XSIAM alerts with optional filters and pagination.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsiam-list-alerts
- description: List XDR endpoints with optional filters, pagination, and sorting.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xdr-list-endpoints
- description: Isolate endpoints from the network via XDR.
  hints:
    destructive: true
    idempotent: false
    openWorld: true
    readOnly: false
  name: xdr-isolate-endpoints
- description: Unisolate endpoints and restore network connectivity via XDR.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xdr-unisolate-endpoints
- description: Initiate a scan on endpoints via XDR.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xdr-scan-endpoints
- description: List XSIAM endpoints with optional filters.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsiam-list-endpoints
- description: Run a script on endpoints via XDR.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xdr-run-script
- description: Get script execution results from XDR.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xdr-get-script-results
- description: Start an XQL query on XDR.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xdr-start-xql-query
- description: Get XQL query results from XDR.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xdr-get-xql-results
- description: Start an XQL query on XSIAM.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xsiam-start-xql-query
- description: Get XQL query results from XSIAM.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsiam-get-xql-results
- description: Get internet-exposed assets from Xpanse.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xpanse-list-exposed-assets
- description: Get internet exposure details for specific assets from Xpanse.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xpanse-get-asset-details
- description: Get Xpanse incidents.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xpanse-list-incidents
- description: Update an Xpanse incident.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: xpanse-update-incident
- description: Get attack surface rules from Xpanse.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xpanse-list-attack-surface-rules
- description: Update an attack surface rule in Xpanse.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: xpanse-update-attack-surface-rule
- description: Get exposed services from Xpanse.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xpanse-list-services
- description: Get owned IP ranges from Xpanse.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xpanse-list-ip-ranges
- description: Create a new investigation in Cortex XSOAR.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xsoar-create-investigation
- description: Retrieve a specific investigation by ID from Cortex XSOAR.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsoar-get-investigation
- description: Add an entry to an investigation in Cortex XSOAR.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xsoar-add-entry
- description: List available playbooks in Cortex XSOAR.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsoar-list-playbooks
- description: Run a playbook on an investigation in Cortex XSOAR.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xsoar-run-playbook
- description: Search for available integrations in Cortex XSOAR.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsoar-search-integrations
- description: Search for integration instances in Cortex XSOAR.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsoar-search-integration-instances
- description: List XSIAM assets with optional filters.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsiam-list-assets
- description: Configure a datasource for XSIAM ingestion.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: xsiam-configure-datasource
- description: Get audit management logs from XDR.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xdr-get-audit-logs
- description: Get audit management logs from Xpanse.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xpanse-get-audit-logs
- description: Get management logs from XSIAM.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: xsiam-get-management-logs
---
