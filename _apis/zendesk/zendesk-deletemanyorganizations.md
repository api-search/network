---
aid: zendesk:zendesk-deletemanyorganizations
name: Zendesk Delete  Api V2 Organizations Destroy_many
tags:
- Organizations
humanURL: 
properties: []
description: >-
  Accepts a comma-separated list of up to 100 organization ids or external ids.  #### Response  This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-...

---
