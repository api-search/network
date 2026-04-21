---
consumed_apis:
- accuweather
description: Unified workflow combining AccuWeather's location, conditions, forecasts, air quality, and storm tracking APIs into a single capability for weather-aware applications. Used by developers, IoT platforms, travel apps, and emergency management systems.
layout: capability
name: AccuWeather Weather Intelligence
operations:
- description: Search for weather locations by text query
  method: GET
  name: search-locations
  path: /v1/locations
- description: Get current weather conditions
  method: GET
  name: get-current-weather
  path: /v1/weather/current/{locationKey}
- description: Get hourly weather forecast
  method: GET
  name: get-hourly-forecast
  path: /v1/weather/forecast/hourly/{locationKey}
- description: Get daily weather forecast
  method: GET
  name: get-daily-forecast
  path: /v1/weather/forecast/daily/{locationKey}
- description: Get MinuteCast precipitation forecast
  method: GET
  name: get-minutecast
  path: /v1/weather/minutecast/{locationKey}
- description: Get current air quality
  method: GET
  name: get-air-quality
  path: /v1/air-quality/{locationKey}
- description: Get all active global storms
  method: GET
  name: get-active-storms
  path: /v1/storms/active/{locationKey}
personas: []
provider_name: AccuWeather
provider_slug: accuweather
search_terms:
- minute-by-minute precipitation forecast
- iot system using weather data for device automation
- search for weather locations by text query
- accuweather
- get minutecast
- get detailed tracking data for a specific tropical storm
- Emergency Management
- unified weather data workflow for location search, conditions, forecasts, air quality, and storm tracking
- IoT Platform
- get current weather conditions for a location key
- get current air quality index and pollutant data
- active tropical storm tracking
- get hourly air quality forecast
- get active storms
- search locations
- emergency response team tracking storms and severe weather
- get hourly air quality
- current and historical weather observation data
- hourly weather forecast
- air quality data
- short and long-range weather prediction
- get current weather
- get current air quality
- Mobile App
- Developer
- current weather conditions for a location
- get daily forecast
- search for weather locations
- aqi and pollutant measurement data
- geographic location search and resolution
- location services
- get daily weather forecast
- weather
- storms
- forecasts
- get hourly weather forecast for the next 12-120 hours
- air quality
- get hourly weather forecast
- software developer building weather-aware applications
- get 1, 5, 7, 10, or 15 day weather forecast
- get hourly forecast
- storm tracking
- get minutecast precipitation forecast
- get accuweather minutecast minute-by-minute precipitation forecast
- get all active global storms
- search for weather locations by partial name or query text
- consumer weather app presenting conditions and forecasts
- get storm details
- active and historical tropical cyclone monitoring
- meteorology
- daily weather forecast
- get current weather conditions
- get air quality
- get all currently active tropical storms globally
slug: weather-intelligence
tags:
- AccuWeather
- Weather
- Forecasts
- Air Quality
- Storm Tracking
- Location Services
tools:
- description: Search for weather locations by partial name or query text
  hints:
    openWorld: true
    readOnly: true
  name: search-locations
- description: Get current weather conditions for a location key
  hints:
    openWorld: true
    readOnly: true
  name: get-current-weather
- description: Get hourly weather forecast for the next 12-120 hours
  hints:
    openWorld: true
    readOnly: true
  name: get-hourly-forecast
- description: Get 1, 5, 7, 10, or 15 day weather forecast
  hints:
    openWorld: true
    readOnly: true
  name: get-daily-forecast
- description: Get AccuWeather MinuteCast minute-by-minute precipitation forecast
  hints:
    openWorld: true
    readOnly: true
  name: get-minutecast
- description: Get current air quality index and pollutant data
  hints:
    openWorld: true
    readOnly: true
  name: get-air-quality
- description: Get hourly air quality forecast
  hints:
    openWorld: true
    readOnly: true
  name: get-hourly-air-quality
- description: Get all currently active tropical storms globally
  hints:
    openWorld: true
    readOnly: true
  name: get-active-storms
- description: Get detailed tracking data for a specific tropical storm
  hints:
    openWorld: true
    readOnly: true
  name: get-storm-details
---
