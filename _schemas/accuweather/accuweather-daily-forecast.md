---
description: DailyForecast schema from AccuWeather API
layout: schema
name: DailyForecast
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
  name: day
  type: object
- description: ''
  name: night
  type: object
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-daily-forecast-schema.json
slug: accuweather-daily-forecast
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: DailyForecast
---
