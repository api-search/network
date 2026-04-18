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
- soar
- xpanse list services
- retrieve a specific investigation by id from cortex xsoar.
- xpanse get audit logs
- search integrations
- unisolate endpoints.
- search xsoar integration instances.
- create a new investigation in cortex xsoar.
- manage enterprise browser policies, user sessions, and deployments.
- conducts automated adversarial testing against ai systems and llm applications.
- xsoar list playbooks
- retrieve a specific incident by id from cortex xsoar.
- xsoar get incident
- xdr update incident
- list playbooks
- xsiam start xql query
- xsoar search incidents
- update an attack surface rule in xpanse.
- xpanse update incident
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- data loss prevention, saas security monitoring, and identity security posture.
- identity and access management, tenant hierarchies, and subscription management.
- compliance officer
- get script execution results from xdr.
- get xdr audit logs.
- get xsiam management logs
- enterprise it
- ai runtime security scanning and automated red teaming for ai applications.
- get xdr audit logs
- search attack surface rules.
- threat intel analyst
- run scripts on endpoints.
- malware researcher
- search exposed assets
- create an incident in xsoar.
- add entry
- list xdr endpoints with optional filters, pagination, and sorting.
- search incidents with filters in cortex xsoar.
- secures ai applications with runtime scanning and vulnerability assessment.
- firewall admin
- search xsiam alerts with filters.
- get audit management logs from xdr.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- manages multi-tenant hierarchies and service group configurations for mssps.
- run a playbook on an investigation in xsoar.
- xdr get incident details
- search ip ranges
- unisolate endpoints and restore network connectivity via xdr.
- incident management — list, search, create, and update incidents.
- investigates dlp incidents and manages sensitive data protection policies.
- xpanse list incidents
- xpanse list attack surface rules
- xdr scan endpoints
- initiate a scan on endpoints.
- configure xsiam datasources.
- start xql queries on xsiam.
- xsoar search integrations
- update an attack surface rule.
- get incident details
- search for integration instances in cortex xsoar.
- xdr list incidents
- get audit management logs from xpanse.
- add an entry to an investigation in xsoar.
- investigates security incidents, triages alerts, and coordinates response actions.
- start an xql query on xdr.
- run script
- update an existing incident in cortex xsoar.
- list xsiam endpoints with filters.
- search xsiam endpoints.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- xpanse update attack surface rule
- xdr get script results
- run a script on endpoints.
- search xdr endpoints.
- cloud security posture management, compliance monitoring, and workload protection.
- mssp operator
- search xdr incidents with filters.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- cybersecurity
- xdr unisolate endpoints
- manages multi-tenant security operations at scale for managed service providers.
- search xpanse incidents with filters.
- get xpanse incidents.
- xsoar search integration instances
- designs and implements network security architectures and policies.
- scan endpoints
- isolate endpoints
- search xdr alerts
- list xdr incidents with optional filters, pagination, and sorting.
- browser security admin
- update an xdr incident.
- search xsiam alerts.
- xsoar add entry
- xdr
- cloud security engineer
- search for integration instances in xsoar.
- get xsiam xql query results
- security operations
- list xsiam alerts with optional filters and pagination.
- scan endpoints.
- list xsiam assets with optional filters.
- sd wan operator
- digital experience monitoring, log management, and best practice assessment.
- network security
- get script execution results.
- get xql query results
- xsoar create incident
- search incidents
- search xsoar integrations.
- search for available integrations in cortex xsoar.
- monitors network health, performance, and digital experience metrics.
- xsiam get xql results
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- red team operator
- cloud security
- isolate endpoints from the network.
- list xsiam incidents with optional filters and pagination.
- run a script on endpoints via xdr.
- search xsiam incidents
- xsoar run playbook
- xdr get audit logs
- isolate endpoints.
- search xpanse incidents
- isolate endpoints from the network via xdr.
- list available playbooks in cortex xsoar.
- xsiam configure datasource
- firewall policy management, network objects, and cloud-native firewall configuration.
- search xdr alerts with filters.
- analyzes suspicious files and samples for malware characteristics.
- data protection analyst
- create incident
- search xsiam incidents.
- detection and response
- get exposed services from xpanse.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- xpanse list ip ranges
- list xdr alerts with optional filters, pagination, and sorting.
- xsiam list incidents
- xdr list alerts
- ai security engineer
- get owned ip ranges from xpanse.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- search xsiam alerts
- xdr run script
- add an entry to an investigation in cortex xsoar.
- configure a datasource for xsiam ingestion.
- get xql query results from xdr.
- xdr isolate endpoints
- proactively searches for threats and iocs across telemetry data.
- executes containment, eradication, and recovery actions during security incidents.
- start an xql query on xsiam.
- manages enterprise browser policies and secure browsing configurations.
- get script results
- soc analyst
- unisolate endpoints
- get xql query results from xsiam.
- create a new investigation in xsoar.
- xsiam list endpoints
- get investigation
- vulnerability manager
- firewall
- run playbook
- list xdr endpoints with filters.
- get details for a specific exposed asset.
- create investigation
- initiate a scan on endpoints via xdr.
- search xpanse incidents.
- configure datasource
- palo alto networks
- search xsiam assets
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- compliance team
- manages service accounts, roles, and access policies for platform api access.
- get internet-exposed assets from xpanse.
- search exposed services.
- list xsiam endpoints with optional filters.
- saas security admin
- update attack surface rule
- create a new incident in cortex xsoar.
- run a playbook on an investigation in cortex xsoar.
- search services
- xsiam get management logs
- sase admin
- xsoar get investigation
- get a specific investigation.
- start xql query
- threat hunter
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- xpanse get asset details
- xsiam list alerts
- get incident details from xdr.
- search integration instances
- tenant operator
- incident responder
- threat intelligence
- start xsiam xql query
- update incident
- run xsoar playbooks.
- search owned ip ranges.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- designs sase and sd-wan network architectures for secure remote access.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- xdr start xql query
- xdr get xql results
- xsiam list assets
- get or update a specific incident.
- update xpanse incident
- search internet-exposed assets.
- search for available integrations in xsoar.
- list incidents
- get xpanse audit logs.
- unisolate endpoints and restore network connectivity.
- subscription manager
- list xdr incidents.
- search xdr alerts.
- search endpoints
- enterprise browser policy management and secure browsing.
- list and manage xsoar playbooks.
- list xsiam assets with filters.
- sre
- xsoar create investigation
- researches threat actors, malware campaigns, and vulnerability trends.
- add entries to investigations.
- start xql queries on xdr.
- get asset details
- update an xpanse incident.
- incident response
- search attack surface rules
- list available playbooks in xsoar.
- network architect
- retrieve a specific investigation by id from xsoar.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- xpanse list exposed assets
- create xsoar investigations.
- get extra data for a specific xdr incident.
- soc
- monitors and remediates cloud security misconfigurations and compliance violations.
- xsoar update incident
- manages logging infrastructure, integrations, and platform automation.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- get attack surface rules from xpanse.
- search xsiam incidents with filters.
- sase
- get internet exposure details for specific assets from xpanse.
- get xsiam management logs.
- network security engineer
- platform engineer
- iam admin
- search incidents with filters.
- network operations
- search xsiam assets.
- xdr list endpoints
- search xsiam endpoints
- get management logs from xsiam.
- get xpanse audit logs
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
