---
description: SubnetRuleRequest schema from Palo Alto Networks ZTNA Connector API
layout: schema
name: SubnetRuleRequest
properties_list:
- description: Display name for the subnet rule.
  name: name
  type: string
- description: CIDR notation subnet this rule covers.
  name: subnet
  type: string
- description: Connector group to use for routing traffic to this subnet.
  name: group_id
  type: string
- description: ''
  name: enabled
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/ztna-connector-api-subnet-rule-request-schema.json
slug: ztna-connector-api-subnet-rule-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SubnetRuleRequest
---
