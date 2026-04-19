---
description: A cargo tracking event
layout: schema
name: TrackingEvent
properties_list:
- description: Event timestamp
  name: timestamp
  type: string
- description: Location IATA code
  name: location
  type: string
- description: Event type
  name: event
  type: string
- description: Event description
  name: description
  type: string
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-cargo-tracking-event-schema.json
slug: alaska-air-cargo-tracking-event
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: TrackingEvent
---
