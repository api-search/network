---
description: SubnetRule schema from Palo Alto Networks ZTNA Connector API
layout: schema
name: SubnetRule
properties_list:
- description: Unique identifier of the subnet rule.
  name: rule_id
  type: string
- description: Display name of the rule.
  name: name
  type: string
- description: CIDR notation subnet this rule covers (e.g., 10.0.0.0/8).
  name: subnet
  type: string
- description: Connector group used to route traffic to this subnet.
  name: group_id
  type: string
- description: Whether this rule is active.
  name: enabled
  type: boolean
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/ztna-connector-api-subnet-rule-schema.json
slug: ztna-connector-api-subnet-rule
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SubnetRule
---
