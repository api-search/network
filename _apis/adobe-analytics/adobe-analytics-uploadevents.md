---
aid: adobe-analytics:adobe-analytics-uploadevents
name: Upload a batch events file
tags:
- Events
humanURL: 
properties: []
description: >-
  Uploads a gzip-compressed CSV file containing batched Analytics event data. Each row in the CSV represents one Analytics hit. The file must include required columns (timestamp, marketingCloudVisitorID or customerID, and reportSuiteID) and may include any additional Analytics variables. The visitor group ID header (x-adobe-vgid) is required and must match the visitor group used for all files in a sequence to ensure correct visitor stitching.

---
