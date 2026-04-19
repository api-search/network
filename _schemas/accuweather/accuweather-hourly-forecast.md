---
description: HourlyForecast schema from AccuWeather API
layout: schema
name: HourlyForecast
properties_list:
- description: ''
  name: dayOfWeek
  type: string
- description: ''
  name: shortDayOfWeek
  type: string
- description: ''
  name: fullDayOfWeek
  type: string
- description: ''
  name: epoch
  type: integer
- description: ''
  name: dateTime
  type: string
- description: ''
  name: displayDate
  type: string
- description: ''
  name: longDisplayDate
  type: string
- description: ''
  name: hasAlert
  type: boolean
- description: ''
  name: icon
  type: integer
- description: ''
  name: temperature
  type: string
- description: ''
  name: precip
  type: string
- description: ''
  name: phrase
  type: string
- description: ''
  name: realFeel
  type: string
- description: ''
  name: realFeelShade
  type: string
- description: ''
  name: isDayLight
  type: boolean
- description: ''
  name: extended
  type: object
- description: ''
  name: airQuality
  type: object
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-hourly-forecast-schema.json
slug: accuweather-hourly-forecast
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: HourlyForecast
---
