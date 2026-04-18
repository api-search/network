---
description: FQDNRuleRequest schema from Palo Alto Networks ZTNA Connector API
layout: schema
name: FQDNRuleRequest
properties_list:
- description: Display name for the FQDN rule.
  name: name
  type: string
- description: FQDN pattern or wildcard this rule matches.
  name: fqdn_pattern
  type: string
- description: Connector group to use for matching FQDNs.
  name: group_id
  type: string
- description: Ports covered by this rule.
  name: ports
  type: array
- description: ''
  name: enabled
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/ztna-connector-api-fqdn-rule-request-schema.json
slug: ztna-connector-api-fqdn-rule-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: FQDNRuleRequest
---
