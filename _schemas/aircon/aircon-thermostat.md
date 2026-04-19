---
description: Represents the state and configuration of a smart thermostat or HVAC control unit.
layout: schema
name: Thermostat
properties_list:
- description: Unique identifier for the thermostat device.
  name: id
  type: string
- description: Human-readable name of the thermostat.
  name: name
  type: string
- description: Current measured temperature in degrees.
  name: current_temperature
  type: number
- description: Target temperature setpoint.
  name: target_temperature
  type: number
- description: Unit of temperature measurement.
  name: temperature_unit
  type: string
- description: Current HVAC operating mode.
  name: hvac_mode
  type: string
- description: Current HVAC operation status.
  name: hvac_status
  type: string
- description: Fan operation mode.
  name: fan_mode
  type: string
- description: Current relative humidity percentage.
  name: humidity
  type: number
- description: Target relative humidity percentage.
  name: target_humidity
  type: number
- description: Whether the thermostat is currently online.
  name: is_online
  type: boolean
- description: Physical location or room of the thermostat.
  name: location
  type: string
- description: Thermostat model identifier.
  name: model
  type: string
- description: Current firmware version of the device.
  name: firmware_version
  type: string
- description: Timestamp of the last status update.
  name: last_updated
  type: string
provider_name: Aircon
provider_slug: aircon
schema_file: json-schema/aircon-thermostat-schema.json
slug: aircon-thermostat
tags:
- Air Conditioning
- HVAC
- Climate Control
- IoT
- Smart Home
- Thermostat
- Building Automation
- Energy Management
title: Thermostat
---
