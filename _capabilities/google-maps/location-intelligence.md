---
consumed_apis:
- google-maps-directions
- google-maps-geocoding
- google-maps-places
description: Unified workflow combining Google Maps Directions, Geocoding, and Places APIs for location-aware applications. Enables developers to geocode addresses, compute routes, search for places, and retrieve place details in a single integration.
layout: capability
name: Google Maps Location Intelligence
operations:
- description: Geocode an address or reverse geocode coordinates
  method: GET
  name: geocode
  path: /v1/geocode
- description: Get directions between two or more locations
  method: GET
  name: get-directions
  path: /v1/directions
- description: Get detailed information about a place
  method: GET
  name: get-place-details
  path: /v1/places/{placeId}
- description: Search for places using a text query
  method: POST
  name: search-places-text
  path: /v1/places/search-text
- description: Search for places near a location
  method: POST
  name: search-places-nearby
  path: /v1/places/search-nearby
- description: Get place predictions for input text
  method: POST
  name: autocomplete-places
  path: /v1/places/autocomplete
personas: []
provider_name: Google Maps Platform
provider_slug: google-maps
search_terms:
- location-based place search
- navigation
- get directions
- places
- address to coordinate conversion and reverse geocoding
- geocode an address to coordinates or reverse geocode coordinates to an address
- directions
- get detailed information about a place
- google maps
- geocode an address or reverse geocode coordinates
- get directions between two or more locations with support for driving, walking, bicycling, and transit
- maps
- routing
- get detailed information about a place including address, rating, hours, and reviews
- get place details
- get a photo for a place by place id and photo reference
- get place predictions for input text
- text-based place search
- geocoding
- route computation between locations
- place autocomplete predictions
- search places text
- location
- search for places using a text query
- search for places near a specific location with type filters
- environment
- autocomplete places
- get directions between two or more locations
- geocode
- search for places near a location
- geolocation
- solar
- get place photo
- search places nearby
- search for places using a natural language text query like 'pizza in new york'
- get place autocomplete predictions as the user types
- place details retrieval
slug: location-intelligence
tags:
- Google Maps
- Location
- Geocoding
- Directions
- Places
tools:
- description: Geocode an address to coordinates or reverse geocode coordinates to an address
  hints:
    openWorld: true
    readOnly: true
  name: geocode
- description: Get directions between two or more locations with support for driving, walking, bicycling, and transit
  hints:
    openWorld: true
    readOnly: true
  name: get-directions
- description: Get detailed information about a place including address, rating, hours, and reviews
  hints:
    openWorld: true
    readOnly: true
  name: get-place-details
- description: Search for places using a natural language text query like 'pizza in New York'
  hints:
    openWorld: true
    readOnly: true
  name: search-places-text
- description: Search for places near a specific location with type filters
  hints:
    openWorld: true
    readOnly: true
  name: search-places-nearby
- description: Get place autocomplete predictions as the user types
  hints:
    openWorld: true
    readOnly: true
  name: autocomplete-places
- description: Get a photo for a place by place ID and photo reference
  hints:
    openWorld: true
    readOnly: true
  name: get-place-photo
---
