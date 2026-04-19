---
description: Soil temperature and moisture data for a polygon.
layout: schema
name: SoilData
properties_list:
- description: Measurement date as Unix timestamp.
  name: dt
  type: integer
- description: Soil surface temperature in Celsius.
  name: t0
  type: number
- description: Soil temperature at 10cm depth in Celsius.
  name: t10
  type: number
- description: Volumetric soil moisture (0 to 1 scale).
  name: moisture
  type: number
provider_name: Agromonitoring
provider_slug: agromonitoring
schema_file: json-schema/agromonitoring-soildata-schema.json
slug: agromonitoring-soildata
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
title: SoilData
---
