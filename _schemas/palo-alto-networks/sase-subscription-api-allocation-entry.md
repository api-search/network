---
description: AllocationEntry schema from Palo Alto Networks SASE Subscription Service API
layout: schema
name: AllocationEntry
properties_list:
- description: Child TSG ID receiving this allocation.
  name: tsg_id
  type: string
- description: Display name of the child TSG.
  name: tsg_name
  type: string
- description: Quantity allocated to this TSG.
  name: allocated_quantity
  type: integer
- description: Quantity currently utilized by this TSG.
  name: utilized_quantity
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-subscription-api-allocation-entry-schema.json
slug: sase-subscription-api-allocation-entry
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AllocationEntry
---
