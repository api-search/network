---
aid: plaid:plaid-itemremove
name: Plaid Remove an Item
tags:
- Plaid
humanURL: 
properties: []
description: >-
  The `/item/remove` endpoint allows you to remove an Item. Once removed, the `access_token`, as well as any processor tokens or bank account tokens associated with the Item, is no longer valid and cannot be used to access any data that was associated with the Item.  Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove access to them specifically using the `/asset_report/remove` endpoint.  Note that in the Dev...

---
