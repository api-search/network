---
description: Real-time telematics data from an AGCO machine.
layout: schema
name: Telemetry
properties_list:
- description: Machine identifier.
  name: machine_id
  type: string
- description: Data collection timestamp.
  name: timestamp
  type: string
- description: Engine RPM.
  name: engine_speed
  type: number
- description: Engine load percentage.
  name: engine_load
  type: number
- description: Cumulative engine hours.
  name: engine_hours
  type: number
- description: Fuel level percentage.
  name: fuel_level
  type: number
- description: Fuel consumption in liters/hour.
  name: fuel_consumption_rate
  type: number
- description: Ground speed in km/h.
  name: ground_speed
  type: number
- description: Engine coolant temperature in Celsius.
  name: coolant_temperature
  type: number
- description: Active diagnostic fault codes.
  name: fault_codes
  type: array
- description: Current machine operating mode.
  name: operating_mode
  type: string
provider_name: agco
provider_slug: agco
schema_file: json-schema/agco-telemetry-schema.json
slug: agco-telemetry
tags: []
title: Telemetry
---
