---
description: NotifChannel schema from Multi-Tenant Notifications API
layout: schema
name: NotifChannel
properties_list:
- description: Notification channel name
  name: name
  type: string
- description: Notification channel type
  name: type
  type: string
- description: Email channel details
  name: emailChannelDetails
  type: object
- description: Webhook channel details
  name: webhookChannelDetails
  type: object
- description: Channel output template
  name: template
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-multitenant-notifications-api-notif-channel-schema.json
slug: sase-multitenant-notifications-api-notif-channel
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: NotifChannel
---
