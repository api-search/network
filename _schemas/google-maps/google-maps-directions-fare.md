---
description: The total fare for a transit route
layout: schema
name: Fare
properties_list:
- description: ISO 4217 currency code
  name: currency
  type: string
- description: The total fare amount in the specified currency
  name: value
  type: number
- description: Human-readable fare text
  name: text
  type: string
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-directions-fare-schema.json
slug: google-maps-directions-fare
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: Fare
---
