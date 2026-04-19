---
description: Detailed keys for the location from AccuWeather to aid in weather data retrieval.
layout: schema
name: LocationSettingsInfo
properties_list:
- description: Unique Id created for favorite and recent locations
  name: id
  type: string
- description: AccuWeather Surefind location key for this location.
  name: locationKey
  type: string
- description: Simple name for a location, such as the name of a city
  name: name
  type: string
- description: Full name for a location, such as the name of an Admin or address
  name: longName
  type: string
- description: Name used to display to the user as the placeholder This differece from the LongName since will be sometimes display location name from the AW API (Non-english/direct location key serach)
  name: displayName
  type: string
- description: AccuWeather station code for this location.
  name: stationCode
  type: string
- description: AccuWeather list of supported data sets for this location.
  name: supportedDataSets
  type: array
- description: True if a location supports MinuteCast data.
  name: supportsMinuteCast
  type: boolean
- description: Latitude for a location
  name: latitude
  type: number
- description: Longitude for a location
  name: longitude
  type: number
- description: True if a location supports probabilities on weather events.
  name: supportsEventConfidence
  type: boolean
provider_name: AccuWeather
provider_slug: accuweather
schema_file: json-schema/accuweather-location-settings-info-schema.json
slug: accuweather-location-settings-info
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
title: LocationSettingsInfo
---
