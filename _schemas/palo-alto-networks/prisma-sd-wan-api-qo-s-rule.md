---
description: QoSRule schema from Palo Alto Networks Prisma SD-WAN API
layout: schema
name: QoSRule
properties_list:
- description: Unique identifier for the QoS rule.
  name: id
  type: string
- description: Name of the QoS rule.
  name: name
  type: string
- description: ''
  name: description
  type: string
- description: Traffic priority for matching flows.
  name: priority
  type: string
- description: DSCP class to apply for marking traffic.
  name: dscp_class
  type: string
- description: Application names or identifiers this rule applies to.
  name: app_filters
  type: array
- description: Upstream bandwidth limit in Mbps for matched traffic.
  name: bandwidth_limit_up
  type: number
- description: Downstream bandwidth limit in Mbps for matched traffic.
  name: bandwidth_limit_down
  type: number
- description: Whether the rule is active.
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
schema_file: json-schema/prisma-sd-wan-api-qo-s-rule-schema.json
slug: prisma-sd-wan-api-qo-s-rule
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: QoSRule
---
