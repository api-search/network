---
description: Response indicating an event was accepted for processing
layout: schema
name: EventCreateResponse
properties_list:
- description: The status of the event creation request
  name: status
  type: string
- description: The unique numeric identifier assigned to the created event
  name: event_id
  type: integer
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-events-event-create-response-schema.json
slug: datadog-events-event-create-response
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: EventCreateResponse
---
