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
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- platform engineer
- sd wan operator
- performance metrics from autonomous dem.
- monitored agents from autonomous dem.
- get application experience scores from autonomous dem.
- get performance metrics.
- xdr
- monitored applications from autonomous dem.
- bpa report retrieval.
- malware researcher
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- application experience scores from autonomous dem.
- query aggregated url monitoring data with filters, time ranges, and grouping.
- get dem agent scores
- network architect
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- network security
- list all tenants available for monitoring.
- update a specific log forwarding profile by id.
- tenant operator
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- get agent and endpoint scores.
- get agent scores
- observability
- network security engineer
- saas security admin
- get bpa report checks
- query aggregated url monitoring data.
- create a syslog destination for a log forwarding profile.
- conducts automated adversarial testing against ai systems and llm applications.
- executes containment, eradication, and recovery actions during security incidents.
- sre
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- query aggregated license monitoring data with filters, time ranges, and grouping.
- get dem application scores
- bpa request operations.
- query aggregated bandwidth monitoring data with filters, time ranges, and grouping.
- get bpa report
- query application data
- list email destinations
- get bpa report check details.
- threat intelligence
- get dem metrics
- query url data
- list syslog destinations for a log forwarding profile.
- monitoring
- list https destinations for a log forwarding profile.
- red team operator
- monitors and remediates cloud security misconfigurations and compliance violations.
- manages logging infrastructure, integrations, and platform automation.
- list monitored applications.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- researches threat actors, malware campaigns, and vulnerability trends.
- soar
- log forwarding profile management.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- list dem applications
- list dem agents
- create syslog destination
- enterprise it
- vulnerability manager
- iam admin
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- manage enterprise browser policies, user sessions, and deployments.
- incident responder
- submit a bpa request for a device.
- investigates security incidents, triages alerts, and coordinates response actions.
- get bpa request status
- ai security engineer
- check the status of a bpa request.
- individual log forwarding profile operations.
- get log forwarding profile
- identity and access management, tenant hierarchies, and subscription management.
- ai runtime security scanning and automated red teaming for ai applications.
- query aggregated threat monitoring data.
- browser security admin
- submit a bpa request.
- list all log forwarding profiles.
- enterprise browser policy management and secure browsing.
- list https destinations
- designs and implements network security architectures and policies.
- cloud security posture management, compliance monitoring, and workload protection.
- monitors network health, performance, and digital experience metrics.
- syslog destination management for log forwarding profiles.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- logging
- query aggregated threat monitoring data with filters, time ranges, and grouping.
- get application experience scores.
- get synthetic test results.
- sase admin
- list monitored agents from autonomous dem.
- list monitored applications from autonomous dem.
- list monitoring tenants
- get synthetic test results from autonomous dem.
- list monitoring tenants.
- create an https destination for a log forwarding profile.
- notifications
- create log forwarding profile
- data protection analyst
- secures ai applications with runtime scanning and vulnerability assessment.
- agent and endpoint scores from autonomous dem.
- query threat data
- sase
- create a new log forwarding profile.
- update log forwarding profile
- investigates dlp incidents and manages sensitive data protection policies.
- compliance team
- query license data
- delete a specific log forwarding profile by id.
- get agent and endpoint scores from autonomous dem.
- cloud security engineer
- bpa request status.
- manages service accounts, roles, and access policies for platform api access.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- threat hunter
- create an email destination for a log forwarding profile.
- manages enterprise browser policies and secure browsing configurations.
- cloud security
- list email destinations for a log forwarding profile.
- query aggregated application monitoring data with filters, time ranges, and grouping.
- get a specific log forwarding profile by id.
- create https destination
- digital experience monitoring, log management, and best practice assessment.
- get dem test results
- firewall policy management, network objects, and cloud-native firewall configuration.
- https destination management for log forwarding profiles.
- threat intel analyst
- cybersecurity
- mssp operator
- digital experience
- proactively searches for threats and iocs across telemetry data.
- get performance metrics
- synthetic test results from autonomous dem.
- manages multi-tenant security operations at scale for managed service providers.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- manages multi-tenant hierarchies and service group configurations for mssps.
- analyzes suspicious files and samples for malware characteristics.
- submit bpa request
- subscription manager
- firewall
- email destination management for log forwarding profiles.
- delete log forwarding profile
- get performance metrics from autonomous dem.
- get a bpa report.
- list monitored applications
- query aggregated license monitoring data.
- create email destination
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- list syslog destinations
- log forwarding profile status.
- palo alto networks
- list monitored agents.
- compliance officer
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- get application scores
- get the status of a log forwarding profile.
- query bandwidth data
- query aggregated application monitoring data.
- data loss prevention, saas security monitoring, and identity security posture.
- list log forwarding profiles
- get log forwarding status
- bpa report check details.
- list monitored agents
- soc analyst
- designs sase and sd-wan network architectures for secure remote access.
- get test results
- firewall admin
- best practice assessment
- network operations
- query aggregated bandwidth monitoring data.
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
