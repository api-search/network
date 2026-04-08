---
aid: zendesk:zendesk-destroymanyusers
name: Zendesk Delete  Api V2 Users Destroy_many
tags:
- Users
humanURL: 
properties: []
description: >-
  Accepts a comma-separated list of up to 100 user ids.  The request takes an `ids` or an `external_ids` query parameter.  #### Allowed for  - Admins  #### Response  This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of...

---
