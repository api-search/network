---
aid: zendesk:zendesk-counttickets
name: Zendesk Get  Api V2 Tickets Count
tags:
- Tickets
humanURL: 
properties: []
description: >-
  Returns an approximate count of tickets in the account. If the count exceeds 100,000, it is updated every 24 hours.  `ccd` lists tickets that the specified user is cc'd on.  The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.  **Note**: When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null. This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complet...

---
