---
description: SecurityPolicy5G schema from Palo Alto Networks SASE 5G Managed Services API
layout: schema
name: SecurityPolicy5G
properties_list:
- description: Unique identifier of the security policy.
  name: policy_id
  type: string
- description: Display name of the security policy.
  name: name
  type: string
- description: Description of the policy's purpose.
  name: description
  type: string
- description: Whether threat prevention inspection is enabled.
  name: threat_prevention
  type: boolean
- description: Whether URL filtering is enabled for 5G data traffic.
  name: url_filtering
  type: boolean
- description: Whether application identification is enabled.
  name: app_identification
  type: boolean
- description: Whether SSL/TLS decryption is enabled.
  name: decryption
  type: boolean
- description: Whether log forwarding is enabled for this policy.
  name: log_forwarding
  type: boolean
- description: Whether this policy is active.
  name: enabled
  type: boolean
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-5g-api-security-policy5-g-schema.json
slug: sase-5g-api-security-policy5-g
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SecurityPolicy5G
---
