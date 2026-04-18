---
description: SecurityPolicy5GRequest schema from Palo Alto Networks SASE 5G Managed Services API
layout: schema
name: SecurityPolicy5GRequest
properties_list:
- description: Display name for the security policy.
  name: name
  type: string
- description: Optional description.
  name: description
  type: string
- description: ''
  name: threat_prevention
  type: boolean
- description: ''
  name: url_filtering
  type: boolean
- description: ''
  name: app_identification
  type: boolean
- description: ''
  name: decryption
  type: boolean
- description: ''
  name: log_forwarding
  type: boolean
- description: ''
  name: enabled
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-5g-api-security-policy5-g-request-schema.json
slug: sase-5g-api-security-policy5-g-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SecurityPolicy5GRequest
---
