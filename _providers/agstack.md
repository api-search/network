---
api_count: 3
apis:
- description: FastAPI-based weather service providing 5-day forecasts, current conditions, Temperature-Humidity Index (THI) for livestock heat stress, UAV flight condition forecasts, and spray condition assessments
  name: OpenAgri Weather Service
  slug: openagri-weather-service
- description: Django REST API for digital farm calendar management. Records farmer operations (planting, spraying, harvesting, irrigation), farm observations, parcel properties, and farm assets. Provides data in bo
  name: OpenAgri Farm Calendar
  slug: openagri-farm-calendar
- description: The AgStack Asset Registry provides global field boundary registration and identification. Submit a field polygon (WKT or GeoJSON) and receive a permanent 256-bit (16-character alphanumeric) geo ID. S
  name: AgStack Asset Registry
  slug: asset-registry
capabilities:
- description: ''
  name: Precision Agriculture
  slug: precision-agriculture
common:
- title: ''
  type: Portal
  url: https://agstack.org/
- title: ''
  type: Documentation
  url: https://agstack.org/projects/
- title: ''
  type: GitHubOrganization
  url: https://github.com/agstack
- title: ''
  type: About
  url: https://agstack.org/about/
- title: Linux Foundation AI and Data
  type: About
  url: https://lfaidata.foundation/
- title: ''
  type: JSON-LD
  url: json-ld/agstack-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/agstack-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/agstack-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/agstack-openagri-weather-service-api.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/agstack-asset-registry-api.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/precision-agriculture.yaml
created: '2026-03-16'
description: AgStack Foundation is a Linux Foundation project providing open-source digital infrastructure for the agriculture sector. Key projects include the Asset Registry (global field boundary registration with unique geo IDs), the OpenAgri Weather Service (agricultural weather forecasts, THI, spray conditions, UAV flight forecasts), and the OpenAgri Farm Calendar (farm operation recording with JSON-LD/OCSM linked data support). AgStack tools support EUDR compliance, precision agriculture, and interoperability across the agtech ecosystem through the OpenAgri Common Semantic Model.
features:
- description: Global registry for agricultural field boundaries — submit WKT or GeoJSON geometry, receive a permanent unique 16-character geo ID
  name: Field Boundary Registry
- description: 5-day weather forecasts, current conditions, and agricultural indicators including THI, spray conditions, and UAV flight suitability
  name: Agricultural Weather Intelligence
- description: Record and manage farm operations (planting, irrigation, spraying, harvesting) with linked data (JSON-LD/OCSM) output
  name: Digital Farm Calendar
- description: All APIs support JSON-LD output conforming to the OpenAgri Common Semantic Model (OCSM) for semantic interoperability
  name: Linked Data Support
- description: Tools for EU Deforestation Regulation compliance — field boundary registration and supply chain traceability via INATrace
  name: EUDR Compliance Support
- description: Evapotranspiration (ETo) calculations and soil moisture analysis for data-driven irrigation decisions
  name: Irrigation Management
- description: All tools are Apache-2.0 licensed, Docker-ready, and deployable on any cloud or on-premises infrastructure
  name: Open Source Infrastructure
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Weather data source for current conditions and forecasts used by the OpenAgri Weather Service
  name: OpenWeatherMap
- description: EU Horizon Europe project (Grant No. 101134083) that funds and drives the OpenAgri microservices ecosystem
  name: OpenAgri
- description: OpenAgri Common Semantic Model — linked data vocabulary for agricultural interoperability used across all OpenAgri APIs
  name: OCSM
- description: Open-source blockchain-based track and trace system for agricultural supply chains
  name: INATrace
- description: TechnoServe Labs mobile and web application for EUDR compliance field data collection integrated with the asset registry
  name: TerraTrac
jsonld:
- class_count: 30
  name: Agstack Context
  property_count: 6
  slug: agstack-context
layout: provider
modified: '2026-04-19'
name: AgStack Foundation
rules:
- name: AgStack Foundation API Rules
  rule_count: 16
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 10
  slug: agstack-spectral-rules
skills: []
slug: agstack
solutions: []
tags:
- Agriculture
- Linux Foundation
- Open Source
- Geospatial
- Precision Agriculture
- Linked Data
url: https://raw.githubusercontent.com/api-evangelist/agstack/refs/heads/main/apis.yml
use_cases:
- description: Farmers and agri-cooperatives register field boundaries in the global asset registry to enable data-driven farm management
  name: Farmer Field Registration
- description: Check spray conditions and UAV flight forecasts before applying pesticides or fertilizers to minimize drift and maximize efficacy
  name: Crop Protection Planning
- description: Monitor Temperature-Humidity Index to detect and prevent heat stress events in dairy and beef cattle herds
  name: Livestock Heat Stress Monitoring
- description: Register plot geolocations and trace agricultural commodities through the supply chain to demonstrate zero-deforestation compliance
  name: EUDR Supply Chain Compliance
- description: Use evapotranspiration data and soil moisture analysis to schedule irrigation and optimize water usage
  name: Precision Irrigation
- description: Share agricultural data between platforms using JSON-LD/OCSM linked data format for semantic interoperability
  name: Interoperable Agtech Integration
---
