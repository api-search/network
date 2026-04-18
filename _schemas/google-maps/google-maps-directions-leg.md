---
description: A leg of a route, representing the journey between two waypoints or the origin/destination.
layout: schema
name: Leg
properties_list:
- description: Array of steps representing each instruction along the leg
  name: steps
  type: array
- description: The human-readable address of the leg's starting point
  name: start_address
  type: string
- description: The human-readable address of the leg's ending point
  name: end_address
  type: string
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-directions-leg-schema.json
slug: google-maps-directions-leg
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: Leg
---
