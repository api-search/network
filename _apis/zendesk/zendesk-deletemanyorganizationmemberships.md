---
aid: zendesk:zendesk-deletemanyorganizationmemberships
name: Zendesk Delete  Api V2 Organization_memberships Destroy_many
tags:
- Organization Memberships
humanURL: 
properties: []
description: >-
  Immediately removes a user from an organization and schedules a job to unassign all working tickets currently assigned to the user and organization combination. The `organization_id` of the unassigned tickets is set to null.  #### Response  This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job...

---
