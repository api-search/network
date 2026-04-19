---
description: CurrentConditions schema from AccuWeather API
layout: schema
name: CurrentConditions
properties_list:
- description: ''
  name: extended
  type: object
- description: ''
  name: isDayTime
  type: boolean
- description: ''
  name: iconCode
  type: integer
- description: ''
  name: now
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
  name: temperature
  type: string
- description: ''
  name: temperatureValue
  type: number
- description: ''
  name: realFeelValue
  type: number
- description: ''
  name: realFeelShadeValue
  type: number
- description: ''
  name: realFeelPhrase
  type: string
- description: ''
  name: realFeelShadePhrase
  type: string
- description: ''
  name: apparentTempImperial
  type: number
- description: ''
  name: windSpeedImperial
  type: number
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-current-conditions-schema.json
slug: accuweather-current-conditions
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: CurrentConditions
---
