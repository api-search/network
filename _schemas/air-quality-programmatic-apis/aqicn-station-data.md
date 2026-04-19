---
description: Station data including AQI and pollutant readings
layout: schema
name: StationData
properties_list:
- description: Overall Air Quality Index value
  name: aqi
  type: integer
- description: Station ID in AQICN database
  name: idx
  type: integer
- description: ''
  name: city
  type: object
- description: ''
  name: time
  type: object
- description: ''
  name: iaqi
  type: object
- description: ''
  name: forecast
  type: object
- description: Data source attributions
  name: attributions
  type: array
provider_name: Air Quality Programmatic APIs
provider_slug: air-quality-programmatic-apis
schema_file: json-schema/aqicn-station-data-schema.json
slug: aqicn-station-data
tags:
- Air Quality
- Environment
- EPA
- Open Data
- Public Health
- IoT
- Government Data
- Real-Time Data
title: StationData
---
