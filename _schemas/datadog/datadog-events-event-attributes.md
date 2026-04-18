---
description: The attributes of an event returned from the Events Explorer
layout: schema
name: EventAttributes
properties_list:
- description: The event title as displayed in the Events Explorer
  name: title
  type: string
- description: The event body text containing details about the event
  name: message
  type: string
- description: ISO 8601 timestamp when the event was recorded
  name: timestamp
  type: string
- description: The event priority level
  name: priority
  type: string
- description: The hostname associated with this event
  name: host
  type: string
- description: List of tags associated with the event in key:value format
  name: tags
  type: array
- description: The alert type category for visual display
  name: alert_type
  type: string
- description: The arbitrary string used to group related events into a rollup
  name: aggregation_key
  type: string
- description: The source technology or integration that generated this event
  name: source_type_name
  type: string
- description: The event status (active or expired)
  name: status
  type: string
- description: Custom key-value attributes associated with the event
  name: attributes
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-events-event-attributes-schema.json
slug: datadog-events-event-attributes
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: EventAttributes
---
