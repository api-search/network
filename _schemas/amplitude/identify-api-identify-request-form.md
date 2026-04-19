---
description: IdentifyRequestForm schema from Amplitude Identify API
layout: schema
name: IdentifyRequestForm
properties_list:
- description: The API key for the Amplitude project.
  name: api_key
  type: string
- description: A JSON-encoded string or array of JSON-encoded identification objects containing user_id or device_id and user_properties.
  name: identification
  type: string
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/identify-api-identify-request-form-schema.json
slug: identify-api-identify-request-form
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: IdentifyRequestForm
---
