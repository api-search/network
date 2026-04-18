---
description: A rule stack containing security policy for Cloud NGFW firewall instances.
layout: schema
name: RuleStack
properties_list:
- description: Unique name of the rule stack.
  name: RuleStackName
  type: string
- description: ''
  name: RuleStackEntry
  type: object
- description: Optimistic lock token for concurrent modification detection.
  name: UpdateToken
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cloud-ngfw-api-rule-stack-schema.json
slug: cloud-ngfw-api-rule-stack
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: RuleStack
---
