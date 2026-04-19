---
description: DeviceInfo schema from AccuWeather API
layout: schema
name: DeviceInfo
properties_list:
- description: Name of the user's browser. Eg. 'Chrome'
  name: name
  type: string
- description: Name of the user's device maker. Eg. 'Apple' or 'Samsung'
  name: brand
  type: string
- description: Version of the user's browser. Eg. '16'
  name: version
  type: string
- description: One of 'mobile', 'tablet', or 'desktop'
  name: category
  type: string
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-device-info-schema.json
slug: accuweather-device-info
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: DeviceInfo
---
