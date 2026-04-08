---
aid: zendesk:zendesk-bulkdeleteautomations
name: Zendesk Delete  Api V2 Automations Destroy_many
tags:
- Automations
humanURL: 
properties: []
description: >-
  Deletes the automations corresponding to the provided comma-separated list of IDs.  **Note**: You might be restricted from deleting some default automations. If included in a bulk deletion, the unrestricted automations will be deleted.  #### Allowed For  * Agents  #### Request Parameters  The DELETE request takes one parameter, an `ids` object that lists the automations to delete.  | Name | Description | ---- | ----------- | ids  | The IDs of the automations to delete  #### Example request  `...

---
