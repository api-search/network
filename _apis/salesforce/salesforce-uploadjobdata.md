---
aid: salesforce:salesforce-uploadjobdata
name: Salesforce Upload job data (CSV)
tags:
- Ingest Job Data
humanURL: 
properties: []
description: >-
  Uploads CSV data to an ingest job that is in the Open state. The CSV must include a header row matching the field API names for the object. Multiple upload calls can be made for the same job; data is appended. After uploading all data, close the job with PATCH /ingest/{jobId} to begin processing.

---
