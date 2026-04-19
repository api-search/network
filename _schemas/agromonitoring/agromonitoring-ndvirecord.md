---
description: Historical NDVI data record for a specific acquisition date.
layout: schema
name: NdviRecord
properties_list:
- description: Acquisition date as Unix timestamp.
  name: dt
  type: integer
- description: Satellite source.
  name: source
  type: string
- description: Cloud coverage percentage.
  name: cl
  type: number
- description: ''
  name: stats
  type: object
provider_name: Agromonitoring
provider_slug: agromonitoring
schema_file: json-schema/agromonitoring-ndvirecord-schema.json
slug: agromonitoring-ndvirecord
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
title: NdviRecord
---
