---
description: A time value with text representation and time zone
layout: schema
name: TimeZoneTextValue
properties_list:
- description: Human-readable time string
  name: text
  type: string
- description: Time expressed in seconds since epoch
  name: value
  type: integer
- description: The time zone of this time value
  name: time_zone
  type: string
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-directions-time-zone-text-value-schema.json
slug: google-maps-directions-time-zone-text-value
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: TimeZoneTextValue
---
