---
description: Request body for nearby search
layout: schema
name: SearchNearbyRequest
properties_list:
- description: Place types to include in results
  name: includedTypes
  type: array
- description: Place types to exclude from results
  name: excludedTypes
  type: array
- description: Primary place types to include
  name: includedPrimaryTypes
  type: array
- description: Primary place types to exclude
  name: excludedPrimaryTypes
  type: array
- description: The language code for results
  name: languageCode
  type: string
- description: The region code for biasing results
  name: regionCode
  type: string
- description: How results should be ranked
  name: rankPreference
  type: string
- description: Maximum number of results (1-20)
  name: maxResultCount
  type: integer
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-search-nearby-request-schema.json
slug: google-maps-places-search-nearby-request
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: SearchNearbyRequest
---
