---
aid: zendesk:zendesk-listtriggerrevisions
name: Zendesk Get  Api V2 Triggers Trigger_id Revisions
tags:
- Triggers
humanURL: 
properties: []
description: >-
  List the revisions associated with a ticket trigger. Ticket trigger revision history is only available on Enterprise plans.  #### Allowed For   * Agents  #### Sideloads  The following sideloads are supported:  | Name  | Will sideload | ----- | ------------- | users | The user that authored each revision  #### Pagination  This endpoint uses cursor-based pagination. The records are ordered in descending order by the `created_at` timestamp, then by `id` on duplicate `created_at` values.  The `cu...

---
