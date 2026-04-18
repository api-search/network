---
description: A place prediction
layout: schema
name: PlacePrediction
properties_list:
- description: The resource name of the suggested place in the format places/{placeId}
  name: place
  type: string
- description: The place ID of the suggested place
  name: placeId
  type: string
- description: List of types that apply to this place
  name: types
  type: array
- description: The distance in meters from the origin
  name: distanceMeters
  type: integer
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-place-prediction-schema.json
slug: google-maps-places-place-prediction
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: PlacePrediction
---
