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
- list available playbooks in cortex xsoar.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- platform engineer
- get xdr audit logs
- search for integration instances in xsoar.
- xpanse list exposed assets
- xpanse get audit logs
- sd wan operator
- list available playbooks in xsoar.
- run a playbook on an investigation in xsoar.
- xsoar update incident
- xdr unisolate endpoints
- list xdr endpoints with optional filters, pagination, and sorting.
- xsoar create investigation
- unisolate endpoints
- xdr
- xsiam get xql results
- detection and response
- xpanse update attack surface rule
- create a new investigation in cortex xsoar.
- list incidents
- list xsiam assets with optional filters.
- malware researcher
- list xdr alerts with optional filters, pagination, and sorting.
- search internet-exposed assets.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- get details for a specific exposed asset.
- search xdr alerts
- get xql query results
- network architect
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- network security
- retrieve a specific incident by id from cortex xsoar.
- get script execution results from xdr.
- get xpanse incidents.
- tenant operator
- get attack surface rules from xpanse.
- get xsiam xql query results
- list and manage xsoar playbooks.
- xpanse list services
- xpanse list incidents
- get asset details
- xsoar list playbooks
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- update incident
- add an entry to an investigation in cortex xsoar.
- run xsoar playbooks.
- get management logs from xsiam.
- xdr list incidents
- update xpanse incident
- xsiam configure datasource
- search xsiam alerts.
- network security engineer
- configure xsiam datasources.
- get or update a specific incident.
- saas security admin
- search xsiam incidents.
- xsiam get management logs
- xdr start xql query
- conducts automated adversarial testing against ai systems and llm applications.
- search xsiam assets.
- executes containment, eradication, and recovery actions during security incidents.
- get xql query results from xdr.
- xdr scan endpoints
- xdr list alerts
- list xsiam endpoints with optional filters.
- sre
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- threat intelligence
- search xsiam endpoints.
- create incident
- create an incident in xsoar.
- run a script on endpoints via xdr.
- xsoar search integration instances
- initiate a scan on endpoints.
- start xql query
- xdr get audit logs
- search xpanse incidents with filters.
- create a new investigation in xsoar.
- update attack surface rule
- red team operator
- monitors and remediates cloud security misconfigurations and compliance violations.
- manages logging infrastructure, integrations, and platform automation.
- incident management — list, search, create, and update incidents.
- run playbook
- search xsiam incidents with filters.
- get internet exposure details for specific assets from xpanse.
- search exposed services.
- list playbooks
- secure access service edge with remote networking, sd-wan, and zero trust access.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- researches threat actors, malware campaigns, and vulnerability trends.
- soar
- search xdr alerts.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- isolate endpoints
- get internet-exposed assets from xpanse.
- retrieve a specific investigation by id from xsoar.
- xdr get script results
- get audit management logs from xdr.
- xsoar search integrations
- isolate endpoints from the network.
- xsoar search incidents
- unisolate endpoints and restore network connectivity via xdr.
- enterprise it
- xdr get incident details
- search xpanse incidents.
- vulnerability manager
- incident response
- search xdr endpoints.
- iam admin
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- manage enterprise browser policies, user sessions, and deployments.
- get owned ip ranges from xpanse.
- incident responder
- add entry
- xdr get xql results
- get audit management logs from xpanse.
- search owned ip ranges.
- update an existing incident in cortex xsoar.
- ai security engineer
- scan endpoints
- start an xql query on xsiam.
- start xql queries on xdr.
- investigates security incidents, triages alerts, and coordinates response actions.
- identity and access management, tenant hierarchies, and subscription management.
- start an xql query on xdr.
- ai runtime security scanning and automated red teaming for ai applications.
- browser security admin
- list xsiam endpoints with filters.
- xsoar get investigation
- search attack surface rules
- xpanse get asset details
- enterprise browser policy management and secure browsing.
- retrieve a specific investigation by id from cortex xsoar.
- search xpanse incidents
- designs and implements network security architectures and policies.
- cloud security posture management, compliance monitoring, and workload protection.
- create xsoar investigations.
- list xsiam assets with filters.
- monitors network health, performance, and digital experience metrics.
- search for integration instances in cortex xsoar.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- list xsiam alerts with optional filters and pagination.
- search xsiam endpoints
- configure datasource
- run scripts on endpoints.
- sase admin
- xpanse list attack surface rules
- xsoar run playbook
- search exposed assets
- list xdr incidents.
- get xpanse audit logs.
- security operations
- update an xpanse incident.
- isolate endpoints from the network via xdr.
- get exposed services from xpanse.
- data protection analyst
- secures ai applications with runtime scanning and vulnerability assessment.
- configure a datasource for xsiam ingestion.
- search services
- get a specific investigation.
- sase
- xdr update incident
- get xql query results from xsiam.
- search xsiam incidents
- update an xdr incident.
- search attack surface rules.
- investigates dlp incidents and manages sensitive data protection policies.
- create investigation
- xsoar create incident
- update an attack surface rule in xpanse.
- compliance team
- manages service accounts, roles, and access policies for platform api access.
- cloud security engineer
- start xsiam xql query
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- scan endpoints.
- add entries to investigations.
- get extra data for a specific xdr incident.
- xsiam list alerts
- threat hunter
- search xsiam assets
- manages enterprise browser policies and secure browsing configurations.
- cloud security
- get script results
- run script
- search xsoar integrations.
- run a script on endpoints.
- get xsiam management logs
- search incidents
- soc
- firewall policy management, network objects, and cloud-native firewall configuration.
- digital experience monitoring, log management, and best practice assessment.
- search incidents with filters in cortex xsoar.
- threat intel analyst
- xpanse list ip ranges
- initiate a scan on endpoints via xdr.
- isolate endpoints.
- mssp operator
- get investigation
- cybersecurity
- unisolate endpoints.
- xsiam list incidents
- xdr isolate endpoints
- proactively searches for threats and iocs across telemetry data.
- get script execution results.
- get xpanse audit logs
- search integrations
- manages multi-tenant security operations at scale for managed service providers.
- create a new incident in cortex xsoar.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- xsoar get incident
- search xsoar integration instances.
- list xsiam incidents with optional filters and pagination.
- unisolate endpoints and restore network connectivity.
- manages multi-tenant hierarchies and service group configurations for mssps.
- update an attack surface rule.
- analyzes suspicious files and samples for malware characteristics.
- list xdr endpoints with filters.
- get xsiam management logs.
- search xdr alerts with filters.
- subscription manager
- search xsiam alerts
- firewall
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- xsiam list assets
- xsoar add entry
- search ip ranges
- xdr list endpoints
- get incident details from xdr.
- run a playbook on an investigation in cortex xsoar.
- palo alto networks
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- search for available integrations in xsoar.
- list xdr incidents with optional filters, pagination, and sorting.
- xpanse update incident
- xsiam start xql query
- search xdr incidents with filters.
- add an entry to an investigation in xsoar.
- data loss prevention, saas security monitoring, and identity security posture.
- search endpoints
- search incidents with filters.
- xdr run script
- soc analyst
- xsiam list endpoints
- search for available integrations in cortex xsoar.
- search xsiam alerts with filters.
- designs sase and sd-wan network architectures for secure remote access.
- firewall admin
- get incident details
- start xql queries on xsiam.
- get xdr audit logs.
- network operations
- search integration instances
- compliance officer
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
