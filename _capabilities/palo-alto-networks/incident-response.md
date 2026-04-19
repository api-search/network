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
- secures ai applications with runtime scanning and vulnerability assessment.
- compliance officer
- get owned ip ranges from xpanse.
- get xpanse audit logs
- xdr
- search xdr endpoints.
- xsiam start xql query
- vulnerability manager
- soar
- retrieve a specific investigation by id from cortex xsoar.
- xsiam get management logs
- network security engineer
- search internet-exposed assets.
- search xpanse incidents.
- search incidents with filters.
- get xdr audit logs
- xsiam list alerts
- update xpanse incident
- search incidents with filters in cortex xsoar.
- create investigation
- manages service accounts, roles, and access policies for platform api access.
- xdr list alerts
- threat hunter
- search xsiam assets.
- get xsiam xql query results
- update an attack surface rule in xpanse.
- browser security admin
- get audit management logs from xpanse.
- incident response
- configure a datasource for xsiam ingestion.
- search xsoar integrations.
- soc analyst
- platform engineer
- get xsiam management logs.
- get a specific investigation.
- manages logging infrastructure, integrations, and platform automation.
- network architect
- digital experience monitoring, log management, and best practice assessment.
- saas security admin
- xpanse update attack surface rule
- search xsiam alerts.
- tenant operator
- search xsiam alerts
- xdr get xql results
- xsiam list incidents
- search exposed assets
- xdr start xql query
- xdr get audit logs
- identity and access management, tenant hierarchies, and subscription management.
- search services
- soc
- xdr run script
- xpanse list services
- iam admin
- ai security engineer
- xdr isolate endpoints
- subscription manager
- get xsiam management logs
- network operations
- monitors network health, performance, and digital experience metrics.
- manages multi-tenant security operations at scale for managed service providers.
- enterprise browser policy management and secure browsing.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- list xdr endpoints with filters.
- get asset details
- search xsiam endpoints
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- create incident
- update an existing incident in cortex xsoar.
- search xsiam assets
- sase
- sase admin
- list xdr incidents.
- list incidents
- initiate a scan on endpoints.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- search xpanse incidents
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- retrieve a specific investigation by id from xsoar.
- firewall
- network security
- designs sase and sd-wan network architectures for secure remote access.
- xdr list endpoints
- search xsiam incidents.
- security operations
- unisolate endpoints
- get attack surface rules from xpanse.
- create an incident in xsoar.
- xsiam list endpoints
- search incidents
- create a new investigation in cortex xsoar.
- xsoar list playbooks
- researches threat actors, malware campaigns, and vulnerability trends.
- search xdr incidents with filters.
- enterprise it
- search exposed services.
- update an xpanse incident.
- get investigation
- search xdr alerts.
- list xsiam alerts with optional filters and pagination.
- xdr update incident
- search xdr alerts with filters.
- run a playbook on an investigation in xsoar.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- search xsiam incidents with filters.
- configure datasource
- scan endpoints
- start an xql query on xdr.
- run a script on endpoints via xdr.
- unisolate endpoints and restore network connectivity via xdr.
- run a script on endpoints.
- incident responder
- initiate a scan on endpoints via xdr.
- add an entry to an investigation in cortex xsoar.
- search endpoints
- cloud security posture management, compliance monitoring, and workload protection.
- get extra data for a specific xdr incident.
- designs and implements network security architectures and policies.
- conducts automated adversarial testing against ai systems and llm applications.
- isolate endpoints from the network via xdr.
- update an xdr incident.
- list xdr incidents with optional filters, pagination, and sorting.
- add entries to investigations.
- search attack surface rules.
- get audit management logs from xdr.
- get incident details from xdr.
- unisolate endpoints and restore network connectivity.
- retrieve a specific incident by id from cortex xsoar.
- get xpanse incidents.
- xsoar search integration instances
- create a new investigation in xsoar.
- search xsiam endpoints.
- search integrations
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- xdr list incidents
- search for integration instances in xsoar.
- xdr unisolate endpoints
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- cybersecurity
- threat intel analyst
- unisolate endpoints.
- get xql query results
- xpanse list ip ranges
- xsoar run playbook
- xsoar add entry
- update an attack surface rule.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- manages enterprise browser policies and secure browsing configurations.
- cloud security
- get exposed services from xpanse.
- get or update a specific incident.
- xpanse list exposed assets
- incident management — list, search, create, and update incidents.
- search for integration instances in cortex xsoar.
- proactively searches for threats and iocs across telemetry data.
- xsiam get xql results
- start xql queries on xdr.
- firewall admin
- list xsiam assets with optional filters.
- get internet-exposed assets from xpanse.
- run scripts on endpoints.
- get script execution results from xdr.
- get management logs from xsiam.
- get xql query results from xdr.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- xpanse get audit logs
- search xpanse incidents with filters.
- data protection analyst
- isolate endpoints from the network.
- red team operator
- firewall policy management, network objects, and cloud-native firewall configuration.
- search xsiam alerts with filters.
- sd wan operator
- start xql queries on xsiam.
- search xsiam incidents
- investigates security incidents, triages alerts, and coordinates response actions.
- get xdr audit logs.
- start xsiam xql query
- add an entry to an investigation in xsoar.
- list playbooks
- search for available integrations in xsoar.
- xsoar update incident
- search owned ip ranges.
- list xdr endpoints with optional filters, pagination, and sorting.
- list available playbooks in cortex xsoar.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- xpanse list attack surface rules
- detection and response
- executes containment, eradication, and recovery actions during security incidents.
- search ip ranges
- search attack surface rules
- xpanse update incident
- update attack surface rule
- get incident details
- xsoar get incident
- manages multi-tenant hierarchies and service group configurations for mssps.
- get xpanse audit logs.
- update incident
- manage enterprise browser policies, user sessions, and deployments.
- xdr scan endpoints
- analyzes suspicious files and samples for malware characteristics.
- xsoar get investigation
- search integration instances
- mssp operator
- configure xsiam datasources.
- sre
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- list xdr alerts with optional filters, pagination, and sorting.
- ai runtime security scanning and automated red teaming for ai applications.
- search xsoar integration instances.
- malware researcher
- compliance team
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- xsoar create investigation
- create a new incident in cortex xsoar.
- data loss prevention, saas security monitoring, and identity security posture.
- run playbook
- threat intelligence
- list xsiam endpoints with filters.
- xsoar create incident
- run xsoar playbooks.
- xsiam list assets
- run script
- xdr get incident details
- palo alto networks
- xdr get script results
- xsoar search incidents
- get script results
- list xsiam incidents with optional filters and pagination.
- isolate endpoints.
- xpanse get asset details
- scan endpoints.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- get details for a specific exposed asset.
- run a playbook on an investigation in cortex xsoar.
- start an xql query on xsiam.
- list xsiam endpoints with optional filters.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- xpanse list incidents
- get xql query results from xsiam.
- create xsoar investigations.
- add entry
- search for available integrations in cortex xsoar.
- list and manage xsoar playbooks.
- cloud security engineer
- get internet exposure details for specific assets from xpanse.
- start xql query
- xsiam configure datasource
- isolate endpoints
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- list xsiam assets with filters.
- search xdr alerts
- get script execution results.
- list available playbooks in xsoar.
- monitors and remediates cloud security misconfigurations and compliance violations.
- investigates dlp incidents and manages sensitive data protection policies.
- xsoar search integrations
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
