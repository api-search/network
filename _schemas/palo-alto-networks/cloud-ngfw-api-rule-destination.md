---
description: Traffic destination matching criteria for a security rule.
layout: schema
name: RuleDestination
properties_list:
- description: Destination CIDR blocks.
  name: Cidrs
  type: array
- description: Destination country codes.
  name: Countries
  type: array
- description: ''
  name: Feeds
  type: array
- description: Names of FQDN lists defined in the rule stack.
  name: FqdnLists
  type: array
- description: ''
  name: PrefixLists
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cloud-ngfw-api-rule-destination-schema.json
slug: cloud-ngfw-api-rule-destination
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: RuleDestination
---
