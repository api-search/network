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
- list all browser users with pagination.
- manage enterprise browser policies, user sessions, and deployments.
- list all browser policies with pagination.
- data protection analyst
- iam admin
- compliance team
- network operations
- get sessions for a specific user.
- cloud security
- list browser policies
- malware researcher
- palo alto networks
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- get browser policy
- incident responder
- xdr
- analyzes suspicious files and samples for malware characteristics.
- platform engineer
- executes containment, eradication, and recovery actions during security incidents.
- sd wan operator
- vulnerability manager
- get user sessions
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- browser security admin
- create a new browser deployment.
- ai runtime security scanning and automated red teaming for ai applications.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- threat intel analyst
- red team operator
- tenant operator
- manages logging infrastructure, integrations, and platform automation.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- monitors and remediates cloud security misconfigurations and compliance violations.
- cybersecurity
- browser security
- create a new browser policy.
- update browser policy
- firewall admin
- secures ai applications with runtime scanning and vulnerability assessment.
- enterprise browser policy management and secure browsing.
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- firewall policy management, network objects, and cloud-native firewall configuration.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- create browser deployment
- list browser deployments
- compliance officer
- investigates dlp incidents and manages sensitive data protection policies.
- sase admin
- cloud security posture management, compliance monitoring, and workload protection.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- network architect
- get a specific browser policy by id.
- mssp operator
- list all browser deployments with pagination.
- update a specific browser policy by id.
- network security engineer
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- prisma access
- data loss prevention, saas security monitoring, and identity security posture.
- list browser users
- researches threat actors, malware campaigns, and vulnerability trends.
- manages service accounts, roles, and access policies for platform api access.
- enterprise browser
- saas security admin
- sre
- manage enterprise browser security policies.
- manages multi-tenant security operations at scale for managed service providers.
- digital experience monitoring, log management, and best practice assessment.
- manages multi-tenant hierarchies and service group configurations for mssps.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- threat hunter
- soc analyst
- soar
- manages enterprise browser policies and secure browsing configurations.
- subscription manager
- manage a specific browser policy by id.
- cloud security engineer
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- sase
- threat intelligence
- designs and implements network security architectures and policies.
- conducts automated adversarial testing against ai systems and llm applications.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- designs sase and sd-wan network architectures for secure remote access.
- get sessions for a specific browser user.
- create browser policy
- firewall
- proactively searches for threats and iocs across telemetry data.
- delete a specific browser policy by id.
- network security
- enterprise it
- manage browser deployments across platforms.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- list enterprise browser users.
- ai security engineer
- investigates security incidents, triages alerts, and coordinates response actions.
- monitors network health, performance, and digital experience metrics.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- delete browser policy
- identity and access management, tenant hierarchies, and subscription management.
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
