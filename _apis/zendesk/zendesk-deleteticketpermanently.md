---
aid: zendesk:zendesk-deleteticketpermanently
name: Zendesk Delete  Api V2 Deleted_tickets Ticket_id
tags:
- Tickets
humanURL: 
properties: []
description: >-
  Permanently deletes a soft-deleted ticket. See [Soft delete](https://support.zendesk.com/hc/en-us/articles/4408834005530#topic_zrm_wbj_1db) in the Zendesk GDPR docs. To soft delete a ticket, use the [Delete Ticket](#delete-ticket) endpoint.  This endpoint enqueues a ticket deletion job and returns a payload with the jobs status.  If the job succeeds, the ticket is permanently deleted. This operation can't be undone.  This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/...

---
