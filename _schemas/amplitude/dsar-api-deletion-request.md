---
description: DeletionRequest schema from Amplitude Data Subject Access Request API
layout: schema
name: DeletionRequest
properties_list:
- description: Array of Amplitude internal user IDs to delete data for. Maximum 100 per request.
  name: amplitude_ids
  type: array
- description: Array of user IDs to delete data for. Maximum 100 per request.
  name: user_ids
  type: array
- description: The email address of the person requesting the deletion for audit purposes.
  name: requester
  type: string
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/dsar-api-deletion-request-schema.json
slug: dsar-api-deletion-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: DeletionRequest
---
