---
description: IoT telemetry data from a remote gas storage tank
layout: schema
name: TankTelemetry
properties_list:
- description: Tank identifier
  name: tank_id
  type: string
- description: Customer account
  name: customer_id
  type: string
- description: Gas product stored
  name: product
  type: string
- description: Current fill level as percentage
  name: level_percent
  type: number
- description: Tank pressure in bar
  name: pressure_bar
  type: number
- description: Tank temperature in Celsius
  name: temperature_c
  type: number
- description: Reading timestamp
  name: timestamp
  type: string
- description: Level % at which reorder is triggered
  name: reorder_threshold
  type: number
provider_name: Air Products and Chemicals
provider_slug: air-products-and-chemicals
schema_file: json-schema/airproducts-tank-telemetry-schema.json
slug: airproducts-tank-telemetry
tags:
- Industrial Gases
- Chemicals
- Energy
- Manufacturing
- Hydrogen
- Enterprise
title: TankTelemetry
---
