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
- run a script on endpoints via xdr.
- search xsiam incidents
- search incidents
- search owned ip ranges.
- update an xdr incident.
- palo alto networks
- unisolate endpoints and restore network connectivity via xdr.
- unisolate endpoints
- retrieve a specific investigation by id from xsoar.
- designs sase and sd-wan network architectures for secure remote access.
- network security engineer
- list playbooks
- isolate endpoints.
- xsiam list assets
- secures ai applications with runtime scanning and vulnerability assessment.
- xdr list alerts
- xdr scan endpoints
- sase admin
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- xpanse get audit logs
- get investigation
- incident management — list, search, create, and update incidents.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- add an entry to an investigation in xsoar.
- xdr isolate endpoints
- xpanse get asset details
- list xdr endpoints with optional filters, pagination, and sorting.
- xdr
- search xdr alerts with filters.
- search services
- start xql queries on xsiam.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- get xql query results from xsiam.
- search exposed services.
- get audit management logs from xdr.
- search xpanse incidents
- get attack surface rules from xpanse.
- configure xsiam datasources.
- search ip ranges
- run xsoar playbooks.
- add an entry to an investigation in cortex xsoar.
- enterprise browser policy management and secure browsing.
- xsiam get management logs
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- search endpoints
- detection and response
- search integrations
- secure access service edge with remote networking, sd-wan, and zero trust access.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- ai security engineer
- data protection analyst
- network architect
- search xsiam endpoints
- data loss prevention, saas security monitoring, and identity security posture.
- xdr get incident details
- get incident details from xdr.
- saas security admin
- search xsiam alerts.
- update incident
- get xql query results from xdr.
- search xdr incidents with filters.
- xpanse list attack surface rules
- search xpanse incidents.
- get xdr audit logs
- cloud security engineer
- manages multi-tenant hierarchies and service group configurations for mssps.
- search xsiam endpoints.
- network security
- create an incident in xsoar.
- run playbook
- xdr unisolate endpoints
- xsoar search integration instances
- manages enterprise browser policies and secure browsing configurations.
- get internet-exposed assets from xpanse.
- isolate endpoints from the network via xdr.
- soar
- xpanse list exposed assets
- xpanse list incidents
- run a playbook on an investigation in xsoar.
- list xsiam endpoints with optional filters.
- get xsiam management logs
- compliance team
- xsiam list incidents
- search xsiam alerts with filters.
- search xpanse incidents with filters.
- investigates dlp incidents and manages sensitive data protection policies.
- xdr update incident
- update an xpanse incident.
- xdr get audit logs
- scan endpoints.
- search for integration instances in cortex xsoar.
- researches threat actors, malware campaigns, and vulnerability trends.
- get xpanse audit logs.
- xdr get xql results
- subscription manager
- get script execution results from xdr.
- create a new investigation in cortex xsoar.
- compliance officer
- xsiam list alerts
- run a playbook on an investigation in cortex xsoar.
- initiate a scan on endpoints via xdr.
- search xsiam incidents.
- get xpanse incidents.
- tenant operator
- xsiam configure datasource
- xsiam get xql results
- vulnerability manager
- executes containment, eradication, and recovery actions during security incidents.
- cybersecurity
- list and manage xsoar playbooks.
- get a specific investigation.
- list xsiam assets with optional filters.
- get xdr audit logs.
- malware researcher
- configure datasource
- designs and implements network security architectures and policies.
- xsoar create incident
- xpanse update attack surface rule
- get management logs from xsiam.
- incident responder
- get xsiam management logs.
- xsoar search incidents
- mssp operator
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- list xdr alerts with optional filters, pagination, and sorting.
- get script results
- start xql queries on xdr.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- list xdr incidents.
- manages service accounts, roles, and access policies for platform api access.
- threat intel analyst
- search exposed assets
- search incidents with filters.
- list xsiam assets with filters.
- xdr list incidents
- xsoar get incident
- xdr list endpoints
- xsiam list endpoints
- xpanse update incident
- xpanse list services
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- firewall admin
- soc analyst
- proactively searches for threats and iocs across telemetry data.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- xsoar update incident
- run a script on endpoints.
- xsoar search integrations
- xsoar create investigation
- get xpanse audit logs
- search xsoar integrations.
- update attack surface rule
- security operations
- isolate endpoints from the network.
- update an attack surface rule in xpanse.
- retrieve a specific incident by id from cortex xsoar.
- search for integration instances in xsoar.
- list incidents
- search xdr endpoints.
- list xsiam incidents with optional filters and pagination.
- network operations
- enterprise it
- manages logging infrastructure, integrations, and platform automation.
- browser security admin
- get audit management logs from xpanse.
- threat hunter
- run script
- xsoar add entry
- get extra data for a specific xdr incident.
- add entries to investigations.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- get internet exposure details for specific assets from xpanse.
- add entry
- create xsoar investigations.
- search xdr alerts
- xdr run script
- search for available integrations in xsoar.
- update an existing incident in cortex xsoar.
- analyzes suspicious files and samples for malware characteristics.
- sase
- start an xql query on xsiam.
- list xsiam endpoints with filters.
- search internet-exposed assets.
- get owned ip ranges from xpanse.
- retrieve a specific investigation by id from cortex xsoar.
- start an xql query on xdr.
- xdr get script results
- monitors and remediates cloud security misconfigurations and compliance violations.
- xsiam start xql query
- search incidents with filters in cortex xsoar.
- soc
- create incident
- unisolate endpoints.
- run scripts on endpoints.
- list available playbooks in xsoar.
- initiate a scan on endpoints.
- search xsoar integration instances.
- start xql query
- xsoar get investigation
- xsoar list playbooks
- monitors network health, performance, and digital experience metrics.
- identity and access management, tenant hierarchies, and subscription management.
- ai runtime security scanning and automated red teaming for ai applications.
- unisolate endpoints and restore network connectivity.
- scan endpoints
- get script execution results.
- create a new investigation in xsoar.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- platform engineer
- search xsiam assets.
- search integration instances
- iam admin
- digital experience monitoring, log management, and best practice assessment.
- search attack surface rules
- get xsiam xql query results
- configure a datasource for xsiam ingestion.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- get or update a specific incident.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- get exposed services from xpanse.
- list xsiam alerts with optional filters and pagination.
- search xsiam incidents with filters.
- get xql query results
- start xsiam xql query
- list available playbooks in cortex xsoar.
- red team operator
- get asset details
- firewall policy management, network objects, and cloud-native firewall configuration.
- search xdr alerts.
- search xsiam assets
- incident response
- sre
- manages multi-tenant security operations at scale for managed service providers.
- get details for a specific exposed asset.
- threat intelligence
- list xdr incidents with optional filters, pagination, and sorting.
- xpanse list ip ranges
- create investigation
- update an attack surface rule.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- conducts automated adversarial testing against ai systems and llm applications.
- investigates security incidents, triages alerts, and coordinates response actions.
- cloud security
- firewall
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- cloud security posture management, compliance monitoring, and workload protection.
- update xpanse incident
- search for available integrations in cortex xsoar.
- manage enterprise browser policies, user sessions, and deployments.
- xsoar run playbook
- get incident details
- xdr start xql query
- create a new incident in cortex xsoar.
- list xdr endpoints with filters.
- search xsiam alerts
- isolate endpoints
- search attack surface rules.
- sd wan operator
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
