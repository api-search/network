---
aid: zendesk:zendesk-recoversuspendedticket
name: Zendesk Put  Api V2 Suspended_tickets Id Recover
tags:
- Suspended Tickets
humanURL: 
properties: []
description: >-
  **Note**: During recovery, the API sets the requester to the authenticated agent who called the API, not the original requester. This prevents the ticket from being re-suspended after recovery. To preserve the original requester, use the [Recover Multiple Suspended Tickets](#recover-multiple-suspended-tickets) endpoint with the single ticket.  This endpoint does not queue an asynchronous job that can be tracked from [Job Statuses](/api-reference/ticketing/ticket-management/job_statuses/). Ins...

---
