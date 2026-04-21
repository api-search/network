---
consumed_apis:
- autonomous-dem
- sase-aggregate-monitoring
- strata-logging-service
- aiops-ngfw-bpa
- sase-multitenant-notifications
description: Unified monitoring and observability capability for tracking digital experience, aggregating security data, managing log forwarding, and running best practice assessments across Autonomous DEM, SASE Aggregate Monitoring, Strata Logging Service, and AIOps BPA APIs.
layout: capability
name: Palo Alto Networks Monitoring and Observability
operations:
- description: Get application experience scores.
  method: GET
  name: get-dem-application-scores
  path: /v1/dem-application-scores
- description: Get agent and endpoint scores.
  method: GET
  name: get-dem-agent-scores
  path: /v1/dem-agent-scores
- description: Get synthetic test results.
  method: GET
  name: get-dem-test-results
  path: /v1/dem-tests/{test_id}/results
- description: List monitored applications.
  method: GET
  name: list-dem-applications
  path: /v1/dem-applications
- description: List monitored agents.
  method: GET
  name: list-dem-agents
  path: /v1/dem-agents
- description: Get performance metrics.
  method: GET
  name: get-dem-metrics
  path: /v1/dem-metrics
- description: Query aggregated threat monitoring data with filters, time ranges, and grouping.
  method: POST
  name: query-threat-data
  path: /v1/monitoring/threats
- description: Query aggregated URL monitoring data with filters, time ranges, and grouping.
  method: POST
  name: query-url-data
  path: /v1/monitoring/urls
- description: Query aggregated application monitoring data with filters, time ranges, and grouping.
  method: POST
  name: query-application-data
  path: /v1/monitoring/applications
- description: Query aggregated bandwidth monitoring data with filters, time ranges, and grouping.
  method: POST
  name: query-bandwidth-data
  path: /v1/monitoring/bandwidth
- description: Query aggregated license monitoring data with filters, time ranges, and grouping.
  method: POST
  name: query-license-data
  path: /v1/monitoring/licenses
- description: List all tenants available for monitoring.
  method: GET
  name: list-monitoring-tenants
  path: /v1/monitoring/tenants
- description: List all log forwarding profiles.
  method: GET
  name: list-log-forwarding-profiles
  path: /v1/log-forwarding-profiles
- description: Create a new log forwarding profile.
  method: POST
  name: create-log-forwarding-profile
  path: /v1/log-forwarding-profiles
- description: Get a specific log forwarding profile by ID.
  method: GET
  name: get-log-forwarding-profile
  path: /v1/log-forwarding-profiles/{profile_id}
- description: Update a specific log forwarding profile by ID.
  method: PUT
  name: update-log-forwarding-profile
  path: /v1/log-forwarding-profiles/{profile_id}
- description: Delete a specific log forwarding profile by ID.
  method: DELETE
  name: delete-log-forwarding-profile
  path: /v1/log-forwarding-profiles/{profile_id}
- description: List syslog destinations for a log forwarding profile.
  method: GET
  name: list-syslog-destinations
  path: /v1/log-forwarding-profiles/{profile_id}/destinations/syslog
- description: Create a syslog destination for a log forwarding profile.
  method: POST
  name: create-syslog-destination
  path: /v1/log-forwarding-profiles/{profile_id}/destinations/syslog
- description: List HTTPS destinations for a log forwarding profile.
  method: GET
  name: list-https-destinations
  path: /v1/log-forwarding-profiles/{profile_id}/destinations/https
- description: Create an HTTPS destination for a log forwarding profile.
  method: POST
  name: create-https-destination
  path: /v1/log-forwarding-profiles/{profile_id}/destinations/https
- description: List email destinations for a log forwarding profile.
  method: GET
  name: list-email-destinations
  path: /v1/log-forwarding-profiles/{profile_id}/destinations/email
- description: Create an email destination for a log forwarding profile.
  method: POST
  name: create-email-destination
  path: /v1/log-forwarding-profiles/{profile_id}/destinations/email
- description: Get the status of a log forwarding profile.
  method: GET
  name: get-log-forwarding-status
  path: /v1/log-forwarding-profiles/{profile_id}/status
- description: Submit a BPA request.
  method: POST
  name: submit-bpa-request
  path: /v1/bpa-requests
- description: Check the status of a BPA request.
  method: GET
  name: get-bpa-request-status
  path: /v1/bpa-requests/{request_id}
- description: Get a BPA report.
  method: GET
  name: get-bpa-report
  path: /v1/bpa-reports/{report_id}
- description: Get BPA report check details.
  method: GET
  name: get-bpa-report-checks
  path: /v1/bpa-reports/{report_id}/checks
personas:
- description: Monitors network health, performance, and digital experience metrics.
  id: network-operations
  name: Network Operations
- description: Manages logging infrastructure, integrations, and platform automation.
  id: platform-engineer
  name: Platform Engineer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
search_terms:
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- query aggregated threat monitoring data with filters, time ranges, and grouping.
- query aggregated license monitoring data with filters, time ranges, and grouping.
- platform engineer
- saas security admin
- query aggregated bandwidth monitoring data with filters, time ranges, and grouping.
- list syslog destinations for a log forwarding profile.
- enterprise it
- list monitoring tenants.
- query aggregated url monitoring data.
- get dem metrics
- bpa request operations.
- threat hunter
- network operations
- monitored applications from autonomous dem.
- create a syslog destination for a log forwarding profile.
- list syslog destinations
- get bpa report check details.
- observability
- list monitored applications
- create an https destination for a log forwarding profile.
- list https destinations
- list monitored agents
- get bpa report checks
- create email destination
- threat intel analyst
- compliance team
- executes containment, eradication, and recovery actions during security incidents.
- create a new log forwarding profile.
- sre
- get a bpa report.
- manages multi-tenant hierarchies and service group configurations for mssps.
- query license data
- firewall
- sase
- incident responder
- network architect
- query threat data
- designs sase and sd-wan network architectures for secure remote access.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- get performance metrics
- cloud security
- log forwarding profile status.
- get application experience scores.
- get dem test results
- firewall admin
- get dem application scores
- synthetic test results from autonomous dem.
- manages service accounts, roles, and access policies for platform api access.
- submit bpa request
- list dem applications
- agent and endpoint scores from autonomous dem.
- designs and implements network security architectures and policies.
- submit a bpa request for a device.
- list log forwarding profiles
- soc analyst
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- network security engineer
- logging
- list all tenants available for monitoring.
- query aggregated url monitoring data with filters, time ranges, and grouping.
- get application scores
- list monitored applications from autonomous dem.
- monitors and remediates cloud security misconfigurations and compliance violations.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- enterprise browser policy management and secure browsing.
- list all log forwarding profiles.
- vulnerability manager
- cloud security engineer
- manage enterprise browser policies, user sessions, and deployments.
- get agent and endpoint scores.
- firewall policy management, network objects, and cloud-native firewall configuration.
- get performance metrics.
- query aggregated application monitoring data.
- data loss prevention, saas security monitoring, and identity security posture.
- monitoring
- log forwarding profile management.
- bpa report check details.
- get synthetic test results.
- update log forwarding profile
- get dem agent scores
- get test results
- malware researcher
- soar
- red team operator
- create https destination
- application experience scores from autonomous dem.
- query aggregated application monitoring data with filters, time ranges, and grouping.
- syslog destination management for log forwarding profiles.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- investigates security incidents, triages alerts, and coordinates response actions.
- investigates dlp incidents and manages sensitive data protection policies.
- conducts automated adversarial testing against ai systems and llm applications.
- https destination management for log forwarding profiles.
- compliance officer
- digital experience
- list monitored applications.
- query application data
- manages enterprise browser policies and secure browsing configurations.
- submit a bpa request.
- create an email destination for a log forwarding profile.
- network security
- get performance metrics from autonomous dem.
- list dem agents
- analyzes suspicious files and samples for malware characteristics.
- monitored agents from autonomous dem.
- subscription manager
- get bpa request status
- query bandwidth data
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- individual log forwarding profile operations.
- ai runtime security scanning and automated red teaming for ai applications.
- check the status of a bpa request.
- threat intelligence
- list email destinations for a log forwarding profile.
- get agent scores
- create log forwarding profile
- list email destinations
- cloud security posture management, compliance monitoring, and workload protection.
- bpa report retrieval.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- update a specific log forwarding profile by id.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- query aggregated license monitoring data.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- list monitoring tenants
- delete log forwarding profile
- bpa request status.
- get synthetic test results from autonomous dem.
- ai security engineer
- mssp operator
- researches threat actors, malware campaigns, and vulnerability trends.
- get bpa report
- digital experience monitoring, log management, and best practice assessment.
- get agent and endpoint scores from autonomous dem.
- palo alto networks
- xdr
- data protection analyst
- create syslog destination
- performance metrics from autonomous dem.
- iam admin
- manages logging infrastructure, integrations, and platform automation.
- cybersecurity
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- get log forwarding status
- notifications
- sase admin
- query aggregated threat monitoring data.
- sd wan operator
- monitors network health, performance, and digital experience metrics.
- best practice assessment
- list monitored agents.
- proactively searches for threats and iocs across telemetry data.
- get the status of a log forwarding profile.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- identity and access management, tenant hierarchies, and subscription management.
- browser security admin
- email destination management for log forwarding profiles.
- query aggregated bandwidth monitoring data.
- secures ai applications with runtime scanning and vulnerability assessment.
- query url data
- list monitored agents from autonomous dem.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- get log forwarding profile
- manages multi-tenant security operations at scale for managed service providers.
- tenant operator
- get application experience scores from autonomous dem.
- get a specific log forwarding profile by id.
- list https destinations for a log forwarding profile.
- delete a specific log forwarding profile by id.
slug: monitoring-and-observability
tags:
- Palo Alto Networks
- Monitoring
- Observability
- Logging
- Digital Experience
- Best Practice Assessment
- Notifications
tools:
- description: Get application experience scores from Autonomous DEM.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-application-scores
- description: Get agent and endpoint scores from Autonomous DEM.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-agent-scores
- description: Get synthetic test results from Autonomous DEM.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-test-results
- description: List monitored applications from Autonomous DEM.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-monitored-applications
- description: List monitored agents from Autonomous DEM.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-monitored-agents
- description: Get performance metrics from Autonomous DEM.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-performance-metrics
- description: Query aggregated threat monitoring data with filters, time ranges, and grouping.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-threat-data
- description: Query aggregated URL monitoring data with filters, time ranges, and grouping.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-url-data
- description: Query aggregated application monitoring data with filters, time ranges, and grouping.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-application-data
- description: Query aggregated bandwidth monitoring data with filters, time ranges, and grouping.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-bandwidth-data
- description: Query aggregated license monitoring data with filters, time ranges, and grouping.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-license-data
- description: List all tenants available for monitoring.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-monitoring-tenants
- description: List all log forwarding profiles.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-log-forwarding-profiles
- description: Create a new log forwarding profile.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-log-forwarding-profile
- description: Get a specific log forwarding profile by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-log-forwarding-profile
- description: Update a specific log forwarding profile by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-log-forwarding-profile
- description: Delete a specific log forwarding profile by ID.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-log-forwarding-profile
- description: List syslog destinations for a log forwarding profile.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-syslog-destinations
- description: Create a syslog destination for a log forwarding profile.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-syslog-destination
- description: List HTTPS destinations for a log forwarding profile.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-https-destinations
- description: Create an HTTPS destination for a log forwarding profile.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-https-destination
- description: List email destinations for a log forwarding profile.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-email-destinations
- description: Create an email destination for a log forwarding profile.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-email-destination
- description: Get the status of a log forwarding profile.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-log-forwarding-status
- description: Submit a BPA request for a device.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: submit-bpa-request
- description: Check the status of a BPA request.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-bpa-request-status
- description: Get a BPA report.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-bpa-report
- description: Get BPA report check details.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-bpa-report-checks
---
