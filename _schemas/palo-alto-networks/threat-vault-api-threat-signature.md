---
description: Threat signature metadata record.
layout: schema
name: ThreatSignature
properties_list:
- description: Unique signature identifier.
  name: id
  type: integer
- description: Signature name.
  name: name
  type: string
- description: Signature type category.
  name: type
  type: string
- description: Signature subtype (e.g., virus, trojan, exploit).
  name: subtype
  type: string
- description: ''
  name: severity
  type: string
- description: Human-readable description of the threat.
  name: description
  type: string
- description: Associated CVE identifiers.
  name: cve
  type: array
- description: Default action applied to traffic matching this signature.
  name: default_action
  type: string
- description: Minimum PAN-OS version supporting this signature.
  name: min_version
  type: string
- description: Maximum PAN-OS version supporting this signature (empty if still active).
  name: max_version
  type: string
- description: ''
  name: status
  type: string
- description: Content version in which this signature was first released.
  name: ori_release_version
  type: string
- description: Most recent content version that updated this signature.
  name: latest_release_version
  type: string
- description: Timestamp when the signature was first released.
  name: first_release_time
  type: string
- description: Timestamp of the most recent signature update.
  name: latest_release_time
  type: string
- description: SHA-256 hashes associated with this signature (antivirus).
  name: sha256
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/threat-vault-api-threat-signature-schema.json
slug: threat-vault-api-threat-signature
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ThreatSignature
---
