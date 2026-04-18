---
description: The response from the Geocoding API
layout: schema
name: GeocodingResponse
properties_list:
- description: Status code indicating the outcome of the request.
  name: status
  type: string
- description: Array of geocoded address results
  name: results
  type: array
- description: Human-readable description of the error, present when status is not OK.
  name: error_message
  type: string
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-geocoding-geocoding-response-schema.json
slug: google-maps-geocoding-geocoding-response
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: GeocodingResponse
---
