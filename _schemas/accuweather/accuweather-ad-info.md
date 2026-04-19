---
description: AdInfo schema from AccuWeather API
layout: schema
name: AdInfo
properties_list:
- description: Simplified ad code for ad slots on the page. Eg. '6581/web/us/*/news_info/country_home'
  name: code
  type: string
- description: One of 'active', 'missing', or 'restricted' indicating a user's ID status Default missing.
  name: status
  type: string
- description: One of 'active', 'missing', or 'restricted' indicating a user can access 3rd party cookies or not. Default missing.
  name: cookie3p
  type: string
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-ad-info-schema.json
slug: accuweather-ad-info
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: AdInfo
---
