---
api_count: 6
apis:
- description: The Nest Device Access API (Google Smart Device Management API) provides programmatic control over Nest thermostats, cameras, and doorbells. Supports reading thermostat state, setting target temperatu
  name: Google Nest Device Access API
  slug: nest-device-access
- description: The Ecobee API provides access to ecobee smart thermostats for reading and writing thermostat data, managing schedules, reading sensor data, and implementing custom home automation. Supports OAuth2 au
  name: Ecobee API
  slug: ecobee
- description: The Resideo API (formerly Honeywell Home API) provides access to Honeywell and Resideo smart thermostats and home security systems. Supports reading and controlling thermostat setpoints, modes, schedu
  name: Resideo (Honeywell Home) API
  slug: resideo-honeywell
- description: The Sensibo API provides control over Sensibo Sky and Air devices that add smart functionality to existing mini-split and window AC units. Supports reading AC state, setting temperature and mode, sche
  name: Sensibo API
  slug: sensibo
- description: OpenWeatherMap provides weather data APIs used in HVAC automation to adapt cooling/heating based on outdoor conditions. Offers current weather, forecasts, historical data, and air quality data relevan
  name: OpenWeatherMap API
  slug: openweathermap
- description: 'The Home Assistant REST API provides access to all home automation entities including climate/HVAC entities. Supports reading thermostat state, setting temperature, changing HVAC mode, and triggering '
  name: Home Assistant REST API
  slug: home-assistant
common:
- title: Aircon Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/aircon/refs/heads/main/vocabulary/aircon-vocabulary.yaml
created: '2024-01-15'
description: A curated index of APIs, data sources, and developer resources related to air conditioning, HVAC (Heating, Ventilation, and Air Conditioning), and climate control systems. This topic collection covers smart thermostat APIs, building automation protocols, IoT climate APIs, and environmental data APIs used in residential, commercial, and industrial HVAC applications.
features:
- description: APIs for reading and setting thermostat temperature, mode, and schedule.
  name: Thermostat Control
- description: Switch between heating, cooling, auto, and fan-only modes programmatically.
  name: HVAC Mode Management
- description: Create and manage time-based HVAC schedules and programs.
  name: Schedule Automation
- description: Read temperature, humidity, and occupancy sensor data from smart thermostats.
  name: Sensor Data Access
- description: Track HVAC runtime, energy consumption, and efficiency metrics.
  name: Energy Monitoring
- description: Combine outdoor weather data with HVAC control for predictive conditioning.
  name: Weather Integration
- description: Integrate HVAC control with broader smart home platforms (Google Home, Apple HomeKit, SmartThings).
  name: Smart Home Integration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Integration with Google Home and Google Assistant for voice control.
  name: Google Home
- description: Integration with Apple HomeKit for iOS smart home control.
  name: Apple HomeKit
- description: Voice control via Amazon Alexa smart home skills.
  name: Amazon Alexa
- description: Open-source home automation platform with broad HVAC device support.
  name: Home Assistant
- description: Automation via IFTTT applets for condition-based HVAC control.
  name: IFTTT
- description: Samsung SmartThings integration for HVAC devices.
  name: SmartThings
jsonld:
- class_count: 6
  name: Aircon Context
  property_count: 22
  slug: aircon-context
layout: provider
modified: '2026-04-19'
name: Aircon
skills: []
slug: aircon
solutions: []
tags:
- Air Conditioning
- HVAC
- Climate Control
- IoT
- Smart Home
- Thermostat
- Building Automation
- Energy Management
url: https://raw.githubusercontent.com/api-evangelist/aircon/refs/heads/main/apis.yml
use_cases:
- description: Automate AC/heating based on occupancy, time, and weather conditions.
  name: Smart Home Automation
- description: Reduce energy costs by dynamically adjusting HVAC based on occupancy and utility pricing.
  name: Energy Optimization
- description: Commercial HVAC monitoring and control across multiple zones and buildings.
  name: Building Management
- description: Track and maintain optimal temperature and humidity levels.
  name: Comfort Monitoring
- description: Control air conditioning remotely via mobile apps and API integrations.
  name: Remote Control
- description: Pre-cool or pre-heat based on weather forecasts and schedules.
  name: Predictive Conditioning
---
