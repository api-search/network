---
api_count: 5
apis:
- description: Provides real-time and historical flight status information including departure and arrival times, delays, codeshares, and flight number lookups. Supports FIDS (Flight Information Display System) data
  name: AeroDataBox Flight API
  slug: aerodatabox-flight-api
- description: Search and retrieve aircraft information by tail number, registration, or ICAO24 hex code. Includes airline fleet lookups, aircraft registration history, and aircraft images. Supports searches by term
  name: AeroDataBox Aircraft API
  slug: aerodatabox-aircraft-api
- description: Retrieve airport information by IATA/ICAO code including runway data, local time, solar time, and distance calculations between airports. Search airports by geographic location, IP address geolocation
  name: AeroDataBox Airport API
  slug: aerodatabox-airport-api
- description: Access current and historical airport delay statistics, global delay summaries, daily route statistics, and flight delay data by flight number. Supports date range queries for trend analysis and perfo
  name: AeroDataBox Statistical API
  slug: aerodatabox-statistical-api
- description: Create, manage, and monitor webhook subscriptions for real-time flight status alerts. Subscribe to flight events by flight number or airport and receive push notifications to your endpoint when flight
  name: AeroDataBox Flight Alert API
  slug: aerodatabox-flight-alert-api
capabilities:
- description: 'Unified capability for real-time aviation intelligence combining flight status, aircraft data, and airport information. Enables developers and travel platforms to build comprehensive flight tracking, '
  name: AeroDataBox Flight Tracking
  slug: flight-tracking
common:
- title: ''
  type: Documentation
  url: https://doc.aerodatabox.com/
- title: ''
  type: Portal
  url: https://www.aerodatabox.com/
- title: RapidAPI
  type: Marketplace
  url: https://rapidapi.com/aerodatabox/api/aerodatabox
- title: API.Market
  type: Marketplace
  url: https://api.market/store/aedbx/aerodatabox
- title: ''
  type: Pricing
  url: https://www.aerodatabox.com/pricing
- title: ''
  type: TermsOfService
  url: https://www.aerodatabox.com/terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://www.aerodatabox.com/privacy-policy
- title: ''
  type: Contact
  url: https://www.aerodatabox.com/contact
- title: ''
  type: SpectralRules
  url: rules/aerodatabox-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/aerodatabox-vocabulary.yaml
- title: Flight Tracking
  type: NaftikoCapability
  url: capabilities/flight-tracking.yaml
- title: ''
  type: JSON-LD
  url: json-ld/aerodatabox-context.jsonld
created: '2025-02-24'
description: AeroDataBox is an affordable aviation and flight data API platform tailored for small and medium businesses, individual developers, researchers, and students. Founded in 2019, the platform provides real-time and historical flight status, aircraft information, airport data, delay statistics, and flight alert webhooks through a RESTful API available on RapidAPI and API.Market. AeroDataBox covers global aviation data across airlines, aircraft, airports, and flight operations.
features:
- description: Live flight tracking with departure and arrival times, current status, and delay information for flights worldwide.
  name: Real-Time Flight Status
- description: Flight Information Display System data showing all departures and arrivals at any airport for a given time window.
  name: FIDS Airport Departures and Arrivals
- description: Lookup aircraft by tail number, registration, or ICAO24 hex code with fleet data, registration history, and images.
  name: Aircraft Search and Profiles
- description: Find airports by geographic coordinates, IP address geolocation, or free-text search with runway data included.
  name: Airport Search by Location
- description: Current and historical delay data for airports and specific flight numbers enabling trend analysis and SLA monitoring.
  name: Flight Delay Statistics
- description: Push notification subscriptions for real-time flight status changes, supporting event-driven application architectures.
  name: Webhook Flight Alerts
- description: FAA Limiting Aircraft Data Displayed (LADD) status lookup to determine if an aircraft is opted out of public tracking.
  name: FAA LADD Status
- description: Sunrise, sunset, and solar position data for any airport and date, useful for scheduling and operations planning.
  name: Solar Time Calculations
- description: Daily route statistics for airports showing which routes operate and their frequency.
  name: Route Statistics
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Available on RapidAPI Hub with interactive API playground and usage metering for easy developer onboarding.
  name: RapidAPI
- description: Available on API.Market marketplace with official OpenAPI v3 specifications for download and code generation.
  name: API.Market
- description: Integrates with any webhook-capable endpoint for real-time flight status push notifications.
  name: Webhook Endpoints
jsonld:
- class_count: 80
  name: Aerodatabox Context
  property_count: 200
  slug: aerodatabox-context
layout: provider
modified: '2026-04-19'
name: AeroDataBox
rules:
- name: AeroDataBox API Rules
  rule_count: 22
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 8
  slug: aerodatabox-spectral-rules
skills: []
slug: aerodatabox
solutions: []
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/apis.yml
use_cases:
- description: Build consumer or enterprise flight tracking apps using real-time status data for specific flights or all flights at an airport.
  name: Flight Tracking Applications
- description: Send flight status alerts to travelers by integrating webhook subscriptions for departure and arrival updates.
  name: Travel Booking Notifications
- description: Monitor airport performance, delay patterns, and route activity for operations research and capacity planning.
  name: Airport Operations Intelligence
- description: Analyze fleet composition, route networks, and on-time performance for competitive intelligence and market research.
  name: Airline Research and Analysis
- description: Access historical delay and route statistics for data-driven journalism and research on aviation trends.
  name: Aviation Data Journalism
- description: Track aircraft registrations and history for aviation finance, insurance, and asset management applications.
  name: Aircraft Valuation and Tracking
- description: Integrate airport search, local time, and solar data into travel planning applications to enhance itinerary building.
  name: Trip Planning Tools
---
