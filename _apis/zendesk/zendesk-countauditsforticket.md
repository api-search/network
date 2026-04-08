---
aid: zendesk:zendesk-countauditsforticket
name: Zendesk Get  Api V2 Tickets Ticket_id Audits Count
tags:
- Ticket Audits
humanURL: 
properties: []
description: >-
  Returns an approximate count of audits for a specified ticket. If the count exceeds 100,000, the count will return a cached result.  This cached result will update every 24 hours.  The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.  **Note**: If the total number of audits for a ticket exceeds 100,000, this endpoint returns a count of 100,000 with a `count[refreshed_at]` value of null. This value is cached for 24 hours, during which any requests r...

---
