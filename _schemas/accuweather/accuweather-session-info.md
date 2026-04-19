---
description: SessionInfo schema from AccuWeather API
layout: schema
name: SessionInfo
properties_list:
- description: Unique ID for the user's session (persistent to 10m after the last pageview)
  name: id
  type: string
- description: Unique ID for the partner from the URL
  name: partner
  type: string
- description: ''
  name: utm
  type: object
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-session-info-schema.json
slug: accuweather-session-info
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: SessionInfo
---
