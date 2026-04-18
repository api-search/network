---
description: An Experience Data Model (XDM) event object.
layout: schema
name: XDMEvent
properties_list:
- description: A map of identity namespaces to arrays of identity objects for cross-device identity stitching.
  name: identityMap
  type: object
- description: The type of event (e.g., web.webpagedetails.pageViews, commerce.productViews, commerce.purchases).
  name: eventType
  type: string
- description: Web-specific event data.
  name: web
  type: object
- description: Commerce-specific event data.
  name: commerce
  type: object
- description: The ISO 8601 timestamp of the event.
  name: timestamp
  type: string
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/data-collection-xdm-event-schema.json
slug: data-collection-xdm-event
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: XDMEvent
---
