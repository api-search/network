---
aid: prometheus:prometheus-deletetsdbseries
name: Prometheus Delete series
tags:
- Admin
humanURL: 
properties: []
description: >-
  Deletes data for a selection of series in a time range by creating tombstones. The series data is not immediately removed but marked for deletion during the next compaction cycle. Requires --web.enable-admin-api flag.

---
