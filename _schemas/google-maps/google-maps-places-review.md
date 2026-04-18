---
description: A review of a place submitted by a user
layout: schema
name: Review
properties_list:
- description: The resource name of the review
  name: name
  type: string
- description: A human-readable relative time description
  name: relativePublishTimeDescription
  type: string
- description: The star rating of this review (1.0-5.0)
  name: rating
  type: number
- description: Timestamp of when the review was published
  name: publishTime
  type: string
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-review-schema.json
slug: google-maps-places-review
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: Review
---
