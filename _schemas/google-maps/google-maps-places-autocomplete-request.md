---
description: Request body for place autocomplete predictions
layout: schema
name: AutocompleteRequest
properties_list:
- description: The text input specifying which place to search for
  name: input
  type: string
- description: Restrict results to primary types
  name: includedPrimaryTypes
  type: array
- description: Restrict results to these region codes
  name: includedRegionCodes
  type: array
- description: The language code for predictions
  name: languageCode
  type: string
- description: Region code for biasing
  name: regionCode
  type: string
- description: Zero-based Unicode character offset of input indicating the cursor position. Use to return more relevant predictions.
  name: inputOffset
  type: integer
- description: Whether to include query predictions in results
  name: includeQueryPredictions
  type: boolean
- description: A random string that groups this request with subsequent Place Details requests for billing.
  name: sessionToken
  type: string
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-autocomplete-request-schema.json
slug: google-maps-places-autocomplete-request
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: AutocompleteRequest
---
