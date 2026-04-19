---
api_count: 1
apis:
- description: 'The AccuWeather One Platform API provides comprehensive weather data including current conditions, hourly and daily forecasts, MinuteCast minute-by-minute precipitation, air quality indices, tropical '
  name: AccuWeather API
  slug: accuweather-api
capabilities:
- description: Unified workflow combining AccuWeather's location, conditions, forecasts, air quality, and storm tracking APIs into a single capability for weather-aware applications. Used by developers, IoT platform
  name: AccuWeather Weather Intelligence
  slug: weather-intelligence
common:
- title: ''
  type: Portal
  url: https://developer.accuweather.com/
- title: ''
  type: GettingStarted
  url: https://developer.accuweather.com/
- title: ''
  type: BestPractices
  url: https://developer.accuweather.com/best-practices
- title: ''
  type: StatusPage
  url: https://status.accuweather.com/
- title: ''
  type: TermsOfService
  url: https://developer.accuweather.com/legal
- title: ''
  type: FAQ
  url: https://developer.accuweather.com/faq-page
- title: ''
  type: Pricing
  url: https://developer.accuweather.com/packages
- title: ''
  type: PrivacyPolicy
  url: https://www.accuweather.com/en/privacy
- title: AccuWeather Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/rules/accuweather-spectral-rules.yml
- title: AccuWeather JSON-LD Context
  type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/json-ld/accuweather-context.jsonld
- title: AccuWeather Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/vocabulary/accuweather-vocabulary.yaml
- title: Weather Intelligence Capability
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/capabilities/weather-intelligence.yaml
created: '2023-11-22'
description: AccuWeather provides the world's most sophisticated weather intelligence to make lives simpler, safer, and better. Their mission is to save lives and protect property through accurate weather forecasting and data. The AccuWeather One Platform API delivers current conditions, forecasts (hourly, daily, minutecast), air quality, storm tracking, lifestyle indices, and imagery to tens of billions of API calls daily.
features:
- description: Access weather data for 3.5 million+ locations worldwide with hyper-local precision pinpointed to exact latitude and longitude.
  name: Global Weather Coverage
- description: Proprietary minute-by-minute precipitation forecasts with start/stop timing for rain, snow, and ice at any location.
  name: MinuteCast Precipitation Forecasts
- description: Comprehensive data including RealFeel temperature, AccuLumen Brightness Index, 50+ lifestyle indices, and detailed atmospheric data.
  name: 250+ Weather Data Parameters
- description: Real-time and forecast air quality index (AQI) with pollutant breakdowns including PM2.5, PM10, ozone, NO2, SO2, and CO.
  name: Air Quality Monitoring
- description: Active storm tracking with positions, forecast tracks, and historical data for tropical cyclones in all global ocean basins.
  name: Tropical Storm Tracking
- description: Radar and satellite imagery maps in multiple resolutions (480x480, 640x480, 1024x1024) for integration into applications.
  name: Weather Imagery
image: /assets/icons/accuweather.png
integrations:
- description: AccuWeather data powers weather experiences on Apple platforms alongside native WeatherKit data.
  name: Apple WeatherKit
- description: Weather-based automation triggers in the Samsung SmartThings IoT ecosystem.
  name: Samsung SmartThings
- description: Weather data integration with Salesforce CRM for weather-aware sales and service workflows.
  name: Salesforce
- description: Azure Maps integration providing AccuWeather data within the Microsoft cloud ecosystem.
  name: Microsoft Azure
jsonld:
- class_count: 47
  name: Accuweather Context
  property_count: 250
  slug: accuweather-context
layout: provider
modified: '2026-04-19'
name: AccuWeather
rules:
- name: AccuWeather API Rules
  rule_count: 24
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 10
  slug: accuweather-spectral-rules
skills: []
slug: accuweather
solutions: []
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/apis.yml
use_cases:
- description: Power mobile and web weather apps with accurate current conditions, forecasts, and location-aware weather data.
  name: Consumer Weather Applications
- description: Trigger IoT device actions based on real-time weather conditions, forecasts, and precipitation alerts.
  name: IoT and Smart Home Automation
- description: Integrate weather data into travel booking, outdoor activity planning, and event management platforms.
  name: Travel and Outdoor Planning
- description: Use storm tracking, severe weather alerts, and precipitation forecasts for emergency response and public safety.
  name: Emergency Management
- description: Access hyper-local weather data and forecasts for precision agriculture, crop management, and environmental monitoring.
  name: Agriculture and Environmental Monitoring
---
