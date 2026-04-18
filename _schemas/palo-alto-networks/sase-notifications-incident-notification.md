---
description: IncidentNotification schema from SASE Multitenant Notifications
layout: schema
name: IncidentNotification
properties_list:
- description: Unique identifier for this notification delivery.
  name: notificationId
  type: string
- description: Notification type identifier.
  name: type
  type: string
- description: Tenant Service Group identifier indicating which tenant context the incident belongs to.
  name: tsg_id
  type: string
- description: Severity classification of the security incident.
  name: severity
  type: string
- description: Brief title summarizing the incident.
  name: title
  type: string
- description: Detailed description of the incident including affected resources, detection context, and recommended actions.
  name: description
  type: string
- description: Timestamp when the incident was detected.
  name: timestamp
  type: string
- description: Incident category such as threat, policy_violation, anomaly, or data_loss.
  name: category
  type: string
- description: List of resources affected by the incident.
  name: affectedResources
  type: array
- description: Direct link to the incident in the SASE management console.
  name: callbackUrl
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-notifications-incident-notification-schema.json
slug: sase-notifications-incident-notification
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: IncidentNotification
---
