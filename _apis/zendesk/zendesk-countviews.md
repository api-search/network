---
aid: zendesk:zendesk-countviews
name: Zendesk Get  Api V2 Views Count
tags:
- Views
humanURL: 
properties: []
description: >-
  Returns an approximate count of shared and personal views available to the current user. If the count exceeds 100,000, the count will return a cached result.  This cached result will update every 24 hours.  The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.  **Note**: When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null. This indicates that the count is being updated in the background, and `count[value]` is limited to 10...

---
