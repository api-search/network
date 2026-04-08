---
aid: zendesk:zendesk-mergeticketsintotargetticket
name: Zendesk Post  Api V2 Tickets Ticket_id Merge
tags:
- Tickets
humanURL: 
properties: []
description: >-
  Merges one or more tickets into the ticket with the specified id.  See [Merging tickets](https://support.zendesk.com/hc/en-us/articles/203690916) in the Support Help Center for ticket merging rules.  Any attachment to the source ticket is copied to the target ticket.  This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-manag...

---
