---
aid: zendesk:zendesk-createorganizationmerge
name: Zendesk Post  Api V2 Organizations Organization_id Merge
tags:
- Organizations
humanURL: 
properties: []
description: >-
  Merges two organizations by moving all users, tickets, and domain names from the organization specified by `{organization_id}` to the organization specified by `winner_id`. After the merge:  - The "losing" organization will be deleted. - Other organization fields and their values will not be carried over to the "winning" organization. - The merge operation creates an `Organization Merge` record which contains a status indicating the progress of the merge.  **Note**: This operation is irrevers...

---
