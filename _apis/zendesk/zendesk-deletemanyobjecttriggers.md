---
aid: zendesk:zendesk-deletemanyobjecttriggers
name: Zendesk Delete  Api V2 Custom_objects Custom_object_key Triggers Destroy_many
tags:
- Object Triggers
humanURL: 
properties: []
description: >-
  Deletes the object triggers corresponding to the provided comma-separated list of ids.   **Note**: You can only bulk-delete triggers associated with one object at a time, specified by the `custom_object_key` in the request.  #### Allowed For  * Administrators * Agents in custom roles with the `manage_triggers` permission (Enterprise only)  #### Request Parameters  The DELETE request takes an `ids` object that lists the object triggers to delete. All of the specified object trigger `ids` must ...

---
