---
description: A scheduled flight between two airports
layout: schema
name: Schedule
properties_list:
- description: Alaska Airlines flight number
  name: flightNumber
  type: string
- description: Operating carrier code
  name: carrier
  type: string
- description: Scheduled departure time (HH:MM local)
  name: departureTime
  type: string
- description: Scheduled arrival time (HH:MM local)
  name: arrivalTime
  type: string
- description: Flight duration in minutes
  name: duration
  type: integer
- description: Aircraft type/model
  name: aircraft
  type: string
- description: Days of week this flight operates
  name: operatingDays
  type: array
- description: Number of intermediate stops
  name: stops
  type: integer
- description: Available cabin class
  name: cabin
  type: string
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-flight-schedules-schedule-schema.json
slug: alaska-air-flight-schedules-schedule
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: Schedule
---
