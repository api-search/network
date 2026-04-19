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
- list xsiam endpoints with optional filters.
- get owned ip ranges from xpanse.
- xdr get audit logs
- scan endpoints
- search incidents
- enterprise it
- search internet-exposed assets.
- get a specific investigation.
- xsoar create incident
- compliance officer
- xsoar list playbooks
- data protection analyst
- search integration instances
- designs sase and sd-wan network architectures for secure remote access.
- update an attack surface rule in xpanse.
- xsoar search integrations
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- xdr scan endpoints
- soc
- malware researcher
- run a script on endpoints.
- ai runtime security scanning and automated red teaming for ai applications.
- network security
- get extra data for a specific xdr incident.
- update an xdr incident.
- researches threat actors, malware campaigns, and vulnerability trends.
- manages enterprise browser policies and secure browsing configurations.
- xsoar add entry
- search for integration instances in cortex xsoar.
- cloud security posture management, compliance monitoring, and workload protection.
- incident response
- get script results
- xpanse get audit logs
- xsiam list incidents
- unisolate endpoints.
- get audit management logs from xpanse.
- xsiam get xql results
- list incidents
- start xql queries on xsiam.
- start xsiam xql query
- xdr start xql query
- list available playbooks in cortex xsoar.
- get details for a specific exposed asset.
- xsiam get management logs
- search attack surface rules
- isolate endpoints.
- search ip ranges
- start an xql query on xsiam.
- xdr get incident details
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- search xsiam incidents
- isolate endpoints
- platform engineer
- proactively searches for threats and iocs across telemetry data.
- xpanse list services
- get asset details
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- analyzes suspicious files and samples for malware characteristics.
- search xsiam incidents with filters.
- firewall policy management, network objects, and cloud-native firewall configuration.
- search integrations
- monitors network health, performance, and digital experience metrics.
- vulnerability manager
- incident management — list, search, create, and update incidents.
- security operations
- start an xql query on xdr.
- run a playbook on an investigation in xsoar.
- list xsiam alerts with optional filters and pagination.
- conducts automated adversarial testing against ai systems and llm applications.
- manages multi-tenant security operations at scale for managed service providers.
- create a new investigation in cortex xsoar.
- manages logging infrastructure, integrations, and platform automation.
- get script execution results from xdr.
- list xsiam assets with filters.
- xpanse list exposed assets
- create a new investigation in xsoar.
- get attack surface rules from xpanse.
- create investigation
- unisolate endpoints and restore network connectivity via xdr.
- search owned ip ranges.
- compliance team
- list xdr endpoints with filters.
- list available playbooks in xsoar.
- designs and implements network security architectures and policies.
- manages multi-tenant hierarchies and service group configurations for mssps.
- unisolate endpoints
- search xsiam endpoints.
- isolate endpoints from the network via xdr.
- search xdr alerts with filters.
- configure a datasource for xsiam ingestion.
- xpanse get asset details
- get xpanse incidents.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- xsoar get incident
- xsiam list endpoints
- unisolate endpoints and restore network connectivity.
- add entry
- list xsiam incidents with optional filters and pagination.
- list xsiam assets with optional filters.
- saas security admin
- xdr get xql results
- list xdr incidents.
- xpanse list incidents
- incident responder
- get xpanse audit logs.
- tenant operator
- isolate endpoints from the network.
- get xsiam management logs
- secure access service edge with remote networking, sd-wan, and zero trust access.
- xsiam list alerts
- get xdr audit logs.
- cloud security engineer
- search services
- search xpanse incidents.
- xpanse list ip ranges
- update xpanse incident
- add an entry to an investigation in xsoar.
- search exposed assets
- list xdr alerts with optional filters, pagination, and sorting.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- search xdr endpoints.
- firewall
- create xsoar investigations.
- search xpanse incidents
- get management logs from xsiam.
- search xsiam alerts.
- search exposed services.
- get xpanse audit logs
- xsiam configure datasource
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- sase
- get audit management logs from xdr.
- get xql query results
- threat intel analyst
- initiate a scan on endpoints via xdr.
- sd wan operator
- manage enterprise browser policies, user sessions, and deployments.
- xsoar create investigation
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- search for integration instances in xsoar.
- network operations
- get xql query results from xsiam.
- xpanse list attack surface rules
- search xsiam assets
- get script execution results.
- xsoar run playbook
- search xsoar integrations.
- manages service accounts, roles, and access policies for platform api access.
- search xdr alerts
- start xql queries on xdr.
- run a playbook on an investigation in cortex xsoar.
- threat hunter
- update an xpanse incident.
- configure xsiam datasources.
- update an attack surface rule.
- retrieve a specific investigation by id from cortex xsoar.
- cybersecurity
- run scripts on endpoints.
- run a script on endpoints via xdr.
- get incident details
- soc analyst
- mssp operator
- firewall admin
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- xdr update incident
- identity and access management, tenant hierarchies, and subscription management.
- retrieve a specific incident by id from cortex xsoar.
- monitors and remediates cloud security misconfigurations and compliance violations.
- xdr list endpoints
- xsoar update incident
- search incidents with filters.
- start xql query
- get xsiam xql query results
- get investigation
- add entries to investigations.
- configure datasource
- update an existing incident in cortex xsoar.
- browser security admin
- get internet exposure details for specific assets from xpanse.
- sase admin
- get internet-exposed assets from xpanse.
- threat intelligence
- palo alto networks
- get incident details from xdr.
- add an entry to an investigation in cortex xsoar.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- soar
- run playbook
- list playbooks
- investigates security incidents, triages alerts, and coordinates response actions.
- create an incident in xsoar.
- search xdr alerts.
- search incidents with filters in cortex xsoar.
- xsoar search incidents
- cloud security
- list and manage xsoar playbooks.
- network architect
- run script
- list xdr incidents with optional filters, pagination, and sorting.
- get exposed services from xpanse.
- xdr list incidents
- create a new incident in cortex xsoar.
- retrieve a specific investigation by id from xsoar.
- get xsiam management logs.
- executes containment, eradication, and recovery actions during security incidents.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- search xdr incidents with filters.
- create incident
- search attack surface rules.
- ai security engineer
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- xdr
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- sre
- update incident
- network security engineer
- search xsiam alerts with filters.
- iam admin
- detection and response
- search endpoints
- get xdr audit logs
- xsoar get investigation
- search xsiam endpoints
- xsoar search integration instances
- data loss prevention, saas security monitoring, and identity security posture.
- list xsiam endpoints with filters.
- digital experience monitoring, log management, and best practice assessment.
- update attack surface rule
- xdr unisolate endpoints
- search for available integrations in cortex xsoar.
- secures ai applications with runtime scanning and vulnerability assessment.
- search xsiam incidents.
- red team operator
- xdr run script
- xdr get script results
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- xpanse update attack surface rule
- enterprise browser policy management and secure browsing.
- xdr list alerts
- xdr isolate endpoints
- search for available integrations in xsoar.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- search xpanse incidents with filters.
- search xsiam alerts
- list xdr endpoints with optional filters, pagination, and sorting.
- scan endpoints.
- run xsoar playbooks.
- initiate a scan on endpoints.
- get xql query results from xdr.
- xsiam list assets
- search xsoar integration instances.
- investigates dlp incidents and manages sensitive data protection policies.
- xsiam start xql query
- xpanse update incident
- subscription manager
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- get or update a specific incident.
- search xsiam assets.
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
