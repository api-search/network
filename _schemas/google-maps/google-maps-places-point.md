---
description: A point in time on a weekly schedule
layout: schema
name: Point
properties_list:
- description: Day of the week (0=Sunday, 6=Saturday)
  name: day
  type: integer
- description: Hour in 24-hour format (0-23)
  name: hour
  type: integer
- description: Minute (0-59)
  name: minute
  type: integer
- description: A specific date for current opening hours
  name: date
  type: object
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-point-schema.json
slug: google-maps-places-point
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: Point
---
