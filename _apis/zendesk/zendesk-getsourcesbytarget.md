---
aid: zendesk:zendesk-getsourcesbytarget
name: Zendesk Get  Api V2 Target_type Target_id Relationship_fields Field_id Source_type
tags:
- Lookup Relationships
humanURL: 
properties: []
description: >-
  Returns a list of source objects whose values are populated with the id of a related target object.  For example, if you have a lookup field called "Success Manager" on a ticket, this endpoint can answer the question, "What tickets (sources) is this user (found by `target_type` and `target_id`) assigned as the 'Success Manager' (field referenced by `field_id`)?"  #### Allowed For  * Agents  #### Pagination  * Cursor pagination (recommended) * Offset pagination  See [Pagination](/api-reference...

---
