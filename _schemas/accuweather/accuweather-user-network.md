---
description: UserNetwork schema from AccuWeather API
layout: schema
name: UserNetwork
properties_list:
- description: Category of 'network speed' for the user. Eg. 'vhigh'
  name: throughput
  type: string
- description: Name of the network for the user. Eg. 'comcast'
  name: network
  type: string
- description: Type of network for the user. Eg. 'cable'
  name: type
  type: string
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-user-network-schema.json
slug: accuweather-user-network
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: UserNetwork
---
