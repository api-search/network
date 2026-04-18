---
consumed_apis:
- prisma-access-browser
description: Browser security capability for managing enterprise browser policies, user sessions, and deployments through the Prisma Access Browser API.
layout: capability
name: Palo Alto Networks Browser Security
operations:
- description: List all browser policies with pagination.
  method: GET
  name: list-browser-policies
  path: /v1/browser-policies
- description: Create a new browser policy.
  method: POST
  name: create-browser-policy
  path: /v1/browser-policies
- description: Get a specific browser policy by ID.
  method: GET
  name: get-browser-policy
  path: /v1/browser-policies/{policy_id}
- description: Update a specific browser policy by ID.
  method: PUT
  name: update-browser-policy
  path: /v1/browser-policies/{policy_id}
- description: Delete a specific browser policy by ID.
  method: DELETE
  name: delete-browser-policy
  path: /v1/browser-policies/{policy_id}
- description: List all browser users with pagination.
  method: GET
  name: list-browser-users
  path: /v1/browser-users
- description: Get sessions for a specific user.
  method: GET
  name: get-user-sessions
  path: /v1/browser-users/{user_id}/sessions
- description: List all browser deployments with pagination.
  method: GET
  name: list-browser-deployments
  path: /v1/browser-deployments
- description: Create a new browser deployment.
  method: POST
  name: create-browser-deployment
  path: /v1/browser-deployments
personas:
- description: Manages enterprise browser policies and secure browsing configurations.
  id: browser-security-admin
  name: Browser Security Admin
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
search_terms:
- get a specific browser policy by id.
- palo alto networks
- create browser deployment
- designs sase and sd-wan network architectures for secure remote access.
- prisma access
- network security engineer
- secures ai applications with runtime scanning and vulnerability assessment.
- sase admin
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- xdr
- update a specific browser policy by id.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- enterprise browser policy management and secure browsing.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- ai security engineer
- update browser policy
- data protection analyst
- network architect
- list browser deployments
- data loss prevention, saas security monitoring, and identity security posture.
- saas security admin
- browser security
- get sessions for a specific browser user.
- manages multi-tenant hierarchies and service group configurations for mssps.
- network security
- enterprise browser
- soar
- manages enterprise browser policies and secure browsing configurations.
- list enterprise browser users.
- compliance team
- get user sessions
- create a new browser policy.
- investigates dlp incidents and manages sensitive data protection policies.
- researches threat actors, malware campaigns, and vulnerability trends.
- manage enterprise browser security policies.
- subscription manager
- compliance officer
- tenant operator
- executes containment, eradication, and recovery actions during security incidents.
- vulnerability manager
- cybersecurity
- malware researcher
- designs and implements network security architectures and policies.
- incident responder
- mssp operator
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- manages service accounts, roles, and access policies for platform api access.
- threat intel analyst
- firewall policy management, network objects, and cloud-native firewall configuration.
- sase
- get sessions for a specific user.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- firewall admin
- soc analyst
- proactively searches for threats and iocs across telemetry data.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- list all browser policies with pagination.
- get browser policy
- manage browser deployments across platforms.
- network operations
- enterprise it
- manages logging infrastructure, integrations, and platform automation.
- browser security admin
- threat hunter
- list all browser users with pagination.
- create a new browser deployment.
- delete a specific browser policy by id.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- analyzes suspicious files and samples for malware characteristics.
- list browser policies
- monitors and remediates cloud security misconfigurations and compliance violations.
- manage a specific browser policy by id.
- monitors network health, performance, and digital experience metrics.
- identity and access management, tenant hierarchies, and subscription management.
- ai runtime security scanning and automated red teaming for ai applications.
- list all browser deployments with pagination.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- platform engineer
- digital experience monitoring, log management, and best practice assessment.
- iam admin
- create browser policy
- delete browser policy
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- red team operator
- sre
- manages multi-tenant security operations at scale for managed service providers.
- threat intelligence
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- conducts automated adversarial testing against ai systems and llm applications.
- firewall
- investigates security incidents, triages alerts, and coordinates response actions.
- cloud security
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- cloud security posture management, compliance monitoring, and workload protection.
- manage enterprise browser policies, user sessions, and deployments.
- cloud security engineer
- list browser users
- sd wan operator
slug: browser-security
tags:
- Palo Alto Networks
- Browser Security
- Enterprise Browser
- Prisma Access
tools:
- description: List all browser policies with pagination.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-browser-policies
- description: Create a new browser policy.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-browser-policy
- description: Get a specific browser policy by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-browser-policy
- description: Update a specific browser policy by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: false
  name: update-browser-policy
- description: Delete a specific browser policy by ID.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-browser-policy
- description: List all browser users with pagination.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-browser-users
- description: Get sessions for a specific user.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-user-sessions
- description: List all browser deployments with pagination.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-browser-deployments
- description: Create a new browser deployment.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-browser-deployment
---
