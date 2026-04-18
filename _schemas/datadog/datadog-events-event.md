---
description: A single event from the Datadog Events Explorer
layout: schema
name: Event
properties_list:
- description: The unique string identifier of the event
  name: id
  type: string
- description: The resource type identifier (always 'event')
  name: type
  type: string
- description: ''
  name: attributes
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-events-event-schema.json
slug: datadog-events-event
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: Event
---
