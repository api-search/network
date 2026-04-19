---
description: The envelope schema for all webhook event notifications sent by the Airbnb platform to partner endpoints, including event metadata and typed payloads.
layout: schema
name: Airbnb Webhook Event
properties_list:
- description: A unique identifier for this webhook event, used for idempotency and deduplication.
  name: event_id
  type: string
- description: The type of event that triggered the webhook notification.
  name: event_type
  type: string
- description: The ISO 8601 timestamp when the event occurred.
  name: timestamp
  type: string
- description: The API version used for the webhook payload format.
  name: api_version
  type: string
- description: The event-specific payload data. Structure varies by event_type.
  name: data
  type: object
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-webhook-event-schema.json
slug: airbnb-webhook-event
tags: []
title: Airbnb Webhook Event
---
