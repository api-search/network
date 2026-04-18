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
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- platform engineer
- sd wan operator
- list all browser policies with pagination.
- manage enterprise browser security policies.
- list enterprise browser users.
- xdr
- malware researcher
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- network architect
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- network security
- tenant operator
- create browser deployment
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- enterprise browser
- network security engineer
- saas security admin
- list browser policies
- conducts automated adversarial testing against ai systems and llm applications.
- executes containment, eradication, and recovery actions during security incidents.
- delete browser policy
- sre
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- threat intelligence
- list all browser users with pagination.
- prisma access
- delete a specific browser policy by id.
- create a new browser policy.
- red team operator
- monitors and remediates cloud security misconfigurations and compliance violations.
- manages logging infrastructure, integrations, and platform automation.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- manage browser deployments across platforms.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- researches threat actors, malware campaigns, and vulnerability trends.
- soar
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- list all browser deployments with pagination.
- enterprise it
- get sessions for a specific user.
- vulnerability manager
- iam admin
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- manage enterprise browser policies, user sessions, and deployments.
- incident responder
- update a specific browser policy by id.
- investigates security incidents, triages alerts, and coordinates response actions.
- ai security engineer
- identity and access management, tenant hierarchies, and subscription management.
- ai runtime security scanning and automated red teaming for ai applications.
- browser security admin
- enterprise browser policy management and secure browsing.
- designs and implements network security architectures and policies.
- cloud security posture management, compliance monitoring, and workload protection.
- monitors network health, performance, and digital experience metrics.
- browser security
- list browser deployments
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- get a specific browser policy by id.
- sase admin
- update browser policy
- data protection analyst
- secures ai applications with runtime scanning and vulnerability assessment.
- sase
- investigates dlp incidents and manages sensitive data protection policies.
- compliance team
- manages service accounts, roles, and access policies for platform api access.
- cloud security engineer
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- threat hunter
- cloud security
- manages enterprise browser policies and secure browsing configurations.
- digital experience monitoring, log management, and best practice assessment.
- firewall policy management, network objects, and cloud-native firewall configuration.
- threat intel analyst
- cybersecurity
- mssp operator
- proactively searches for threats and iocs across telemetry data.
- manages multi-tenant security operations at scale for managed service providers.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- manages multi-tenant hierarchies and service group configurations for mssps.
- get user sessions
- analyzes suspicious files and samples for malware characteristics.
- subscription manager
- firewall
- manage a specific browser policy by id.
- create a new browser deployment.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- get browser policy
- create browser policy
- palo alto networks
- list browser users
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- get sessions for a specific browser user.
- data loss prevention, saas security monitoring, and identity security posture.
- soc analyst
- designs sase and sd-wan network architectures for secure remote access.
- firewall admin
- network operations
- compliance officer
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
