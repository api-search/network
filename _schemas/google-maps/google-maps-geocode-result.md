---
description: A geocoding result from the Google Maps Geocoding API. Represents the conversion between a human-readable address and geographic coordinates. Contains the formatted address, individual address components, geometry with precise location and viewport, place ID, plus code, and address type classifications. Based on the Google Maps Platform Geocoding API documentation.
layout: schema
name: Google Maps Geocode Result
properties_list:
- description: An array of address components that together compose the full address. Each component includes long and short names along with type classifications that describe the role of that component (e.g., stre
  name: address_components
  type: array
- description: The human-readable address of this location, composed from the individual address components. This is typically the full postal address.
  name: formatted_address
  type: string
- description: The geographic geometry of this geocoding result, including the precise location coordinates, location type classification, recommended viewport, and optional bounds
  name: geometry
  type: object
- description: A unique identifier for this place that can be used with other Google APIs (Places API, Place Details, etc.). Place IDs are stable across sessions and can be stored for later retrieval.
  name: place_id
  type: string
- description: The Open Location Code (plus code) for this location. Plus codes provide a simple way to encode locations that can be used where traditional addresses are unavailable.
  name: plus_code
  type: object
- description: An array of type tags describing this address result. These types indicate the nature of the geocoded entity (e.g., street_address, route, locality, political, country, postal_code).
  name: types
  type: array
- description: Indicates that the geocoder did not return an exact match for the original request, though it was able to match part of the requested address. You may wish to examine the original request for misspell
  name: partial_match
  type: boolean
- description: An array of locality names (city/town names) contained within a postal code result. Only present when the result is a postal code that contains multiple localities.
  name: postcode_localities
  type: array
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-geocode-result-schema.json
slug: google-maps-geocode-result
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: Google Maps Geocode Result
---
