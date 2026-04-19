---
class_count: 30
classes:
- Asset
- FieldBoundary
- GeoId
- WeatherForecast
- FarmCalendar
- FarmOperation
- AgriculturalMachine
- Parcel
- id
- type
- geo_id
- boundary
- coordinates
- wkt
- centroid
- overlap_percentage
- humidity
- wind_speed
- cloud_coverage
- thi
- title
- description
- farm
- parcel
- activity_type
- product
- quantity
- unit
- operator
- notes
context_file: json-ld/agstack-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agstack/refs/heads/main/json-ld/agstack-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agstack from AgStack Foundation.
layout: jsonld
name: Agstack Context
namespaces:
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: agstack
  uri: https://agstack.org/vocab/
- prefix: ocsm
  uri: https://openagri.eu/vocab/ocsm/
- prefix: geo
  uri: http://www.opengis.net/ont/geosparql#
- prefix: dcterms
  uri: http://purl.org/dc/terms/
properties:
- container: ''
  name: lat
  type: float
- container: ''
  name: lon
  type: float
- container: ''
  name: temperature
  type: float
- container: ''
  name: created_at
  type: dateTime
- container: ''
  name: updated_at
  type: dateTime
- container: ''
  name: date
  type: date
property_count: 6
provider_name: AgStack Foundation
provider_slug: agstack
slug: agstack-context
tags:
- Agriculture
- Linux Foundation
- Open Source
- Geospatial
- Precision Agriculture
- Linked Data
- JSON-LD
- Linked Data
- Semantic Web
---
