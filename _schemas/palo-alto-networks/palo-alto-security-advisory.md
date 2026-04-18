---
description: Schema for a Palo Alto Networks PSIRT (Product Security Incident Response Team) security advisory in CVE JSON 5.0 format. Security advisories disclose vulnerabilities affecting Palo Alto Networks products including PAN-OS, Cortex XDR, Prisma Cloud, Prisma Access, GlobalProtect, Cortex XSOAR, and other solutions. Each advisory provides vulnerability details, CVSS scoring, affected product versions, fixed versions, workarounds, and references. Advisories are published on security.paloaltonetworks.com and updated as new information becomes available.
layout: schema
name: Palo Alto Networks Security Advisory
properties_list:
- description: Identifies the CVE JSON record type. Must be 'CVE_RECORD' for standard CVE records published by a CVE Numbering Authority.
  name: dataType
  type: string
- description: Top-level metadata about the CVE record including the CVE identifier, assigning organization, publication state, and timestamps.
  name: cveMetadata
  type: object
- description: Container objects holding the vulnerability details contributed by the CNA (Palo Alto Networks PSIRT) and any authorized data publishers (ADP) such as CISA or NVD.
  name: containers
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/palo-alto-security-advisory-schema.json
slug: palo-alto-security-advisory
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Palo Alto Networks Security Advisory
---
