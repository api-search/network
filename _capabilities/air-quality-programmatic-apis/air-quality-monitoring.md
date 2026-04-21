---
consumed_apis:
- aqicn
description: Unified workflow for querying real-time air quality data, monitoring station health, and spatial air quality analysis. Used by environmental monitoring applications and public health systems.
layout: capability
name: Air Quality Monitoring Workflow
operations:
- description: Get current AQI for a city
  method: GET
  name: get-aqi-by-city
  path: /v1/air-quality/city/{city}
- description: Get AQI for coordinates
  method: GET
  name: get-aqi-by-coordinates
  path: /v1/air-quality/coordinates
- description: Search stations by keyword
  method: GET
  name: search-stations
  path: /v1/stations/search
personas: []
provider_name: Air Quality Programmatic APIs
provider_slug: air-quality-programmatic-apis
search_terms:
- epa
- get real-time air quality index (aqi) and pollutant data for a city
- search stations
- search monitoring stations
- get aqi for coordinates
- government data
- open data
- get aqi by coordinates
- search air quality stations
- researcher or analyst studying air quality trends and patterns
- real-time data
- iot
- get current aqi for a city
- search stations by keyword
- app developer integrating air quality data into mobile or web applications
- environment
- monitoring
- Developer
- search for air quality monitoring stations by city or station name
- air quality
- air quality by city name
- get real-time aqi for a geographic location using latitude and longitude
- Environmental Analyst
- query real-time aqi and search monitoring stations
- air quality by coordinates
- public health
- get aqi by city
slug: air-quality-monitoring
tags:
- Air Quality
- Environment
- Public Health
- Open Data
- Monitoring
tools:
- description: Get real-time air quality index (AQI) and pollutant data for a city
  hints:
    openWorld: true
    readOnly: true
  name: get-aqi-by-city
- description: Get real-time AQI for a geographic location using latitude and longitude
  hints:
    openWorld: true
    readOnly: true
  name: get-aqi-by-coordinates
- description: Search for air quality monitoring stations by city or station name
  hints:
    openWorld: true
    readOnly: true
  name: search-air-quality-stations
---
