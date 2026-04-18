---
description: Geocoded information for a waypoint
layout: schema
name: GeocodedWaypoint
properties_list:
- description: Status of the geocoding operation
  name: geocoder_status
  type: string
- description: Place ID of the geocoded waypoint
  name: place_id
  type: string
- description: Address type(s) of the geocoded waypoint
  name: types
  type: array
- description: Whether the geocoder did not return an exact match
  name: partial_match
  type: boolean
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-directions-geocoded-waypoint-schema.json
slug: google-maps-directions-geocoded-waypoint
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: GeocodedWaypoint
---
