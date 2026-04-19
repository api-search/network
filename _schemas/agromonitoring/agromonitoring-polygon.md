---
description: A registered field polygon for crop monitoring.
layout: schema
name: Polygon
properties_list:
- description: Unique identifier for the polygon.
  name: id
  type: string
- description: Display name for the polygon/field.
  name: name
  type: string
- description: Field area in hectares.
  name: area
  type: number
- description: Timestamp when the polygon was created.
  name: created_at
  type: string
- description: ''
  name: geo_json
  type: object
provider_name: Agromonitoring
provider_slug: agromonitoring
schema_file: json-schema/agromonitoring-polygon-schema.json
slug: agromonitoring-polygon
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
title: Polygon
---
