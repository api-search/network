---
description: PageInfo schema from AccuWeather API
layout: schema
name: PageInfo
properties_list:
- description: Page group like 'three-day' or 'hourly' designating the page category
  name: group
  type: string
- description: URL of the page
  name: url
  type: string
- description: Referrer of the page
  name: referrer
  type: string
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-page-info-schema.json
slug: accuweather-page-info
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: PageInfo
---
