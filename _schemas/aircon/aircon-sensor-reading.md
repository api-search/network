---
description: A sensor measurement from a climate or environmental sensor associated with an HVAC system.
layout: schema
name: SensorReading
properties_list:
- description: Unique identifier for the sensor.
  name: sensor_id
  type: string
- description: Type of sensor measurement.
  name: sensor_type
  type: string
- description: Measured sensor value.
  name: value
  type: number
- description: Unit of the measurement.
  name: unit
  type: string
- description: Physical location of the sensor.
  name: location
  type: string
- description: Whether the sensor is actively used for thermostat control.
  name: in_use
  type: boolean
- description: Timestamp of the reading.
  name: timestamp
  type: string
provider_name: Aircon
provider_slug: aircon
schema_file: json-schema/aircon-sensor-reading-schema.json
slug: aircon-sensor-reading
tags:
- Air Conditioning
- HVAC
- Climate Control
- IoT
- Smart Home
- Thermostat
- Building Automation
- Energy Management
title: SensorReading
---
