---
description: UV radiation index for a location.
layout: schema
name: UvIndexData
properties_list:
- description: Latitude of the location.
  name: lat
  type: number
- description: Longitude of the location.
  name: lon
  type: number
- description: Measurement date in ISO 8601 format.
  name: date_iso
  type: string
- description: Measurement date as Unix timestamp.
  name: date
  type: integer
- description: UV index value (scale 0-11+).
  name: value
  type: number
provider_name: Agromonitoring
provider_slug: agromonitoring
schema_file: json-schema/agromonitoring-uvindexdata-schema.json
slug: agromonitoring-uvindexdata
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
title: UvIndexData
---
