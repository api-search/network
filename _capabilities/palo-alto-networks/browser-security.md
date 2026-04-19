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
- create a new browser policy.
- delete browser policy
- enterprise it
- compliance officer
- data protection analyst
- designs sase and sd-wan network architectures for secure remote access.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- ai runtime security scanning and automated red teaming for ai applications.
- network security
- malware researcher
- enterprise browser
- create browser deployment
- researches threat actors, malware campaigns, and vulnerability trends.
- manages enterprise browser policies and secure browsing configurations.
- cloud security posture management, compliance monitoring, and workload protection.
- manage a specific browser policy by id.
- get user sessions
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- proactively searches for threats and iocs across telemetry data.
- platform engineer
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- analyzes suspicious files and samples for malware characteristics.
- manage enterprise browser security policies.
- firewall policy management, network objects, and cloud-native firewall configuration.
- monitors network health, performance, and digital experience metrics.
- vulnerability manager
- manages multi-tenant security operations at scale for managed service providers.
- conducts automated adversarial testing against ai systems and llm applications.
- manages logging infrastructure, integrations, and platform automation.
- list all browser users with pagination.
- compliance team
- list browser users
- designs and implements network security architectures and policies.
- manages multi-tenant hierarchies and service group configurations for mssps.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- list all browser policies with pagination.
- saas security admin
- tenant operator
- incident responder
- update a specific browser policy by id.
- get sessions for a specific user.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- cloud security engineer
- get browser policy
- manage browser deployments across platforms.
- create a new browser deployment.
- update browser policy
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- firewall
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- sase
- sd wan operator
- threat intel analyst
- manage enterprise browser policies, user sessions, and deployments.
- prisma access
- network operations
- manages service accounts, roles, and access policies for platform api access.
- threat hunter
- cybersecurity
- firewall admin
- soc analyst
- mssp operator
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- identity and access management, tenant hierarchies, and subscription management.
- monitors and remediates cloud security misconfigurations and compliance violations.
- browser security admin
- sase admin
- threat intelligence
- palo alto networks
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- get a specific browser policy by id.
- soar
- list browser deployments
- list browser policies
- get sessions for a specific browser user.
- investigates security incidents, triages alerts, and coordinates response actions.
- list all browser deployments with pagination.
- cloud security
- network architect
- delete a specific browser policy by id.
- executes containment, eradication, and recovery actions during security incidents.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- ai security engineer
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- xdr
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- sre
- network security engineer
- iam admin
- browser security
- data loss prevention, saas security monitoring, and identity security posture.
- digital experience monitoring, log management, and best practice assessment.
- secures ai applications with runtime scanning and vulnerability assessment.
- red team operator
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- enterprise browser policy management and secure browsing.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- list enterprise browser users.
- create browser policy
- investigates dlp incidents and manages sensitive data protection policies.
- subscription manager
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
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
