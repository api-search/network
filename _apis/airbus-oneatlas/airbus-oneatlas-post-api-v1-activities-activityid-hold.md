---
aid: airbus-oneatlas:airbus-oneatlas-post-api-v1-activities-activityid-hold
name: Hold activity
tags:
- Control
- Deliver
humanURL: 
properties: []
description: >-
  Hold activity and set activity status to `ON_HOLD` only for manual activities such as control or physical delivering.  If the activity is already terminated (status `ARCHIVED`, `CANCELED`, `FAILED` or `SUCCESSED`), the response is an HTTP `400` error code.  This endpoints **should not be forged** but retrieved from the `_links` map in list activities response or any endpoint that create or modify an activity.

---
