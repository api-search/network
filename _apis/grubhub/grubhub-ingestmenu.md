---
aid: grubhub:grubhub-ingestmenu
name: Ingest a normalized menu
tags:
- Menu Ingestion
humanURL: 
properties: []
description: >-
  Uploads a complete menu to Grubhub including schedules, sections, items, and modifiers. The API uses external IDs to perform a diff between the current and uploaded versions. Matching external IDs will have their fields updated, new IDs will create objects, and missing IDs will cause the associated items to be removed. Processing completes asynchronously after the endpoint responds.

---
