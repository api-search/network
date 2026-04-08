---
aid: zendesk:zendesk-showusercompliancedeletionstatuses
name: Zendesk Get  Api V2 Users User_id Compliance_deletion_statuses
tags:
- Users
humanURL: 
properties: []
description: >-
  Returns the GDPR status for each user per area of compliance. A Zendesk area of compliance is typically a product like "support/explore" but can be more fine-grained for areas within the product lines.  If the user is not in the account, the request returns a 404 status.  ```http Status: 404 {   "error":"RecordNotFound",   "description":"Not found" } ```  #### Allowed For  * Agents, with restrictions  #### Pagination  * Cursor pagination (recommended) * Offset pagination  See [Pagination](/ap...

---
