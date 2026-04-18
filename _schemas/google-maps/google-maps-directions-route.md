---
description: A single route containing a set of legs from the origin to the destination with any specified waypoints.
layout: schema
name: Route
properties_list:
- description: A short textual description for the route, suitable for naming and disambiguating the route from alternatives.
  name: summary
  type: string
- description: Array of route legs, one for each segment between waypoints. A route with no waypoints will contain one leg.
  name: legs
  type: array
- description: An array indicating the order of any waypoints in the calculated route. Waypoints may be reordered if the request was passed optimize:true.
  name: waypoint_order
  type: array
- description: Copyright text for display
  name: copyrights
  type: string
- description: Warnings to be displayed when showing the route
  name: warnings
  type: array
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-directions-route-schema.json
slug: google-maps-directions-route
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: Route
---
