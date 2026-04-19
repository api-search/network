---
description: A notification about an event or a task.
layout: schema
name: Notification
properties_list:
- description: The notification progress.
  name: progress
  type: integer
- description: ''
  name: user
  type: object
- description: The notification unique identifier.
  name: uuid
  type: string
- description: The notification name.
  name: name
  type: string
- description: The operation title.
  name: title
  type: string
- description: The notification description.
  name: description
  type: string
- description: The time that this notification was created.
  name: created_at
  type: string
- description: The time that the task or event this notification is tracking was started at.
  name: started_at
  type: string
- description: The time that the task or event this notification is tracking was completed at.
  name: completed_at
  type: string
- description: The status of the notification.
  name: status
  type: string
- description: The notification type.
  name: type
  type: string
- description: A collection of metadata related to the notification.
  name: metadata
  type: object
- description: ''
  name: labels
  type: object
- description: ''
  name: _links
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-notification-schema.json
slug: acquia-cloud-notification
tags:
- Content
- Experience
title: Notification
---
