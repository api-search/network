---
description: Place schema from X API v2
layout: schema
name: Place
properties_list:
- description: ''
  name: contained_within
  type: array
- description: The full name of the county in which this place exists.
  name: country
  type: string
- description: A two-letter ISO 3166-1 alpha-2 country code.
  name: country_code
  type: string
- description: The full name of this place.
  name: full_name
  type: string
- description: ''
  name: geo
  type: object
- description: The identifier for this place.
  name: id
  type: string
- description: The human readable name of this place.
  name: name
  type: string
- description: ''
  name: place_type
  type: string
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-place-schema.json
slug: x-api-place
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: Place
---
