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
- unisolate endpoints and restore network connectivity via xdr.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- list playbooks
- xsoar run playbook
- update an xpanse incident.
- search for integration instances in xsoar.
- platform engineer
- get incident details from xdr.
- saas security admin
- xpanse update incident
- soc
- get or update a specific incident.
- search xdr alerts with filters.
- get internet-exposed assets from xpanse.
- enterprise it
- start an xql query on xsiam.
- get a specific investigation.
- threat hunter
- add an entry to an investigation in xsoar.
- network operations
- get xdr audit logs.
- search xsiam alerts.
- list available playbooks in cortex xsoar.
- threat intel analyst
- compliance team
- search xsiam alerts with filters.
- get audit management logs from xdr.
- get xql query results from xsiam.
- incident response
- initiate a scan on endpoints via xdr.
- add an entry to an investigation in cortex xsoar.
- create incident
- sre
- executes containment, eradication, and recovery actions during security incidents.
- manages multi-tenant hierarchies and service group configurations for mssps.
- firewall
- sase
- xsoar get incident
- xpanse list ip ranges
- incident responder
- network architect
- xpanse list services
- update an existing incident in cortex xsoar.
- designs sase and sd-wan network architectures for secure remote access.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- get attack surface rules from xpanse.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- search services
- retrieve a specific incident by id from cortex xsoar.
- xsoar get investigation
- cloud security
- scan endpoints
- xsiam list incidents
- firewall admin
- add entries to investigations.
- xsiam configure datasource
- search xsoar integration instances.
- manages service accounts, roles, and access policies for platform api access.
- run a playbook on an investigation in xsoar.
- list xsiam endpoints with optional filters.
- designs and implements network security architectures and policies.
- search xsiam assets.
- run a script on endpoints.
- xpanse list exposed assets
- search xsiam endpoints
- xdr list alerts
- search integration instances
- xdr unisolate endpoints
- update attack surface rule
- create a new investigation in cortex xsoar.
- search xsoar integrations.
- xsoar search integrations
- soc analyst
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- xdr list incidents
- create xsoar investigations.
- network security engineer
- list xsiam assets with optional filters.
- xsiam list alerts
- create a new incident in cortex xsoar.
- xdr update incident
- xsoar search integration instances
- get xsiam management logs.
- monitors and remediates cloud security misconfigurations and compliance violations.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- enterprise browser policy management and secure browsing.
- xsoar search incidents
- vulnerability manager
- cloud security engineer
- manage enterprise browser policies, user sessions, and deployments.
- list xdr incidents.
- search for available integrations in xsoar.
- xdr start xql query
- firewall policy management, network objects, and cloud-native firewall configuration.
- update an attack surface rule in xpanse.
- get xql query results from xdr.
- search xsiam endpoints.
- search endpoints
- xsiam get xql results
- data loss prevention, saas security monitoring, and identity security posture.
- malware researcher
- create a new investigation in xsoar.
- search xpanse incidents with filters.
- xsoar create investigation
- soar
- xpanse get asset details
- red team operator
- list xsiam endpoints with filters.
- get xql query results
- start xsiam xql query
- isolate endpoints
- list xsiam alerts with optional filters and pagination.
- configure datasource
- secure access service edge with remote networking, sd-wan, and zero trust access.
- search xpanse incidents
- xdr get incident details
- search exposed services.
- list xsiam incidents with optional filters and pagination.
- xpanse list attack surface rules
- investigates security incidents, triages alerts, and coordinates response actions.
- run a playbook on an investigation in cortex xsoar.
- search attack surface rules.
- update an xdr incident.
- list xdr endpoints with filters.
- xdr list endpoints
- investigates dlp incidents and manages sensitive data protection policies.
- xpanse update attack surface rule
- conducts automated adversarial testing against ai systems and llm applications.
- search xdr alerts
- xsiam start xql query
- search for integration instances in cortex xsoar.
- xsiam list assets
- search xpanse incidents.
- run a script on endpoints via xdr.
- compliance officer
- manages enterprise browser policies and secure browsing configurations.
- network security
- get xpanse audit logs
- xdr run script
- search owned ip ranges.
- analyzes suspicious files and samples for malware characteristics.
- search incidents with filters in cortex xsoar.
- search xdr incidents with filters.
- search xsiam alerts
- get xsiam xql query results
- get asset details
- subscription manager
- get management logs from xsiam.
- run xsoar playbooks.
- xdr isolate endpoints
- get internet exposure details for specific assets from xpanse.
- list xdr incidents with optional filters, pagination, and sorting.
- get script execution results from xdr.
- get audit management logs from xpanse.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- ai runtime security scanning and automated red teaming for ai applications.
- threat intelligence
- search xdr endpoints.
- search xdr alerts.
- list xdr alerts with optional filters, pagination, and sorting.
- cloud security posture management, compliance monitoring, and workload protection.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- list xsiam assets with filters.
- search incidents with filters.
- get xsiam management logs
- xsoar add entry
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- update an attack surface rule.
- search ip ranges
- retrieve a specific investigation by id from cortex xsoar.
- search xsiam incidents
- update xpanse incident
- scan endpoints.
- create an incident in xsoar.
- xsoar update incident
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- list xdr endpoints with optional filters, pagination, and sorting.
- ai security engineer
- initiate a scan on endpoints.
- run playbook
- retrieve a specific investigation by id from xsoar.
- get extra data for a specific xdr incident.
- xdr get xql results
- configure xsiam datasources.
- search incidents
- get details for a specific exposed asset.
- mssp operator
- isolate endpoints.
- start xql queries on xsiam.
- search internet-exposed assets.
- researches threat actors, malware campaigns, and vulnerability trends.
- list and manage xsoar playbooks.
- digital experience monitoring, log management, and best practice assessment.
- run scripts on endpoints.
- palo alto networks
- search xsiam incidents with filters.
- unisolate endpoints
- start an xql query on xdr.
- get script results
- update incident
- get xpanse audit logs.
- data protection analyst
- get incident details
- xsiam get management logs
- xdr
- get xdr audit logs
- configure a datasource for xsiam ingestion.
- get script execution results.
- isolate endpoints from the network via xdr.
- iam admin
- manages logging infrastructure, integrations, and platform automation.
- start xql query
- cybersecurity
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- sase admin
- search integrations
- sd wan operator
- xsoar create incident
- monitors network health, performance, and digital experience metrics.
- get owned ip ranges from xpanse.
- start xql queries on xdr.
- unisolate endpoints.
- proactively searches for threats and iocs across telemetry data.
- search attack surface rules
- search xsiam incidents.
- xsoar list playbooks
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- identity and access management, tenant hierarchies, and subscription management.
- run script
- xdr get script results
- list incidents
- security operations
- get exposed services from xpanse.
- xdr get audit logs
- browser security admin
- secures ai applications with runtime scanning and vulnerability assessment.
- add entry
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- unisolate endpoints and restore network connectivity.
- search for available integrations in cortex xsoar.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- xdr scan endpoints
- get xpanse incidents.
- xpanse list incidents
- manages multi-tenant security operations at scale for managed service providers.
- create investigation
- isolate endpoints from the network.
- tenant operator
- search xsiam assets
- xsiam list endpoints
- detection and response
- get investigation
- incident management — list, search, create, and update incidents.
- xpanse get audit logs
- search exposed assets
- list available playbooks in xsoar.
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
