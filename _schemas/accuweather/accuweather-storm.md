---
description: Storm schema from AccuWeather API
layout: schema
name: Storm
properties_list:
- description: ''
  name: accuId
  type: integer
- description: ''
  name: eventKey
  type: string
- description: ''
  name: isActive
  type: boolean
- description: ''
  name: basin
  type: string
- description: ''
  name: basinId
  type: string
- description: ''
  name: basinSlug
  type: string
- description: ''
  name: governmentId
  type: integer
- description: ''
  name: level
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: updatedStormName
  type: string
- description: ''
  name: stormPositions
  type: array
- description: ''
  name: peakPosition
  type: object
- description: ''
  name: start
  type: string
- description: ''
  name: startEpoch
  type: integer
- description: ''
  name: end
  type: string
- description: ''
  name: localStart
  type: string
- description: ''
  name: localEnd
  type: string
- description: ''
  name: year
  type: integer
- description: ''
  name: isFuture
  type: boolean
- description: ''
  name: stormLink
  type: string
- description: ''
  name: localizedStartDate
  type: string
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-storm-schema.json
slug: accuweather-storm
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: Storm
---
