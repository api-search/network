---
aid: zendesk:zendesk-puttagsticket
name: Zendesk Put  Api V2 Tickets Ticket_id Tags
tags:
- API
humanURL: 
properties: []
description: >-
  You can also add tags to multiple tickets with the [Update Many Tickets](/api-reference/ticketing/tickets/tickets/#update-many-tickets) endpoint.  #### Safe Update  If the same ticket is updated by multiple API requests at the same time, some tags could be lost because of ticket update collisions. Include `updated_stamp` and `safe_update` properties in the request body to make a safe update.  For `updated_stamp`, retrieve and specify the ticket's latest `updated_at` timestamp. The tag update ...

---
