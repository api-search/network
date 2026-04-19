---
api_count: 5
apis:
- description: The Amadeus Hotel Booking API lets you complete hotel reservations at over 150,000 hotels and accommodations worldwide. Create bookings using hotel offer IDs returned by the Hotel Search API, manage g
  name: Hotel Booking API
  slug: hotel-booking-api
- description: The Amadeus Flight Create Orders API enables creation of flight bookings from flight offers returned by the Flight Offers Search API. Create confirmed airline reservations for one or more travelers, r
  name: Flight Create Orders API
  slug: flight-create-orders-api
- description: The Amadeus Flight Order Management API allows you to retrieve and cancel existing flight orders. Look up booking details using the order ID, retrieve full itinerary and traveler information, and canc
  name: Flight Order Management API
  slug: flight-order-management-api
- description: The Amadeus Transfer Booking API allows you to book ground transfer services including airport taxis, private cars, and shuttle services. Create transfer reservations from search results returned by t
  name: Transfer Booking API
  slug: transfer-booking-api
- description: The Amadeus Transfer Management API enables management of confirmed ground transfer bookings. Cancel existing transfer reservations and retrieve booking details using transfer order IDs obtained durin
  name: Transfer Management API
  slug: transfer-management-api
capabilities:
- description: Unified workflow capability for complete travel booking encompassing flight reservations, hotel bookings, and ground transfer arrangements. Used by online travel agencies, travel chatbots, and corpora
  name: Amadeus Travel Booking
  slug: travel-booking
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
  url: rules/amadeus-reservations-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/travel-booking.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amadeus-reservations-vocabulary.yaml
created: '2024-01-01'
description: Amadeus Reservations provides APIs for creating and managing travel bookings including flight orders, hotel reservations, and ground transfer bookings. These APIs power the full reservation lifecycle for online travel agencies, corporate travel platforms, and travel management companies, connecting to Amadeus's global distribution network of airlines, hotels, and transfer operators.
features:
- description: Book rooms at over 150,000 hotels worldwide using Amadeus GDS connectivity, with instant confirmation and property reference numbers.
  name: Hotel Booking at Scale
- description: Create confirmed airline reservations with full PNR support across hundreds of airlines in the Amadeus inventory.
  name: Flight Order Creation
- description: Create reservations for multiple travelers in a single API call, managing individual passenger details and fare assignments.
  name: Multi-Traveler Bookings
- description: Book airport taxis, private cars, and shuttle services with real-time availability and instant confirmation.
  name: Ground Transfer Bookings
- description: Retrieve and cancel existing flight and transfer reservations programmatically with full booking detail access.
  name: Order Management
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Flight Create Orders works with Flight Offers Search to convert priced flight offers into confirmed airline reservations.
  name: Amadeus Flight Offers Search
- description: Hotel Booking completes the hotel shopping flow started by Hotel Search, converting hotel offers into confirmed reservations.
  name: Amadeus Hotel Search
- description: Transfer Booking confirms ground transportation offers returned by the Transfer Search API.
  name: Amadeus Transfer Search
- description: Validate and reprice flight offers before booking to ensure accurate pricing at time of reservation creation.
  name: Amadeus Flight Offers Price
- description: Use Hotel Name Autocomplete to let users search for properties before fetching offers and creating hotel bookings.
  name: Amadeus Hotel Name Autocomplete
jsonld:
- class_count: 45
  name: Amadeus Flight Create Orders Context
  property_count: 123
  slug: amadeus-flight-create-orders-context
- class_count: 46
  name: Amadeus Flight Order Management Context
  property_count: 126
  slug: amadeus-flight-order-management-context
- class_count: 1
  name: Amadeus Hotel Booking Address Context
  property_count: 5
  slug: amadeus-hotel-booking-address-context
- class_count: 1
  name: Amadeus Hotel Booking Arrival Context
  property_count: 4
  slug: amadeus-hotel-booking-arrival-context
- class_count: 1
  name: Amadeus Hotel Booking Create Context
  property_count: 4
  slug: amadeus-hotel-booking-create-context
- class_count: 1
  name: Amadeus Hotel Booking Errors Context
  property_count: 1
  slug: amadeus-hotel-booking-errors-context
- class_count: 2
  name: Amadeus Hotel Booking Guest Context
  property_count: 6
  slug: amadeus-hotel-booking-guest-context
- class_count: 1
  name: Amadeus Hotel Booking Guests Context
  property_count: 2
  slug: amadeus-hotel-booking-guests-context
- class_count: 6
  name: Amadeus Hotel Booking Hotel Context
  property_count: 29
  slug: amadeus-hotel-booking-hotel-context
- class_count: 2
  name: Amadeus Hotel Booking Hotel_ Context
  property_count: 2
  slug: amadeus-hotel-booking-hotel_-context
- class_count: 2
  name: Amadeus Hotel Booking Payment Context
  property_count: 5
  slug: amadeus-hotel-booking-payment-context
- class_count: 1
  name: Amadeus Hotel Booking Price Context
  property_count: 5
  slug: amadeus-hotel-booking-price-context
- class_count: 1
  name: Amadeus Hotel Booking Qualified Context
  property_count: 2
  slug: amadeus-hotel-booking-qualified-context
- class_count: 1
  name: Amadeus Hotel Booking Room Context
  property_count: 3
  slug: amadeus-hotel-booking-room-context
- class_count: 1
  name: Amadeus Hotel Booking Warning Context
  property_count: 7
  slug: amadeus-hotel-booking-warning-context
- class_count: 2
  name: Amadeus Transfer Booking Address Context
  property_count: 7
  slug: amadeus-transfer-booking-address-context
- class_count: 1
  name: Amadeus Transfer Booking Agency Context
  property_count: 1
  slug: amadeus-transfer-booking-agency-context
- class_count: 1
  name: Amadeus Transfer Booking Baggage Context
  property_count: 2
  slug: amadeus-transfer-booking-baggage-context
- class_count: 1
  name: Amadeus Transfer Booking Cancellation Context
  property_count: 7
  slug: amadeus-transfer-booking-cancellation-context
- class_count: 2
  name: Amadeus Transfer Booking Contact Context
  property_count: 1
  slug: amadeus-transfer-booking-contact-context
- class_count: 1
  name: Amadeus Transfer Booking Corporation Context
  property_count: 2
  slug: amadeus-transfer-booking-corporation-context
- class_count: 1
  name: Amadeus Transfer Booking Credit Context
  property_count: 5
  slug: amadeus-transfer-booking-credit-context
- class_count: 1
  name: Amadeus Transfer Booking Discount Context
  property_count: 2
  slug: amadeus-transfer-booking-discount-context
- class_count: 1
  name: Amadeus Transfer Booking Distance Context
  property_count: 2
  slug: amadeus-transfer-booking-distance-context
- class_count: 2
  name: Amadeus Transfer Booking Equipment Context
  property_count: 7
  slug: amadeus-transfer-booking-equipment-context
- class_count: 1
  name: Amadeus Transfer Booking Error_400 Context
  property_count: 1
  slug: amadeus-transfer-booking-error_400-context
- class_count: 1
  name: Amadeus Transfer Booking Error_401 Context
  property_count: 1
  slug: amadeus-transfer-booking-error_401-context
- class_count: 1
  name: Amadeus Transfer Booking Error_500 Context
  property_count: 1
  slug: amadeus-transfer-booking-error_500-context
- class_count: 2
  name: Amadeus Transfer Booking Extra Context
  property_count: 9
  slug: amadeus-transfer-booking-extra-context
- class_count: 0
  name: Amadeus Transfer Booking Fee Context
  property_count: 0
  slug: amadeus-transfer-booking-fee-context
- class_count: 1
  name: Amadeus Transfer Booking Issue Context
  property_count: 5
  slug: amadeus-transfer-booking-issue-context
- class_count: 2
  name: Amadeus Transfer Booking Location Context
  property_count: 5
  slug: amadeus-transfer-booking-location-context
- class_count: 1
  name: Amadeus Transfer Booking Loyalty Context
  property_count: 2
  slug: amadeus-transfer-booking-loyalty-context
- class_count: 1
  name: Amadeus Transfer Booking Name Context
  property_count: 4
  slug: amadeus-transfer-booking-name-context
- class_count: 1
  name: Amadeus Transfer Booking Partner Context
  property_count: 1
  slug: amadeus-transfer-booking-partner-context
- class_count: 1
  name: Amadeus Transfer Booking Passenger Context
  property_count: 2
  slug: amadeus-transfer-booking-passenger-context
- class_count: 1
  name: Amadeus Transfer Booking Payment Context
  property_count: 4
  slug: amadeus-transfer-booking-payment-context
- class_count: 1
  name: Amadeus Transfer Booking Points Context
  property_count: 1
  slug: amadeus-transfer-booking-points-context
- class_count: 0
  name: Amadeus Transfer Booking Quotation Context
  property_count: 0
  slug: amadeus-transfer-booking-quotation-context
- class_count: 1
  name: Amadeus Transfer Booking Seat Context
  property_count: 3
  slug: amadeus-transfer-booking-seat-context
- class_count: 2
  name: Amadeus Transfer Booking Service Context
  property_count: 7
  slug: amadeus-transfer-booking-service-context
- class_count: 1
  name: Amadeus Transfer Booking Stop Context
  property_count: 3
  slug: amadeus-transfer-booking-stop-context
- class_count: 0
  name: Amadeus Transfer Booking Tax Context
  property_count: 0
  slug: amadeus-transfer-booking-tax-context
- class_count: 2
  name: Amadeus Transfer Booking Transfer Context
  property_count: 23
  slug: amadeus-transfer-booking-transfer-context
- class_count: 0
  name: Amadeus Transfer Booking Transportation Context
  property_count: 0
  slug: amadeus-transfer-booking-transportation-context
- class_count: 2
  name: Amadeus Transfer Booking Travel Context
  property_count: 7
  slug: amadeus-transfer-booking-travel-context
- class_count: 2
  name: Amadeus Transfer Booking Vehicle Context
  property_count: 5
  slug: amadeus-transfer-booking-vehicle-context
- class_count: 1
  name: Amadeus Transfer Management Error_400 Context
  property_count: 1
  slug: amadeus-transfer-management-error_400-context
- class_count: 1
  name: Amadeus Transfer Management Error_401 Context
  property_count: 1
  slug: amadeus-transfer-management-error_401-context
- class_count: 1
  name: Amadeus Transfer Management Error_404 Context
  property_count: 1
  slug: amadeus-transfer-management-error_404-context
- class_count: 1
  name: Amadeus Transfer Management Error_500 Context
  property_count: 1
  slug: amadeus-transfer-management-error_500-context
- class_count: 1
  name: Amadeus Transfer Management Issue Context
  property_count: 5
  slug: amadeus-transfer-management-issue-context
- class_count: 1
  name: Amadeus Transfer Management Transfer Context
  property_count: 2
  slug: amadeus-transfer-management-transfer-context
layout: provider
modified: '2026-04-19'
name: Amadeus Reservations
rules:
- name: Amadeus Reservations API Rules
  rule_count: 20
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 7
  slug: amadeus-reservations-spectral-rules
skills: []
slug: amadeus-reservations
solutions: []
tags:
- Booking
- Flights
- Hotels
- Reservations
- Travel
url: https://raw.githubusercontent.com/api-evangelist/amadeus-reservations/refs/heads/main/apis.yml
use_cases:
- description: Power end-to-end booking flows for flights, hotels, and transfers on consumer-facing OTA platforms.
  name: Online Travel Agency Booking Engine
- description: Enable corporate travel managers to book and manage business travel including flights and hotel accommodations with policy compliance.
  name: Corporate Travel Management
- description: Integrate booking capabilities into mobile travel apps providing users with seamless reservation creation from search to confirmation.
  name: Travel App Integration
- description: Build complete multi-modal itineraries combining flight bookings with hotel reservations and ground transfers through unified API access.
  name: Itinerary Builder
- description: Enable AI-powered travel assistants to create and manage bookings on behalf of travelers through conversational interfaces.
  name: Travel Chatbot
---
