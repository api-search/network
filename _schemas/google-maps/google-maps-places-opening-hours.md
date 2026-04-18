---
description: Information about the opening hours of a place
layout: schema
name: OpeningHours
properties_list:
- description: Whether the place is currently open
  name: openNow
  type: boolean
- description: The periods that this place is open during the week. Periods covering a full day have an open event with day 0 and time 0000, and no close event.
  name: periods
  type: array
- description: Localized strings describing the opening hours for each day of the week
  name: weekdayDescriptions
  type: array
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-opening-hours-schema.json
slug: google-maps-places-opening-hours
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: OpeningHours
---
