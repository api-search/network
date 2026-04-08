---
aid: zendesk:zendesk-listdeletedusers
name: Zendesk Get  Api V2 Deleted_users
tags:
- Users
humanURL: 
properties: []
description: >-
  Returns deleted users, including permanently deleted users.  If the results contains permanently deleted users, the users' properties that normally contain personal data, such as `email` and `phone`, are null. The `name` property is "Permanently Deleted User".  #### Pagination  * Cursor pagination (recommended) * Offset pagination  See [Pagination](/api-reference/introduction/pagination/).  Returns a maximum of 100 records per page.  #### Allowed For  * Agents

---
