---
description: Content release notes for a specific PAN-OS content version.
layout: schema
name: ReleaseNote
properties_list:
- description: Content version identifier (e.g., 8000-7000).
  name: version
  type: string
- description: ''
  name: type
  type: string
- description: ''
  name: release_date
  type: string
- description: Number of new signatures in this release.
  name: new_signatures
  type: integer
- description: Number of modified signatures in this release.
  name: modified_signatures
  type: integer
- description: Number of deprecated signatures in this release.
  name: deprecated_signatures
  type: integer
- description: Release notes text.
  name: notes
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/threat-vault-api-release-note-schema.json
slug: threat-vault-api-release-note
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ReleaseNote
---
