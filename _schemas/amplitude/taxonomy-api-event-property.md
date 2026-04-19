---
description: EventProperty schema from Amplitude Taxonomy API
layout: schema
name: EventProperty
properties_list:
- description: The name of the event property.
  name: event_property
  type: string
- description: The event type this property belongs to.
  name: event_type
  type: string
- description: A description of the event property.
  name: description
  type: string
- description: The data type of the property.
  name: type
  type: string
- description: Whether the property is required.
  name: is_required
  type: boolean
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/taxonomy-api-event-property-schema.json
slug: taxonomy-api-event-property
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: EventProperty
---
