---
aid: zendesk:zendesk-bulkdeletetickets
name: Zendesk Delete  Api V2 Tickets Destroy_many
tags:
- Tickets
humanURL: 
properties: []
description: >-
  Accepts a comma-separated list of up to 100 ticket ids.  #### Allowed For  * Admins * Agents with permission to delete tickets  Agent delete permissions are set in Support. See [Deleting tickets](https://support.zendesk.com/hc/en-us/articles/203690936) in the Support Help Center.  This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing...

---
