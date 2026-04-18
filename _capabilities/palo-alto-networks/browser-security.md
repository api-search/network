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
- firewall policy management, network objects, and cloud-native firewall configuration.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- xdr
- sase
- list browser deployments
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- sase admin
- sd wan operator
- cloud security engineer
- secure access service edge with remote networking, sd-wan, and zero trust access.
- data loss prevention, saas security monitoring, and identity security posture.
- prisma access
- compliance team
- analyzes suspicious files and samples for malware characteristics.
- cybersecurity
- ai runtime security scanning and automated red teaming for ai applications.
- sre
- list browser users
- secures ai applications with runtime scanning and vulnerability assessment.
- compliance officer
- update browser policy
- manages logging infrastructure, integrations, and platform automation.
- browser security
- threat hunter
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- soar
- investigates dlp incidents and manages sensitive data protection policies.
- data protection analyst
- manages multi-tenant hierarchies and service group configurations for mssps.
- ai security engineer
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- get user sessions
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- saas security admin
- enterprise browser
- researches threat actors, malware campaigns, and vulnerability trends.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- threat intel analyst
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- firewall
- manage browser deployments across platforms.
- network architect
- list all browser deployments with pagination.
- proactively searches for threats and iocs across telemetry data.
- delete browser policy
- browser security admin
- create a new browser deployment.
- monitors and remediates cloud security misconfigurations and compliance violations.
- cloud security
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- create browser deployment
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- designs and implements network security architectures and policies.
- create browser policy
- threat intelligence
- list all browser policies with pagination.
- firewall admin
- manages multi-tenant security operations at scale for managed service providers.
- executes containment, eradication, and recovery actions during security incidents.
- palo alto networks
- manage a specific browser policy by id.
- digital experience monitoring, log management, and best practice assessment.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- incident responder
- investigates security incidents, triages alerts, and coordinates response actions.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- get browser policy
- list all browser users with pagination.
- monitors network health, performance, and digital experience metrics.
- network operations
- conducts automated adversarial testing against ai systems and llm applications.
- enterprise browser policy management and secure browsing.
- cloud security posture management, compliance monitoring, and workload protection.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- manage enterprise browser security policies.
- get sessions for a specific browser user.
- list browser policies
- red team operator
- designs sase and sd-wan network architectures for secure remote access.
- delete a specific browser policy by id.
- enterprise it
- soc analyst
- subscription manager
- platform engineer
- network security
- mssp operator
- tenant operator
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- create a new browser policy.
- manages enterprise browser policies and secure browsing configurations.
- manages service accounts, roles, and access policies for platform api access.
- get sessions for a specific user.
- malware researcher
- manage enterprise browser policies, user sessions, and deployments.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- network security engineer
- update a specific browser policy by id.
- vulnerability manager
- iam admin
- identity and access management, tenant hierarchies, and subscription management.
- list enterprise browser users.
- get a specific browser policy by id.
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
