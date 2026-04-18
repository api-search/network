---
description: An encoded location reference, derived from latitude and longitude coordinates, that represents an area. Plus codes can be used as a replacement for street addresses in places where they do not exist.
layout: schema
name: PlusCode
properties_list:
- description: The global (full) plus code consisting of area code and local code (e.g., 849VCWC8+R9).
  name: global_code
  type: string
- description: The compound plus code consisting of the local code and a locality description (e.g., CWC8+R9 Mountain View, CA, USA).
  name: compound_code
  type: string
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-geocoding-plus-code-schema.json
slug: google-maps-geocoding-plus-code
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: PlusCode
---
