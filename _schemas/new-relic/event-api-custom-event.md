---
description: A custom event to record. Must include eventType. All other attributes are user-defined key-value pairs. Attribute names must not start with nr. (reserved). Values can be strings, numbers, or booleans.
layout: schema
name: CustomEvent
properties_list:
- description: The type of event. Used as the NRDB event table name. Must match the pattern [a-zA-Z0-9:_ ]+, max 255 characters.
  name: eventType
  type: string
- description: Unix epoch timestamp in seconds. If omitted, the current time is used. Cannot be more than 48 hours in the past or 24 hours in the future.
  name: timestamp
  type: integer
provider_name: New Relic
provider_slug: new-relic
schema_file: json-schema/event-api-custom-event-schema.json
slug: event-api-custom-event
tags:
- Analysis
- Analytics
- APM
- DevOps
- Infrastructure
- Monitoring
- Observability
- Performance
- Platform
title: CustomEvent
---
