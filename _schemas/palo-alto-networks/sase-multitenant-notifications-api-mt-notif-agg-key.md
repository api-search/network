---
description: MtNotifAggKey schema from Multi-Tenant Notifications API
layout: schema
name: MtNotifAggKey
properties_list:
- description: TSG Id
  name: tsgId
  type: string
- description: Notification Type
  name: notifType
  type: string
- description: Notification category - is associated with notification type
  name: category
  type: string
- description: Notification sub-category - is associated with notification type and notification category
  name: subCategory
  type: string
- description: InApp Notification Flag
  name: inAppFlag
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-multitenant-notifications-api-mt-notif-agg-key-schema.json
slug: sase-multitenant-notifications-api-mt-notif-agg-key
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: MtNotifAggKey
---
