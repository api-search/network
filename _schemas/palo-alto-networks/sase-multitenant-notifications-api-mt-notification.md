---
description: MtNotification schema from Multi-Tenant Notifications API
layout: schema
name: MtNotification
properties_list:
- description: Notification id
  name: id
  type: string
- description: Notification name
  name: name
  type: string
- description: Description of the notification
  name: body
  type: string
- description: Action to be taken on receiving the notification (if applicable)
  name: action
  type: string
- description: Notification creation time
  name: createdTime
  type: number
- description: Multi-Tenant Notification Aggregation Key
  name: aggKey
  type: object
- description: List of impacted tenants
  name: impactedTenants
  type: array
- description: Number of tenants impacted by the multi-tenant notification
  name: impactedTenantCount
  type: number
- description: Read state of the notification
  name: notifReadState
  type: string
- description: List of output channels that the notification is sent on
  name: notifChannels
  type: array
- description: Notification type
  name: notifType
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-multitenant-notifications-api-mt-notification-schema.json
slug: sase-multitenant-notifications-api-mt-notification
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: MtNotification
---
