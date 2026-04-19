---
api_count: 4
apis:
- description: The Alaska Airlines Flight Status API provides real-time flight status, departure and arrival information, gate assignments, and delay details for Alaska Airlines (AS) and Horizon Air (QX) flights.
  name: Alaska Airlines Flight Status API
  slug: flight-status-api
- description: The Alaska Airlines Flight Schedules API provides access to flight schedule data including route information, operating days, departure and arrival times, and equipment information across the Alaska A
  name: Alaska Airlines Flight Schedules API
  slug: flight-schedules-api
- description: Alaska Air Cargo APIs enable partners to book shipments, track cargo, get rate estimates, and access schedules across 115+ cargo destinations worldwide. Alaska Airlines operates the only U.S. passenge
  name: Alaska Air Cargo API
  slug: cargo-api
- description: The Alaska Mileage Plan partner API enables airline partners, hotel chains, car rental companies, and other loyalty partners to report and redeem miles for members. Alaska's Mileage Plan is consistent
  name: Alaska Airlines Mileage Plan API
  slug: mileage-plan-api
capabilities:
- description: 'Workflow capability combining Alaska Airlines Flight Status and Cargo APIs for travel operations management. Enables travel agents, corporate travel managers, and freight forwarders to track flights, '
  name: Alaska Airlines Travel Operations
  slug: travel-operations
common:
- title: ''
  type: Website
  url: https://www.alaskaair.com
- title: ''
  type: Portal
  url: https://developers.alaskaair.com/
- title: ''
  type: Blog
  url: https://www.alaskaair.com/content/about-us/news-and-events
- title: ''
  type: Support
  url: https://www.alaskaair.com/content/about-us/investor-relations
- title: API Support Email
  type: Support
  url: api.support@alaskaair.com
- title: Alaska Air Cargo Portal
  type: Documentation
  url: https://www.alaskacargo.com/
- title: ''
  type: SpectralRules
  url: rules/alaska-air-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/alaska-air-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/alaska-air-context.jsonld
- title: Flight Status API Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/flight-status-api.yaml
- title: Cargo API Shared Capability
  type: NaftikoCapability
  url: capabilities/shared/cargo-api.yaml
- title: Travel Operations Workflow
  type: NaftikoCapability
  url: capabilities/travel-operations.yaml
created: '2024-01-01'
description: Alaska Air Group is the parent company of Alaska Airlines and Horizon Air, providing passenger and cargo air transportation throughout the United States, Mexico, Canada, Costa Rica, and Belize. Alaska Airlines offers a developer portal at developers.alaskaair.com for accessing flight status, schedules, and other APIs, and operates Alaska Air Cargo serving 115+ destinations worldwide with dedicated cargo aircraft.
features:
- description: Track live flight status, departure and arrival times, gate assignments, and delay information for Alaska Airlines and Horizon Air flights.
  name: Real-Time Flight Status
- description: Access flight schedule data including routes, operating days, departure/arrival times, and equipment across the Alaska network.
  name: Flight Schedules
- description: Book shipments and track cargo across 115+ destinations worldwide via Alaska Air Cargo's network, including dedicated widebody aircraft.
  name: Cargo Booking and Tracking
- description: Get real-time rate estimates for cargo shipments based on origin, destination, weight, dimensions, and special handling requirements.
  name: Cargo Rate Estimates
- description: Enable partner mile accrual and redemption for Alaska's Mileage Plan loyalty program across airline, hotel, car rental, and retail partners.
  name: Mileage Plan Partner Integration
- description: Alaska Air Cargo operates the only U.S. passenger airline with dedicated cargo aircraft (Airbus A330s and Boeing 787s) for increased capacity on key routes.
  name: Dedicated Cargo Aircraft
- description: Support for dangerous goods transport, live animal shipments via Pet Connect, and international cargo across Asia, Pacific, Canada, and Mexico.
  name: Specialized Cargo Services
- description: Developer portal powered by Microsoft Azure API Management with subscription-based key management, interactive API console, and automatic API documentation generation.
  name: API Management via Azure
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Developer portal and API gateway powered by Azure API Management with subscription key management and interactive testing console.
  name: Microsoft Azure API Management
- description: Alaska Air Cargo partnerships including connections with Hawaiian Airlines cargo network for Pacific and inter-island routes.
  name: Hawaiian Airlines
- description: Member of the oneworld airline alliance enabling Mileage Plan accrual and redemption across 13 member airlines.
  name: One World Alliance
- description: Third-party travel API provider enabling search, booking, and ticket issuance for Alaska Airlines flights.
  name: Duffel
- description: Customer service platform integration for Alaska Air Cargo live chat and support operations.
  name: Five9
jsonld:
- class_count: 22
  name: Alaska Air Context
  property_count: 84
  slug: alaska-air-context
layout: provider
modified: '2026-04-19'
name: Alaska Airlines
rules:
- name: Alaska Airlines API Rules
  rule_count: 32
  severity_counts:
    error: 16
    hint: 0
    info: 2
    warn: 14
  slug: alaska-air-spectral-rules
skills: []
slug: alaska-air
solutions: []
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
url: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/apis.yml
use_cases:
- description: Integrate Alaska Airlines flight schedules and status into online travel agencies and booking platforms for real-time availability and status updates.
  name: Travel Agent and OTA Integration
- description: Enable freight forwarders and cargo brokers to book shipments, get rate quotes, and track Alaska Air Cargo shipments programmatically.
  name: Cargo Partner Booking
- description: Integrate Mileage Plan mile accrual into partner platforms (hotels, car rentals, credit cards) to automatically report earned miles.
  name: Loyalty Partner Mile Reporting
- description: Power airport operations systems and display boards with real-time Alaska Airlines flight status and gate assignment data.
  name: Airport Operations Display
- description: Integrate Alaska Airlines flight data into corporate travel management systems for booking, tracking, and expense reporting.
  name: Corporate Travel Management
- description: Embed Alaska Airlines flight status and schedule data into third-party mobile applications for travelers.
  name: Mobile App Integration
---
