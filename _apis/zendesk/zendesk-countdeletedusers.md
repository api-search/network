---
aid: zendesk:zendesk-countdeletedusers
name: Zendesk Get  Api V2 Deleted_users Count
tags:
- Users
humanURL: 
properties: []
description: >-
  Returns an approximate count of deleted users, including permanently deleted users. If the count exceeds 100,000, it is updated every 24 hours.  The response includes a `refreshed_at` property in a `count` object that contains a timestamp indicating when the count was last updated.  **Note**: When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null. This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update...

---
