---
description: IdentifyRequestBody schema from Amplitude Identify API
layout: schema
name: IdentifyRequestBody
properties_list:
- description: The API key for the Amplitude project.
  name: api_key
  type: string
- description: An array of identification objects containing user_id or device_id and user_properties.
  name: identification
  type: array
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/identify-api-identify-request-body-schema.json
slug: identify-api-identify-request-body
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: IdentifyRequestBody
---
