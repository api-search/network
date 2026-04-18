---
description: DataplaneUpgradeNotification schema from SASE Multitenant Notifications
layout: schema
name: DataplaneUpgradeNotification
properties_list:
- description: Unique identifier for this notification delivery.
  name: notificationId
  type: string
- description: Notification type identifier.
  name: type
  type: string
- description: Tenant Service Group identifier for the affected tenant.
  name: tsg_id
  type: string
- description: SASE compute region where the dataplane upgrade is occurring, such as us-east-1, eu-west-1, or ap-southeast-1.
  name: region
  type: string
- description: Current dataplane software version before the upgrade.
  name: currentVersion
  type: string
- description: Target dataplane software version after the upgrade completes.
  name: targetVersion
  type: string
- description: Scheduled start time for the dataplane upgrade maintenance window.
  name: scheduledTime
  type: string
- description: Estimated end time for the dataplane upgrade maintenance window.
  name: estimatedEndTime
  type: string
- description: Current status of the dataplane upgrade.
  name: status
  type: string
- description: Timestamp when this notification was generated.
  name: timestamp
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-notifications-dataplane-upgrade-notification-schema.json
slug: sase-notifications-dataplane-upgrade-notification
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DataplaneUpgradeNotification
---
