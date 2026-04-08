---
aid: zendesk:zendesk-deletemanytriggers
name: Zendesk Delete  Api V2 Triggers Destroy_many
tags:
- Triggers
humanURL: 
properties: []
description: >-
  Deletes the ticket triggers corresponding to the provided comma-separated list of IDs.  #### Allowed For  * Agents  #### Request Parameters  The DELETE request takes one parameter, an `ids` object that lists the ticket triggers to delete.  | Name | Description | ---- | ----------- | ids  | The IDs of the triggers to delete  #### Example request  ```js {   "ids": "25,23,27,22" } ```

---
