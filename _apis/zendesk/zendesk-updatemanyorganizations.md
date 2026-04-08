---
aid: zendesk:zendesk-updatemanyorganizations
name: Zendesk Put  Api V2 Organizations Update_many
tags:
- Organizations
humanURL: 
properties: []
description: >-
  Bulk or batch updates up to 100 organizations.  #### Bulk update  To make the same change to multiple organizations, use the following endpoint and data format:  `https://{subdomain}.zendesk.com/api/v2/organizations/update_many.json?ids=1,2,3`  ```js {   "organization": {     "notes": "Priority"   } } ```  #### Batch update  To make different changes to multiple organizations, use the following endpoint and data format:  `https://{subdomain}.zendesk.com/api/v2/organizations/update_many.json` ...

---
