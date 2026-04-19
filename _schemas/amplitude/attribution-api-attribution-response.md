---
description: AttributionResponse schema from Amplitude Attribution API
layout: schema
name: AttributionResponse
properties_list:
- description: The HTTP status code of the response.
  name: code
  type: integer
- description: The number of events successfully ingested.
  name: events_ingested
  type: integer
- description: The time the server received the upload in milliseconds since epoch.
  name: server_upload_time
  type: integer
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/attribution-api-attribution-response-schema.json
slug: attribution-api-attribution-response
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: AttributionResponse
---
