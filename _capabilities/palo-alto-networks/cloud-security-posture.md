---
consumed_apis:
- prisma-cloud-cspm
- prisma-cloud-code-security
- prisma-cloud-dspm
- prisma-cloud-mssp
description: Unified cloud security posture capability for managing alerts, policies, compliance, code security scanning, and data security posture across Prisma Cloud CSPM, Code Security, and DSPM.
layout: capability
name: Palo Alto Networks Cloud Security Posture
operations:
- description: ''
  method: POST
  name: login
  path: /v1/auth/login
- description: ''
  method: GET
  name: get-alerts
  path: /v1/alerts
- description: ''
  method: GET
  name: get-alert
  path: /v1/alerts/{id}
- description: ''
  method: POST
  name: dismiss-alerts
  path: /v1/alerts/dismiss
- description: ''
  method: POST
  name: reopen-alerts
  path: /v1/alerts/reopen
- description: ''
  method: GET
  name: list-data-security-alerts
  path: /v1/data-security-alerts
- description: ''
  method: GET
  name: list-policies
  path: /v1/policies
- description: ''
  method: POST
  name: create-policy
  path: /v1/policies
- description: ''
  method: GET
  name: get-policy
  path: /v1/policies/{policyId}
- description: ''
  method: PUT
  name: update-policy
  path: /v1/policies/{policyId}
- description: ''
  method: GET
  name: list-dspm-policies
  path: /v1/dspm-policies
- description: ''
  method: GET
  name: list-cloud-accounts
  path: /v1/cloud-accounts
- description: ''
  method: POST
  name: add-cloud-account
  path: /v1/cloud-accounts/{cloudType}
- description: ''
  method: DELETE
  name: remove-cloud-account
  path: /v1/cloud-accounts/{cloudType}/{id}
- description: ''
  method: POST
  name: search-asset
  path: /v1/search/assets
- description: ''
  method: POST
  name: search-config
  path: /v1/search/config
- description: ''
  method: GET
  name: list-compliance-standards
  path: /v1/compliance-standards
- description: ''
  method: GET
  name: list-reports
  path: /v1/reports
- description: ''
  method: GET
  name: list-repositories
  path: /v1/repositories
- description: ''
  method: POST
  name: add-repository
  path: /v1/repositories
- description: ''
  method: DELETE
  name: remove-repository
  path: /v1/repositories
- description: ''
  method: GET
  name: list-scan-integrations
  path: /v1/scan-integrations
- description: ''
  method: POST
  name: trigger-scan
  path: /v1/scans
- description: ''
  method: GET
  name: get-scan-status
  path: /v1/scans/{scan_id}
- description: ''
  method: GET
  name: list-suppressions
  path: /v1/suppressions
- description: ''
  method: POST
  name: create-suppression
  path: /v1/suppressions
- description: ''
  method: DELETE
  name: delete-suppression
  path: /v1/suppressions/{suppression_id}
- description: ''
  method: GET
  name: get-errors-by-branch
  path: /v1/code-errors
- description: ''
  method: GET
  name: get-fix-suggestions-for-pr
  path: /v1/fix-suggestions
- description: ''
  method: GET
  name: list-data-assets
  path: /v1/data-assets
- description: ''
  method: GET
  name: get-data-asset
  path: /v1/data-assets/{id}
- description: ''
  method: GET
  name: list-risks
  path: /v1/data-risks
- description: ''
  method: GET
  name: get-risk
  path: /v1/data-risks/{id}
- description: ''
  method: PUT
  name: update-risk-status
  path: /v1/data-risks/{id}/status
- description: ''
  method: GET
  name: list-data-stores
  path: /v1/data-stores
- description: ''
  method: GET
  name: list-classifications
  path: /v1/classifications
personas:
- description: Monitors and remediates cloud security misconfigurations and compliance violations.
  id: cloud-security-engineer
  name: Cloud Security Engineer
- description: Ensures cloud infrastructure meets regulatory and industry compliance standards.
  id: compliance-officer
  name: Compliance Officer
- description: Manages multi-tenant security operations at scale for managed service providers.
  id: mssp-operator
  name: MSSP Operator
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
search_terms:
- get alert
- retrieve a list of discovered data assets
- get risk
- reopen cspm alerts
- enterprise it
- add cloud account
- delete suppression
- get code errors
- compliance officer
- retrieve a list of data security risks
- data protection analyst
- create a new code security suppression
- designs sase and sd-wan network architectures for secure remote access.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- ai runtime security scanning and automated red teaming for ai applications.
- network security
- malware researcher
- researches threat actors, malware campaigns, and vulnerability trends.
- get fix suggestions for a pull request
- manages enterprise browser policies and secure browsing configurations.
- cloud security posture management, compliance monitoring, and workload protection.
- dismiss cspm alerts
- add a new repository for code security scanning
- remove cloud account
- mssp
- list data risks
- list all ci/cd scan integrations with pagination
- retrieve a list of dspm policies
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- proactively searches for threats and iocs across telemetry data.
- list suppressions
- platform engineer
- list all code security suppressions with pagination and filtering
- create policy
- remove repository
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- analyzes suspicious files and samples for malware characteristics.
- delete a specific code security suppression by id
- search assets
- firewall policy management, network objects, and cloud-native firewall configuration.
- update risk status
- monitors network health, performance, and digital experience metrics.
- retrieve details for a specific cspm policy
- list reports
- vulnerability manager
- update the status of a specific data security risk
- manages multi-tenant security operations at scale for managed service providers.
- conducts automated adversarial testing against ai systems and llm applications.
- retrieve details for a specific data security risk
- manages logging infrastructure, integrations, and platform automation.
- remove a repository from code security scanning
- trigger a new code security scan for a repository
- get data risk
- authenticate
- compliance team
- list scan integrations
- designs and implements network security architectures and policies.
- manages multi-tenant hierarchies and service group configurations for mssps.
- list classifications
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- saas security admin
- tenant operator
- incident responder
- create a new cspm security policy
- get code security errors for a specific repository branch
- secure access service edge with remote networking, sd-wan, and zero trust access.
- reopen alerts
- get alerts
- dismiss one or more cspm alerts
- cloud security engineer
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- list cspm alerts
- firewall
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- sase
- sd wan operator
- threat intel analyst
- manage enterprise browser policies, user sessions, and deployments.
- list policies
- retrieve a list of cspm alerts based on filters
- get scan status
- network operations
- retrieve details for a specific data asset
- list dspm policies
- get the status of a code security scan
- manages service accounts, roles, and access policies for platform api access.
- threat hunter
- list compliance standards
- cybersecurity
- reopen one or more previously dismissed cspm alerts
- firewall admin
- data security
- get policy
- retrieve a list of all compliance standards
- soc analyst
- dismiss alerts
- get fix suggestions
- mssp operator
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- remove an onboarded cloud account
- monitors and remediates cloud security misconfigurations and compliance violations.
- get cspm alert
- identity and access management, tenant hierarchies, and subscription management.
- browser security admin
- sase admin
- list data security alerts
- threat intelligence
- palo alto networks
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- get fix suggestions for pr
- retrieve a list of all compliance reports
- retrieve a list of data stores
- search for cloud configuration data using rql queries
- retrieve a list of data classifications
- trigger scan
- soar
- authenticate to prisma cloud and retrieve a jwt token
- list data assets
- investigates security incidents, triages alerts, and coordinates response actions.
- list data stores
- cloud security
- network architect
- executes containment, eradication, and recovery actions during security incidents.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- cspm
- retrieve details for a specific cspm alert
- ai security engineer
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- xdr
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- sre
- network security engineer
- create suppression
- iam admin
- search asset
- login
- list risks
- retrieve a list of dspm data security alerts
- retrieve a list of all cspm policies
- list all code security repositories with pagination and filtering
- data loss prevention, saas security monitoring, and identity security posture.
- digital experience monitoring, log management, and best practice assessment.
- search for cloud assets using rql queries
- update policy
- get errors by branch
- secures ai applications with runtime scanning and vulnerability assessment.
- search config
- get data asset
- red team operator
- list repositories
- compliance
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- list cloud accounts
- enterprise browser policy management and secure browsing.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- update an existing cspm security policy
- onboard a new cloud account
- update data risk status
- add repository
- investigates dlp incidents and manages sensitive data protection policies.
- subscription manager
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- retrieve a list of all onboarded cloud accounts
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
slug: cloud-security-posture
tags:
- Palo Alto Networks
- Cloud Security
- CSPM
- Compliance
- Data Security
- MSSP
tools:
- description: Authenticate to Prisma Cloud and retrieve a JWT token
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: authenticate
- description: Retrieve a list of CSPM alerts based on filters
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-cspm-alerts
- description: Retrieve details for a specific CSPM alert
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-cspm-alert
- description: Dismiss one or more CSPM alerts
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: dismiss-cspm-alerts
- description: Reopen one or more previously dismissed CSPM alerts
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: reopen-cspm-alerts
- description: Retrieve a list of DSPM data security alerts
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-data-security-alerts
- description: Retrieve a list of all CSPM policies
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-policies
- description: Create a new CSPM security policy
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-policy
- description: Retrieve details for a specific CSPM policy
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-policy
- description: Update an existing CSPM security policy
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-policy
- description: Retrieve a list of DSPM policies
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-dspm-policies
- description: Retrieve a list of all onboarded cloud accounts
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-cloud-accounts
- description: Onboard a new cloud account
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: add-cloud-account
- description: Remove an onboarded cloud account
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: remove-cloud-account
- description: Search for cloud assets using RQL queries
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: search-assets
- description: Search for cloud configuration data using RQL queries
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: search-config
- description: Retrieve a list of all compliance standards
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-compliance-standards
- description: Retrieve a list of all compliance reports
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-reports
- description: List all code security repositories with pagination and filtering
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-repositories
- description: Add a new repository for code security scanning
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: add-repository
- description: Remove a repository from code security scanning
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: remove-repository
- description: List all CI/CD scan integrations with pagination
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-scan-integrations
- description: Trigger a new code security scan for a repository
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: trigger-scan
- description: Get the status of a code security scan
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-scan-status
- description: List all code security suppressions with pagination and filtering
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-suppressions
- description: Create a new code security suppression
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-suppression
- description: Delete a specific code security suppression by ID
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-suppression
- description: Get code security errors for a specific repository branch
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-code-errors
- description: Get fix suggestions for a pull request
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-fix-suggestions
- description: Retrieve a list of discovered data assets
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-data-assets
- description: Retrieve details for a specific data asset
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-data-asset
- description: Retrieve a list of data security risks
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-data-risks
- description: Retrieve details for a specific data security risk
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-data-risk
- description: Update the status of a specific data security risk
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-data-risk-status
- description: Retrieve a list of data stores
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-data-stores
- description: Retrieve a list of data classifications
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-classifications
---
