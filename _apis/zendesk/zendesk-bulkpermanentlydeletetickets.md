---
aid: zendesk:zendesk-bulkpermanentlydeletetickets
name: Zendesk Delete  Api V2 Deleted_tickets Destroy_many
tags:
- Tickets
humanURL: 
properties: []
description: >-
  Permanently deletes up to 100 soft-deleted tickets. See [Soft delete](https://support.zendesk.com/hc/en-us/articles/4408834005530#topic_zrm_wbj_1db) in the Zendesk GDPR docs. To soft delete tickets, use the [Bulk Delete Tickets](#bulk-delete-tickets) endpoint.  This endpoint accepts a comma-separated list of up to 100 ticket ids. It enqueues a ticket deletion job and returns a payload with the jobs status.  If one ticket fails to be deleted, the endpoint still attempts to delete the others. I...

---
