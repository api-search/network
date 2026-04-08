---
aid: plaid:plaid-sandboxitemresetlogin
name: Plaid Force a Sandbox Item into an error state
tags:
- Plaid
humanURL: 
properties: []
description: >-
  `/sandbox/item/reset_login/` forces an Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/item/reset_login`, You can then use Plaid Link update mode to restore the Item to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the ...

---
