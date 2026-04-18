---
description: Entitlement schema from Palo Alto Networks SASE Subscription Service API
layout: schema
name: Entitlement
properties_list:
- description: Feature or capability name.
  name: feature
  type: string
- description: Licensed quantity for this entitlement.
  name: licensed_quantity
  type: integer
- description: Quantity already allocated to child TSGs.
  name: allocated_quantity
  type: integer
- description: Remaining quantity available for allocation.
  name: available_quantity
  type: integer
- description: Unit of measure.
  name: unit
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-subscription-api-entitlement-schema.json
slug: sase-subscription-api-entitlement
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Entitlement
---
