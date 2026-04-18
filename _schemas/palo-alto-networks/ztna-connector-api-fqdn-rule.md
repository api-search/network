---
description: FQDNRule schema from Palo Alto Networks ZTNA Connector API
layout: schema
name: FQDNRule
properties_list:
- description: Unique identifier of the FQDN rule.
  name: rule_id
  type: string
- description: Display name of the rule.
  name: name
  type: string
- description: FQDN pattern or wildcard (e.g., *.internal.example.com) that this rule matches.
  name: fqdn_pattern
  type: string
- description: Connector group used to resolve and access matching FQDNs.
  name: group_id
  type: string
- description: Ports covered by this rule.
  name: ports
  type: array
- description: Whether this rule is active.
  name: enabled
  type: boolean
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/ztna-connector-api-fqdn-rule-schema.json
slug: ztna-connector-api-fqdn-rule
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: FQDNRule
---
