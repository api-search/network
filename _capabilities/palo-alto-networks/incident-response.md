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
- search xsoar integrations.
- palo alto networks
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- ai security engineer
- get xsiam management logs.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- xpanse update attack surface rule
- investigates security incidents, triages alerts, and coordinates response actions.
- xdr get script results
- cybersecurity
- get xql query results
- xsiam list incidents
- unisolate endpoints.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- soar
- search incidents
- run script
- create a new investigation in xsoar.
- get incident details
- xsiam get management logs
- get xdr audit logs
- soc analyst
- designs and implements network security architectures and policies.
- manages service accounts, roles, and access policies for platform api access.
- search owned ip ranges.
- start xql queries on xdr.
- search for available integrations in xsoar.
- conducts automated adversarial testing against ai systems and llm applications.
- sase
- list available playbooks in xsoar.
- search xdr alerts.
- incident management — list, search, create, and update incidents.
- sd wan operator
- list xdr endpoints with filters.
- xsoar get incident
- list xdr incidents.
- search attack surface rules.
- xdr list alerts
- add an entry to an investigation in cortex xsoar.
- xpanse list incidents
- search xsiam incidents
- secure access service edge with remote networking, sd-wan, and zero trust access.
- unisolate endpoints and restore network connectivity.
- start an xql query on xdr.
- create incident
- unisolate endpoints and restore network connectivity via xdr.
- get or update a specific incident.
- vulnerability manager
- search integration instances
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- search xpanse incidents with filters.
- run xsoar playbooks.
- researches threat actors, malware campaigns, and vulnerability trends.
- xsoar search integration instances
- search xsiam incidents with filters.
- initiate a scan on endpoints via xdr.
- xpanse list exposed assets
- list incidents
- list xsiam endpoints with filters.
- get xql query results from xdr.
- xsiam list endpoints
- get management logs from xsiam.
- xsiam list alerts
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- malware researcher
- get asset details
- mssp operator
- get a specific investigation.
- incident responder
- xdr run script
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- browser security admin
- xpanse list attack surface rules
- sase admin
- isolate endpoints
- run a script on endpoints.
- search integrations
- search xsoar integration instances.
- get xql query results from xsiam.
- run playbook
- xsoar search incidents
- manages multi-tenant security operations at scale for managed service providers.
- xpanse get asset details
- platform engineer
- get exposed services from xpanse.
- configure a datasource for xsiam ingestion.
- list xsiam endpoints with optional filters.
- search for integration instances in cortex xsoar.
- xsoar search integrations
- scan endpoints.
- xdr scan endpoints
- security operations
- cloud security engineer
- xdr get xql results
- xsoar run playbook
- get xpanse incidents.
- start xql queries on xsiam.
- xdr unisolate endpoints
- search xsiam alerts with filters.
- get xsiam management logs
- search xdr incidents with filters.
- configure datasource
- unisolate endpoints
- list xsiam alerts with optional filters and pagination.
- firewall
- search internet-exposed assets.
- network security engineer
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- xpanse list ip ranges
- monitors and remediates cloud security misconfigurations and compliance violations.
- retrieve a specific investigation by id from cortex xsoar.
- get investigation
- manages enterprise browser policies and secure browsing configurations.
- search incidents with filters.
- create a new incident in cortex xsoar.
- isolate endpoints from the network.
- start xsiam xql query
- search xsiam incidents.
- xsoar get investigation
- search xsiam endpoints.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- get script results
- create xsoar investigations.
- add entries to investigations.
- search endpoints
- compliance team
- retrieve a specific investigation by id from xsoar.
- search xpanse incidents.
- search xsiam endpoints
- get internet-exposed assets from xpanse.
- search xdr alerts
- search ip ranges
- xpanse list services
- xsoar create incident
- xdr get audit logs
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- soc
- designs sase and sd-wan network architectures for secure remote access.
- cloud security
- update incident
- cloud security posture management, compliance monitoring, and workload protection.
- run a script on endpoints via xdr.
- get internet exposure details for specific assets from xpanse.
- threat hunter
- data loss prevention, saas security monitoring, and identity security posture.
- iam admin
- xdr list incidents
- sre
- get xsiam xql query results
- search xsiam assets.
- run a playbook on an investigation in cortex xsoar.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- create a new investigation in cortex xsoar.
- list xsiam incidents with optional filters and pagination.
- get incident details from xdr.
- saas security admin
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- get extra data for a specific xdr incident.
- manages logging infrastructure, integrations, and platform automation.
- isolate endpoints from the network via xdr.
- secures ai applications with runtime scanning and vulnerability assessment.
- xsiam list assets
- list available playbooks in cortex xsoar.
- list xdr endpoints with optional filters, pagination, and sorting.
- xdr list endpoints
- manage enterprise browser policies, user sessions, and deployments.
- start xql query
- get details for a specific exposed asset.
- get audit management logs from xdr.
- proactively searches for threats and iocs across telemetry data.
- data protection analyst
- list xdr incidents with optional filters, pagination, and sorting.
- xdr isolate endpoints
- manages multi-tenant hierarchies and service group configurations for mssps.
- update attack surface rule
- firewall policy management, network objects, and cloud-native firewall configuration.
- search xdr alerts with filters.
- xdr start xql query
- xpanse get audit logs
- threat intel analyst
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- initiate a scan on endpoints.
- search services
- configure xsiam datasources.
- ai runtime security scanning and automated red teaming for ai applications.
- executes containment, eradication, and recovery actions during security incidents.
- create investigation
- xsiam start xql query
- search xdr endpoints.
- xdr update incident
- compliance officer
- search xpanse incidents
- red team operator
- list xsiam assets with filters.
- search incidents with filters in cortex xsoar.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- analyzes suspicious files and samples for malware characteristics.
- detection and response
- get attack surface rules from xpanse.
- threat intelligence
- update an xdr incident.
- list xsiam assets with optional filters.
- scan endpoints
- update an xpanse incident.
- update an attack surface rule.
- update an existing incident in cortex xsoar.
- search xsiam assets
- add entry
- xsoar create investigation
- search exposed services.
- get audit management logs from xpanse.
- monitors network health, performance, and digital experience metrics.
- subscription manager
- add an entry to an investigation in xsoar.
- digital experience monitoring, log management, and best practice assessment.
- isolate endpoints.
- network architect
- enterprise it
- list playbooks
- xsoar update incident
- get xpanse audit logs
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- search for integration instances in xsoar.
- xsiam configure datasource
- search xsiam alerts
- network security
- search xsiam alerts.
- search exposed assets
- start an xql query on xsiam.
- xsoar list playbooks
- search attack surface rules
- update an attack surface rule in xpanse.
- get script execution results from xdr.
- identity and access management, tenant hierarchies, and subscription management.
- run scripts on endpoints.
- retrieve a specific incident by id from cortex xsoar.
- xsoar add entry
- firewall admin
- xpanse update incident
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- xsiam get xql results
- list xdr alerts with optional filters, pagination, and sorting.
- get owned ip ranges from xpanse.
- update xpanse incident
- xdr
- create an incident in xsoar.
- get xdr audit logs.
- network operations
- run a playbook on an investigation in xsoar.
- investigates dlp incidents and manages sensitive data protection policies.
- list and manage xsoar playbooks.
- tenant operator
- enterprise browser policy management and secure browsing.
- search for available integrations in cortex xsoar.
- get script execution results.
- incident response
- get xpanse audit logs.
- xdr get incident details
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
