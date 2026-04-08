---
aid: symphony:symphony-readevents
name: Symphony Read Real Time Events from an event stream (aka datafeed)
tags:
- Events
humanURL: 
properties: []
description: >-
  _Available on Agent 22.5.1 and above.This endpoint provides messages and events from all conversations that the user is in or events from the whole pod depending on the "type" field value. When "type":"fanout" is provided in the body, then only events from streams  the accountbelongs to are returned. Otherwise, if "type": "datahose" is provided in the body, then events returned are not limited to the streams user belongs to. In this case, at least one event type must be provided in the "filte...

---
