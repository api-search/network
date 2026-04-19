---
description: DsarStatusResponse schema from Amplitude Data Subject Access Request API
layout: schema
name: DsarStatusResponse
properties_list:
- description: The unique identifier for the DSAR request.
  name: request_id
  type: string
- description: The processing status of the request.
  name: status
  type: string
- description: The URL to download the requested data. Only present when status is complete.
  name: download_url
  type: string
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/dsar-api-dsar-status-response-schema.json
slug: dsar-api-dsar-status-response
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: DsarStatusResponse
---
