---
description: Base schema for all webhook event payloads
layout: schema
name: WebhookEventBase
properties_list:
- description: The type of event that triggered this webhook
  name: eventType
  type: string
- description: Unique identifier for this event instance
  name: eventId
  type: string
- description: The Learning Manager account ID
  name: accountId
  type: string
- description: ISO 8601 timestamp when the event occurred
  name: timestamp
  type: string
- description: The system component that generated the event
  name: source
  type: string
provider_name: Adobe Captivate
provider_slug: adobe-captivate
schema_file: json-schema/learning-manager-webhooks-webhook-event-base-schema.json
slug: learning-manager-webhooks-webhook-event-base
tags:
- Authoring
- Education
- eLearning
- LMS
- SCORM
- Training
- xAPI
title: WebhookEventBase
---
