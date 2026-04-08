---
aid: zendesk:zendesk-countusers
name: Zendesk Get  Api V2 Users Count
tags:
- Users
humanURL: 
properties: []
description: >-
  Returns an approximate count of users. If the count exceeds 100,000, it is updated every 24 hours.  The response includes a `refreshed_at` property in a `count` object that contains a timestamp indicating when the count was last updated.  **Note**: When the count exceeds 100,000, the `refreshed_at` property may occasionally be null. This indicates that the count is being updated in the background. The `count` object's `value` property is limited to 100,000 until the update is complete.  #### ...

---
