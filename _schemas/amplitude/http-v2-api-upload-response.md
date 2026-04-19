---
description: UploadResponse schema from Amplitude HTTP V2 API
layout: schema
name: UploadResponse
properties_list:
- description: The HTTP status code of the response.
  name: code
  type: integer
- description: The number of events successfully ingested.
  name: events_ingested
  type: integer
- description: The size of the request payload in bytes.
  name: payload_size_bytes
  type: integer
- description: The time the server received the upload in milliseconds since epoch.
  name: server_upload_time
  type: integer
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/http-v2-api-upload-response-schema.json
slug: http-v2-api-upload-response
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: UploadResponse
---
