---
description: The attributes for a new event to be created
layout: schema
name: EventCreateAttributes
properties_list:
- description: The event title displayed in the Events Explorer (max 100 characters)
  name: title
  type: string
- description: The event body text with additional details about the event (max 4000 characters)
  name: message
  type: string
- description: Unix timestamp in seconds for when the event occurred; defaults to current time if not specified
  name: timestamp
  type: integer
- description: The event priority level for filtering and sorting in the Events Explorer
  name: priority
  type: string
- description: The hostname to associate with this event for infrastructure correlation
  name: host
  type: string
- description: List of tags to apply to the event in key:value format for filtering
  name: tags
  type: array
- description: The alert type category for visual display in the Events Explorer
  name: alert_type
  type: string
- description: An arbitrary string used to group related events into a rollup (max 100 characters)
  name: aggregation_key
  type: string
- description: The source technology or integration that generated this event (e.g., aws, chef, nagios)
  name: source_type_name
  type: string
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-events-event-create-attributes-schema.json
slug: datadog-events-event-create-attributes
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: EventCreateAttributes
---
