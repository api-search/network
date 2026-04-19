---
description: Energy consumption and runtime report for an HVAC system over a time period.
layout: schema
name: EnergyReport
properties_list:
- description: ID of the thermostat this report covers.
  name: thermostat_id
  type: string
- description: Start of the reporting period.
  name: period_start
  type: string
- description: End of the reporting period.
  name: period_end
  type: string
- description: Total minutes the heating system ran.
  name: heating_runtime_minutes
  type: integer
- description: Total minutes the cooling system ran.
  name: cooling_runtime_minutes
  type: integer
- description: Total minutes the fan ran independently.
  name: fan_runtime_minutes
  type: integer
- description: Estimated energy consumption in kilowatt-hours.
  name: estimated_kwh
  type: number
- description: Average indoor temperature during the period.
  name: average_indoor_temp
  type: number
- description: Average outdoor temperature during the period.
  name: average_outdoor_temp
  type: number
provider_name: Aircon
provider_slug: aircon
schema_file: json-schema/aircon-energy-report-schema.json
slug: aircon-energy-report
tags:
- Air Conditioning
- HVAC
- Climate Control
- IoT
- Smart Home
- Thermostat
- Building Automation
- Energy Management
title: EnergyReport
---
