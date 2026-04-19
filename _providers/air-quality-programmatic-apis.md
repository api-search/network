---
api_count: 2
apis:
- description: Real-time and forecast air quality data from 11,000+ monitoring stations globally. Returns AQI measurements for PM2.5, PM10, NO2, CO, SO2, and ozone pollutants by city, station, geographic coordinates
  name: AQICN Real-Time Air Quality API
  slug: air-quality-programmatic-apis
- description: JSON API returning real-time AQI station data by city name, station name, geographic coordinates, or IP geolocation. Includes pollutant breakdowns (PM2.5, PM10, NO2, CO, SO2, O3), weather data, and mu
  name: AQICN JSON Air Quality API
  slug: aqicn-json-api
capabilities:
- description: Unified workflow for querying real-time air quality data, monitoring station health, and spatial air quality analysis. Used by environmental monitoring applications and public health systems.
  name: Air Quality Monitoring Workflow
  slug: air-quality-monitoring
common:
- title: ''
  type: FAQ
  url: https://aqicn.org/faq/
- title: ''
  type: Authentication
  url: https://aqicn.org/data-platform/token/
- title: ''
  type: Portal
  url: https://aqicn.org/map/
- title: ''
  type: Portal
  url: https://aqicn.org/data-platform/
- title: ''
  type: TermsOfService
  url: https://aqicn.org/api/tos/
- title: ''
  type: SpectralRules
  url: rules/aqicn-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/air-quality-monitoring.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/aqicn-vocabulary.yaml
created: '2024-11-07'
description: Air Quality Programmatic APIs provide real-time and forecast air quality data from 11,000+ monitoring stations in 1,000+ cities worldwide. APIs deliver Air Quality Index (AQI) measurements for PM2.5, PM10, NO2, CO, SO2, and ozone pollutants. Provided by AQICN (World Air Quality Index project) in partnership with the US EPA and global environmental agencies. Data is available via JSON API and map tile API for visualization.
features:
- description: Live air quality index readings from 11,000+ monitoring stations updated continuously.
  name: Real-Time AQI Data
- description: Data from 1,000+ cities worldwide including US EPA, China MEP, Europe EEA, and other monitoring networks.
  name: Global Coverage
- description: Pollutant-specific AQI for PM2.5, PM10, nitrogen dioxide, carbon monoxide, sulfur dioxide, and ozone.
  name: Multi-Pollutant Data
- description: 3-8 day air quality forecasts for major monitoring stations.
  name: Air Quality Forecasts
- description: Find nearest stations by latitude/longitude, city name, or IP-based geolocation.
  name: Geolocation Queries
- description: Raster map tiles for overlaying real-time AQI data on web maps (Leaflet, Google Maps, etc.).
  name: Map Tile API
- description: Search and discover monitoring stations by name or location within a geographic boundary.
  name: Station Search
- description: Current weather conditions co-located with air quality measurements.
  name: Weather Data
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Integrate AQI map tiles with Leaflet.js for interactive air quality maps.
  name: Leaflet Maps
- description: Overlay AQI data on Google Maps using the tile API.
  name: Google Maps
- description: Data aggregated from US EPA AirNow monitoring network.
  name: US EPA AirNow
- description: Complementary open air quality data platform with API access.
  name: OpenAQ
jsonld:
- class_count: 11
  name: Aqicn Context
  property_count: 24
  slug: aqicn-context
layout: provider
modified: '2026-04-19'
name: Air Quality Programmatic APIs
rules:
- name: Air Quality Programmatic APIs API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: aqicn-spectral-rules
skills: []
slug: air-quality-programmatic-apis
solutions: []
tags:
- Air Quality
- Environment
- EPA
- Open Data
- Public Health
- IoT
- Government Data
- Real-Time Data
url: https://raw.githubusercontent.com/api-search/air-quality-programmatic-apis/refs/heads/main/apis.yml
use_cases:
- description: Build apps that show users real-time air quality for their location with health recommendations.
  name: Air Quality Mobile Apps
- description: Create web dashboards visualizing air quality trends across cities and regions.
  name: Environmental Monitoring Dashboards
- description: Access historical and real-time air quality data for epidemiological and public health research.
  name: Public Health Research
- description: Integrate air quality data into smart city platforms and IoT systems for environmental management.
  name: Smart City Integration
- description: Provide air quality-based recommendations for outdoor activities in fitness and weather apps.
  name: Outdoor Activity Planning
---
