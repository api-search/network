---
description: The response from the Directions API
layout: schema
name: DirectionsResponse
properties_list:
- description: Status code of the directions request
  name: status
  type: string
- description: Array of routes from the origin to the destination. Each route contains legs, overview polylines, warnings, and waypoint order.
  name: routes
  type: array
- description: Contains geocoding information for the origin, destination, and each waypoint.
  name: geocoded_waypoints
  type: array
- description: Human-readable error message when status is not OK
  name: error_message
  type: string
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-directions-directions-response-schema.json
slug: google-maps-directions-directions-response
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: DirectionsResponse
---
