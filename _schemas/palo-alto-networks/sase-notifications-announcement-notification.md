---
description: AnnouncementNotification schema from SASE Multitenant Notifications
layout: schema
name: AnnouncementNotification
properties_list:
- description: Unique identifier for this notification delivery.
  name: notificationId
  type: string
- description: Notification type identifier.
  name: type
  type: string
- description: Announcement title.
  name: title
  type: string
- description: Full announcement body with details about the platform change, maintenance window, or service update.
  name: body
  type: string
- description: Category of the announcement.
  name: category
  type: string
- description: List of SASE services affected by the announcement, such as Prisma Access, GlobalProtect, ADEM, SWG, or ZTNA.
  name: affectedServices
  type: array
- description: Date and time when the announced change takes effect.
  name: effectiveDate
  type: string
- description: Timestamp when the announcement was published.
  name: timestamp
  type: string
- description: Tenant Service Group identifier if the announcement is tenant-specific. Omitted for global announcements.
  name: tsg_id
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-notifications-announcement-notification-schema.json
slug: sase-notifications-announcement-notification
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AnnouncementNotification
---
