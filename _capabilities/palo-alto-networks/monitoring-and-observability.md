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
- get application experience scores from autonomous dem.
- get agent and endpoint scores.
- manage enterprise browser policies, user sessions, and deployments.
- data protection analyst
- iam admin
- email destination management for log forwarding profiles.
- query application data
- compliance team
- network operations
- cloud security
- query aggregated license monitoring data with filters, time ranges, and grouping.
- get bpa report
- get dem agent scores
- malware researcher
- create log forwarding profile
- performance metrics from autonomous dem.
- palo alto networks
- query license data
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- query aggregated url monitoring data with filters, time ranges, and grouping.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- get bpa report checks
- query aggregated license monitoring data.
- query aggregated application monitoring data with filters, time ranges, and grouping.
- query aggregated bandwidth monitoring data with filters, time ranges, and grouping.
- log forwarding profile status.
- get performance metrics from autonomous dem.
- list monitored applications.
- bpa report retrieval.
- incident responder
- digital experience
- create syslog destination
- syslog destination management for log forwarding profiles.
- get a bpa report.
- create email destination
- xdr
- observability
- analyzes suspicious files and samples for malware characteristics.
- agent and endpoint scores from autonomous dem.
- platform engineer
- executes containment, eradication, and recovery actions during security incidents.
- sd wan operator
- list monitored applications from autonomous dem.
- vulnerability manager
- monitoring
- application experience scores from autonomous dem.
- get performance metrics.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- check the status of a bpa request.
- browser security admin
- list https destinations
- ai runtime security scanning and automated red teaming for ai applications.
- query aggregated application monitoring data.
- delete a specific log forwarding profile by id.
- list log forwarding profiles
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- threat intel analyst
- list monitored agents
- red team operator
- tenant operator
- manages logging infrastructure, integrations, and platform automation.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- monitors and remediates cloud security misconfigurations and compliance violations.
- cybersecurity
- list email destinations for a log forwarding profile.
- firewall admin
- list all tenants available for monitoring.
- secures ai applications with runtime scanning and vulnerability assessment.
- create an https destination for a log forwarding profile.
- enterprise browser policy management and secure browsing.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- firewall policy management, network objects, and cloud-native firewall configuration.
- logging
- submit a bpa request for a device.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- get bpa report check details.
- compliance officer
- investigates dlp incidents and manages sensitive data protection policies.
- monitored applications from autonomous dem.
- get log forwarding status
- get dem application scores
- sase admin
- cloud security posture management, compliance monitoring, and workload protection.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- notifications
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- network architect
- mssp operator
- create a new log forwarding profile.
- synthetic test results from autonomous dem.
- get test results
- query bandwidth data
- network security engineer
- create a syslog destination for a log forwarding profile.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- delete log forwarding profile
- query aggregated threat monitoring data.
- submit bpa request
- query aggregated url monitoring data.
- list email destinations
- list syslog destinations
- data loss prevention, saas security monitoring, and identity security posture.
- bpa request status.
- get log forwarding profile
- researches threat actors, malware campaigns, and vulnerability trends.
- get agent and endpoint scores from autonomous dem.
- query url data
- manages service accounts, roles, and access policies for platform api access.
- list dem applications
- list monitoring tenants
- saas security admin
- get agent scores
- query aggregated bandwidth monitoring data.
- get the status of a log forwarding profile.
- sre
- manages multi-tenant security operations at scale for managed service providers.
- digital experience monitoring, log management, and best practice assessment.
- log forwarding profile management.
- manages multi-tenant hierarchies and service group configurations for mssps.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- threat hunter
- soc analyst
- soar
- manages enterprise browser policies and secure browsing configurations.
- create https destination
- submit a bpa request.
- best practice assessment
- monitored agents from autonomous dem.
- subscription manager
- list monitored applications
- cloud security engineer
- bpa report check details.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- sase
- list all log forwarding profiles.
- threat intelligence
- designs and implements network security architectures and policies.
- identity and access management, tenant hierarchies, and subscription management.
- conducts automated adversarial testing against ai systems and llm applications.
- query threat data
- bpa request operations.
- query aggregated threat monitoring data with filters, time ranges, and grouping.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- list syslog destinations for a log forwarding profile.
- designs sase and sd-wan network architectures for secure remote access.
- get a specific log forwarding profile by id.
- get application experience scores.
- create an email destination for a log forwarding profile.
- firewall
- get bpa request status
- list monitored agents.
- get synthetic test results.
- proactively searches for threats and iocs across telemetry data.
- list monitoring tenants.
- enterprise it
- network security
- list https destinations for a log forwarding profile.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- get application scores
- get dem test results
- list monitored agents from autonomous dem.
- ai security engineer
- investigates security incidents, triages alerts, and coordinates response actions.
- update log forwarding profile
- get synthetic test results from autonomous dem.
- get dem metrics
- monitors network health, performance, and digital experience metrics.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- update a specific log forwarding profile by id.
- https destination management for log forwarding profiles.
- individual log forwarding profile operations.
- list dem agents
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
