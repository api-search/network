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
- environment
- place autocomplete predictions
- route computation between locations
- geolocation
- geocode
- routing
- location-based place search
- location
- get directions between two or more locations with support for driving, walking, bicycling, and transit
- address to coordinate conversion and reverse geocoding
- google maps
- geocode an address or reverse geocode coordinates
- get directions between two or more locations
- text-based place search
- geocode an address to coordinates or reverse geocode coordinates to an address
- search for places using a natural language text query like 'pizza in new york'
- get a photo for a place by place id and photo reference
- search places nearby
- places
- search places text
- solar
- search for places near a location
- directions
- maps
- get directions
- get place predictions for input text
- place details retrieval
- get detailed information about a place
- get place autocomplete predictions as the user types
- get place photo
- get place details
- geocoding
- autocomplete places
- navigation
- search for places near a specific location with type filters
- search for places using a text query
- get detailed information about a place including address, rating, hours, and reviews
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
