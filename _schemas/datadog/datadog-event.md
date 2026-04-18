---
description: A Datadog event representing a notable change or activity within monitored infrastructure or applications. Events are displayed in the Datadog Events Explorer and can be overlaid on metric graphs for correlating infrastructure changes with performance impacts. Common event sources include code deployments, configuration changes, alert state transitions, auto-scaling actions, health check state changes, and custom business events submitted via the API. Events are retained for 180 days.
layout: schema
name: Datadog Event
properties_list:
- description: The unique string identifier assigned by Datadog to this event. Used to retrieve a specific event via the API. Events submitted via the v1 API use numeric IDs, while v2 events use string identifiers.
  name: id
  type: string
- description: The resource type identifier for events (always 'event')
  name: type
  type: string
- description: ''
  name: attributes
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-event-schema.json
slug: datadog-event
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: Datadog Event
---
