---
description: Satellite imagery metadata with vegetation index statistics.
layout: schema
name: SatelliteImage
properties_list:
- description: Acquisition date as Unix timestamp.
  name: dt
  type: integer
- description: Satellite source (Sentinel-2 or Landsat-8).
  name: source
  type: string
- description: Cloud coverage percentage for this image.
  name: cl
  type: number
- description: Vegetation index statistics for the polygon.
  name: stats
  type: object
- description: URLs to image tiles (truecolor, falsecolor, ndvi).
  name: image
  type: object
provider_name: Agromonitoring
provider_slug: agromonitoring
schema_file: json-schema/agromonitoring-satelliteimage-schema.json
slug: agromonitoring-satelliteimage
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
title: SatelliteImage
---
