---
description: IdentifyResponse schema from Amplitude Identify API
layout: schema
name: IdentifyResponse
properties_list:
- description: The HTTP status code of the response.
  name: code
  type: integer
- description: The time the server received the request in milliseconds since epoch.
  name: server_upload_time
  type: integer
- description: The number of identify operations successfully processed.
  name: events_ingested
  type: integer
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/identify-api-identify-response-schema.json
slug: identify-api-identify-response
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: IdentifyResponse
---
