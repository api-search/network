---
description: WebhookChannelDetails schema from Multi-Tenant Notifications API
layout: schema
name: WebhookChannelDetails
properties_list:
- description: List of Webhook URLs - do not include token in the URL
  name: urls
  type: array
- description: Webhook Authentication Type
  name: authType
  type: string
- description: Webhook token value
  name: token
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-multitenant-notifications-api-webhook-channel-details-schema.json
slug: sase-multitenant-notifications-api-webhook-channel-details
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: WebhookChannelDetails
---
