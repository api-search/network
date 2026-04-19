---
api_count: 4
apis:
- description: The Amadeus Points of Interest API provides data on tourist attractions, restaurants, museums, nightlife, shopping, and parks near a specified location. Returns POI name, category, geographic coordina
  name: Points of Interest API
  slug: points-of-interest-api
- description: The Amadeus Hotel Ratings API uses sentiment analysis of hotel reviews to provide overall hotel ratings and ratings for specific categories including location, comfort, service, staff, internet, food,
  name: Hotel Ratings API
  slug: hotel-ratings-api
- description: The Amadeus Travel Recommendations API provides personalized destination recommendations based on a traveler's origin city and travel history. Returns top recommended cities with descriptions, scoring
  name: Travel Recommendations API
  slug: travel-recommendations-api
- description: The Amadeus Location Score API scores geographic locations for different traveler personas including Shopping, Restaurant, Nightlife, Sightseeing, and Beach. Helps travelers and travel apps understand
  name: Location Score API
  slug: location-score-api
capabilities:
- description: Workflow capability for discovering destinations and media content, combining Points of Interest, Hotel Ratings, Travel Recommendations, and Location Score APIs. Used by travel app developers, destina
  name: Amadeus Destination Discovery
  slug: destination-discovery
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
  url: rules/amadeus-traveler-media-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/destination-discovery.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amadeus-traveler-media-vocabulary.yaml
created: '2024-01-01'
description: The Amadeus Traveler Media APIs provide access to travel-related media and destination content, including photos, ratings, and information for points of interest, hotels, and destinations worldwide. These APIs power travel apps, destination guides, and travel planning platforms with rich content for tourist attractions, hotel sentiment ratings, travel recommendations, and location scoring.
features:
- description: Discover tourist attractions, restaurants, museums, and nightlife venues near any geographic location with ranking scores.
  name: Points of Interest Discovery
- description: Access sentiment-based hotel ratings derived from thousands of traveler reviews covering all key aspects of the hotel experience.
  name: Hotel Sentiment Ratings
- description: Get AI-powered destination recommendations tailored to a traveler's origin and travel history patterns.
  name: Personalized Travel Recommendations
- description: Score any neighborhood for specific traveler personas including Shoppers, Foodies, Nightlife Seekers, Sightseers, and Beach Lovers.
  name: Location Scoring by Persona
- description: Combine POI data, hotel ratings, and location scores to create comprehensive destination guides and travel media content.
  name: Rich Destination Content
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Combine hotel ratings with hotel search results to display sentiment scores alongside pricing for better hotel selection.
  name: Amadeus Hotel Search
- description: Pair hotel ratings with property images and descriptions from the Hotel Content API for complete hotel profiles.
  name: Amadeus Hotel Content API
- description: Extend POI discovery with bookable tours and activities from the Amadeus Tours and Activities API.
  name: Amadeus Tours and Activities
- description: Use city search to identify destination cities before fetching POIs and travel recommendations for that location.
  name: Amadeus City Search
- description: Combine travel recommendations with flight inspiration search to suggest both destinations and available flights.
  name: Amadeus Flight Inspiration Search
jsonld:
- class_count: 2
  name: Amadeus Hotel Ratings Collection Context
  property_count: 8
  slug: amadeus-hotel-ratings-collection-context
- class_count: 1
  name: Amadeus Hotel Ratings Error Context
  property_count: 3
  slug: amadeus-hotel-ratings-error-context
- class_count: 1
  name: Amadeus Hotel Ratings Error400 Context
  property_count: 1
  slug: amadeus-hotel-ratings-error400-context
- class_count: 1
  name: Amadeus Hotel Ratings Error401 Context
  property_count: 1
  slug: amadeus-hotel-ratings-error401-context
- class_count: 1
  name: Amadeus Hotel Ratings Error500 Context
  property_count: 1
  slug: amadeus-hotel-ratings-error500-context
- class_count: 1
  name: Amadeus Hotel Ratings Hotel Context
  property_count: 6
  slug: amadeus-hotel-ratings-hotel-context
- class_count: 0
  name: Amadeus Hotel Ratings Score Context
  property_count: 0
  slug: amadeus-hotel-ratings-score-context
- class_count: 1
  name: Amadeus Hotel Ratings Warning Context
  property_count: 5
  slug: amadeus-hotel-ratings-warning-context
- class_count: 0
  name: Amadeus Location Score Category Context
  property_count: 0
  slug: amadeus-location-score-category-context
- class_count: 1
  name: Amadeus Location Score Errors Context
  property_count: 5
  slug: amadeus-location-score-errors-context
- class_count: 1
  name: Amadeus Location Score Meta Context
  property_count: 2
  slug: amadeus-location-score-meta-context
- class_count: 1
  name: Amadeus Location Score Response_Error Context
  property_count: 1
  slug: amadeus-location-score-response_error-context
- class_count: 1
  name: Amadeus Location Score Response_Location Context
  property_count: 3
  slug: amadeus-location-score-response_location-context
- class_count: 1
  name: Amadeus Location Score Warning Context
  property_count: 4
  slug: amadeus-location-score-warning-context
- class_count: 9
  name: Amadeus Points Of Interest Context
  property_count: 20
  slug: amadeus-points-of-interest-context
- class_count: 1
  name: Amadeus Travel Recommendations Errors Context
  property_count: 5
  slug: amadeus-travel-recommendations-errors-context
- class_count: 1
  name: Amadeus Travel Recommendations Meta Context
  property_count: 2
  slug: amadeus-travel-recommendations-meta-context
- class_count: 0
  name: Amadeus Travel Recommendations Recommended Context
  property_count: 0
  slug: amadeus-travel-recommendations-recommended-context
- class_count: 1
  name: Amadeus Travel Recommendations Response_Error Context
  property_count: 1
  slug: amadeus-travel-recommendations-response_error-context
- class_count: 1
  name: Amadeus Travel Recommendations Response_Recommended Context
  property_count: 3
  slug: amadeus-travel-recommendations-response_recommended-context
- class_count: 1
  name: Amadeus Travel Recommendations Warning Context
  property_count: 4
  slug: amadeus-travel-recommendations-warning-context
layout: provider
modified: '2026-04-19'
name: Amadeus Traveler Media
rules:
- name: Amadeus Traveler Media API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: amadeus-traveler-media-spectral-rules
skills: []
slug: amadeus-traveler-media
solutions: []
tags:
- Content
- Destination
- Media
- Photos
- Points of Interest
- Tourism
- Travel
url: https://raw.githubusercontent.com/api-evangelist/amadeus-traveler-media/refs/heads/main/apis.yml
use_cases:
- description: Build destination guide features in travel apps showing attractions, restaurants, and nightlife with ratings and location context.
  name: Travel App Destination Guide
- description: Display sentiment-based ratings alongside hotel pricing to help travelers choose accommodation based on experience quality.
  name: Hotel Comparison Platform
- description: Power "where should I go next" features with personalized destination recommendations based on traveler history and preferences.
  name: Personalized Travel Inspiration
- description: Help travelers understand the character of hotels or Airbnb locations using location scores for shopping, dining, and nightlife.
  name: Neighborhood Explorer
- description: Enable AI travel assistants to recommend attractions, rate hotels, and suggest destinations based on traveler interests.
  name: AI Travel Concierge
---
