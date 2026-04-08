---
aid: zendesk:zendesk-incrementalsampleexport
name: Zendesk Get  Api V2 Incremental Incremental_resource Sample
tags:
- Incremental Export
humanURL: 
properties: []
description: >-
  Use this endpoint to test the incremental export format. It's more strict in terms of rate limiting, at 10 requests per 20 minutes instead of 10 requests per minute. It also returns only up to 50 results per request. Otherwise, it's identical to the above APIs.  Use the `incremental_resource` parameter to specify the resource. Possible values are "tickets", "ticket_events", "users", or "organizations".

---
