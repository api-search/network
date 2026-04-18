---
description: A photo associated with a place
layout: schema
name: Photo
properties_list:
- description: The resource name of the photo in the format places/{placeId}/photos/{photoReference}
  name: name
  type: string
- description: Maximum available width in pixels
  name: widthPx
  type: integer
- description: Maximum available height in pixels
  name: heightPx
  type: integer
- description: The authors of this photo
  name: authorAttributions
  type: array
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-photo-schema.json
slug: google-maps-places-photo
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: Photo
---
