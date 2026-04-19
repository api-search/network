---
description: UploadRequestBody schema from Amplitude HTTP V2 API
layout: schema
name: UploadRequestBody
properties_list:
- description: The API key for the Amplitude project to which events will be sent.
  name: api_key
  type: string
- description: An array of event objects to upload. Maximum of 10 events per batch is recommended.
  name: events
  type: array
- description: ''
  name: options
  type: object
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/http-v2-api-upload-request-body-schema.json
slug: http-v2-api-upload-request-body
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: UploadRequestBody
---
