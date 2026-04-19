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
- secures ai applications with runtime scanning and vulnerability assessment.
- xdr
- vulnerability manager
- soar
- get sessions for a specific user.
- update browser policy
- network security engineer
- manage enterprise browser security policies.
- list browser users
- manages service accounts, roles, and access policies for platform api access.
- threat hunter
- browser security admin
- soc analyst
- platform engineer
- manages logging infrastructure, integrations, and platform automation.
- network architect
- digital experience monitoring, log management, and best practice assessment.
- saas security admin
- get a specific browser policy by id.
- tenant operator
- identity and access management, tenant hierarchies, and subscription management.
- ai security engineer
- iam admin
- list browser policies
- subscription manager
- network operations
- monitors network health, performance, and digital experience metrics.
- manages multi-tenant security operations at scale for managed service providers.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- list enterprise browser users.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- sase
- sase admin
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- create browser policy
- firewall
- network security
- designs sase and sd-wan network architectures for secure remote access.
- list browser deployments
- update a specific browser policy by id.
- researches threat actors, malware campaigns, and vulnerability trends.
- enterprise it
- list all browser deployments with pagination.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- create a new browser deployment.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- incident responder
- cloud security posture management, compliance monitoring, and workload protection.
- designs and implements network security architectures and policies.
- conducts automated adversarial testing against ai systems and llm applications.
- get sessions for a specific browser user.
- delete a specific browser policy by id.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- cybersecurity
- threat intel analyst
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- manages enterprise browser policies and secure browsing configurations.
- cloud security
- proactively searches for threats and iocs across telemetry data.
- firewall admin
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- delete browser policy
- data protection analyst
- red team operator
- firewall policy management, network objects, and cloud-native firewall configuration.
- prisma access
- sd wan operator
- investigates security incidents, triages alerts, and coordinates response actions.
- list all browser policies with pagination.
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- manage browser deployments across platforms.
- executes containment, eradication, and recovery actions during security incidents.
- manages multi-tenant hierarchies and service group configurations for mssps.
- manage enterprise browser policies, user sessions, and deployments.
- create browser deployment
- analyzes suspicious files and samples for malware characteristics.
- mssp operator
- sre
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- browser security
- ai runtime security scanning and automated red teaming for ai applications.
- malware researcher
- compliance team
- manage a specific browser policy by id.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- data loss prevention, saas security monitoring, and identity security posture.
- enterprise browser
- threat intelligence
- palo alto networks
- create a new browser policy.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- list all browser users with pagination.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- get browser policy
- get user sessions
- cloud security engineer
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- compliance officer
- monitors and remediates cloud security misconfigurations and compliance violations.
- investigates dlp incidents and manages sensitive data protection policies.
- enterprise browser policy management and secure browsing.
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
