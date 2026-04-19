---
description: An experience event representing a time-series observation of an action or state change associated with a profile, such as a page view, product interaction, purchase, or campaign engagement.
layout: schema
name: Adobe Experience Cloud Event
properties_list:
- description: A unique identifier for this event instance.
  name: eventId
  type: string
- description: The type of experience event.
  name: eventType
  type: string
- description: The ISO 8601 timestamp when the event occurred.
  name: timestamp
  type: string
- description: Identity namespaces and values associated with this event.
  name: identityMap
  type: object
- description: Web-specific event details.
  name: web
  type: object
- description: Commerce-specific event details.
  name: commerce
  type: object
- description: The device used during the event.
  name: device
  type: object
- description: Environment details at the time of the event.
  name: environment
  type: object
- description: The source system that generated the event.
  name: source
  type: object
provider_name: Adobe Experience Cloud
provider_slug: adobe-experience-cloud
schema_file: json-schema/adobe-experience-cloud-event.json
slug: adobe-experience-cloud-event
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
title: Adobe Experience Cloud Event
---
