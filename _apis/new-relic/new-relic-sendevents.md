---
aid: new-relic:new-relic-sendevents
name: New Relic Send custom events
tags:
- Events
humanURL: 
properties: []
description: >-
  Sends one or more custom events to the specified New Relic account. The request body must be a JSON array of event objects. Each event must include an eventType attribute. Payloads may be gzip-compressed. Events are immediately available for querying via NRQL after processing. A single request may contain up to 2000 events and must not exceed 1 MB uncompressed.

---
