---
description: Identification schema from Amplitude Identify API
layout: schema
name: Identification
properties_list:
- description: A readable ID specified by you. Required unless device_id is present.
  name: user_id
  type: string
- description: A device-specific identifier. Required unless user_id is present.
  name: device_id
  type: string
- description: An object containing user property operations. Each key is an operation type and the value is an object of property names to values.
  name: user_properties
  type: object
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/identify-api-identification-schema.json
slug: identify-api-identification
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Identification
---
