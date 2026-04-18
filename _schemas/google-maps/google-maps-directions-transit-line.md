---
description: Information about a transit line
layout: schema
name: TransitLine
properties_list:
- description: The full name of this transit line
  name: name
  type: string
- description: The short name of this transit line
  name: short_name
  type: string
- description: The color commonly used in signage for this line
  name: color
  type: string
- description: The color of the text commonly used for this line
  name: text_color
  type: string
- description: ''
  name: vehicle
  type: object
- description: ''
  name: agencies
  type: array
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-directions-transit-line-schema.json
slug: google-maps-directions-transit-line
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: TransitLine
---
