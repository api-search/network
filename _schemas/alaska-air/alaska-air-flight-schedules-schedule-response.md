---
description: Flight schedule query response
layout: schema
name: ScheduleResponse
properties_list:
- description: Origin airport IATA code
  name: origin
  type: string
- description: Destination airport IATA code
  name: destination
  type: string
- description: Query departure date
  name: departureDate
  type: string
- description: List of scheduled flights
  name: schedules
  type: array
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-flight-schedules-schedule-response-schema.json
slug: alaska-air-flight-schedules-schedule-response
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: ScheduleResponse
---
