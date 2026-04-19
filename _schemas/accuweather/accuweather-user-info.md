---
description: UserInfo schema from AccuWeather API
layout: schema
name: UserInfo
properties_list:
- description: Unique ID for the user (persistent across sessions)
  name: id
  type: string
- description: Language code set for the product for the user (en-us, en-gb, etc.)
  name: language
  type: string
- description: Country code for the user's location. Eg. US
  name: country
  type: string
- description: Region code for the user's location. Eg. PA
  name: region
  type: string
- description: City for the location
  name: city
  type: string
- description: DMA for the user's location. Eg. 566. Not available outside of the US.
  name: dma
  type: string
- description: Date of the user's first visit. I.e. Cookie creation date
  name: start
  type: string
- description: Valid string of the user's current UTC offset in hh:mm:ss format. Ex. -05:00 or 05:00
  name: offset
  type: string
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-user-info-schema.json
slug: accuweather-user-info
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: UserInfo
---
