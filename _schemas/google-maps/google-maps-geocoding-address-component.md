---
description: An individual address component of a geocoding result
layout: schema
name: AddressComponent
properties_list:
- description: The full text description of the address component
  name: long_name
  type: string
- description: An abbreviated textual name for the address component
  name: short_name
  type: string
- description: Array indicating the type of the address component
  name: types
  type: array
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-geocoding-address-component-schema.json
slug: google-maps-geocoding-address-component
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: AddressComponent
---
