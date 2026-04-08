---
aid: zendesk:zendesk-countsatisfactionratings
name: Zendesk Get  Api V2 Satisfaction_ratings Count
tags:
- Satisfaction Ratings
humanURL: 
properties: []
description: >-
  Returns an approximate count of satisfaction ratings in the account. If the count exceeds 100,000, the count will return a cached result. This cached result will update every 24 hours.  The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.  **Note**: When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null. This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the updat...

---
