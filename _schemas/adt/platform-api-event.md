---
description: A security event or alarm history entry.
layout: schema
name: Event
properties_list:
- description: Unique identifier of the event.
  name: id
  type: string
- description: Type of security event.
  name: type
  type: string
- description: Human-readable description of the event.
  name: description
  type: string
- description: ID of the device that triggered the event.
  name: deviceId
  type: string
- description: Timestamp when the event occurred.
  name: timestamp
  type: string
- description: ID of the user associated with the event.
  name: userId
  type: string
provider_name: ADT
provider_slug: adt
schema_file: json-schema/platform-api-event-schema.json
slug: platform-api-event
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: Event
---
