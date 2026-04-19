---
api_count: 2
apis:
- description: The Amadeus Hotel Content API provides detailed property information including descriptions, amenities, facilities, contact details, and media assets such as images and multimedia content for hotels i
  name: Hotel Content API
  slug: hotel-content-api
- description: The Amadeus Hotel List API returns hotel property data including name, address, geographic coordinates, and time zone for each hotel bookable through Amadeus. This API is the starting point for buildi
  name: Hotel List API
  slug: hotel-list-api
capabilities:
- description: Workflow capability for discovering and retrieving hotel media content, combining the Hotel List API for property discovery with the Hotel Content API for rich media retrieval. Used by travel platform
  name: Amadeus Hotel Media Discovery
  slug: hotel-media-discovery
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
  url: rules/amadeus-media-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/hotel-media-discovery.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amadeus-media-vocabulary.yaml
created: '2024-01-01'
description: Amadeus Media provides APIs and data services for accessing travel-related media content, including hotel images, property descriptions, multimedia assets, and rich content for hospitality and travel applications. Amadeus partners with trusted content providers such as Leonardo to deliver high-quality hotel media through enterprise-grade APIs used by online travel agencies, metasearch platforms, and hospitality technology providers.
features:
- description: Access high-quality images and multimedia assets for hotel properties through the Enterprise Hotel Content API and trusted content partners like Leonardo.
  name: Hotel Property Images
- description: Retrieve detailed hotel descriptions, amenity lists, facility information, and property attributes for comprehensive hotel profiles.
  name: Rich Property Descriptions
- description: Access geographic coordinates, addresses, and time zones for over 770,000 hotels in the Amadeus global inventory.
  name: Geolocation Data
- description: Enterprise API tier provides access to detailed hotel content including media that is not available in self-service APIs due to licensing constraints.
  name: Enterprise Content Access
- description: Hotel content and descriptions available in multiple languages to support international travel applications and global markets.
  name: Multi-Language Support
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Amadeus recommends Leonardo as the trusted data provider for hotel images and property media, offering a comprehensive library of hotel photography.
  name: Leonardo (Hotel Images)
- description: Developers can supplement Amadeus hotel data with Google Places API to retrieve hotel images and business information for properties in the Amadeus inventory.
  name: Google Places API
- description: Combine with Amadeus Hotel Search to display media alongside hotel offers and pricing for a complete shopping experience.
  name: Amadeus Hotel Search API
- description: Integrate hotel content with the booking flow to present property images and descriptions before and during the reservation process.
  name: Amadeus Hotel Booking API
- description: Pair hotel media with sentiment-based ratings to create compelling hotel profile pages that combine visual content with review insights.
  name: Amadeus Hotel Ratings API
jsonld:
- class_count: 13
  name: Amadeus Hotel Content Context
  property_count: 37
  slug: amadeus-hotel-content-context
- class_count: 4
  name: Amadeus Hotel List Context
  property_count: 12
  slug: amadeus-hotel-list-context
layout: provider
modified: '2026-04-19'
name: Amadeus Media
rules:
- name: Amadeus Media API Rules
  rule_count: 31
  severity_counts:
    error: 17
    hint: 0
    info: 4
    warn: 10
  slug: amadeus-media-spectral-rules
skills: []
slug: amadeus-media
solutions: []
tags:
- Content
- Hotels
- Images
- Media
- Travel
url: https://raw.githubusercontent.com/api-evangelist/amadeus-media/refs/heads/main/apis.yml
use_cases:
- description: Power hotel search pages with rich property photos, descriptions, and amenity information sourced directly from Amadeus content services.
  name: Online Travel Agency Hotel Listings
- description: Integrate Amadeus hotel content into metasearch engines to display property images and descriptions alongside rate comparisons.
  name: Metasearch Platform Integration
- description: Enhance hotel booking flows with compelling property imagery and detailed descriptions to improve conversion rates.
  name: Hotel Booking Engine Content
- description: Display hotel photos and media in mobile travel apps to give users visual context when browsing and booking accommodation.
  name: Travel App Media Display
- description: Provide hotel content and imagery in corporate travel management systems to help business travelers make informed accommodation decisions.
  name: Corporate Travel Platform
---
