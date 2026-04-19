---
description: ''
layout: schema
name: Schedule
properties_list:
- description: The unique identifier of the schedule entry.
  name: id
  type: string
- description: The identifier of the associated experience.
  name: experience_id
  type: string
- description: The date of the scheduled session.
  name: date
  type: string
- description: The start time in HH:MM format.
  name: start_time
  type: string
- description: The end time in HH:MM format.
  name: end_time
  type: string
- description: The maximum number of guests for this session.
  name: max_guests
  type: integer
- description: The current number of booked guests.
  name: booked_guests
  type: integer
- description: The number of remaining available spots.
  name: available_spots
  type: integer
- description: The status of the schedule entry.
  name: status
  type: string
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-schedule-schema.json
slug: airbnb-schedule
tags: []
title: Schedule
---
