---
description: An address component of a place
layout: schema
name: PlaceAddressComponent
properties_list:
- description: The full text of the address component
  name: longText
  type: string
- description: An abbreviated text for the address component
  name: shortText
  type: string
- description: The types of this address component
  name: types
  type: array
- description: The language code for this component
  name: languageCode
  type: string
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-place-address-component-schema.json
slug: google-maps-places-place-address-component
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: PlaceAddressComponent
---
