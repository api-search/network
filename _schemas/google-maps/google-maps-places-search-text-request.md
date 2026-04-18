---
description: Request body for text search
layout: schema
name: SearchTextRequest
properties_list:
- description: The text query for the search
  name: textQuery
  type: string
- description: Restrict results to a specific place type
  name: includedType
  type: string
- description: The language code for results
  name: languageCode
  type: string
- description: The region code for biasing results
  name: regionCode
  type: string
- description: How results should be ranked
  name: rankPreference
  type: string
- description: Maximum number of results to return (1-20)
  name: maxResultCount
  type: integer
- description: Filter results by price level
  name: priceLevels
  type: array
- description: Return only places that are currently open
  name: openNow
  type: boolean
- description: Filter results to those with at least this rating
  name: minRating
  type: number
- description: If true, only return results that match the includedType exactly
  name: strictTypeFiltering
  type: boolean
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-search-text-request-schema.json
slug: google-maps-places-search-text-request
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: SearchTextRequest
---
