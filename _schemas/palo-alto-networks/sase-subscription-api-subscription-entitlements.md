---
description: SubscriptionEntitlements schema from Palo Alto Networks SASE Subscription Service API
layout: schema
name: SubscriptionEntitlements
properties_list:
- description: Unique identifier of the subscription.
  name: subscription_id
  type: string
- description: Product name.
  name: product_name
  type: string
- description: Granular entitlements included in the subscription.
  name: entitlements
  type: array
- description: Current license allocations by child TSG.
  name: allocations
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-subscription-api-subscription-entitlements-schema.json
slug: sase-subscription-api-subscription-entitlements
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SubscriptionEntitlements
---
