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
- submit a synchronous ai security scan.
- palo alto networks
- designs sase and sd-wan network architectures for secure remote access.
- get the status of a red team vulnerability scan.
- network security engineer
- secures ai applications with runtime scanning and vulnerability assessment.
- get red team scan results
- sase admin
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- get results of a red team vulnerability scan with optional filters.
- submit an asynchronous ai security scan.
- start red team scan
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- submit async scan
- xdr
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- create red team target
- enterprise browser policy management and secure browsing.
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- submit sync scan
- delete a specific red team scan target by id.
- ai security engineer
- get or delete a specific red team scan target.
- data protection analyst
- network architect
- data loss prevention, saas security monitoring, and identity security posture.
- prompt injection
- saas security admin
- submit a synchronous ai security scan of model inputs/outputs for threats like prompt injection, data leakage, and malicious content.
- get async scan results
- manages multi-tenant hierarchies and service group configurations for mssps.
- network security
- soar
- manages enterprise browser policies and secure browsing configurations.
- get results of a previously submitted asynchronous ai security scan.
- get results of a red team vulnerability scan.
- compliance team
- investigates dlp incidents and manages sensitive data protection policies.
- researches threat actors, malware campaigns, and vulnerability trends.
- get a specific ai security profile by name.
- ai red teaming
- subscription manager
- compliance officer
- tenant operator
- executes containment, eradication, and recovery actions during security incidents.
- vulnerability manager
- cybersecurity
- malware researcher
- list all available attack categories for red team vulnerability scans.
- designs and implements network security architectures and policies.
- get red team scan status
- incident responder
- ai security
- list all ai security profiles with pagination.
- start a new red team vulnerability scan against a target ai application.
- mssp operator
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- get results of an asynchronous ai security scan.
- submit an asynchronous ai security scan of model inputs/outputs for threats.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- manages service accounts, roles, and access policies for platform api access.
- threat intel analyst
- firewall policy management, network objects, and cloud-native firewall configuration.
- sase
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- get ai profile
- get results of a red team vulnerability scan with optional category and severity filters.
- firewall admin
- soc analyst
- proactively searches for threats and iocs across telemetry data.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- start a new red team vulnerability scan against a target.
- network operations
- enterprise it
- manages logging infrastructure, integrations, and platform automation.
- browser security admin
- threat hunter
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- manage ai red teaming scan targets.
- analyzes suspicious files and samples for malware characteristics.
- list all available attack categories for red team scans.
- get a specific ai security profile.
- list all red team scan targets.
- monitors and remediates cloud security misconfigurations and compliance violations.
- monitors network health, performance, and digital experience metrics.
- list ai profiles
- submit an asynchronous scan of ai model inputs/outputs for threats.
- identity and access management, tenant hierarchies, and subscription management.
- get a specific red team scan target by id.
- ai runtime security scanning and automated red teaming for ai applications.
- start ai red team vulnerability scans.
- get the results of a previously submitted asynchronous scan.
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- list attack categories
- platform engineer
- digital experience monitoring, log management, and best practice assessment.
- iam admin
- llm security
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- get red team target
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- list ai security profiles.
- red team operator
- sre
- manages multi-tenant security operations at scale for managed service providers.
- create a new red team scan target for ai application vulnerability testing.
- threat intelligence
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- conducts automated adversarial testing against ai systems and llm applications.
- firewall
- investigates security incidents, triages alerts, and coordinates response actions.
- cloud security
- list all red team scan targets with optional type filter.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- cloud security posture management, compliance monitoring, and workload protection.
- manage enterprise browser policies, user sessions, and deployments.
- list available attack categories for red teaming.
- list red team targets
- create a new red team scan target.
- cloud security engineer
- delete red team target
- sd wan operator
- submit a synchronous scan of ai model inputs/outputs for threats.
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
