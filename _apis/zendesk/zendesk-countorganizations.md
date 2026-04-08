---
aid: zendesk:zendesk-countorganizations
name: Zendesk Get  Api V2 Organizations Count
tags:
- Organizations
humanURL: 
properties: []
description: >-
  Returns an approximate count of organizations. If the count exceeds 100,000, it is updated every 24 hours.  The `refreshed_at` property of the `count` object is a timestamp that indicates when the count was last updated.  When the count exceeds 100,000, the `refreshed_at` property may occasionally be null. This indicates that the count is being updated in the background and the `value` property of the `count` object is limited to 100,000 until the update is complete.  #### Allowed For  * Agents

---
