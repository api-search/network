---
class_count: 11
classes:
- AQIStation
- StationData
- name
- url
- CityInfo
- TimeInfo
- PollutantData
- ForecastData
- ForecastDay
- Attribution
- StationSearchResult
context_file: json-ld/aqicn-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/air-quality-programmatic-apis/refs/heads/main/json-ld/aqicn-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Aqicn from Air Quality Programmatic APIs.
layout: jsonld
name: Aqicn Context
namespaces:
- prefix: aqicn
  uri: https://aqicn.org/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: status
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: aqi
  type: integer
- container: ''
  name: idx
  type: integer
- container: ''
  name: city
  type: string
- container: ''
  name: time
  type: string
- container: ''
  name: iaqi
  type: string
- container: ''
  name: forecast
  type: string
- container: set
  name: attributions
  type: string
- container: set
  name: geo
  type: string
- container: ''
  name: s
  type: string
- container: ''
  name: tz
  type: string
- container: ''
  name: v
  type: integer
- container: ''
  name: pm25
  type: string
- container: ''
  name: pm10
  type: string
- container: ''
  name: no2
  type: string
- container: ''
  name: o3
  type: string
- container: ''
  name: so2
  type: string
- container: ''
  name: co
  type: string
- container: ''
  name: daily
  type: string
- container: ''
  name: avg
  type: integer
- container: ''
  name: day
  type: string
- container: ''
  name: max
  type: integer
- container: ''
  name: min
  type: integer
property_count: 24
provider_name: Air Quality Programmatic APIs
provider_slug: air-quality-programmatic-apis
slug: aqicn-context
tags:
- Air Quality
- Environment
- EPA
- Open Data
- Public Health
- IoT
- Government Data
- Real-Time Data
- JSON-LD
- Linked Data
- Semantic Web
---
