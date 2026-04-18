---
description: An attack surface rule defining criteria for classifying internet exposures as incidents.
layout: schema
name: AttackSurfaceRule
properties_list:
- description: ''
  name: attack_surface_rule_id
  type: string
- description: ''
  name: attack_surface_rule_name
  type: string
- description: Rule category (e.g., Unencrypted, Misconfigured, Unauthorized).
  name: category
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: remediation_guidance
  type: string
- description: ''
  name: enabled_status
  type: string
- description: ''
  name: severity
  type: string
- description: ''
  name: created
  type: integer
- description: ''
  name: modified
  type: integer
- description: ''
  name: release_status
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xpanse-api-attack-surface-rule-schema.json
slug: cortex-xpanse-api-attack-surface-rule
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AttackSurfaceRule
---
