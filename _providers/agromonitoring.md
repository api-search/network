---
api_count: 1
apis:
- description: The Agromonitoring Agro API provides satellite imagery, vegetation index time series (NDVI, EVI, DSWI, LSWI), weather data, soil conditions, and UV index for registered agricultural field polygons. En
  name: Agromonitoring
  slug: agromonitoring
capabilities:
- description: ''
  name: Crop Monitoring
  slug: crop-monitoring
common:
- title: ''
  type: Portal
  url: https://agromonitoring.com/
- title: ''
  type: Documentation
  url: https://agromonitoring.com/api/
- title: ''
  type: GettingStarted
  url: https://agromonitoring.com/api/agro/#auth
- title: ''
  type: Pricing
  url: https://agromonitoring.com/subscriptions
- title: ''
  type: FAQ
  url: https://agromonitoring.com/faq/
- title: ''
  type: TermsOfService
  url: https://agromonitoring.com/terms/
- title: ''
  type: PrivacyPolicy
  url: https://agromonitoring.com/privacy/
- title: ''
  type: JSON-LD
  url: json-ld/agromonitoring-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/agromonitoring-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/agromonitoring-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/agromonitoring-api.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/crop-monitoring.yaml
created: '2025-02-06'
description: Agromonitoring is a technology company specializing in satellite-based agricultural monitoring. Using Sentinel-2 and Landsat imagery combined with weather and soil data, Agromonitoring provides vegetation index time series (NDVI, EVI, DSWI, LSWI), current weather, multi-day forecasts, and soil conditions for registered field polygons. The platform enables precision agriculture workflows including crop health assessment, irrigation optimization, yield prediction, and climate risk monitoring.
features:
- description: Register, retrieve, and delete georeferenced agricultural field polygons using GeoJSON geometry
  name: Field Polygon Management
- description: Search Sentinel-2 and Landsat satellite archives for cloud-free imagery over registered fields
  name: Satellite Imagery Search
- description: Access NDVI, EVI, EVI2, NRI, DSWI, and LSWI historical time series to track crop health and stress
  name: Vegetation Index Time Series
- description: Real-time weather conditions including temperature, humidity, wind speed, pressure, and cloud cover
  name: Current Weather Data
- description: Multi-day weather forecasts to support irrigation scheduling and field operation planning
  name: Weather Forecasting
- description: Soil temperature at surface and 10cm depth plus volumetric soil moisture content
  name: Soil Monitoring
- description: Solar UV radiation index to assess sun exposure and radiation stress on crops
  name: UV Index Data
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Agromonitoring uses OpenWeatherMap weather infrastructure for current and forecast data
  name: OpenWeatherMap
- description: European Space Agency Sentinel-2 satellite data is a primary imagery source
  name: Sentinel-2
- description: NASA/USGS Landsat imagery is available as an additional satellite data source
  name: Landsat
jsonld:
- class_count: 33
  name: Agromonitoring Context
  property_count: 6
  slug: agromonitoring-context
layout: provider
modified: '2026-04-19'
name: Agromonitoring
rules:
- name: Agromonitoring API Rules
  rule_count: 20
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 10
  slug: agromonitoring-spectral-rules
skills: []
slug: agromonitoring
solutions: []
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
url: https://raw.githubusercontent.com/api-evangelist/agromonitoring/refs/heads/main/apis.yml
use_cases:
- description: Track vegetation index trends over the growing season to identify stress, disease, or nutrient deficiencies early
  name: Crop Health Monitoring
- description: Combine soil moisture, weather forecast, and NDVI data to optimize irrigation scheduling and reduce water usage
  name: Irrigation Management
- description: Use satellite-derived vegetation indices across the growing season to build yield prediction models
  name: Yield Prediction
- description: Register precise field polygon boundaries for targeted data retrieval and zonal analysis
  name: Field Boundary Mapping
- description: Apply variable-rate inputs using spatial variability data from satellite imagery and vegetation indices
  name: Precision Agriculture
- description: Monitor weather extremes, drought, and soil conditions to assess climate-related agricultural risks
  name: Climate Risk Assessment
---
