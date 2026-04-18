---
description: Represents a single event in the Dynatrace environment. Events can be ingested via the API or detected automatically by Dynatrace.
layout: schema
name: Event
properties_list:
- description: The unique identifier of the event.
  name: eventId
  type: string
- description: The type of the event.
  name: eventType
  type: string
- description: The display title of the event.
  name: title
  type: string
- description: The start time of the event as a Unix timestamp in milliseconds.
  name: startTime
  type: integer
- description: The end time of the event as a Unix timestamp in milliseconds. Null for open events.
  name: endTime
  type: integer
- description: ''
  name: entityId
  type: object
- description: Additional key-value metadata attached to the event.
  name: properties
  type: object
- description: The current status of the event. OPEN indicates the event is still active; CLOSED indicates it has ended.
  name: status
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/events-api-v2-event-schema.json
slug: events-api-v2-event
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: Event
---
