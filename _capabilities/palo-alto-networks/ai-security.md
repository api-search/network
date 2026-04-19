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
- create red team target
- start a new red team vulnerability scan against a target ai application.
- submit a synchronous ai security scan.
- submit a synchronous scan of ai model inputs/outputs for threats.
- get a specific ai security profile by name.
- enterprise it
- llm security
- compliance officer
- data protection analyst
- designs sase and sd-wan network architectures for secure remote access.
- list all available attack categories for red team scans.
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- ai runtime security scanning and automated red teaming for ai applications.
- network security
- malware researcher
- get the status of a red team vulnerability scan.
- researches threat actors, malware campaigns, and vulnerability trends.
- manages enterprise browser policies and secure browsing configurations.
- start red team scan
- get red team scan results
- cloud security posture management, compliance monitoring, and workload protection.
- list available attack categories for red teaming.
- get red team target
- get a specific ai security profile.
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- proactively searches for threats and iocs across telemetry data.
- platform engineer
- start a new red team vulnerability scan against a target.
- get or delete a specific red team scan target.
- get red team scan status
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- analyzes suspicious files and samples for malware characteristics.
- firewall policy management, network objects, and cloud-native firewall configuration.
- delete red team target
- monitors network health, performance, and digital experience metrics.
- vulnerability manager
- get the results of a previously submitted asynchronous scan.
- get async scan results
- conducts automated adversarial testing against ai systems and llm applications.
- manages multi-tenant security operations at scale for managed service providers.
- manages logging infrastructure, integrations, and platform automation.
- submit an asynchronous scan of ai model inputs/outputs for threats.
- compliance team
- get ai profile
- designs and implements network security architectures and policies.
- manages multi-tenant hierarchies and service group configurations for mssps.
- list ai security profiles.
- submit an asynchronous ai security scan of model inputs/outputs for threats.
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- saas security admin
- tenant operator
- incident responder
- secure access service edge with remote networking, sd-wan, and zero trust access.
- submit sync scan
- cloud security engineer
- ai red teaming
- list attack categories
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- get results of a red team vulnerability scan with optional filters.
- submit an asynchronous ai security scan.
- firewall
- list all red team scan targets.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- sase
- sd wan operator
- threat intel analyst
- list all red team scan targets with optional type filter.
- manage enterprise browser policies, user sessions, and deployments.
- get results of a red team vulnerability scan with optional category and severity filters.
- prompt injection
- network operations
- ai security
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
- start ai red team vulnerability scans.
- threat intelligence
- palo alto networks
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- get results of an asynchronous ai security scan.
- list red team targets
- soar
- investigates security incidents, triages alerts, and coordinates response actions.
- cloud security
- manage ai red teaming scan targets.
- network architect
- executes containment, eradication, and recovery actions during security incidents.
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- ai security engineer
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- delete a specific red team scan target by id.
- xdr
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- sre
- get a specific red team scan target by id.
- network security engineer
- create a new red team scan target for ai application vulnerability testing.
- get results of a previously submitted asynchronous ai security scan.
- iam admin
- get results of a red team vulnerability scan.
- data loss prevention, saas security monitoring, and identity security posture.
- digital experience monitoring, log management, and best practice assessment.
- secures ai applications with runtime scanning and vulnerability assessment.
- red team operator
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- create a new red team scan target.
- enterprise browser policy management and secure browsing.
- submit async scan
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- list all available attack categories for red team vulnerability scans.
- submit a synchronous ai security scan of model inputs/outputs for threats like prompt injection, data leakage, and malicious content.
- list ai profiles
- investigates dlp incidents and manages sensitive data protection policies.
- list all ai security profiles with pagination.
- subscription manager
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
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
