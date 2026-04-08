---
aid: statsig:statsig-logserverevent
name: Log server events
tags:
- Events
humanURL: 
properties: []
description: >-
  Logs one or more events from the server SDK to Statsig for analytics and experiment analysis. Server SDKs batch exposure events from local gate checks and custom events, then flush them periodically to this endpoint. The STATSIG-CLIENT-TIME header is required for timestamp normalization.

---
