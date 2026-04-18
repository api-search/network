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
- get performance metrics
- palo alto networks
- monitored agents from autonomous dem.
- designs sase and sd-wan network architectures for secure remote access.
- network security engineer
- secures ai applications with runtime scanning and vulnerability assessment.
- syslog destination management for log forwarding profiles.
- sase admin
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- get bpa report
- submit bpa request
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- xdr
- create syslog destination
- get application scores
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- observability
- get bpa request status
- get dem agent scores
- log forwarding profile management.
- get log forwarding profile
- enterprise browser policy management and secure browsing.
- bpa report retrieval.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- get bpa report check details.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- get agent and endpoint scores.
- list monitored agents.
- list monitored agents from autonomous dem.
- ai security engineer
- update a specific log forwarding profile by id.
- data protection analyst
- network architect
- list email destinations for a log forwarding profile.
- data loss prevention, saas security monitoring, and identity security posture.
- saas security admin
- create a syslog destination for a log forwarding profile.
- bpa report check details.
- manages multi-tenant hierarchies and service group configurations for mssps.
- delete log forwarding profile
- network security
- query aggregated threat monitoring data with filters, time ranges, and grouping.
- query aggregated application monitoring data.
- manages enterprise browser policies and secure browsing configurations.
- soar
- list monitoring tenants
- create an email destination for a log forwarding profile.
- compliance team
- get agent and endpoint scores from autonomous dem.
- application experience scores from autonomous dem.
- investigates dlp incidents and manages sensitive data protection policies.
- researches threat actors, malware campaigns, and vulnerability trends.
- query threat data
- get a bpa report.
- get dem metrics
- get test results
- query aggregated bandwidth monitoring data with filters, time ranges, and grouping.
- get application experience scores from autonomous dem.
- subscription manager
- compliance officer
- get log forwarding status
- list dem applications
- tenant operator
- executes containment, eradication, and recovery actions during security incidents.
- vulnerability manager
- query application data
- cybersecurity
- agent and endpoint scores from autonomous dem.
- update log forwarding profile
- malware researcher
- monitoring
- designs and implements network security architectures and policies.
- individual log forwarding profile operations.
- get performance metrics from autonomous dem.
- get performance metrics.
- incident responder
- create an https destination for a log forwarding profile.
- email destination management for log forwarding profiles.
- submit a bpa request for a device.
- mssp operator
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- get dem application scores
- performance metrics from autonomous dem.
- query aggregated license monitoring data.
- list monitored applications
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- manages service accounts, roles, and access policies for platform api access.
- get agent scores
- get synthetic test results from autonomous dem.
- threat intel analyst
- firewall policy management, network objects, and cloud-native firewall configuration.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- list https destinations
- bpa request operations.
- sase
- firewall admin
- soc analyst
- proactively searches for threats and iocs across telemetry data.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- list log forwarding profiles
- list dem agents
- notifications
- monitored applications from autonomous dem.
- get bpa report checks
- query aggregated bandwidth monitoring data.
- query aggregated license monitoring data with filters, time ranges, and grouping.
- network operations
- enterprise it
- manages logging infrastructure, integrations, and platform automation.
- browser security admin
- threat hunter
- create https destination
- list email destinations
- list monitored applications.
- list all tenants available for monitoring.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- https destination management for log forwarding profiles.
- get a specific log forwarding profile by id.
- get dem test results
- submit a bpa request.
- analyzes suspicious files and samples for malware characteristics.
- query aggregated threat monitoring data.
- query license data
- delete a specific log forwarding profile by id.
- monitors and remediates cloud security misconfigurations and compliance violations.
- list https destinations for a log forwarding profile.
- monitors network health, performance, and digital experience metrics.
- list monitored applications from autonomous dem.
- identity and access management, tenant hierarchies, and subscription management.
- log forwarding profile status.
- check the status of a bpa request.
- query url data
- ai runtime security scanning and automated red teaming for ai applications.
- list syslog destinations
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- platform engineer
- list monitored agents
- digital experience monitoring, log management, and best practice assessment.
- synthetic test results from autonomous dem.
- iam admin
- list monitoring tenants.
- query bandwidth data
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- logging
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- list all log forwarding profiles.
- query aggregated url monitoring data.
- list syslog destinations for a log forwarding profile.
- red team operator
- create log forwarding profile
- get synthetic test results.
- digital experience
- bpa request status.
- sre
- manages multi-tenant security operations at scale for managed service providers.
- threat intelligence
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- best practice assessment
- conducts automated adversarial testing against ai systems and llm applications.
- investigates security incidents, triages alerts, and coordinates response actions.
- cloud security
- firewall
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- cloud security posture management, compliance monitoring, and workload protection.
- manage enterprise browser policies, user sessions, and deployments.
- get application experience scores.
- query aggregated application monitoring data with filters, time ranges, and grouping.
- create email destination
- create a new log forwarding profile.
- get the status of a log forwarding profile.
- query aggregated url monitoring data with filters, time ranges, and grouping.
- cloud security engineer
- sd wan operator
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
