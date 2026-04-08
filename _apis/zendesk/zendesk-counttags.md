---
aid: zendesk:zendesk-counttags
name: Zendesk Get  Api V2 Tags Count
tags:
- API
humanURL: 
properties: []
description: >-
  Returns an approximate count of tags. If the count exceeds 100,000, it is updated every 24 hours.  The `refreshed_at` property of the `count` object is a timestamp that indicates when the count was last updated.  **Note**: When the count exceeds 100,000, the `refreshed_at` property in the `count` object may occasionally be null. This indicates that the count is being updated in the background and the `value` property in the `count` object is limited to 100,000 until the update is complete.  #...

---
