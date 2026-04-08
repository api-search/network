---
aid: zendesk:zendesk-groupmembershipbulkcreate
name: Zendesk Post  Api V2 Group_memberships Create_many
tags:
- Group Memberships
humanURL: 
properties: []
description: >-
  Assigns up to 100 agents to given groups.  #### Allowed For  * Admins * Agents assigned to a custom role with permissions to manage group memberships (Enterprise only)  #### Response  This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion.

---
