---
description: Represents an audit event for activities performed by users on the Productiv platform.
layout: schema
name: AuditEvent
properties_list:
- description: The unique identifier of the event.
  name: eventId
  type: string
- description: The type of audit event.
  name: eventType
  type: string
- description: When the event occurred.
  name: timestamp
  type: string
- description: The email of the user who performed the action.
  name: userEmail
  type: string
- description: Additional details about the event.
  name: details
  type: object
provider_name: Productiv
provider_slug: productiv
schema_file: json-schema/audit-event.json
slug: audit-event
tags:
- Application Portfolio
- Provisioning
- SaaS Management
- Spend Management
- Usage Analytics
title: AuditEvent
---
