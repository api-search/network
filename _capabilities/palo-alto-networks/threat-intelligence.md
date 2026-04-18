---
consumed_apis:
- threat-vault
- wildfire
- dns-security
- security-advisory
description: Unified threat intelligence capability for researching IOCs, submitting malware samples, analyzing DNS threats, and tracking security advisories across Threat Vault, WildFire, DNS Security, and Security Advisories.
layout: capability
name: Palo Alto Networks Threat Intelligence
operations:
- description: Search for threats by type, ID, SHA256, name, CVE, or date range.
  method: GET
  name: get-threats
  path: /v1/threats
- description: Get the history of a specific threat by ID and type.
  method: GET
  name: get-threat-history
  path: /v1/threats/{threat_id}/history
- description: Get Advanced Threat Prevention reports.
  method: GET
  name: get-atp-reports
  path: /v1/atp-reports
- description: Get packet captures from ATP reports.
  method: GET
  name: get-atp-report-pcaps
  path: /v1/atp-reports/pcaps
- description: Get release notes for threat content updates.
  method: GET
  name: get-release-notes
  path: /v1/release-notes
- description: Get Threat Vault usage statistics.
  method: GET
  name: get-threat-vault-stats
  path: /v1/threat-vault-stats
- description: Submit a file for WildFire analysis.
  method: POST
  name: submit-file
  path: /v1/samples/files
- description: Submit a URL for WildFire analysis.
  method: POST
  name: submit-url
  path: /v1/samples/urls
- description: Submit a link for WildFire analysis.
  method: POST
  name: submit-link
  path: /v1/samples/links
- description: Get the verdict for a file hash.
  method: POST
  name: get-verdict
  path: /v1/verdicts
- description: Get verdicts for multiple file hashes (max 500).
  method: POST
  name: get-bulk-verdicts
  path: /v1/verdicts/bulk
- description: Get the analysis report for a file hash.
  method: POST
  name: get-analysis-report
  path: /v1/analysis-reports
- description: Download a sample file by hash.
  method: POST
  name: download-sample
  path: /v1/analysis-reports/samples
- description: Get packet capture for a file hash.
  method: POST
  name: get-analysis-pcap
  path: /v1/analysis-reports/pcaps
- description: Get threat intelligence for a specific domain.
  method: GET
  name: get-domain
  path: /v1/domains
- description: Get threat intelligence for multiple domains.
  method: GET
  name: get-domain-bulk
  path: /v1/domains/bulk
- description: Get DNS network statistics for a given time range.
  method: GET
  name: get-dns-stats
  path: /v1/dns-stats
- description: List security advisories with optional filtering by severity and affected product.
  method: GET
  name: list-advisories
  path: /v1/advisories
- description: Get details of a specific security advisory by ID.
  method: GET
  name: get-advisory
  path: /v1/advisories/{advisory_id}
- description: Get a security advisory by its CVE identifier.
  method: GET
  name: get-advisory-by-cve
  path: /v1/advisories/cve/{cve_id}
- description: List all products affected by security advisories.
  method: GET
  name: list-affected-products
  path: /v1/affected-products
personas:
- description: Researches threat actors, malware campaigns, and vulnerability trends.
  id: threat-intel-analyst
  name: Threat Intelligence Analyst
- description: Analyzes suspicious files and samples for malware characteristics.
  id: malware-researcher
  name: Malware Researcher
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
search_terms:
- list palo alto networks security advisories with optional filtering by severity and affected product.
- get release notes for threat content updates.
- submit url
- get dns stats
- palo alto networks
- track digital experience, aggregate security data, manage log forwarding, run assessments, and handle notifications.
- ai security engineer
- manage service accounts, access policies, tenant hierarchies, subscriptions, and identity data.
- get dns threat intelligence for a specific domain.
- investigates security incidents, triages alerts, and coordinates response actions.
- cybersecurity
- soar
- threat research, malware analysis, ioc correlation, and vulnerability tracking.
- download pcap
- download a packet capture for a file hash from wildfire.
- download a sample file by hash.
- manages service accounts, roles, and access policies for platform api access.
- designs and implements network security architectures and policies.
- soc analyst
- get signature history for a specific threat.
- list security advisories
- conducts automated adversarial testing against ai systems and llm applications.
- get threat intelligence for a specific domain.
- submit link for analysis
- submit url for analysis
- sase
- get verdict
- sd wan operator
- get analysis report
- get wildfire verdicts for file hashes.
- download sample
- get release notes
- query domain threat intelligence from dns security.
- secure access service edge with remote networking, sd-wan, and zero trust access.
- get threat intelligence for multiple domains.
- download a malware sample from wildfire.
- vulnerability manager
- submit a link for wildfire malware analysis.
- get the wildfire analysis report for a file hash.
- research iocs, submit malware samples, analyze dns threats, and track security advisories.
- get advanced threat prevention reports from threat vault.
- download atp pcap files.
- palo alto networks security advisories.
- bulk lookup domains
- researches threat actors, malware campaigns, and vulnerability trends.
- get wildfire verdicts for multiple file hashes.
- mssp operator
- malware researcher
- get wildfire verdicts for multiple file hashes (max 500).
- investigate incidents, triage alerts, manage endpoints, execute response playbooks, and assess attack surface.
- download a malware sample file by hash from wildfire.
- incident responder
- search threat signatures by type, id, sha256, name, cve, or date range.
- threat vault api usage statistics.
- download atp pcaps
- manage cloud alerts, enforce policies, monitor compliance, scan code, and assess data security.
- get domain
- sase admin
- browser security admin
- get details of a specific palo alto networks security advisory by id.
- manages multi-tenant security operations at scale for managed service providers.
- submit file for analysis
- platform engineer
- get a security advisory by its cve identifier.
- malware analysis
- cloud security engineer
- get a security advisory by cve identifier.
- get atp reports
- list security advisories with optional filtering by severity and affected product.
- get packet capture for a file hash.
- firewall
- network security engineer
- manage remote networks, ztna connectors, sd-wan sites, 5g security, and service provider interconnects.
- search threat signatures
- download packet captures from atp reports in threat vault.
- monitors and remediates cloud security misconfigurations and compliance violations.
- get the history of a specific threat by id and type.
- get atp report pcaps
- get release notes for threat content updates from threat vault.
- get security advisory
- manages enterprise browser policies and secure browsing configurations.
- list advisories
- products affected by security advisories.
- get packet captures from atp reports.
- manages firewall policies, objects, and configurations across physical and virtual firewalls.
- submit link
- get threat vault stats
- compliance team
- list all products affected by security advisories.
- get threats
- manage dlp incidents, email violations, saas assets, posture checks, and identity security.
- designs sase and sd-wan network architectures for secure remote access.
- cloud security
- get the wildfire verdict for a file hash.
- cloud security posture management, compliance monitoring, and workload protection.
- get advisory
- threat hunter
- data loss prevention, saas security monitoring, and identity security posture.
- get the history of a specific threat signature by id and type from threat vault.
- iam admin
- sre
- submit a url for wildfire analysis.
- ioc research
- lookup domain
- bulk query domain threat intelligence.
- manages sd-wan sites, wan interfaces, and path policies for branch connectivity.
- manages logging infrastructure, integrations, and platform automation.
- saas security admin
- secures ai applications with runtime scanning and vulnerability assessment.
- get dns network stats
- scan ai model inputs and outputs for threats and red-team ai applications for vulnerabilities.
- get a specific security advisory by id.
- submit file
- list affected products
- submit a link for wildfire analysis.
- manage enterprise browser policies, user sessions, and deployments.
- get the analysis report for a file hash.
- get threat vault usage statistics.
- proactively searches for threats and iocs across telemetry data.
- get a palo alto networks security advisory by its cve identifier.
- data protection analyst
- manages multi-tenant hierarchies and service group configurations for mssps.
- firewall policy management, network objects, and cloud-native firewall configuration.
- get advisory by cve
- get analysis pcap
- get domain bulk
- threat intel analyst
- manage firewall objects, security rules, nat rules, and cloud ngfw rule stacks.
- ai runtime security scanning and automated red teaming for ai applications.
- executes containment, eradication, and recovery actions during security incidents.
- dns network statistics.
- get the verdict for a file hash.
- submit a file for wildfire analysis.
- compliance officer
- ensures cloud infrastructure meets regulatory and industry compliance standards.
- red team operator
- get threat vault api usage statistics.
- get bulk verdicts
- analyzes suspicious files and samples for malware characteristics.
- threat intelligence
- advanced threat prevention reports.
- search for threat signatures by type, id, sha256, name, cve, or date range in threat vault.
- monitors network health, performance, and digital experience metrics.
- subscription manager
- list all palo alto networks products affected by security advisories.
- get threat history
- digital experience monitoring, log management, and best practice assessment.
- vulnerability management
- network architect
- enterprise it
- incident detection, investigation, response, and automation across endpoints, network, and cloud.
- network security
- submit a url for wildfire malware analysis.
- get packet captures from wildfire analysis.
- get advanced threat prevention reports.
- get dns network statistics for a given time range.
- search for threats by type, id, sha256, name, cve, or date range.
- content release notes for threat updates.
- identity and access management, tenant hierarchies, and subscription management.
- get details of a specific security advisory by id.
- firewall admin
- manages prisma access, sd-wan, and ztna configurations for the sase platform.
- xdr
- network operations
- get dns threat intelligence for multiple domains in bulk.
- investigates dlp incidents and manages sensitive data protection policies.
- get wildfire analysis reports.
- tenant operator
- get verdicts for multiple file hashes (max 500).
- submit a file for wildfire malware analysis.
- enterprise browser policy management and secure browsing.
slug: threat-intelligence
tags:
- Palo Alto Networks
- Threat Intelligence
- Malware Analysis
- IOC Research
- Vulnerability Management
tools:
- description: Search for threat signatures by type, ID, SHA256, name, CVE, or date range in Threat Vault.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: search-threat-signatures
- description: Get the history of a specific threat signature by ID and type from Threat Vault.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-threat-history
- description: Get Advanced Threat Prevention reports from Threat Vault.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-atp-reports
- description: Download packet captures from ATP reports in Threat Vault.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: download-atp-pcaps
- description: Get release notes for threat content updates from Threat Vault.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-release-notes
- description: Get Threat Vault API usage statistics.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-threat-vault-stats
- description: Submit a file for WildFire malware analysis.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: submit-file-for-analysis
- description: Submit a URL for WildFire malware analysis.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: submit-url-for-analysis
- description: Submit a link for WildFire malware analysis.
  hints:
    destructive: false
    idempotent: false
    openWorld: true
    readOnly: false
  name: submit-link-for-analysis
- description: Get the WildFire verdict for a file hash.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-verdict
- description: Get WildFire verdicts for multiple file hashes (max 500).
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-bulk-verdicts
- description: Get the WildFire analysis report for a file hash.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-analysis-report
- description: Download a malware sample file by hash from WildFire.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: download-sample
- description: Download a packet capture for a file hash from WildFire.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: download-pcap
- description: Get DNS threat intelligence for a specific domain.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: lookup-domain
- description: Get DNS threat intelligence for multiple domains in bulk.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: bulk-lookup-domains
- description: Get DNS network statistics for a given time range.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-dns-network-stats
- description: List Palo Alto Networks security advisories with optional filtering by severity and affected product.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-security-advisories
- description: Get details of a specific Palo Alto Networks security advisory by ID.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-security-advisory
- description: Get a Palo Alto Networks security advisory by its CVE identifier.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: get-advisory-by-cve
- description: List all Palo Alto Networks products affected by security advisories.
  hints:
    destructive: false
    idempotent: true
    openWorld: true
    readOnly: true
  name: list-affected-products
---
