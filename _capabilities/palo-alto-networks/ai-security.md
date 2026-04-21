---
consumed_apis:
- prisma-airs
- prisma-airs-red-teaming
description: Unified AI security capability for scanning AI model inputs/outputs for threats and red-teaming AI applications for vulnerabilities across Prisma AIRS and AI Red Teaming APIs.
layout: capability
name: Palo Alto Networks AI Security
operations:
- description: Submit a synchronous scan of AI model inputs/outputs for threats.
  method: POST
  name: submit-sync-scan
  path: /v1/ai-scans/sync
- description: Submit an asynchronous scan of AI model inputs/outputs for threats.
  method: POST
  name: submit-async-scan
  path: /v1/ai-scans/async
- description: Get the results of a previously submitted asynchronous scan.
  method: GET
  name: get-async-scan-results
  path: /v1/ai-scans/async/{scan_id}/results
- description: List all AI security profiles with pagination.
  method: GET
  name: list-ai-profiles
  path: /v1/ai-profiles
- description: Get a specific AI security profile by name.
  method: GET
  name: get-ai-profile
  path: /v1/ai-profiles/{profile_name}
- description: Create a new red team scan target.
  method: POST
  name: create-red-team-target
  path: /v1/red-team-targets
- description: List all red team scan targets.
  method: GET
  name: list-red-team-targets
  path: /v1/red-team-targets
- description: Get a specific red team scan target by ID.
  method: GET
  name: get-red-team-target
  path: /v1/red-team-targets/{target_id}
- description: Delete a specific red team scan target by ID.
  method: DELETE
  name: delete-red-team-target
  path: /v1/red-team-targets/{target_id}
- description: Start a new red team vulnerability scan against a target.
  method: POST
  name: start-red-team-scan
  path: /v1/red-team-scans
- description: Get the status of a red team vulnerability scan.
  method: GET
  name: get-red-team-scan-status
  path: /v1/red-team-scans/{scan_id}
- description: Get results of a red team vulnerability scan with optional filters.
  method: GET
  name: get-red-team-scan-results
  path: /v1/red-team-scans/{scan_id}/results
- description: List all available attack categories for red team scans.
  method: GET
  name: list-attack-categories
  path: /v1/attack-categories
personas:
- description: Secures AI applications with runtime scanning and vulnerability assessment.
  id: ai-security-engineer
  name: AI Security Engineer
- description: Conducts automated adversarial testing against AI systems and LLM applications.
  id: red-team-operator
  name: Red Team Operator
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
search_terms:
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- submit async scan
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- platform engineer
- list all red team scan targets with optional type filter.
- list red team targets
- saas security admin
- enterprise it
- get a specific red team scan target by id.
- threat hunter
- network operations
- start red team scan
- get results of an asynchronous ai security scan.
- manage ai red teaming scan targets.
- threat intel analyst
- compliance team
- get the status of a red team vulnerability scan.
- executes containment, eradication, and recovery actions during security incidents.
- sre
- manages multi-tenant hierarchies and service group configurations for mssps.
- firewall
- sase
- incident responder
- delete a specific red team scan target by id.
- network architect
- list all ai security profiles with pagination.
- get the results of a previously submitted asynchronous scan.
- designs sase and sd-wan network architectures for secure remote access.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- create a new red team scan target.
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- cloud security
- list ai security profiles.
- firewall admin
- prompt injection
- manages service accounts, roles, and access policies for platform api access.
- designs and implements network security architectures and policies.
- soc analyst
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- network security engineer
- monitors and remediates cloud security misconfigurations and compliance violations.
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- enterprise browser policy management and secure browsing.
- cloud security engineer
- vulnerability manager
- manage enterprise browser policies, user sessions, and deployments.
- firewall policy management, network objects, and cloud-native firewall configuration.
- submit sync scan
- get a specific ai security profile.
- submit a synchronous ai security scan of model inputs/outputs for threats like prompt injection, data leakage, and malicious content.
- get red team scan results
- submit an asynchronous scan of ai model inputs/outputs for threats.
- data loss prevention, saas security monitoring, and identity security posture.
- malware researcher
- soar
- red team operator
- get ai profile
- get results of a red team vulnerability scan.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- investigates security incidents, triages alerts, and coordinates response actions.
- submit an asynchronous ai security scan of model inputs/outputs for threats.
- investigates dlp incidents and manages sensitive data protection policies.
- get async scan results
- list attack categories
- ai security
- conducts automated adversarial testing against ai systems and llm applications.
- submit an asynchronous ai security scan.
- compliance officer
- get a specific ai security profile by name.
- get results of a previously submitted asynchronous ai security scan.
- manages enterprise browser policies and secure browsing configurations.
- network security
- analyzes suspicious files and samples for malware characteristics.
- start a new red team vulnerability scan against a target ai application.
- subscription manager
- list ai profiles
- submit a synchronous scan of ai model inputs/outputs for threats.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- ai runtime security scanning and automated red teaming for ai applications.
- threat intelligence
- create red team target
- cloud security posture management, compliance monitoring, and workload protection.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- get red team target
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- get results of a red team vulnerability scan with optional filters.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- get results of a red team vulnerability scan with optional category and severity filters.
- ai security engineer
- mssp operator
- list available attack categories for red teaming.
- researches threat actors, malware campaigns, and vulnerability trends.
- digital experience monitoring, log management, and best practice assessment.
- palo alto networks
- xdr
- data protection analyst
- start ai red team vulnerability scans.
- list all red team scan targets.
- iam admin
- manages logging infrastructure, integrations, and platform automation.
- delete red team target
- cybersecurity
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- sase admin
- start a new red team vulnerability scan against a target.
- sd wan operator
- list all available attack categories for red team vulnerability scans.
- monitors network health, performance, and digital experience metrics.
- proactively searches for threats and iocs across telemetry data.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- identity and access management, tenant hierarchies, and subscription management.
- browser security admin
- secures ai applications with runtime scanning and vulnerability assessment.
- get or delete a specific red team scan target.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- manages multi-tenant security operations at scale for managed service providers.
- tenant operator
- create a new red team scan target for ai application vulnerability testing.
- get red team scan status
- ai red teaming
- submit a synchronous ai security scan.
- llm security
- list all available attack categories for red team scans.
slug: ai-security
tags:
- Palo Alto Networks
- AI Security
- AI Red Teaming
- LLM Security
- Prompt Injection
tools:
- description: Submit a synchronous AI security scan of model inputs/outputs for threats like prompt injection, data leakage, and malicious content.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: submit-sync-scan
- description: Submit an asynchronous AI security scan of model inputs/outputs for threats.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: submit-async-scan
- description: Get results of a previously submitted asynchronous AI security scan.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-async-scan-results
- description: List all AI security profiles with pagination.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-ai-profiles
- description: Get a specific AI security profile by name.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-ai-profile
- description: Create a new red team scan target for AI application vulnerability testing.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: create-red-team-target
- description: List all red team scan targets with optional type filter.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-red-team-targets
- description: Get a specific red team scan target by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-red-team-target
- description: Delete a specific red team scan target by ID.
  hints:
    destructive: true
    idempotent: true
    openWorld: true
    readOnly: false
  name: delete-red-team-target
- description: Start a new red team vulnerability scan against a target AI application.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: start-red-team-scan
- description: Get the status of a red team vulnerability scan.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-red-team-scan-status
- description: Get results of a red team vulnerability scan with optional category and severity filters.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-red-team-scan-results
- description: List all available attack categories for red team vulnerability scans.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-attack-categories
---
