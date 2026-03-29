---
aid: airbus-oneatlas:airbus-oneatlas-post-api-v1-activities-activityid-cancel
name: Cancel activity
tags:
- Monitor
humanURL: 
properties: []
description: >-
  Cancel an activity.  If the activity is already terminated (status `ARCHIVED`, `CANCELED`, `FAILED` or `SUCCESSED`), the response is an HTTP `400` error code.  This endpoints **should not be forged** but retrieved from the `_links` map in list activities response or any endpoint that create or modify an activity.

---
