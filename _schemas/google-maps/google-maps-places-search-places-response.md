---
description: Response from text search and nearby search
layout: schema
name: SearchPlacesResponse
properties_list:
- description: List of places matching the search criteria
  name: places
  type: array
- description: A token that can be sent as pageToken in a subsequent request to retrieve the next page of results.
  name: nextPageToken
  type: string
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-search-places-response-schema.json
slug: google-maps-places-search-places-response
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: SearchPlacesResponse
---
