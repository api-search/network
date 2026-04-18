---
description: A PSIRT security advisory for a Palo Alto Networks product.
layout: schema
name: Advisory
properties_list:
- description: Palo Alto Networks advisory identifier (e.g., PAN-SA-2024-0001).
  name: advisory_id
  type: string
- description: CVE identifier (e.g., CVE-2024-3400).
  name: cve_id
  type: string
- description: Advisory title summarizing the vulnerability.
  name: title
  type: string
- description: Detailed description of the vulnerability including impact and attack vector.
  name: description
  type: string
- description: Severity rating based on CVSS v3.1 base score.
  name: severity
  type: string
- description: CVSS v3.1 base score (0.0 to 10.0).
  name: cvss_score
  type: number
- description: CVSS v3.1 vector string (e.g., CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).
  name: cvss_vector
  type: string
- description: CWE identifier for the vulnerability class.
  name: cwe
  type: string
- description: Products and version ranges affected by this vulnerability.
  name: affected_products
  type: array
- description: Product versions in which the vulnerability is fixed.
  name: fixed_versions
  type: array
- description: Available workarounds or mitigations if a fix is not yet deployed.
  name: workarounds
  type: string
- description: Known exploit activity status.
  name: exploit_status
  type: string
- description: Date and time when the advisory was first published.
  name: published_date
  type: string
- description: Date and time of the most recent advisory update.
  name: last_modified_date
  type: string
- description: External references and related advisories.
  name: references
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/security-advisory-api-advisory-schema.json
slug: security-advisory-api-advisory
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Advisory
---
