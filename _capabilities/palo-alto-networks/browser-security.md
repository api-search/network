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
- palo alto networks
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- ai security engineer
- list browser users
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- investigates security incidents, triages alerts, and coordinates response actions.
- cybersecurity
- soar
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- list enterprise browser users.
- browser security
- designs and implements network security architectures and policies.
- soc analyst
- manages service accounts, roles, and access policies for platform api access.
- conducts automated adversarial testing against ai systems and llm applications.
- sase
- sd wan operator
- secure access service edge with remote networking, sd-wan, and zero trust access.
- prisma access
- list all browser users with pagination.
- vulnerability manager
- update browser policy
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- create browser deployment
- researches threat actors, malware campaigns, and vulnerability trends.
- list all browser policies with pagination.
- mssp operator
- malware researcher
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- incident responder
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- browser security admin
- sase admin
- manages multi-tenant security operations at scale for managed service providers.
- get sessions for a specific user.
- platform engineer
- manage browser deployments across platforms.
- cloud security engineer
- firewall
- get sessions for a specific browser user.
- network security engineer
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- monitors and remediates cloud security misconfigurations and compliance violations.
- manages enterprise browser policies and secure browsing configurations.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- manage a specific browser policy by id.
- compliance team
- get user sessions
- create a new browser policy.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- designs sase and sd-wan network architectures for secure remote access.
- cloud security
- list all browser deployments with pagination.
- cloud security posture management, compliance monitoring, and workload protection.
- get a specific browser policy by id.
- threat hunter
- data loss prevention, saas security monitoring, and identity security posture.
- iam admin
- sre
- create a new browser deployment.
- manages logging infrastructure, integrations, and platform automation.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- saas security admin
- secures ai applications with runtime scanning and vulnerability assessment.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- manage enterprise browser policies, user sessions, and deployments.
- proactively searches for threats and iocs across telemetry data.
- data protection analyst
- manages multi-tenant hierarchies and service group configurations for mssps.
- firewall policy management, network objects, and cloud-native firewall configuration.
- threat intel analyst
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- ai runtime security scanning and automated red teaming for ai applications.
- executes containment, eradication, and recovery actions during security incidents.
- list browser deployments
- compliance officer
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- red team operator
- analyzes suspicious files and samples for malware characteristics.
- threat intelligence
- create browser policy
- update a specific browser policy by id.
- enterprise browser
- delete browser policy
- monitors network health, performance, and digital experience metrics.
- subscription manager
- digital experience monitoring, log management, and best practice assessment.
- list browser policies
- network architect
- enterprise it
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- network security
- identity and access management, tenant hierarchies, and subscription management.
- firewall admin
- manage enterprise browser security policies.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- xdr
- network operations
- delete a specific browser policy by id.
- investigates dlp incidents and manages sensitive data protection policies.
- tenant operator
- enterprise browser policy management and secure browsing.
- get browser policy
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
