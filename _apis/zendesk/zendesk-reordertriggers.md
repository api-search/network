---
aid: zendesk:zendesk-reordertriggers
name: Zendesk Put  Api V2 Triggers Reorder
tags:
- Triggers
humanURL: 
properties: []
description: >-
  Alters the firing order of ticket triggers in the account. See [Reordering and sorting triggers](https://support.zendesk.com/hc/en-us/articles/115015696088) in the Zendesk Help Center. The firing order is set in a `trigger_ids` array in the request body.  You must include every ticket trigger id in your account to reorder the ticket triggers. If not, the endpoint will return 404 Forbidden.  Reordering ticket triggers via the API is not permitted if you have more than one ticket trigger catego...

---
