---
class_count: 33
classes:
- Polygon
- SatelliteImage
- NdviRecord
- WeatherData
- SoilData
- UvIndexData
- id
- name
- geo_json
- coordinates
- resolution
- coverage
- cloud_coverage
- ndvi
- evi
- evi2
- nri
- dswi
- lswi
- temp
- feels_like
- temp_min
- temp_max
- pressure
- humidity
- wind_speed
- wind_deg
- clouds
- description
- t0
- t10
- moisture
- uvi
context_file: json-ld/agromonitoring-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agromonitoring/refs/heads/main/json-ld/agromonitoring-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agromonitoring from Agromonitoring.
layout: jsonld
name: Agromonitoring Context
namespaces:
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: agro
  uri: https://api.agromonitoring.com/vocab/
- prefix: geo
  uri: http://www.opengis.net/ont/geosparql#
properties:
- container: ''
  name: created_at
  type: dateTime
- container: ''
  name: updated_at
  type: dateTime
- container: ''
  name: valid_time_start
  type: dateTime
- container: ''
  name: valid_time_end
  type: dateTime
- container: ''
  name: image_time
  type: dateTime
- container: ''
  name: dt
  type: dateTime
property_count: 6
provider_name: Agromonitoring
provider_slug: agromonitoring
slug: agromonitoring-context
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
- JSON-LD
- Linked Data
- Semantic Web
---
