---
description: StormPosition schema from AccuWeather API
layout: schema
name: StormPosition
properties_list:
- description: ''
  name: coordinates
  type: object
- description: ''
  name: dateTime
  type: string
- description: ''
  name: localDate
  type: string
- description: ''
  name: localDayOfWeek
  type: string
- description: ''
  name: dateTimeLabelShort
  type: string
- description: ''
  name: dateTimeLabel
  type: string
- description: ''
  name: shortDateShortTimeLabel
  type: string
- description: ''
  name: direction
  type: string
- description: ''
  name: isCurrent
  type: boolean
- description: ''
  name: isHistorical
  type: boolean
- description: ''
  name: isMarked
  type: boolean
- description: ''
  name: isPeak
  type: boolean
- description: ''
  name: latitude
  type: number
- description: ''
  name: longitude
  type: number
- description: ''
  name: maximumSustainedWind
  type: string
- description: ''
  name: maximumSustainedWindValue
  type: number
- description: ''
  name: maximumWindGust
  type: string
- description: ''
  name: maximumWindGustValue
  type: number
- description: ''
  name: windDegrees
  type: number
- description: ''
  name: minimumPressure
  type: string
- description: ''
  name: position
  type: string
- description: ''
  name: speed
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: localizedStatus
  type: string
- description: ''
  name: statusName
  type: string
- description: ''
  name: statusIcon
  type: string
- description: ''
  name: statusIconString
  type: string
- description: ''
  name: landmarkReferences
  type: array
- description: ''
  name: eventKey
  type: string
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-storm-position-schema.json
slug: accuweather-storm-position
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: StormPosition
---
