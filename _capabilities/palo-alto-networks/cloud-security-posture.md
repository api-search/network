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
- cspm
- palo alto networks
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- ai security engineer
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- get code security errors for a specific repository branch
- investigates security incidents, triages alerts, and coordinates response actions.
- cybersecurity
- delete a specific code security suppression by id
- list all ci/cd scan integrations with pagination
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- soar
- list cspm alerts
- list cloud accounts
- designs and implements network security architectures and policies.
- manages service accounts, roles, and access policies for platform api access.
- list reports
- soc analyst
- search for cloud assets using rql queries
- conducts automated adversarial testing against ai systems and llm applications.
- sase
- get scan status
- get fix suggestions for a pull request
- sd wan operator
- create a new cspm security policy
- update policy
- secure access service edge with remote networking, sd-wan, and zero trust access.
- update an existing cspm security policy
- search asset
- add cloud account
- vulnerability manager
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- list scan integrations
- researches threat actors, malware campaigns, and vulnerability trends.
- remove repository
- retrieve details for a specific cspm policy
- retrieve a list of dspm policies
- mssp operator
- malware researcher
- list data security alerts
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- incident responder
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- remove cloud account
- sase admin
- browser security admin
- get errors by branch
- manages multi-tenant security operations at scale for managed service providers.
- platform engineer
- get fix suggestions
- update risk status
- authenticate to prisma cloud and retrieve a jwt token
- update data risk status
- cloud security engineer
- reopen alerts
- list dspm policies
- list suppressions
- create a new code security suppression
- get alert
- firewall
- network security engineer
- remove an onboarded cloud account
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- retrieve a list of all compliance reports
- update the status of a specific data security risk
- list data risks
- trigger a new code security scan for a repository
- monitors and remediates cloud security misconfigurations and compliance violations.
- create suppression
- get data risk
- authenticate
- manages enterprise browser policies and secure browsing configurations.
- retrieve a list of data security risks
- reopen one or more previously dismissed cspm alerts
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- compliance team
- list repositories
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- designs sase and sd-wan network architectures for secure remote access.
- cloud security
- list compliance standards
- retrieve a list of discovered data assets
- cloud security posture management, compliance monitoring, and workload protection.
- data security
- threat hunter
- retrieve details for a specific data security risk
- data loss prevention, saas security monitoring, and identity security posture.
- list policies
- iam admin
- sre
- retrieve a list of all cspm policies
- manages logging infrastructure, integrations, and platform automation.
- dismiss alerts
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- saas security admin
- secures ai applications with runtime scanning and vulnerability assessment.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- create policy
- reopen cspm alerts
- get risk
- manage enterprise browser policies, user sessions, and deployments.
- trigger scan
- retrieve details for a specific data asset
- proactively searches for threats and iocs across telemetry data.
- data protection analyst
- login
- manages multi-tenant hierarchies and service group configurations for mssps.
- firewall policy management, network objects, and cloud-native firewall configuration.
- get alerts
- threat intel analyst
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- retrieve a list of cspm alerts based on filters
- get fix suggestions for pr
- ai runtime security scanning and automated red teaming for ai applications.
- executes containment, eradication, and recovery actions during security incidents.
- get data asset
- compliance officer
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- red team operator
- retrieve a list of dspm data security alerts
- search config
- analyzes suspicious files and samples for malware characteristics.
- threat intelligence
- retrieve details for a specific cspm alert
- retrieve a list of data classifications
- compliance
- list all code security suppressions with pagination and filtering
- list classifications
- list data assets
- list all code security repositories with pagination and filtering
- monitors network health, performance, and digital experience metrics.
- retrieve a list of data stores
- subscription manager
- digital experience monitoring, log management, and best practice assessment.
- search for cloud configuration data using rql queries
- network architect
- enterprise it
- list risks
- dismiss cspm alerts
- add a new repository for code security scanning
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- network security
- dismiss one or more cspm alerts
- list data stores
- add repository
- identity and access management, tenant hierarchies, and subscription management.
- firewall admin
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- xdr
- retrieve a list of all compliance standards
- onboard a new cloud account
- search assets
- get cspm alert
- network operations
- investigates dlp incidents and manages sensitive data protection policies.
- retrieve a list of all onboarded cloud accounts
- tenant operator
- delete suppression
- mssp
- get the status of a code security scan
- remove a repository from code security scanning
- enterprise browser policy management and secure browsing.
- get policy
- get code errors
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
