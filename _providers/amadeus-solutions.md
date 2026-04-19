---
api_count: 4
apis:
- description: 'The Amadeus Flight Offers Search API enables searching and comparing flight offers from over 400 airlines. Search one-way, round-trip, or multi-city itineraries with cabin class, baggage, and pricing '
  name: Flight Offers Search API
  slug: flight-offers-search-api
- description: The Amadeus Flight Offers Price API confirms the availability and price of a flight offer before booking. Validates current pricing, seat availability, and fare conditions for offers returned by Fligh
  name: Flight Offers Price API
  slug: flight-offers-price-api
- description: The Amadeus Branded Fares Upsell API provides upgrade options for travelers, enabling upsell from basic economy to premium economy, business, or first class branded fares. Returns available upgrade op
  name: Branded Fares Upsell API
  slug: branded-fares-upsell-api
- description: The Amadeus Seat Map Display API provides cabin layout and seat availability information for a flight. Returns detailed seat maps with seat characteristics, availability status, and pricing for seat s
  name: Seat Map Display API
  slug: seat-map-display-api
capabilities:
- description: Unified workflow capability for complete flight shopping encompassing search, pricing, upsell, and seat selection. Used by OTA developers, airline retailing platforms, and travel chatbots to build end
  name: Amadeus Flight Shopping
  slug: flight-shopping
common:
- title: ''
  type: Portal
  url: https://developers.amadeus.com/
- title: ''
  type: GettingStarted
  url: https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/
- title: ''
  type: Authentication
  url: https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262
- title: ''
  type: SignUp
  url: https://developers.amadeus.com/register
- title: ''
  type: Pricing
  url: https://developers.amadeus.com/pricing
- title: ''
  type: Blog
  url: https://developers.amadeus.com/blog
- title: ''
  type: FAQ
  url: https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/faq/
- title: ''
  type: Support
  url: https://developers.amadeus.com/support
- title: ''
  type: TermsOfService
  url: https://developers.amadeus.com/legal/terms-and-conditions
- title: ''
  type: PrivacyPolicy
  url: https://developers.amadeus.com/legal/privacy-policy
- title: ''
  type: GitHubOrganization
  url: https://github.com/amadeus4dev
- title: Python SDK
  type: SDK
  url: https://github.com/amadeus4dev/amadeus-python
- title: Node.js SDK
  type: SDK
  url: https://github.com/amadeus4dev/amadeus-node
- title: Java SDK
  type: SDK
  url: https://github.com/amadeus4dev/amadeus-java
- title: ''
  type: StatusPage
  url: https://developers.amadeus.com/status
- title: ''
  type: SpectralRules
  url: rules/amadeus-solutions-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/flight-shopping.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amadeus-solutions-vocabulary.yaml
created: '2024-01-01'
description: Amadeus is a leading technology partner for the global travel industry, providing technology solutions for airlines, airports, hotels, travel sellers, and corporate travel. The Amadeus platform includes a global distribution system (GDS), passenger service systems, airport operations, hospitality management, and a suite of APIs enabling developers to search, price, book, and manage travel across air, hotel, and ground transportation.
features:
- description: Access flight schedules and availability from over 400 airlines through a single integration with the Amadeus GDS.
  name: Global Flight Inventory
- description: Connect to airline NDC offers alongside traditional GDS content for a comprehensive view of available fares and ancillaries.
  name: NDC Content Support
- description: Display branded fare options with included services, restrictions, and price differences to enable informed purchase decisions.
  name: Branded Fares and Fare Families
- description: Access seat selection, baggage, meals, and other ancillary services through integrated APIs alongside fare shopping.
  name: Ancillary Services
- description: Confirm current pricing and availability before booking with the Flight Offers Price API to prevent pricing discrepancies.
  name: Real-Time Pricing
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Convert searched and priced flight offers into confirmed bookings using the Flight Create Orders API.
  name: Amadeus Flight Create Orders
- description: Combine flight search with hotel search to build complete trip planning experiences for travelers.
  name: Amadeus Hotel Search
- description: Enhance destination content alongside flight search with attractions, experiences, and activities data.
  name: Amadeus Points of Interest
- description: Add ground transportation options to flight itineraries through the Transfer Search API.
  name: Amadeus Transfer Search
- description: Integrate travel payments processing through Amadeus Outpayce for airline and OTA payment acceptance.
  name: Outpayce (Payments)
jsonld:
- class_count: 22
  name: Amadeus Branded Fares Upsell Context
  property_count: 56
  slug: amadeus-branded-fares-upsell-context
- class_count: 37
  name: Amadeus Flight Offers Price Context
  property_count: 98
  slug: amadeus-flight-offers-price-context
- class_count: 32
  name: Amadeus Flight Offers Search Context
  property_count: 94
  slug: amadeus-flight-offers-search-context
- class_count: 48
  name: Amadeus Seat Map Display Context
  property_count: 136
  slug: amadeus-seat-map-display-context
layout: provider
modified: '2026-04-19'
name: Amadeus Solutions
rules:
- name: Amadeus Solutions API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 4
  slug: amadeus-solutions-spectral-rules
skills: []
slug: amadeus-solutions
solutions:
- description: Next-generation airline retailing platform enabling offer and order management for airlines pursuing NDC-based retailing strategies.
  name: Amadeus Nevio (Airline Retailing)
- description: Core passenger service system for full-service carriers providing reservations, inventory management, and departure control.
  name: Amadeus Altéa (Passenger Service System)
- description: Distribution platform for travel agencies providing GDS access, NDC content, and LCC integrations through a unified API.
  name: Amadeus Selling Platform Connect
- description: Corporate travel and expense management platform integrated with Microsoft Teams and major enterprise collaboration tools.
  name: Amadeus Cytric (Corporate Travel)
- description: Airport operations technology including baggage, passenger experience, ground handling, and border control solutions.
  name: Amadeus Airport IT
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
url: https://raw.githubusercontent.com/api-evangelist/amadeus-solutions/refs/heads/main/apis.yml
use_cases:
- description: Build complete flight shopping experiences searching, pricing, and booking flights across hundreds of airlines through a unified API.
  name: Flight Search and Booking Engine
- description: Power airline direct channels with offer creation, branded fares, seat maps, and ancillary upsell capabilities.
  name: Airline Retailing Platform
- description: Enable policy-compliant flight shopping for corporate travelers with fare filtering, approval workflows, and reporting.
  name: Corporate Travel Management
- description: Aggregate flight offers for price comparison across airlines with detailed fare family and service information.
  name: Travel Metasearch
- description: Enable conversational travel assistants to search and compare flights using natural language queries.
  name: AI Travel Assistant
---
