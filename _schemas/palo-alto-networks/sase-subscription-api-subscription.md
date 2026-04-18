---
description: Subscription schema from Palo Alto Networks SASE Subscription Service API
layout: schema
name: Subscription
properties_list:
- description: Unique identifier of the subscription.
  name: subscription_id
  type: string
- description: Tenant Service Group ID this subscription is associated with.
  name: tsg_id
  type: string
- description: Product name (e.g., Prisma Access, Prisma SD-WAN).
  name: product_name
  type: string
- description: Product SKU identifier.
  name: sku
  type: string
- description: Current subscription status.
  name: status
  type: string
- description: Total licensed quantity (e.g., number of users or devices).
  name: licensed_quantity
  type: integer
- description: Unit of measure for the licensed quantity (e.g., users, devices, Mbps).
  name: licensed_unit
  type: string
- description: Currently utilized quantity.
  name: utilized_quantity
  type: integer
- description: Subscription start date.
  name: start_date
  type: string
- description: Subscription end date.
  name: end_date
  type: string
- description: Support tier included with the subscription.
  name: support_level
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-subscription-api-subscription-schema.json
slug: sase-subscription-api-subscription
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Subscription
---
