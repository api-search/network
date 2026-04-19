---
description: Weather conditions for a specific date and location.
layout: schema
name: WeatherData
properties_list:
- description: Date as Unix timestamp.
  name: dt
  type: integer
- description: ''
  name: temp
  type: object
- description: Relative humidity percentage.
  name: humidity
  type: integer
- description: Wind speed in m/s (or mph for imperial).
  name: wind_speed
  type: number
- description: Wind direction in degrees.
  name: wind_deg
  type: integer
- description: Cloud coverage percentage.
  name: clouds
  type: integer
- description: Precipitation amount in mm.
  name: rain
  type: number
- description: UV index value.
  name: uvi
  type: number
provider_name: Agromonitoring
provider_slug: agromonitoring
schema_file: json-schema/agromonitoring-weatherdata-schema.json
slug: agromonitoring-weatherdata
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
title: WeatherData
---
