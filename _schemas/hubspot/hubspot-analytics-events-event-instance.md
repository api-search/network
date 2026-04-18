---
description: Represents a single event instance that occurred in the system
layout: schema
name: EventInstance
properties_list:
- description: Unique identifier for the event instance
  name: id
  type: string
- description: The type of event that occurred
  name: eventType
  type: string
- description: The ID of the CRM object associated with this event
  name: objectId
  type: string
- description: The type of CRM object (e.g., contact, company, deal)
  name: objectType
  type: string
- description: ISO 8601 timestamp when the event occurred
  name: occurredAt
  type: string
- description: Additional properties associated with the event
  name: properties
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-analytics-events-event-instance-schema.json
slug: hubspot-analytics-events-event-instance
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: EventInstance
---
