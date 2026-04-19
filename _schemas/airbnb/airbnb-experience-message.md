---
description: ''
layout: schema
name: ExperienceMessage
properties_list:
- description: The unique identifier of the message.
  name: id
  type: string
- description: The identifier of the associated booking.
  name: booking_id
  type: string
- description: Whether the message was sent by the host or guest.
  name: sender_type
  type: string
- description: The text content of the message.
  name: message
  type: string
- description: The timestamp when the message was sent.
  name: created_at
  type: string
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-experience-message-schema.json
slug: airbnb-experience-message
tags: []
title: ExperienceMessage
---
