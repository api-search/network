---
description: A time-based schedule program for HVAC setpoints and modes.
layout: schema
name: HvacSchedule
properties_list:
- description: Unique identifier for the schedule.
  name: id
  type: string
- description: Human-readable name of the schedule.
  name: name
  type: string
- description: ID of the thermostat this schedule applies to.
  name: thermostat_id
  type: string
- description: Heating setpoint temperature for this schedule period.
  name: heat_setpoint
  type: number
- description: Cooling setpoint temperature for this schedule period.
  name: cool_setpoint
  type: number
- description: Days of the week this schedule applies.
  name: days
  type: array
- description: Start time in HH:MM 24-hour format.
  name: start_time
  type: string
- description: End time in HH:MM 24-hour format.
  name: end_time
  type: string
- description: Whether this schedule is active.
  name: is_enabled
  type: boolean
provider_name: Aircon
provider_slug: aircon
schema_file: json-schema/aircon-hvac-schedule-schema.json
slug: aircon-hvac-schedule
tags:
- Air Conditioning
- HVAC
- Climate Control
- IoT
- Smart Home
- Thermostat
- Building Automation
- Energy Management
title: HvacSchedule
---
