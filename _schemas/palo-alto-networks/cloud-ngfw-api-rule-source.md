---
description: Traffic source matching criteria for a security rule.
layout: schema
name: RuleSource
properties_list:
- description: Source CIDR blocks (e.g., 10.0.0.0/8).
  name: Cidrs
  type: array
- description: Source country codes (ISO 3166-1 alpha-2).
  name: Countries
  type: array
- description: Threat intelligence feed names.
  name: Feeds
  type: array
- description: Names of prefix lists defined in the rule stack.
  name: PrefixLists
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cloud-ngfw-api-rule-source-schema.json
slug: cloud-ngfw-api-rule-source
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: RuleSource
---
