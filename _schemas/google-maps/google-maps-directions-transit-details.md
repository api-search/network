---
description: Transit-specific information for transit steps
layout: schema
name: TransitDetails
properties_list:
- description: The direction in which to travel on this transit line
  name: headsign
  type: string
- description: The expected number of seconds between departures from the same stop at the current time
  name: headway
  type: integer
- description: The number of stops from departure to arrival
  name: num_stops
  type: integer
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-directions-transit-details-schema.json
slug: google-maps-directions-transit-details
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: TransitDetails
---
