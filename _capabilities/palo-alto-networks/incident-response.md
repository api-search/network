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
- get incident details from xdr.
- create investigation
- xsiam get xql results
- xdr run script
- search xsiam incidents.
- xpanse list services
- search xdr endpoints.
- update an existing incident in cortex xsoar.
- manage enterprise browser policies, user sessions, and deployments.
- xsoar search integration instances
- data protection analyst
- list and manage xsoar playbooks.
- iam admin
- compliance team
- initiate a scan on endpoints via xdr.
- network operations
- cloud security
- xsoar create investigation
- search for available integrations in cortex xsoar.
- start xql query
- get a specific investigation.
- search exposed assets
- get script results
- xpanse get asset details
- malware researcher
- search xpanse incidents with filters.
- palo alto networks
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- xsoar create incident
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- incident response
- add entries to investigations.
- xsoar get investigation
- get xql query results
- xdr list endpoints
- incident responder
- xdr
- detection and response
- search xsiam alerts.
- isolate endpoints
- list playbooks
- search xsiam incidents
- search xsiam alerts with filters.
- xsoar get incident
- xdr start xql query
- platform engineer
- executes containment, eradication, and recovery actions during security incidents.
- search internet-exposed assets.
- sd wan operator
- xdr get xql results
- analyzes suspicious files and samples for malware characteristics.
- start xql queries on xsiam.
- search xsiam alerts
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- vulnerability manager
- list available playbooks in cortex xsoar.
- search incidents
- start xql queries on xdr.
- get internet exposure details for specific assets from xpanse.
- scan endpoints.
- list xsiam assets with optional filters.
- list xdr incidents.
- search xsiam endpoints.
- xdr list alerts
- get investigation
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- search incidents with filters.
- update an attack surface rule.
- get xdr audit logs.
- browser security admin
- create xsoar investigations.
- run a playbook on an investigation in xsoar.
- get incident details
- ai runtime security scanning and automated red teaming for ai applications.
- create incident
- xsiam get management logs
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- xdr unisolate endpoints
- xpanse list exposed assets
- threat intel analyst
- red team operator
- create a new investigation in cortex xsoar.
- xdr get audit logs
- tenant operator
- manages logging infrastructure, integrations, and platform automation.
- get xql query results from xsiam.
- get audit management logs from xpanse.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- monitors and remediates cloud security misconfigurations and compliance violations.
- cybersecurity
- get xql query results from xdr.
- search for available integrations in xsoar.
- firewall admin
- add an entry to an investigation in cortex xsoar.
- get owned ip ranges from xpanse.
- secures ai applications with runtime scanning and vulnerability assessment.
- retrieve a specific investigation by id from xsoar.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- run xsoar playbooks.
- search exposed services.
- firewall policy management, network objects, and cloud-native firewall configuration.
- search xsiam assets.
- run scripts on endpoints.
- list xdr endpoints with filters.
- search xsoar integrations.
- xpanse list attack surface rules
- compliance officer
- secure access service edge with remote networking, sd-wan, and zero trust access.
- configure a datasource for xsiam ingestion.
- update xpanse incident
- xdr list incidents
- xdr get script results
- sase admin
- investigates dlp incidents and manages sensitive data protection policies.
- isolate endpoints from the network.
- list xsiam alerts with optional filters and pagination.
- retrieve a specific investigation by id from cortex xsoar.
- xsiam configure datasource
- cloud security posture management, compliance monitoring, and workload protection.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- run script
- isolate endpoints from the network via xdr.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- search ip ranges
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- search attack surface rules
- xsoar search incidents
- xsiam list assets
- network architect
- mssp operator
- search endpoints
- xsoar add entry
- get xpanse audit logs.
- search integrations
- soc
- isolate endpoints.
- get xpanse audit logs
- xpanse list ip ranges
- network security engineer
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- scan endpoints
- data loss prevention, saas security monitoring, and identity security posture.
- search services
- list xdr endpoints with optional filters, pagination, and sorting.
- search xpanse incidents
- list xsiam endpoints with filters.
- list incidents
- search xdr alerts.
- list xsiam incidents with optional filters and pagination.
- create a new investigation in xsoar.
- list xdr alerts with optional filters, pagination, and sorting.
- start xsiam xql query
- researches threat actors, malware campaigns, and vulnerability trends.
- search xdr alerts with filters.
- manages service accounts, roles, and access policies for platform api access.
- update incident
- search attack surface rules.
- saas security admin
- get internet-exposed assets from xpanse.
- search for integration instances in xsoar.
- sre
- manages multi-tenant security operations at scale for managed service providers.
- digital experience monitoring, log management, and best practice assessment.
- get extra data for a specific xdr incident.
- update an xdr incident.
- manages multi-tenant hierarchies and service group configurations for mssps.
- threat hunter
- create an incident in xsoar.
- retrieve a specific incident by id from cortex xsoar.
- run a script on endpoints via xdr.
- soc analyst
- initiate a scan on endpoints.
- update an attack surface rule in xpanse.
- xsoar update incident
- list xsiam endpoints with optional filters.
- manages enterprise browser policies and secure browsing configurations.
- soar
- xdr update incident
- xpanse get audit logs
- get xpanse incidents.
- subscription manager
- unisolate endpoints.
- run playbook
- search xdr incidents with filters.
- xdr isolate endpoints
- create a new incident in cortex xsoar.
- unisolate endpoints
- cloud security engineer
- incident management — list, search, create, and update incidents.
- xsoar search integrations
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- get audit management logs from xdr.
- search for integration instances in cortex xsoar.
- sase
- security operations
- designs and implements network security architectures and policies.
- xsiam list alerts
- threat intelligence
- configure datasource
- conducts automated adversarial testing against ai systems and llm applications.
- add an entry to an investigation in xsoar.
- list xsiam assets with filters.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- list xdr incidents with optional filters, pagination, and sorting.
- search xsiam incidents with filters.
- get script execution results.
- search owned ip ranges.
- update an xpanse incident.
- designs sase and sd-wan network architectures for secure remote access.
- get script execution results from xdr.
- search incidents with filters in cortex xsoar.
- list available playbooks in xsoar.
- get xdr audit logs
- xsiam list incidents
- enterprise browser policy management and secure browsing.
- xsoar run playbook
- start an xql query on xsiam.
- get xsiam management logs.
- firewall
- xdr get incident details
- get xsiam management logs
- get asset details
- search xpanse incidents.
- search xsiam assets
- get exposed services from xpanse.
- configure xsiam datasources.
- proactively searches for threats and iocs across telemetry data.
- xpanse update incident
- start an xql query on xdr.
- search xdr alerts
- enterprise it
- network security
- update attack surface rule
- get management logs from xsiam.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- xsiam list endpoints
- search xsoar integration instances.
- unisolate endpoints and restore network connectivity via xdr.
- ai security engineer
- investigates security incidents, triages alerts, and coordinates response actions.
- get details for a specific exposed asset.
- get or update a specific incident.
- xsoar list playbooks
- xpanse update attack surface rule
- get attack surface rules from xpanse.
- run a script on endpoints.
- xpanse list incidents
- run a playbook on an investigation in cortex xsoar.
- search integration instances
- monitors network health, performance, and digital experience metrics.
- add entry
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- xdr scan endpoints
- xsiam start xql query
- search xsiam endpoints
- get xsiam xql query results
- unisolate endpoints and restore network connectivity.
- identity and access management, tenant hierarchies, and subscription management.
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
