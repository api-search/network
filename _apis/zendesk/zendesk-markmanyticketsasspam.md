---
aid: zendesk:zendesk-markmanyticketsasspam
name: Zendesk Put  Api V2 Tickets Mark_many_as_spam
tags:
- Tickets
humanURL: 
properties: []
description: >-
  Accepts a comma-separated list of up to 100 ticket ids.  This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#j...

---
