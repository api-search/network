---
description: Geographic location information associated with an event.
layout: schema
name: EventLocation
properties_list:
- description: The two-letter ISO country code.
  name: country
  type: string
- description: The region or state.
  name: region
  type: string
- description: The city name.
  name: city
  type: string
- description: The latitude coordinate.
  name: latitude
  type: number
- description: The longitude coordinate.
  name: longitude
  type: number
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-events-event-location-schema.json
slug: 1password-events-event-location
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: EventLocation
---
